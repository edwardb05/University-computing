import numpy as np
import matplotlib.pyplot as plt
from Task_B import BwEuler
def analyticalfunc(t,t0,y0):
    
    c = (y0 - 1 + t0**2) * np.exp(t0**2)
    y= 1- t**2 + c*np.exp(-t**2)
    return y
    


def func(t,y):
    dy= -2*y*t -2*t**3
    return dy


def FwEuler(t0, y0, h, te):
    # init t array
    t = np.arange(t0, te+h, h)
    y = np.zeros(len(t))
    # set init conditions
    y[0] = y0
    
    
    for i in range(len(t) - 1):
        
        y[i + 1] = y[i] + h * func(t[i], y[i])
    
    # Return the time points and solution values
    return t, y



def ODERK4(t0, y0, h, te):
    N = int((te - t0) / h) + 1  # Number of steps
    t = np.linspace(t0, te, N)  # Time array
    y = np.zeros(N)  # Solution array
    y[0] = y0
    
    for i in range(N - 1):
        k1 = h * func(t[i], y[i])
        k2 = h * func(t[i] + h / 2, y[i] + k1 / 2)
        k3 = h * func(t[i] + h / 2, y[i] + k2 / 2)
        k4 = h * func(t[i] + h, y[i] + k3)
        
        y[i + 1] = y[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    
    return t, y



t0 = 0
y0 = -10
te = 100
h=0.1

t = np.arange(t0, te+h, h)

t1,y1 = FwEuler(t0,y0,h,te)
t2,y2 = ODERK4(t0,y0,h,te)
t3,y3 = BwEuler(t0,y0,h,te)
y4 = analyticalfunc(t,t0,y0)

print(y1)
print(y2)
print(y3)
print(y4)

plt.figure(figsize=(10, 6))  # Set the figure size

# Plot each dataset
plt.plot(t1, y1, label='fw', color='blue')      # First dataset
plt.plot(t2, y2, label='rk', color='red')     # Second dataset
plt.plot(t3, y3, label='bw', color='green')   # Third dataset
plt.plot(t, y4, label='analytical', color='purple')

# Add titles and labels
plt.title('Plot of Sine, Cosine, and Tangent Functions')
plt.xlabel('X values')
plt.ylabel('Y values')

# Show legend
plt.legend()

# Set limits for y-axis to avoid extreme values of tangent
plt.ylim(-10, 10)  # Adjust y-axis limits for better visualization

# Show the grid
plt.grid()

# Display the plot
plt.show()
        
