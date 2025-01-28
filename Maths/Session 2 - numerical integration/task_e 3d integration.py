# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv
import numpy as np
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


a = 67 # major axis
b = 56 # minor axis
h = 25 # minor axis

# set the step intervals in x and y
dx = 0.08
dy = 0.08

# set the x range, not including the boundaries
x = np.arange(-a+dx,a,dx)
N = len(x)
# the y range depends of the various values of x, and cannot be fixed here

# integrate in dy, for all the value of x, i.e. find G(x)

G = np.zeros(N)
# for every x
for i in range(0,N):
    # determine the boundaries m and p for this x
    mx = np.sqrt(b**2*(1-x[i]**2/a**2))
    px = mx
    # set the y points for this x, not including the boundaries
    y = np.arange(-mx+dy,px,dy)
    z = np.zeros(len(y))
    # determine the values of the function z(x,y)
    for j in range(0,len(y)):
        z[j] = np.sqrt(h**2*(1-x[i]**2/a**2-y[j]**2/b**2)) 
    
    # integrate in dy from cx to dx (for this specific x)
    G[i] = trapz(y,z) # G(x)

# integrate G(x) in dx
I = trapz(x,G)

print(I)

# for an hemisphere the volume is:
print((4/3*np.pi*a*b*h)/2)


# PLotting----------
import matplotlib.pyplot as pl


# plot the dome

# set domain by using the two angles t and p
# Create a mesh grid
theta = np.linspace(-np.pi/2, np.pi/2, 50) 
phi = np.linspace(-np.pi/2, np.pi/2, 50)
Theta, Phi = np.meshgrid(theta, phi)

# Calculate the coordinates of points on the ellipsoid surface
X = a * np.sin(Theta) * np.cos(Phi)
Y = b * np.sin(Theta) * np.sin(Phi)
Z = h * np.cos(Theta)

# Create a 3D surface plot
fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='Oranges')

# Set labels and title
ax.set_title('Royal Albert Hall dome')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')
ax.view_init(15, 60)
pl.show()

