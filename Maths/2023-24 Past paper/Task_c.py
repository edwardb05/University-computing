import numpy as np
import matplotlib.pyplot as pl

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



# Using the bisection method to find the root of a function
def bisection_method(a,b,tol,Tn,tn):
        
    while abs(a-b)>tol:
        # calculate the mid point
        xm = (a + b) / 2
        # establish in which subinterval the solution lies
        # compute f(a) * f(xm)
        ff = LagInterp(tn,Tn,[a])[0] * LagInterp(tn,Tn,[xm])[0]
        if ff < 0: 
            # the solution lies in the left interval as the signs are different
            # set the upper bracket as xm
            b = xm
        else:
            # the solution lies in the right interval
            # set the lower bracket as xm
            a = xm
    
    # the true solution is bracketed within the latest interval [a,b]
    # we can approximate it with the midpoint
    sol = (a + b) / 2
    if LagInterp(tn,Tn,[sol])[0]<10:
        return sol
    else:

        return "No solution found in range"

# opening a file and reading lines
def openfile(file):
    numbers = []  # Initialize an empty list
    # Open the file in read mode
    with open(file, 'r') as file:
        for line in file:
            
            # Strip and convert to integer (use float() for decimal numbers)
            number = int(line.strip())
            numbers.append(number)
    return (numbers)

Tn = openfile("2023-24 Past paper/Temperatures.txt")
time = np.arange(0,6,0.5)

print(bisection_method(0,5.5,0.005,Tn, time))