import numpy as np
import matplotlib.pyplot as plt

# Using the bisection method to find the root of a function

# Setting the function to find the new yn, ynd1 is the yn from timestep before
def func(yn, ynd1, h, t):
    # Use discretize function from the book
    ans = h**2*(-2*(yn-ynd1)/h + yn**2*np.sin(yn)-np.exp(yn)*t**2)
    return(ans)


def bisection_method(a,b,tol,ynd1,h,t):
        
    while abs(a-b)>tol:
        # calculate the mid point
        xm = (a + b) / 2
        # establish in which subinterval the solution lies
        # compute f(a) * f(xm)
        ff = func(a,ynd1,h,t) * func(xm,ynd1,h,t)
        if ff < 0: 
            # the solution lies in the left interval as the signs are different
            # set the upper bracket as xm
            b = xm
        else:
            # the solution lies in the right interval
            # set the lower bracket as xm
            a = xm
    
    # the true solution is bracketed within the latest interval [a,b]
    # we can approximate it with the midpoint
    sol = (a + b) / 2
    return sol





# set time domain
dt= 0.01
t = np.arange(0,5+dt,dt)

# initialize time and speed arrays
y= np.ndarray(len(t))
v=np.ndarray(len(t)-1)

# Set initial conditions
y[0] = 1
v[0]=0.5
y[1] =y[0]+v[0]*dt


# Iterate through each time step finding the new y
for i in range(2, len(t)):
    y[i] =bisection_method(-50,50,0.001 ,y[i-1],dt,t[i])
    v[i-1]= (y[i]- y[i-1])/dt


# Plotting the y results in blue
plt.plot(t,y, label='y against time', color='b')

# Plotting speed results in red 
plt.plot(t[:-1],v, label='speed against time', color='r')
plt.show()