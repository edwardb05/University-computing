import numpy as np
import matplotlib.pyplot as plt

# Define the system of ODEs
def func1( P,N):
    # Rate of change of Susceptible individuals (S)
    dy = 0.3*P*N-0.8*P
    return dy

def func2(P, N, ):
    # Rate of change of Infected individuals (I)
    dy = 1.1*N- N *P
    return dy

# def func3(S, I, R, b):
#     # Rate of change of Recovered individuals (R)
#     dy = b * I
#     return dy

# Forward Euler Method for the system of ODEs
def FwEulerN(t0, te, h, Y0, ):
    # Time points
    t = np.arange(t0, te + h, h)
    
    # Create an array to store solutions, each row corresponds to S, I, R
    Y = np.zeros((len(t), 2))  # 3 columns for S, I, R

    # Initial conditions
    Y[0, :] = Y0
    
    # Implement the Forward Euler method
    for i in range(len(t) - 1):
        P, N = Y[i, 0], Y[i, 1],
        
        # Update each component using the respective ODEs
        Y[i + 1, 0] = Y[i, 0] + h * func1(P,N)  # Update P
        Y[i + 1, 1] = Y[i, 1] + h * func2(P, N, )  # Update N
  
    
    # Return the time points and the solution (S, I, R)
    return t, Y

t0 = 0
Y0 = [0.8, 7]  # Initial conditions
te = 40         # Total time period (in months)
h = 0.005       # Step size (in months), ensure it's a float

# Create time array from t0 to te with step size h
t = np.arange(t0, te + h, h)

t1,y1 = FwEulerN(t0,te,h,Y0)


print(y1)
