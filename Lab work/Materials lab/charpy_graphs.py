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
    spline = Akima1DInterpolator(temperatures, energy_mean)
    y_smooth = spline(x_smooth)

    # Compute the gradient (first derivative)
    gradient = np.gradient(y_smooth, x_smooth)

    # Define a threshold for a "flat" region
    flat_threshold = np.max(np.abs(gradient)) * 0.17 # 17% of max gradient

    # Identify indices where gradient is small (shelves)
    flat_indices = np.where(np.abs(gradient) < flat_threshold)[0]

    # Identify upper and lower shelf regions based on flatness
    upper_shelf_indices = flat_indices[flat_indices > len(x_smooth) * 0.7]  # Last 30%
    lower_shelf_indices = flat_indices[flat_indices < len(x_smooth) * 0.3]  # First 30%

    if len(upper_shelf_indices) > 0:
        upper_shelf = np.mean(y_smooth[upper_shelf_indices])
    else:
        upper_shelf = np.mean(y_smooth[-100:])

    if len(lower_shelf_indices) > 0:
        lower_shelf = np.mean(y_smooth[lower_shelf_indices])
    else:
        lower_shelf = np.mean(y_smooth[:100])

    # Define DBTT (Midpoint Energy)
    dbtt_energy = (upper_shelf + lower_shelf) / 2

    # Find DBTT: Temperature where energy is closest to dbtt_energy
    idx = np.argmin(np.abs(y_smooth - dbtt_energy))
    dbtt_temp = x_smooth[idx]

    # Find transition region (where gradient is NOT flat)
    transition_indices = np.where(np.abs(gradient) >= flat_threshold)[0]
    transition_start = transition_indices[0]
    transition_end = transition_indices[-1]

    # Create figure
    plt.figure(figsize=(8, 6))

    # Plot lower shelf as a horizontal dotted line from the start until DBTT
    lower_shelf_x = x_smooth[x_smooth <= dbtt_temp]
    plt.plot(lower_shelf_x, [lower_shelf] * len(lower_shelf_x), color=color, linestyle='dotted', label="Lower Shelf")

    # Plot upper shelf as a horizontal dotted line from DBTT to the end
    upper_shelf_x = x_smooth[x_smooth >= dbtt_temp]
    plt.plot(upper_shelf_x, [upper_shelf] * len(upper_shelf_x), color=color, linestyle='dashed', label="Upper Shelf")

    # Plot curved transition region
    plt.plot(x_smooth[transition_start:transition_end], y_smooth[transition_start:transition_end], color=color, label=material)

    # Plot original data with error bars
    plt.errorbar(temperatures, energy_mean, yerr=energy_std, fmt='o', color=color, capsize=5, label="Data ± Std Dev")

    # Mark DBTT with vertical line
    plt.axvline(x=dbtt_temp, color='black', linestyle='--', alpha=0.6)
    plt.text(dbtt_temp, dbtt_energy + 5, f"DBTT: {dbtt_temp:.1f}°C", color='black', ha='right', fontsize=10, fontweight='bold')

    # Formatting
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Energy (J)")
    plt.title(f"Ductile to Brittle Transition Temperature ({material})")
    plt.legend()
    plt.grid(True)

    # Show plot
    plt.show()

# Define materials and colors
matcol = [
    ("Cold Drawn Steel", "blue"),
    ("Annealed  Steel", "red"),
    ("Normalised Steel", "green"),
    ("Zinc", "purple"),
    ("Aluminium", "black")
]

# Plot each material separately
for material, color in matcol:
    read_and_plot(material, color)
