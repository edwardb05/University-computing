import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import Akima1DInterpolator

file_path = "Charpy and Hardness Data 2025.xlsx"  # Update with actual file path

def read_and_plot(material, color):
    df = pd.read_excel(file_path, sheet_name=material)

    # Group by temperature: Calculate mean and standard deviation
    df_grouped = df.groupby("Temperature (°C)").agg({"Energy (J)": ["mean", "std"]}).reset_index()
    df_grouped.columns = ["Temperature (°C)", "Energy (J)", "Energy Std"]
    
    temperatures = df_grouped["Temperature (°C)"].values
    energy_mean = df_grouped["Energy (J)"].values
    energy_std = df_grouped["Energy Std"].fillna(0).values  

    # Generate smooth x values
    x_smooth = np.linspace(temperatures.min(), temperatures.max(), 1000)

    # Create Akima spline interpolation
    spline = Akima1DInterpolator(temperatures, energy_mean, method="makima")
    y_smooth = spline(x_smooth)

    # Compute the gradient (first derivative)
    gradient = np.gradient(y_smooth, x_smooth)

    # Define a threshold for a "flat" region
    flat_threshold = np.max(np.abs(gradient)) * 0.12  # 17% of max gradient

    # Identify indices where gradient is small (shelves)
    flat_indices = np.where(np.abs(gradient) < flat_threshold)[0]

    # Define the threshold for a significant energy jump (change in energy)
    energy_jump_threshold = np.max(np.diff(y_smooth)) * 0.3  # 30% of the maximum energy jump

    # Initialize the lower shelf end index to None
    lower_shelf_end_idx = None

    # Loop through the flat indices to find where the significant jump occurs
    for i in range(1, len(flat_indices)):
        idx1 = flat_indices[i-1]
        idx2 = flat_indices[i]
        
        energy_diff = np.abs(y_smooth[idx2] - y_smooth[idx1])
        
        if energy_diff > energy_jump_threshold:
            lower_shelf_end_idx = idx1  # The end of the lower shelf is the previous index
            break

    # If no significant energy jump found, use the last flat index
    if lower_shelf_end_idx is None:
        lower_shelf_end_idx = flat_indices[-1]

    # Now, let's define the lower shelf as the average energy value at the lower shelf indices
    lower_shelf = np.mean(y_smooth[flat_indices[:lower_shelf_end_idx+1]])

    # Define DBTT (Midpoint Energy) as the average of upper and lower shelves
    dbtt_energy = (lower_shelf + np.mean(y_smooth[flat_indices[-1]])) / 2

    # Find DBTT: Temperature where energy is closest to dbtt_energy
    idx = np.argmin(np.abs(y_smooth - dbtt_energy))
    dbtt_temp = x_smooth[idx]

    # Define the upper shelf: The region after the DBTT
    upper_shelf = np.mean(y_smooth[flat_indices[-1]:]) if len(flat_indices) > 0 else np.mean(y_smooth[-100:])

    # Plot lower shelf as a horizontal dotted line from the start until NDT
    lower_shelf_x = x_smooth[x_smooth <= x_smooth[lower_shelf_end_idx]]
    plt.plot(lower_shelf_x, [lower_shelf] * len(lower_shelf_x), color=color, linestyle='dotted', label="Lower Shelf")

    # # Plot upper shelf as a horizontal dashed line from DBTT to the end
    upper_shelf_x = x_smooth[x_smooth >= dbtt_temp]
    plt.plot(upper_shelf_x, [upper_shelf] * len(upper_shelf_x), color=color, linestyle='dashed', label="Upper Shelf")

    # Plot curved transition region
    plt.plot(x_smooth, y_smooth, color=color, label=material)

    # Plot original data with error bars
    plt.errorbar(temperatures, energy_mean, yerr=energy_std, fmt='o', color=color, capsize=5, label="Data ± Std Dev")

    # # Mark the end of the lower shelf (NDT) with a vertical line
    NDT_temp = x_smooth[lower_shelf_end_idx]
    plt.axvline(x=NDT_temp, color='orange', linestyle='--', alpha=0.6)
    plt.text(NDT_temp-4, lower_shelf +15, f"NDT: {NDT_temp:.1f}°C", color='orange', ha='right', fontsize=10, fontweight='bold')

    # # Mark DBTT with a vertical line
    plt.axvline(x=dbtt_temp, color='black', linestyle='--', alpha=0.6)
    plt.text(dbtt_temp+100, dbtt_energy + 5, f"DBTT: {dbtt_temp:.1f}°C", color='black', ha='right', fontsize=10, fontweight='bold')

    # Formatting
    plt.ylim((0,200))
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Energy (J)")
    plt.title(f"Ductile to Brittle Transition Temperature ({material})")
    plt.legend()
    plt.grid(True)

# Define materials and colors
matcol = [
    ("Cold Drawn Steel", "blue"),
    ("Annealed  Steel", "red"),
    ("Normalised Steel", "green"),
    ("Zinc", "purple"),
    ("Aluminium", "black")
]

# Plot each material separately
plt.figure(figsize=(8, 6))
for material, color in matcol:
    read_and_plot(material, color)
    plt.show()
