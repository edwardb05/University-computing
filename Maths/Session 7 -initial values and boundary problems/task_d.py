# Task D
# This script solves the spatial 2-D heat conduction equation
import numpy as np
import matplotlib.pyplot as pl
import math as mt
import time
from mpl_toolkits import mplot3d

# set the input data
# spatial domain
xa = 0
xb = 0.4
ya = 0
yb = 0.3
pw = 0.06  # potato size

dx = 0.01 # spatial increment
dy = dx
# temporal domain
dt = 1 # temporal increment
tend = 9000  # temporal span

# set the physics
Toven = 25 # initial Temperature of oven
Tpot = -15 # initial Temperature of potato
Tw = 180 # T of oven walls

alphaAir = 1.9e-5 # thermal diffusivity of air
alphapot = 1.3e-7 # thermal diffusivity of potato
# ================================================


# position of the potato
xap = (xb-xa)/2 - pw/2
xbp = (xb-xa)/2 + pw/2
yap = (yb-ya)/2 - pw/2 
ybp = (yb-ya)/2 + pw/2


# greate the spatial grid points
x = np.arange(xa,xb+dx,dx)
Nx = len(x)
y = np.arange(ya,yb+dy,dy)
Ny = len(y)
# create the temporal grid points
t = np.arange(0,tend+dt,dt)
Nt = len(t)

# create the solution matrix
T = np.ndarray((Nt,Nx,Ny))

# I am defining a matix alpha of thermal diffusivity, in case we wish to have different spatial values, 
# i.e. the diffusivity of the potato where the potato lays.
alpha = np.ndarray((Nx,Ny))
alpha[:,:] = alphaAir


# set the inital value everywhere in the oven
T[0,:,:] = Toven
# initialise the tempearture of the potato
for i in range(0,Nx):
    for j in range(0,Ny):
        if (xap<=x[i]<=xbp) and (yap<=y[j]<=ybp):
            T[0,i,j] = Tpot
            alpha[i,j] = alphapot

# check the Courant condition
Courant = np.max(alpha) * dt/ dx**2

# compute the constant coefficient
cx = alpha * dt / dx**2
cy = alpha * dt / dy**2
print((cx,cy))

# compute the solution incrementally at subsequent time steps
for p in range(1,Nt):
    # compute at time step p, i.e. t = p * dt
    # do it for every node in the spatial grid
    # start with the boundaries
    T[p,0,:] = Tw # N
    T[p,Nx-1,:] = Tw # S
    T[p,:,0] = Tw # W
    T[p,:,Ny-1] = Tw # E
    # do the interior nodes
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            # apply the discretised equation
            T[p,i,j] = cx[i,j]*(T[p-1,i+1,j]+T[p-1,i-1,j]) + \
                       cy[i,j]*(T[p-1,i,j+1]+T[p-1,i,j-1]) + \
                       (1 - 2*cx[i,j] - 2*cy[i,j]) * T[p-1,i,j]



print( np.min(T[-1,:,:]) )

# plot surface or contour plot
(Yg, Xg) = np.meshgrid(y,x)
pl.contourf(Xg,Yg,T[-1,:,:])    
pl.colorbar()
pl.show()

