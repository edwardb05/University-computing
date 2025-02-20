import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = "Charpy and Hardness Data 2025.xlsx"  # Update with actual file path

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

    # Compute the gradient (first derivative) using differences between points
    gradient = np.diff(energy_sorted) / np.diff(temperatures_sorted)
    gradient = np.append(gradient, gradient[-1])  # Extend to match length

    # Define a threshold for a "flat" region
    flat_threshold = np.max(np.abs(gradient)) * 0.12  # 12% of max gradient

    # Identify indices where gradient is small (shelves)
    flat_indices = np.where(np.abs(gradient) < flat_threshold)[0]

    # Define lower shelf: average energy of initial flat region
    lower_shelf_end_idx = flat_indices[flat_indices < len(temperatures_sorted) // 2][-1] if len(flat_indices) > 0 else 0
    lower_shelf = np.mean(energy_sorted[:lower_shelf_end_idx + 1])
    lower_shelf_end_temp = temperatures_sorted[lower_shelf_end_idx]

    # Define upper shelf: average energy of final flat region
    upper_shelf_start_idx = flat_indices[flat_indices > len(temperatures_sorted) // 2][0] if len(flat_indices) > len(temperatures_sorted) // 2 else -1
    upper_shelf = np.mean(energy_sorted[upper_shelf_start_idx:])
    upper_shelf_start_temp = temperatures_sorted[upper_shelf_start_idx]

    # Define DBTT: Midpoint energy between shelves
    dbtt_energy = (lower_shelf + upper_shelf) / 2

    # Find transition points for the connecting line
    # Lower shelf ends at NDT (end of lower flat region)
    ndt_temp = lower_shelf_end_temp
    # Upper shelf starts where energy approaches upper shelf level (simplified)
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
    plt.ylim((0, 200))
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