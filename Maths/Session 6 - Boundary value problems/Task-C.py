import numpy as np
import matplotlib.pyplot as plt


def MyGauss(A,b):
    
    # number of equations
    n = len(b)
    
    # eliminate the unknowns, from first to (n-1)th unknown, to form an upper triangular matrix
    for i in range(0,n-1):
        # eliminate the i-th unknown from the (i+1)th row downwards
        # i.e. set the zeros in column i.
        for j in range(i+1,n):
            # eliminate on row j

            # A(i,i) is the pivot coefficient
            p = A[j,i] / A[i,i]
        
            # compute the new elements of row j in matrix A
            # use slicing
            A[j,:] = A[j,:] - p * A[i,:]
            # or, alternatively, loop for every cell of row j
            #for k in range(i,n):
            #    A[j,k] = A[j,k] - p * A[i,k]

            # compute the new element of row j in vector b
            b[j] = b[j] - p * b[i]
    
    # evauate, by back substitution the solution
    # start from the last unknown and go upward till the first unknown
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        # contribution from b (right hand side of the equation)
        x[i] = b[i] / A[i,i]
        # contribution from the other (already evaluated) unknowns
        # (within the left hand side of the equation)
        for k in range(i+1,n):
            x[i] = x[i] - A[i,k] * x[k] / A[i,i]

    return x

def myfunc(x):
    K = 16.75
    R = 0.015
    fx = 1 / x
    gx = 0
    px = -10**8*np.exp(-x/R)/(x*K)
    return fx,gx,px

def myodebc(a,b,bca,bcb,N,R):

    # define the range
    x = np.linspace(a,b,N+1)
    # find the interval
    h = x[1] - x[0]


    # build a set of algebraic equation A * y = b
    # where A is N+1 by N+1
    A = np.zeros((N+1,N+1))
    b = np.zeros(N+1)
    # set the boundary conditions
    # boundary a: we need the forward scheme
    A[0,0] = R[1] - R[0]/h
    A[0,1] = R[0]/h
    b[0] = bca
    
    # boundary b: we need the backward scheme
    A[N,N-1] = -R[2]/h
    A[N,N] = R[2]/h + R[3]
    b[N] = bcb

        
    # set equations for the interior points
    for i in range(1,N):
        # evaluate the functions f, g and p at this x
        (f, g, p) = myfunc(x[i])
        A[i,i-1] = 1/h**2 - f / (2*h)
        A[i,i] = g - 2 / h**2
        A[i,i+1] = 1/h**2 + f / (2*h)
        b[i] = p
            
    #y = MyGauss(A,b)
    y = np.dot(np.linalg.inv(A),b)
    
    
    return (x,y)

# Vals given in q
h = 6*10**4
K = 16.75
R = 0.015
w = 0.003
Tw = 473

# 1
# set the b.c.
c = np.zeros(4)
# at boundary a
c[0] = 1
c[1] = 0
bca = -6.32*10**5 / K
# at boundary b
c[2] = 1
c[3] = h / K
bcb = h / K * Tw

(x,y) = myodebc(R,R+w,bca,bcb,50,c)
print(x)
print(np.where(np.isclose(x, 0.0156))[0])
print(y[np.where(np.isclose(x, 0.0156))[0]])
plt.plot(x,y, label='N=10', color='b', marker='o', linestyle='-', markersize=5)
plt.show()

