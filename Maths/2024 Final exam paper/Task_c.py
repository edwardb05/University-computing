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
x = np.arange(0+dx,2*np.pi,dx)
N = len(x)
# the y range depends of the various values of x, and cannot be fixed here

# integrate in dy, for all the value of x, i.e. find G(x)

G = np.zeros(N)
# for every x
for i in range(0,N):

    # determine the boundaries m and p for this x
    mx = np.sin(x[i])
    px = 0
    if mx >= 0:
        y = np.arange(px+dy,mx,dy)
    elif mx<= 0:
        y = np.arange(mx+dy,px,dy)
    z = np.zeros(len(y))
    # determine the values of the function z(x,y)
    for j in range(0,len(y)):
        z[j] = np.sin(x[i]*y[j])
    
    # integrate in dy from cx to dx (for this specific x)
    G[i] = trapz(y,z) # G(x)

# integrate G(x) in dx
I = trapz(x,G)

print(I)



# set domain by using the two coordinates x and y and splitting it into positive and negative sin(x)
x1 = np.linspace(0, np.pi, 1000) 

y1 = np.linspace( 0,1, 1000)
# Create a mesh grid
X1, Y1 = np.meshgrid(x1, y1)
print(X1)
print(Y1)
# Setting the limits for the first half of the sine wave
X1[Y1-np.sin(X1)>0] = 0
X1[Y1<0 ] = 0
Y1[Y1-np.sin(X1)>0 ] = 0
Y1[Y1<0 ] = 0
Z1= np.sin(X1*Y1)

# set domain by using the two coordinates x and y for the negative part
x2 = np.linspace(np.pi, np.pi*2 ,1000) 
y2 = np.linspace(-1,0, 1000)
# Create a mesh grid
X2, Y2 = np.meshgrid(x2, y2)


# Setting the limits for the second half of the sine wave
X2[Y2-np.sin(X2)<0 ] = 0
X2[Y2>0 ] = 0
Y2[Y2-np.sin(X2)<0 ] = 0
Y2[Y2>0 ] = 0
# Calculate the coordinates of points on the sine wave surface
Z2= np.sin(X2*Y2)
    

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, Y1, Z1, cmap='Oranges')
ax.plot_surface(X2, Y2, Z2, cmap='Oranges')

# Set labels and title
ax.set_title("Plotting sin(x*y) on sin(x)")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')
ax.view_init(15, 60)
plt.show()



