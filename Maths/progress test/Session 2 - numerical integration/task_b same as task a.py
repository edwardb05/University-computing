# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:54:45 2024

@author: eb1723
"""
# same as task b with new intergral
# equidistant nodes
import numpy as np
import matplotlib.pyplot as plt
def integrate(b):
    a = 0
    N = 4  # Number of intervals
    
    # Define the function f 
    def f(x):
        return 1 / np.sqrt(x**1.10 + 2023)
    
    x = np.linspace(a, b, N)
    y = f(x)

    # Trapezoidal rule integration
    I = ((b - a) / (N - 1)) * (y[0] / 2 + np.sum(y[1:-1]) + y[-1] / 2)

    print("Integration result:", I)
    return I

# integrate with a list of values
blist =[10,100,1000,10000]
I_values =[]
for b in blist:
    I_values.append( integrate(b))

plt.scatter(blist,I_values)
plt.show()



