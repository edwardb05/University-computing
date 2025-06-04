import numpy as np
import matplotlib.pyplot as pl

# Calculating an
def calcan(x,y):
# Initiate answer
    an=0 
    # cycle through each x 
    for i in range(len(x)):
        res = 1
        # Cycle through remaining x's
        for j in range(len (x)):
            # If the x doesnt match the x we're currently on times our result by 1/ (xi-xj)
            if j != i:
                res= res*(1/(x[i]-x[j]))
        # add all the coefficients up
        an = an + y[i]*res


    return an

# Initialize x and y
x=[2,4,6,8]
y=[8,64,216,512]


print(calcan(x,y))