# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:38:28 2024

@author: eb1723
"""

import numpy as np
import matplotlib.pyplot as pl


def func(x):
    return 1/(1+25*x**2)


def MyGauss(A,b):
    
    # number of equations
    n = len(b)
    
    # eliminate the unknowns, from first to (n-1)th unknown, to form an upper triangular matrix
    for i in range(0,n-1):
        # eliminate the i-th unknown from the (i+1)th row downwards
        # i.e. set the zeros in column i.
        for j in range(i+1,n):
            # eliminate on row j

            # A(i,i) is the pivot coefficient
            p = A[j,i] / A[i,i]
        
            # compute the new elements of row j in matrix A
            # use slicing
            #A[j,:] = A[j,:] - p * A[i,:]
            # or, alternatively, loop for every cell of row j
            #for k in range(i,n):
            #    A[j,k] = A[j,k] - p * A[i,k]
            A[j,:] = A[j,:] - p * A[i,:]

            # compute the new element of row j in vector b
            b[j] = b[j] - p * b[i]
    
    
    # evauate, by back substitution the solution
    # start from the last unknown and go upward till the first unknown
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        # contribution from b (right hand side of the equation)
        x[i] = b[i] / A[i,i]
        # contribution from the other (already evaluated) unknowns
        # (within the left hand side of the equation)
        for k in range(i+1,n):
            x[i] = x[i] - A[i,k] * x[k] / A[i,i]

    return x


def Spline(xn,yn,bclower,bcupper,x):
    Nx = len(xn)
    y = np.zeros(len(x))
    # determine cubic coefficients aj, bj, cj, dj
    # there need to be ns = Nx - 1 cubic splines
    ns = Nx - 1

    aj = np.ndarray(ns)
    bj = np.ndarray(ns)
    cj = np.ndarray(ns)
    dj = np.ndarray(ns)

    # form the matrix A (of unknown)
    A = np.zeros((Nx,Nx))
    b = np.zeros(Nx)

    A[0,0] = 1
    b[0] = bclower
    A[-1,-1] = 1
    b[-1] = bcupper
    for j in range(1,ns):
        A[j,j-1] = 1 / (xn[j]-xn[j-1])
        A[j,j] = 2 / (xn[j]-xn[j-1]) + 2 / (xn[j+1]-xn[j])
        A[j,j+1] = 1 / (xn[j+1]-xn[j])

        b[j] = 3 * ( (yn[j]-yn[j-1]) / (xn[j]-xn[j-1])**2 + (yn[j+1]-yn[j]) / (xn[j+1]-xn[j])**2 )

    # invert the matrix
    #v = np.linalg.inv(A).dot(b)
    v = MyGauss(A,b)
    # determine the coefficients
    for j in range(0,ns):
        aj[j] = yn[j]
        bj[j] = v[j]
        cj[j] = 3*(yn[j+1]-yn[j])/(xn[j+1]-xn[j])**2 - (v[j+1]+2*v[j])/(xn[j+1]-xn[j])
        dj[j] = -2*(yn[j+1]-yn[j])/(xn[j+1]-xn[j])**3 + (v[j+1]+v[j])/(xn[j+1]-xn[j])**2

    # interpolate with spline
    for j in range(0,ns):
        # mask so only correct values of x are used
        y[(xn[j]<=x) & (x<=xn[j+1])] = aj[j] + bj[j]*(x[(xn[j]<=x) & (x<=xn[j+1])]-xn[j]) +  \
              cj[j]*(x[(xn[j]<=x) & (x<=xn[j+1])]-xn[j])**2 + dj[j]*(x[(xn[j]<=x) & (x<=xn[j+1])]-xn[j])**3
        
    return y


a = -1 # lower interval
b = 1 # upper interval
Nx = 9 # number of nodes
xn = np.linspace(a,b,Nx)
# Creates y values for all x values
yn = func(xn)

bclower = 0.0740
bcupper = -0.0740
# set the domain of interpolation
dx = 0.05
x = np.arange(-1,1+dx,dx)

y = Spline(xn,yn,bclower,bcupper,x)
print(x[-5])
print(y[-5])

# plot polynomial in the interpolating range
pl.plot(x,y,c='Red')
# plot the initial nodal info only
pl.scatter(xn,yn,c='Blue')
# plot the actual function
pl.plot(x,func(x),c='Green')
pl.show()