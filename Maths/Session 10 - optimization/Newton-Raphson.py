# Using Newton-Raphson method to find optimization
def func(x):
    return x**2 +(x-2)**3-4

def derivative(x):
    return 2*x + 3*(x-2)**2

def myNewton(x0, tol):
    x = x0
    err = 10*tol
    while err> tol:
        x1 = x - func(x) / derivative(x)
        err = abs(x1 - x)
    return x
