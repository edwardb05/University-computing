import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
x = np.linspace(-10, 10, 20)  # X coordinates
y = np.linspace(-10, 10, 20)  # Y coordinates
X, Y = np.meshgrid(x, y)  # Create a grid

# Define the velocity components u and v
# Example: Circular flow field
u = 1+0.1*X  # Horizontal velocity component
v = -0.1*Y  # Vertical velocity component

# Plot the velocity field using quiver
plt.figure(figsize=(7,7))
plt.quiver(X, Y, u, v, color='b')  # Quiver function for vector field

# Add labels and title
plt.title('2D Velocity Field')
plt.xlabel('X')
plt.ylabel('Y')

plt.grid()
plt.show()

plt.figure(figsize=(7,7))
plt.streamplot(X, Y, u, v, color=np.sqrt(u**2 + v**2), cmap='plasma')

# Add labels and title
plt.title('2D Velocity Field - Streamplot')
plt.xlabel('X')
plt.ylabel('Y')

plt.grid()
plt.show()
