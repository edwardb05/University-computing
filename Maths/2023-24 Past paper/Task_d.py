import matplotlib.pyplot as plt
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


R = 10
r=4
# set the step intervals in x and y
dx = 0.01
dy = 0.01

# set the x range, not including the boundaries
x = np.arange(-14+dx,14,dx)
N = len(x)
# the y range depends of the various values of x, and cannot be fixed here

# integrate in dy, for all the value of x, i.e. find G(x)

G = np.zeros(N)
# for every x
for i in range(0,N):
    if x[i] <= 6 and x[i]>= -6:

        # determine the boundaries m and p for this x
        mx = np.sqrt(-x[i]**2+(R-r)**2)
        px = np.sqrt(-x[i]**2+(R+r)**2)

        # set the y points for this x, not including the boundaries
        y = np.concatenate([np.arange(-px+dy,-mx,dy),np.arange(mx+dy,px,dy)])
    else:
        mx = np.sqrt(-x[i]**2+(R+r)**2)
        y = np.arange(-mx+dy,mx,dy)

    z = np.zeros(len(y))
    # determine the values of the function z(x,y)
    for j in range(0,len(y)):
        z[j] = np.sqrt(r**2-(R-np.sqrt(x[i]**2+y[j]**2))**2) 
    
    # integrate in dy from cx to dx (for this specific x)
    G[i] = trapz(y,z) # G(x)

# integrate G(x) in dx
I = 2*trapz(x,G)

print(I)

# plot the dome

# set domain by using the two angles t and p
# Create a mesh grid
x = np.linspace(-20, 20, 1000) 

y = np.linspace(-20, 20, 1000)
X, Y = np.meshgrid(x, y)


# Calculate the coordinates of points on the ellipsoid surface

Z = np.sqrt( r**2 - ( R-np.sqrt(X**2+Y**2) )**2 )
    

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='Oranges')
ax.plot_surface(X, Y, -Z, cmap='Oranges')

# Set labels and title
ax.set_title("Dougnyt")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')
ax.view_init(15, 60)
plt.show()



