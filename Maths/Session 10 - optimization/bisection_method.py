# Using the bisection method to find the root of a function
def func(x):
    return x**2 +(x-2)**3-4

def bisection_method(a,b,tol):
        
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

print(bisection_method(0,5,0.000001))