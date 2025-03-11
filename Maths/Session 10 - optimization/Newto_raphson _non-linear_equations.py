# newton Raphson method for solving non-linear equations
import numpy as np

# set of functions of the system
def sysfuncs(X):
    # X is a one dimensional vector with as many elements as the number of functions, i.e. u, v, etc.
    # define a vector for the output
    UV = np.ndarray(len(X))
    # evaluate all the functions at point X
    # X is a vector long as the number of independent variables, i.e. x, y, etc.
    # alter and write here the various functions
    UV[0] = X[0]**2 + 1 - X[1]
    UV[1] = 2*np.cos(X[0]) - X[1]
    return UV

def Jacobian(X,Dx):
    # establish how many functions/independent variables, aka the size of the Jacobian
    N = len(X)
    # set an empty array N x N
    Jac = np.ndarray((N,N))
    # calculate and fill column by column, i.e. derivative of each function with respect to the same
    # independent variable
    # We will apply the central difference scheme for the derivative:
    # df/dx = (f at successive point - f at previous point) / dx
    for i in range(N):
        # set the successive point for the independend variable in question
        X[i] += Dx[i]
        # evaluate all the functions at this point
        Fplus = sysfuncs(X)
        # set the precedent point for the independend variable in question
        X[i] -= 2*Dx[i]
        # evaluate all the functions at this point
        Fminus = sysfuncs(X)
        # determine the derivatives for the column ith
        Jac[:,i] = (Fplus - Fminus) / (2*Dx[i])
    return Jac

def MatVect(A,b):
    # this function performs matrix-vector multiplication
    N = A.shape[0]
    y = np.zeros(N)
    for i in range(N):
        for k in range(N):
            y[i] += A[i,k] * b[k]
    return y

# solve a set of non linear equations
# set the accuracy requested
eps = 0.001
# set the initial guess
X0 = np.array([0.2, 1.8])

# set dx (of the order of or smaller than eps)
Dx = np.array([0.5*eps, 0.5*eps])
# set initial guess as solution
Xn = X0
# set the error large enough, to enter the loop once
err = 10*eps
# repeat while the error is too large
while err > eps:
    # set the current solution as old solution
    Xp = Xn
    # compute teh Jacobian
    J = Jacobian(Xn,Dx)
    # invert the Jacobian
    Jinv = np.linalg.inv(J)
    # apply Newton's methods
    Xn = Xp - MatVect(Jinv,sysfuncs(Xn))
    # assess the error: consider the maximum error, amongst errors for all variables
    err = np.max(np.abs(Xn-Xp))


print(Xn)
