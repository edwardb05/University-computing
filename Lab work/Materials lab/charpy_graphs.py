import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import Akima1DInterpolator

file_path = "Charpy and Hardness Data 2025.xlsx" 

def read_and_plot(material, color):
    df = pd.read_excel(file_path, sheet_name=material)

    # Group by temperature: Calculate mean and standard deviation
    df_grouped = df.groupby("Temperature (°C)").agg({"Energy (J)": ["mean", "std"]}).reset_index()
    df_grouped.columns = ["Temperature (°C)", "Energy (J)", "Energy Std"]
    
    temperatures = df_grouped["Temperature (°C)"].values
    energy_mean = df_grouped["Energy (J)"].values
    energy_std = df_grouped["Energy Std"].fillna(0).values  

    # Sort data by temperature
    sorted_indices = np.argsort(temperatures)
    temperatures_sorted = temperatures[sorted_indices]
    energy_sorted = energy_mean[sorted_indices]
    energy_std_sorted = energy_std[sorted_indices]

    # Generate smooth curve for gradient calculation
    x_smooth = np.linspace(temperatures_sorted.min(), temperatures_sorted.max(), 1000)
    spline = Akima1DInterpolator(temperatures_sorted, energy_sorted)
    y_smooth = spline(x_smooth)

    # Compute the gradient from the smooth curve
    gradient = np.gradient(y_smooth, x_smooth)

    # Define a stricter threshold for a "flat" region
    flat_threshold = np.max(np.abs(gradient)) * 0.08  # 8% of max gradient

    # Identify flat regions in the smooth curve
    flat_indices = np.where(np.abs(gradient) < flat_threshold)[0]

    # Map flat indices back to original data points
    x_smooth_to_data = np.interp(x_smooth[flat_indices], temperatures_sorted, np.arange(len(temperatures_sorted)))
    flat_data_indices = np.unique(np.round(x_smooth_to_data).astype(int))

    # Define lower shelf: Find the end by detecting a significant energy jump
    energy_jump_threshold = np.max(np.diff(y_smooth)) * 0.3  # 30% of max energy jump
    lower_shelf_end_idx = None
    for i in range(len(flat_data_indices) - 1):
        idx1, idx2 = flat_data_indices[i], flat_data_indices[i + 1]
        if idx2 - idx1 > 1:  # Check for a gap in flat indices (start of transition)
            energy_diff = energy_sorted[idx2] - energy_sorted[idx1]
            if energy_diff > energy_jump_threshold:
                lower_shelf_end_idx = idx1
                break
    if lower_shelf_end_idx is None:
        lower_shelf_end_idx = flat_data_indices[0] if len(flat_data_indices) > 0 else 0  # Default to first flat point

    lower_shelf = np.mean(energy_sorted[:lower_shelf_end_idx + 1])
    lower_shelf_end_temp = temperatures_sorted[lower_shelf_end_idx]

    # Define upper shelf: Start after the largest energy jump
    upper_shelf_start_idx = None
    max_jump = 0
    for i in range(len(energy_sorted) - 1):
        jump = energy_sorted[i + 1] - energy_sorted[i]
        if jump > max_jump and i > lower_shelf_end_idx:
            max_jump = jump
            upper_shelf_start_idx = i + 1
    if upper_shelf_start_idx is None:
        upper_shelf_start_idx = len(energy_sorted) - 1  # Default to last point

    upper_shelf = np.mean(energy_sorted[upper_shelf_start_idx:])
    upper_shelf_start_temp = temperatures_sorted[upper_shelf_start_idx]

    # Define DBTT: Midpoint energy between shelves
    dbtt_energy = (lower_shelf + upper_shelf) / 2

    # Define transition points for the connecting line
    ndt_temp = lower_shelf_end_temp
    transition_start_temp = ndt_temp
    transition_end_temp = upper_shelf_start_temp

    # Plot lower shelf as a solid horizontal line
    lower_shelf_x = temperatures_sorted[temperatures_sorted <= ndt_temp]
    plt.plot(lower_shelf_x, [lower_shelf] * len(lower_shelf_x), color=color, linestyle='-', linewidth=2, label="Lower Shelf")

    # Plot transition line connecting lower shelf to upper shelf
    plt.plot([transition_start_temp, transition_end_temp], [lower_shelf, upper_shelf], color=color, linestyle='-', linewidth=2, label="Transition")

    # Plot upper shelf as a solid horizontal line
    upper_shelf_x = temperatures_sorted[temperatures_sorted >= transition_end_temp]
    plt.plot(upper_shelf_x, [upper_shelf] * len(upper_shelf_x), color=color, linestyle='-', linewidth=2, label="Upper Shelf")

    # Plot original data with error bars
    plt.errorbar(temperatures_sorted, energy_sorted, yerr=energy_std_sorted, fmt='o', color=color, capsize=5, label="Data ± Std Dev")

    # Mark NDT (end of lower shelf) with a vertical line
    plt.axvline(x=ndt_temp, color='orange', linestyle='--', alpha=0.6)
    plt.text(ndt_temp - 4, lower_shelf + 15, f"NDT: {ndt_temp:.1f}°C", color='orange', ha='right', fontsize=10, fontweight='bold')

    # Mark DBTT: Temperature where transition line crosses dbtt_energy
    dbtt_temp = transition_start_temp + (dbtt_energy - lower_shelf) * (transition_end_temp - transition_start_temp) / (upper_shelf - lower_shelf)
    plt.axvline(x=dbtt_temp, color='black', linestyle='--', alpha=0.6)
    plt.text(dbtt_temp + 10, dbtt_energy + 5, f"DBTT: {dbtt_temp:.1f}°C", color='black', ha='right', fontsize=10, fontweight='bold')

    # Formatting
    plt.ylim(0,200)
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
for material, color in matcol:
    plt.figure(figsize=(8, 6))
    read_and_plot(material, color)
    plt.show()