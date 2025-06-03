import numpy as np
import matplotlib.pyplot as pl


# opening a file and reading lines
def openfile(file):
    numbers = []  # Initialize an empty list
    # Open the file in read mode
    with open(file, 'r') as file:
        for line in file:
            
            # Strip and convert to integer (use float() for decimal numbers)
            number = float(line.strip("\n"))
            print (number)
            numbers.append(number)
    return (numbers)

# Lagrange Basis Polynomial
def Langragian(j, xp, xn):
    res = 1
    for k in range(len(xn)):
        if k != j:
            res *= (xp - xn[k]) / (xn[j] - xn[k])
    return res


# Lagrange Interpolation Function
def LagInterp(xn, yn, x):  
    y = []
    for xi in x:
        yf = 0
        # Look through notes for langragian interpolation definition
        for j in range(len(xn)):  # Loop through all the known points
            yf += yn[j] * Langragian(j, xi, xn)  # Apply Lagrange formula
        y.append(yf)
    return y



# # Define the known data points (xn and their corresponding function values yn)
xn = openfile("2021-22 Past papers/LogoXn.txt")
yn = openfile("2021-22 Past papers/LogoYn.txt")


# Define x values for interpolation (in this case, from 0 to 3 with step 0.05)
x = np.arange(-19, 19.05, 0.5)

# Apply Lagrange interpolation to the cubic set of data points
y_interpolated = LagInterp(xn, yn, x)

# Plot the Lagrange Interpolation result (Red curve)
pl.scatter(x, y_interpolated, c='Red', label='Lagrange Interpolation')

# Plot the initial nodal points (Blue dots)
pl.scatter(xn, yn, c='Blue', label='Data Points')
# Show the plot
pl.show()


pl.scatter(xn, yn, c='Blue', label='Data Points')
pl.show()
