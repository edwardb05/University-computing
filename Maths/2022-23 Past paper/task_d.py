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



# set the step intervals in x and y
dx = 0.01
dy = 0.01

# set the x range, not including the boundaries
x = np.arange(-3+dx,3,dx)
N = len(x)
# the y range depends of the various values of x, and cannot be fixed here

# integrate in dy, for all the value of x, i.e. find G(x)

G = np.zeros(N)
# for every x
for i in range(0,N):
    # determine the boundaries m and p for this x
    mx = np.sqrt(4*(1-x[i]**2/9))
    px = mx
    # set the y points for this x, not including the boundaries
    y = np.arange(-mx+dy,px,dy)
    z = np.zeros(len(y))
    # determine the values of the function z(x,y)
    for j in range(0,len(y)):
        z[j] = x[i]**2+y[j]**2 
    
    # integrate in dy from cx to dx (for this specific x)
    G[i] = trapz(y,z) # G(x)

# integrate G(x) in dx
I = trapz(x,G)

print(I)

# plot the dome

# set domain by using the two angles t and p
# Create a mesh grid
x = np.linspace(-3, 3, 50) 
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)
X[X**2/9+Y**2/4>1] = 0
Y[X**2/9+Y**2/4>1] = 0
# Calculate the coordinates of points on the ellipsoid surface

Z = X**2+Y**2

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='Oranges')

# Set labels and title
ax.set_title('Royal Albert Hall dome')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')
ax.view_init(15, 60)
plt.show()