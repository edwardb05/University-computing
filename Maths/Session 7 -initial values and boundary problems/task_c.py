import numpy as np
import matplotlib.pyplot as pl
import math as mt
import time
from mpl_toolkits import mplot3d

# init conditions

t0 = 0 
tend = 60*60

T0 = 10
Tainf = 50
Tbinf = 50

alpha = 1.172*10**-5
length = 0.5

dt= 0.38
dx =0.003

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
    T[p,0] = Tainf
    T[p,Nx-1] = Tbinf
    # do every i interval of space
    for i in range(1,Nx-1):
        T[p,i] = ((alpha*dt)/dx**2) * ( T[p-1,i+1] + T[p-1,i-1] ) + (1 - 2*((alpha*dt)/dx**2)) * T[p-1,i]

courant = (alpha*dt)/dx**2
print(courant)
pl.plot(x,T[-1,:])
pl.grid()
pl.show()
print(T[-1,:])
