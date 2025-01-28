import numpy as np
import matplotlib.pyplot as pl
import math as mt
import time
from mpl_toolkits import mplot3d

# init conditions

t0 = 0 
tend = 1200

T0 = 10
Tinf = 10
Tw = 5
Tcenter = 100

k= 40
h = 500
alpha = 1.172*10**-5
length = 0.5

dt= 1
dx =0.01

x = np.arange(0,length+dx,dx)
Nx= len(x)
t= np.arange(t0,tend+dt,dt)
Nt= len(t)

# create a time and space array
T = np.ndarray((Nt,Nx))

# setting init values at time 0
T[0,:] = T0

for p in range(1,Nt):
    # work out for every time 'p'
    # start with ends
    # uses the robin conditions to set boundary conditions
    T[p,0] = (h*Tw+k/dx*T[p-1,1]) / (h+k/dx)
    T[p,Nx-1] = (h*Tw+k/dx*T[p-1,Nx-2]) / (h+k/dx)
    # do every i interval of space
    for i in range(1,Nx-1):
        T[p,i] = ((alpha*dt)/dx**2) * ( T[p-1,i+1] + T[p-1,i-1] ) + (1 - 2*((alpha*dt)/dx**2)) * T[p-1,i]
    T[p,mt.ceil(Nx/2)] = 100

# pl.plot(x,T[0,:])
# pl.plot(x,T[600,:])
# pl.plot(x,T[1200,:])

pl.plot(t,T[:,19])

pl.grid()
pl.show()

