import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = "perc_crystallinity.xlsx"  # read the percent crystallinity file
df = pd.read_excel(file_path)

temperatures = df["Temp/°C"].values  # Find the temp values

# Function to plot each material with point-to-point lines
def plot_point_to_point(material_name, color):
    y_values = df[material_name].values
    
    # Sort data to ensure it’s in correct order
    sorted_indices = np.argsort(temperatures)
    temperatures_sorted = temperatures[sorted_indices]
    y_values_sorted = y_values[sorted_indices]
    
    # Create a new figure 
    plt.figure(figsize=(8, 6))
    
    # Plot point-to-point line and original points
    plt.plot(temperatures_sorted, y_values_sorted, label=material_name, color=color)  # Connect points directly
    plt.scatter(temperatures_sorted, y_values_sorted, color=color, marker='o')  # Original points
    
    # Find the approximate temperature where the line crosses 50% (linear interpolation between points)
    for i in range(len(y_values_sorted) - 1):
        y1, y2 = y_values_sorted[i], y_values_sorted[i + 1]
        x1, x2 = temperatures_sorted[i], temperatures_sorted[i + 1]
        if (y1 < 50 and y2 > 50) or (y1 > 50 and y2 < 50):  # Check if 50% is crossed
            # Linear interpolation to find exact crossing point
            intersection_temp = x1 + (50 - y1) * (x2 - x1) / (y2 - y1)
            plt.axvline(x=intersection_temp, color='black', linestyle='--', alpha=0.6)
            plt.text(intersection_temp - 5, 52, f"{intersection_temp:.1f}°C", color='black', ha='right')
            break  # Stop after finding the first crossing
    
    # Add horizontal line at 50% crystallinity
    plt.axhline(y=50, color='gray', linestyle='--', label="50% Crystallinity")
    
    # Formatting
    plt.ylim(0, 110)
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Cleavage Fracture Percentage")
    plt.title(f"Cleavage Fracture vs Temperature ({material_name})")
    plt.legend()
    plt.grid(True)
    
    # Show the plot for this material
    plt.show()

# Define materials and colors
matcol = [
    ("Steel Cold Drawn", "blue"),
    ("Steel Annealed", "red"),
    ("Steel Normalised", "green"),
    ("Zinc", "purple"),
    ("Aluminium", "black")
]

# Plot each material in its own separate figure
for material, color in matcol:
    plot_point_to_point(material, color)

