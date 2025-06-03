import numpy as np
import matplotlib.pyplot as pl
import math as mt
import time
from mpl_toolkits import mplot3d

# init conditions

t0 = 0 
tend = 100000000

Tp0 = 6
Tw0 = 2
Tainf = 35
Tbinf = 35
R= 30

# Setting steps
dt= 1
dx =0.5

# Domains
length = np.arange(-R,R,dx)
Nx= len(length)

t= np.arange(t0,tend+dt,dt)
Nt= len(t)

averagep = []
averagew = []
# set the thermal diffusivity
alpha = np.ndarray(Nx)
# set the diffusivity T for watermelon
alpha[:int(Nx/2)] = 4.5e-2
# set the diffusivity for pistachio
alpha[int(Nx/2):] = 8.6e-2

# create a time and space array
T = np.ndarray((Nt,Nx))

# setting init values at time 0
T[0,0] = Tainf
T[0,Nx-1] = Tbinf
T[0, 1:Nx//2] =Tw0
T[0, (Nx//2): Nx-1] = Tp0

# Courant value check
CFlP = (alpha[0]*dt)/dx**2
CFLW = (alpha[-1]*dt)/dx**2
print(CFlP)
print(CFLW)

Melted = False
i=0
while Melted == False:
    i+=1
    # work out for every time 'i'
    # start with ends
    T[i,0] = Tainf
    T[i,Nx-1] = Tbinf
    # do every i interval of space
    for x in range(1,Nx-1):
        T[i,x] = ((alpha[x]*dt)/dx**2) * ( T[i-1,x+1] -2*T[i-1,x] + T[i-1,x-1]) +T[i-1,x]
    avgw = np.average(T[i,1:Nx//2])
    avgp = np.average(T[i,(Nx//2): Nx-1])
    averagew.append(avgw)
    averagep.append (avgp)
    if avgp >= 15 or avgw >= 15:
        Melted = True

pl.plot(length, T[i, :])
pl.title("Final temperature distribution")
pl.xlabel("x-position")
pl.ylabel("Temperature (°C)")
pl.grid()
pl.show()

pl.plot(t[0:i], averagep, label='Pistachio (Tp)')
pl.plot(t[0:i], averagew, label='Watermelon (Tw)')
pl.title("Average Temperature of Regions Over Time")
pl.xlabel("Time (s)")
pl.ylabel("Temperature (°C)")
pl.legend()
pl.grid()
pl.show()


# Print final state
print("Final temperature profile:")
print(T[i, :])