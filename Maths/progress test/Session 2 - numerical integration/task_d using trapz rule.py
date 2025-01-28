# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:01:50 2024

@author: eb1723
"""
import matplotlib.pyplot as plt
import numpy as np
import csv

#  real use of trapz rule

# import from task c
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

# amount of nodes in files
N = 72

# initialize northbank and south bank nodes
xn = np.zeros(N)
yn = np.zeros(N)
xs = np.zeros(N)
ys = np.zeros(N)
# read in the coordinates of the banks
f = open('Thames.txt','r')
banks = csv.reader(f)
# extract coordinates of north and south banks
i = 0
for nodes in banks:
    xn[i] = float(nodes[0])
    yn[i] = float(nodes[1])
    xs[i] = float(nodes[2])
    ys[i] = float(nodes[3])
    i += 1
f.close()


plt.plot(xn,yn,xs,ys)
plt.axis('equal')
plt.show()
# use trapezoid rule to work area
area = trapz(xn,yn)- trapz(xs,ys)
areakm = area/(1000**2)
print(areakm)