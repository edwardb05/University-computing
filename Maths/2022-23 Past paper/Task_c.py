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
xn = openfile("2022-23 Past paper/Xn.txt")
yn = openfile("2022-23 Past paper/Yn.txt")

x2n = [xn[i] for i in range(0, len(xn), 2)]
y2n = [yn[i] for i in range(0, len(yn), 2)]

x2n1 =[xn[i+1] for i in range(0, len(xn)-2, 2)]
y2n1 =[yn[i+1] for i in range(0, len(yn)-2, 2)]

x = [0.25,0.75,1.25,1.75,2.25,2.75,3.25,3.75,4.25,4.75,5.25,5.75]

yeven =  LagInterp(x2n,y2n,x)
yodd =  LagInterp(x2n1,y2n1,x)
y =  LagInterp(xn,yn,x)

pl.plot(x,yeven, label='only even values', color='r')
pl.plot(x,yodd, label='only odd values', color='b')
pl.plot(x,y, label='all', color='g')

pl.show()