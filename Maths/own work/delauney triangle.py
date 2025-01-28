import numpy as np
from scipy.spatial import Delaunay
from scipy.interpolate import LinearNDInterpolator
import matplotlib.pyplot as plt

# Define your 5 known locations (x, y) and their temperatures
points = np.array([
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]
])
temperatures = np.array([7, 5, 8, 5])  # Temperature values at each point

# Perform Delaunay triangulation
tri = Delaunay(points)

# Create the interpolator using the triangulation
interpolator = LinearNDInterpolator(points, temperatures)

# Define a grid to visualize the interpolated temperature field
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]  # Create a grid from 0 to 6 in both x and y

# Interpolate the temperature over the grid
grid_temp = interpolator(grid_x, grid_y)

# Plot the result
plt.figure(figsize=(8, 6))
plt.imshow(grid_temp.T, extent=(0, 1, 0, 1), origin='lower', cmap='coolwarm', aspect='auto') # Transpose grid_temp
plt.colorbar(label="Temperature (°C)")
plt.scatter(points[:, 0], points[:, 1], c=temperatures, edgecolors='k', s=100, cmap='coolwarm')
plt.triplot(points[:, 0], points[:, 1], tri.simplices, 'k--', lw=0.75)  # Plot the triangles
plt.title("Interpolated Temperature Field")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.show()

# Example: Specific points where you want interpolated temperature values
specific_points = np.array([
    [0.5, 0.5],
   
])

# Get interpolated temperature values at these specific points
interpolated_temperatures = interpolator(specific_points)

print("Interpolated temperatures at specific points:")
for i, (point, temp) in enumerate(zip(specific_points, interpolated_temperatures)):
    print(f"Point {point}: {temp:.2f} °C")
