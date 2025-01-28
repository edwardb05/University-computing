# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:07:37 2024

@author: eb1723
"""
import numpy as np
import matplotlib.pyplot as pl
# newton interpolation
# Function to interpolate (sin(x) in this case)
def func(x):
    return 1/(1+25*x**2)

def NewtDivDiff(xn,yn):
    # recursive form
    
    # determine number of points
    N = len(xn)
    # set the order: 1 node -> f0; 2 nodes -> f1, etc.
    N = N - 1

    if N == 0:
        # f is the point itself
        f = yn[0]
    else:
        # f is defined recursively as (slide 64):
        # f = ( f[x0,...x(n-1)] - f[x1,...xn] ) / ( x0 - xn)
        f = ( NewtDivDiff(xn[:-1],yn[:-1]) - NewtDivDiff(xn[1:],yn[1:]) ) / ( xn[0] - xn[-1] )
    return f

def NetwonInterp(xn,yn,x):
    Nx = len(xn)
    # determine order
    k = Nx - 1
    
    y = []

    for xp in x:
        # determine pn at x = xp
        yp = yn[0]
        for i in range(1,k+1):
            prod = 1
            for j in range(0,i):
                prod *= (xp-xn[j])

            yp += prod * NewtDivDiff(xn[0:i+1],yn[0:i+1])

        y += [yp]
    
    y = np.array(y)
        
    return y
a = -1 # lower interval
b = 1 # upper interval
Nx = 4 # number of nodes
xn = np.linspace(a,b,Nx)
yn = func(xn)
# determine order
k = Nx - 1

# set the domain of interpolation
dx = 0.05
x = np.arange(-1,1+dx,dx)

y = NetwonInterp(xn,yn,x)

print(x[-5],y[-5])

# convert list into array
y = np.array(y)   
# plot polynomial in the interpolating range
pl.plot(x,y,c='Red')
# plot the initial nodal info only
pl.scatter(xn,yn,c='Blue')
# plot the actual function
pl.plot(x,func(x),c='Green')
pl.show()