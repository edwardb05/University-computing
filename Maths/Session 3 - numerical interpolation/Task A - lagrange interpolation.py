import numpy as np
import matplotlib.pyplot as pl

# Function to interpolate (sin(x) in this case)



xn = [0,1,2]


#
# Lagrange Basis Polynomial
def Langragian(j, xp, xn):
    res = 1
    for k in range(len(xn)):
        if k != j:
            res *= (xp - xn[k]) / (xn[j] - xn[k])
    return res

for j in range(3):
    print(Langragian(j,1.25,xn))

# # Lagrange Interpolation Function
# def LagInterp(xn, yn, x):  
#     y = []
#     for xi in x:
#         yf = 0
#         # Look through notes for langragian interpolation definition
#         for j in range(len(xn)):  # Loop through all the known points
#             yf += yn[j] * Langragian(j, xi, xn)  # Apply Lagrange formula
#         y.append(yf)
#     return y



# # # Define the known data points (xn and their corresponding function values yn)
# # xnlin = [1, 2]
# # xnquad = [1, 1.5, 2]
# # xncub = [1, 4/3, 5/3, 2]

# # # Generate corresponding function values for the known points
# # ynlin = func(np.array(xnlin))
# # ynquad = func(np.array(xnquad))
# # yncub = func(np.array(xncub))

# # # Define x values for interpolation (in this case, from 0 to 3 with step 0.05)
# # x = np.arange(0, 3.05, 0.05)
# # print(x[22])
# # # Apply Lagrange interpolation to the cubic set of data points
# # y_interpolated = LagInterp(xncub, yncub, x)
# # print(y_interpolated[22])
# # # Plot the Lagrange Interpolation result (Red curve)
# # pl.plot(x, y_interpolated, c='Red', label='Lagrange Interpolation')

# # # Plot the initial nodal points (Blue dots)
# # pl.scatter(xncub, yncub, c='Blue', label='Data Points')

# # # Plot the actual function (Green curve)
# # pl.plot(x, func(x), c='Green', label='Actual Function (sin(x))')



# # # Show the plot
# # pl.show()



# # # Task A4
# # # error analysis

# # a = 1 # lower interval
# # b = 2 # upper interval
# # xp = np.array(1.25)

# # y = []
# # for Nx in range(2,17):
# #     xn = np.linspace(a,b,Nx)
# #     yn = func(xn)
# #     y += [LagInterp(xn,yn,xp)]
    
# # # compute the basic error 
# # y = np.array(y)
# # for i in range(0,14):
# #     error = y[i+1] - y[i]
# #     print(i+1,error)
# #     pl.scatter(i+1,np.log(error))
# # pl.show()
