
import numpy as np

# Define the function
def f(x, y):
    return 4 * x * y - 2 * x**2 - 4 * y**2 

# Starting point
x0, y0 = 3, 2

# Number of iterations
num_iterations = 100



# Define the numerical partial derivatives of the function, by using the forward scheme
def df_dx(x, y, h=1e-6):
    return (f(x + h, y) - f(x, y)) / h

def df_dy(x, y, h=1e-6):
    return (f(x, y + h) - f(x, y)) / h

# Define the numerical second partial derivatives (Hessian matrix), by using the forward scheme
def d2f_dx2(x, y, h=1e-6):
    return (df_dx(x + h, y) - df_dx(x, y)) / h

def d2f_dy2(x, y, h=1e-6):
    return (df_dy(x, y + h) - df_dy(x, y)) / h

def d2f_dxdy(x, y, h=1e-6):
    return (df_dy(x + h, y) - df_dy(x, y)) / h


# Optimization loop
for i in range(num_iterations):
    # Compute the gradient at the current point
    grad_x = df_dx(x0, y0)
    grad_y = df_dy(x0, y0)
    
    # Compute the Hessian matrix at the current point
    Hessian = np.array([[d2f_dx2(x0, y0), d2f_dxdy(x0, y0)],
                        [d2f_dxdy(x0, y0), d2f_dy2(x0, y0)]])
    
    # Compute the inverse of the Hessian matrix
    inv_Hessian = np.linalg.inv(Hessian)
    
    # Compute the search direction
    search_direction = np.dot(-inv_Hessian, np.array([grad_x, grad_y]))
    
    # Update the current point using the search direction and a predetermined step size
    alpha = 0.1  # Predetermined step size
    x0 += alpha * search_direction[0]
    y0 += alpha * search_direction[1]

# Print the final point and the maximum value
print("Location of maximum (x, y):", round(x0, 2), round(y0, 2))
print("Maximum value of f(x, y):", round(f(x0, y0), 2))