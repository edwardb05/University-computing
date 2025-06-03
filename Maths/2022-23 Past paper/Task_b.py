import numpy as np 
import matplotlib.pyplot as plt


# Using the bisection method to find the root of a function
def func(theta, thetan1, thetan2, dt):
    ans = (theta - 2*thetan1+ thetan2)/dt**2 +c/m*(theta - thetan1)/dt +(g/L)*np.sin(theta)
    print(ans)
    return(ans)
def bisection_method(a,b,tol,thetan1,thetan2):
        
    while abs(a-b)>tol:
        # calculate the mid point
        xm = (a + b) / 2
        # establish in which subinterval the solution lies
        # compute f(a) * f(xm)
        ff = func(a,thetan1,thetan2,dt) * func(xm,thetan1, thetan2,dt)
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
    # if func(sol, thetan1,thetan2,dt) <0.03:
    #     return sol
    # else:
    #     return "No solution found in range"




# Set constants
g=9.81
m=10
c= 0.001
L= 2
# set time domain
dt= 0.1
t = np.arange(0,20.1,dt)

theta = np.ndarray(len(t))
v=np.ndarray(len(t)-1)
theta[0] = 45
theta[1] =45 
v[0]=0

for i in range(2, len(t)):
    theta[i] =(bisection_method(-np.pi,np.pi,0.001 ,thetan1=(np.pi*2*theta[i-1])/360, thetan2=(np.pi*2*theta[i-2])/360))*180/np.pi
    v[i-1]= (theta[i]- theta[i-1])/dt



plt.plot(t,theta, label='angle against time', color='b')
plt.plot(t[:-1],v, label='speed against time', color='r')
plt.show()