import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
m1 = 1
m2 = 1
g=9.81
l1=1
l2=0.5

# Define the system of ODEs
def func1(td1):
    
    # Rate of change of Susceptible individuals (S)
    dy = td1
    return dy

def func2( t1,td1,t2,td2,):
    # Rate of change of Infected individuals (I)
    dy = (m2*g*np.sin(t2)*np.cos(t1-t2)-m2*np.sin(t1-t2)*(l1*td1**2*np.cos(t1-t2)+l2*td2**2)-(m1+m2)*g*np.sin(t1))/l1*(m1+m2*(np.sin(t1-t2))**2)
    return dy

def func3(td2):
    
    # Rate of change of Susceptible individuals (S)
    dy = td2
    return dy

def func4( t1,td1,t2,td2,):
    # Rate of change of Infected individuals (I)
    dy = ((m1+m2)*(l1*td1**2*np.sin(t1-t2)+g*np.sin(t1)*np.cos(t1-t2)-g*np.sin(t2))+m2*l2*td2**2*np.sin(t1-t2)*np.cos(t1-t2))/l2*(m1+m2*(np.sin(t1-t2)**2))
    return dy

# Forward Euler Method for the system of ODEs
def FwEulerN(t0, te, h, Y0, ):
    # Time points
    t = np.arange(t0, te + h, h)
    
    # Create an array to store solutions, each row corresponds to S, I, R
    Y = np.zeros((len(t), 4))  # 3 columns for S, I, R

    # Initial conditions
    Y[0,:] = Y0

    
    
    # Implement the Forward Euler method
    for i in range(len(t) - 1):
        t1, td1,t2,td2 = Y[i, 0], Y[i, 1], Y[i, 2], Y[i, 3]
        
        # Update each component using the respective ODEs
        Y[i + 1, 0] = Y[i, 0] + h * func1(td1,)  # Update P
        Y[i + 1, 1] = Y[i, 1] + h * func2(t1,td1,t2,td2)  # Update N
        Y[i + 1, 2] = Y[i, 2] + h * func3(td2)  # Update N
        Y[i + 1, 3] = Y[i, 3] + h * func4(t1,td1,t2,td2)  # Update N
  
    
    # Return the time points and the solution (S, I, R)
    return t, Y

t0 = 0
Y0 = [np.pi/4,0,-np.pi/4,0]  # Initial conditions
te = 4       # Total time period (in months)
h = 0.002      # Step size (in months), ensure it's a float

# Create time array from t0 to te with step size h
t = np.arange(t0, te + h, h)

t1,y1 = FwEulerN(t0,te,h,Y0)

print(t1)
print(y1)
