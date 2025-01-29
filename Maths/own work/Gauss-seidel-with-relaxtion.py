import numpy as np

# Define the system Au = b
A = np.array([[-4, 2, 0],
              [1, -4, 1],
              [0, 2, -4]])

b = np.array([-2, -44, 238])

# Initial guess
u = np.array([0, 0, 0], dtype=float)  # Starting with [0, 0, 0], ensure it's float

# Stopping criterion
tolerance = 1  # Relative error threshold (%)
lamb = 1.1  # Relaxation factor

# Gauss-Seidel Iteration
iterations = 0
while True:
    u_new = np.zeros_like(u)
 
    
    # Update each value in u using Gauss-Seidel formula adding relaxation ter,
    u_new[0] = ((b[0] - A[0, 1] * u[1] - A[0, 2] * u[2]) / A[0, 0]) * lamb  + (1 - lamb) * u[0]
    u_new[1] = ((b[1] - A[1, 0] * u_new[0] - A[1, 2] * u[2]) / A[1, 1])* lamb  + (1 - lamb) * u[1]
    u_new[2] = ((b[2] - A[2, 0] * u_new[0] - A[2, 1] * u_new[1]) / A[2, 2])* lamb  + (1 - lamb) * u[2]



    
    # Calculate relative error
    relative_errors = np.abs((u_new - u) / u_new) * 100
    max_error = np.max(relative_errors)
    
    # Update iteration count and check convergence
    iterations += 1
    if max_error <= tolerance:
        u = u_new
        break
    
    # Update u for the neut iteration
    u = u_new
# Output results
print(f"Solution: {u}")  # Final solution with decimals
print(f"Iterations: {iterations}")
