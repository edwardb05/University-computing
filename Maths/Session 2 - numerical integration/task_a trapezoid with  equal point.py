# # -*- coding: utf-8 -*-
# # equidistant nodes
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# intergration with trapezoid rule (see notes for definition) b is end condination
def integrate(b):
    a = np.sqrt(2)
    h= 0.01  # Number of intervals
    
    # Define the function f 
    def f(x):
        return (1/np.sqrt(x)) + np.sqrt(x)
    
    x = np.arange(a, b+0.01, h )
    
    print(x)
    
    
    N = len(x)
    y = f(x)
    print(y)
    # Trapezoidal rule integration
    I = ((b - a) / (N - 1)) * (y[0] / 2 + np.sum(y[1:-1]) + y[-1] / 2)

    print("Integration result:", I)
    return I



print(integrate(np.sqrt(23))) 


# blist =[10,100,1000,10000]
# I_values =[]
# for b in blist:
# #     I_values.append( intergrate(b))
# # print(I_values)
# plt.scatter(blist,I_values)
# plt.show()

## task 3
# import numpy as np
# import matplotlib.pyplot as plt
# def integrate(b):
#     a = 0
#     N = 4  # Number of intervals
    
#     # Define the function f 
#     def f(x):
#         return 1 / np.sqrt(x**17.10 + 2023)
    
#     x = np.linspace(a, b, N)
#     y = f(x)

#     # Trapezoidal rule integration
#     I = ((b - a) / (N - 1)) * (y[0] / 2 + np.sum(y[1:-1]) + y[-1] / 2)

#     print("Integration result:", I)
#     return I

# blist =[10,100,1000,10000]
# I_values =[]
# for b in blist:
#     I_values.append( intergrate(b))
# print(I_values)
# plt.scatter(blist,I_values)
# plt.show()
