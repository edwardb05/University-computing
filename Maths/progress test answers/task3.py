import matplotlib.pyplot as plt
import numpy as np
import csv
import numpy as np
# Task E: compute the volume

# prepare arrays to receive data from input file
def trapz(x,y):
    # get the number of subintervals
    N = len(x) - 1
    # compute the integral
    # set range for the trapezia: there are as many trapezia as the number of intervals
    R = range(0,N)
    S = 0
    for i in R:
        # compute the area of this single trapezium (remind yourself the area of a trapezium)
        S += 0.5 * (y[i+1] + y[i]) * (x[i+1] - x[i])
    return S

x = np.arange(0,1.01,0.01)
y = np.arange(0,2.01,0.01)
Nx = len(x)
Ny = len(y)
Xg = np.zeros((Ny,Nx))
Yg = np.zeros((Ny,Nx))
Zgb = np.zeros((Ny,Nx))
Zgt = np.zeros((Ny,Nx))
# read in the data
(Xg, Yg) = np.meshgrid(x,y)
f = np.exp(-Xg)+np.sin(Yg)
# organise data in grids of dimensions (Ny,Nx)

# integrate in dx, for all the value of y, i.e. find G(y)
G = np.zeros(Ny)
for i in range(0,Ny):
    x = Xg[i,:] # define the set of x nodes
    zt = f[i,:] # define the set of z values describing the top surface

    G[i] = trapz(x,zt) 

# integrate G(y) in dy

I = trapz(y,G)

print(I)