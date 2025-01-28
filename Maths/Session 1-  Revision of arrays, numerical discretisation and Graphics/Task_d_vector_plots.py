import numpy as np
import matplotlib.pyplot as pl
#  task d

# initialize a mesh grid
x = np.arange(-5,5+0.1,0.1)
y = x
(Xg, Yg) = np.meshgrid(x,y)

# find length of x axis
Nx = len(x)

# init an array with dimensions of Nx and 3 layers
F = np.ndarray( (Nx,Nx,2) )


# (a)

# sets i value of vextor to  x, this is encompassing 'xi' in the equation
#F[:,:,0] = Xg
# sets y value of vector to y, this is encompassing 'yj' in the equation
#F[:,:,1] = Yg

# (b)
F[:,:,0] = Yg
F[:,:,1] = -Xg
# plots a streamplot with i and j vector values
pl.streamplot(Xg,Yg,F[:,:,0],F[:,:,1])
pl.show()

