import numpy as np

# Using the bisection method to find the root of a function
def funcx(x):
    return 30*np.sin((30*2*np.pi)/360)-x

def funcz(x):
    return 30 +30*np.cos((30*2*np.pi)/360)-x

def bisection_method(a,b,tol, func):
        
    while abs(a-b)>tol:
        # calculate the mid point
        xm = (a + b) / 2
        # establish in which subinterval the solution lies
        # compute f(a) * f(xm)
        ff = func(a) * func(xm)
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
    if func(sol) <0.01:
        return sol
    else:
        return "No solution found in range"

print(bisection_method(0,30,0.001, funcx))
print(bisection_method(0,60,0.001, funcz))