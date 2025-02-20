import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import Akima1DInterpolator

file_path = "perc_crystallinity.xlsx"  # read the pecent crystanillty file
df = pd.read_excel(file_path)

temperatures = df["Temp/°C"].values #Find the temp values

# Function to plot each material 
def plot_spline_trend(material_name, color):
    y_values = df[material_name].values
    
    # Sort data to ensure its in correct order
    sorted_indices = np.argsort(temperatures)
    temperatures_sorted = temperatures[sorted_indices]
    y_values_sorted = y_values[sorted_indices]
    
    # Generate smooth x values
    x_smooth = np.linspace(temperatures_sorted[0], temperatures_sorted[-1], 1000)
    
    # Create cubic spline interpolation
    spline = Akima1DInterpolator(temperatures_sorted, y_values_sorted)
    y_smooth = spline(x_smooth)
    
    # Create a new figure 
    plt.figure(figsize=(8, 6))
    
    # Plot curve and original points
    plt.plot(x_smooth, y_smooth, label=material_name, color=color)
    plt.scatter(temperatures_sorted, y_values_sorted, color=color, marker='o')  # Original points
    
    # Find the index where y_smooth is closest to 50
    idx = np.argmin(np.abs(y_smooth - 50))  # Get index of closest value
    intersection_temp = x_smooth[idx]       # Get corresponding x (temperature)
    
    # Check if the curve actually reaches 50%
    if np.abs(y_smooth[idx] - 50) < 1:  # Only mark if it's very close to 50%
        plt.axvline(x=intersection_temp, color='black', linestyle='--', alpha=0.6)
        plt.text(intersection_temp-5, 52, f"{intersection_temp:.1f}°C", color='black', ha='right')#write text to the left of the curve
        
    # Add horizontal line at 50% crystallinity
    plt.axhline(y=50, color='gray', linestyle='--', label="50% Crystallinity")
    
    # Formatting
    plt.ylim(0,110)
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
    plot_spline_trend(material, color)

