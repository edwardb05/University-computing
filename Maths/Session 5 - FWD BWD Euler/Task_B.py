import numpy as np



def func(t,y):
    dy= -2*y*t -2*t**3
    return dy

def BwEuler(t0, y0, h, te):
    # init t array
    t = np.arange(t0, te+h, h)
    y = np.zeros(len(t))
    # set init conditions
    y[0] = y0
    
    
    for i in range(1,len(t)):
        
        y[i] = (y[i-1]-2*h*t[i]**3)/(1+2*h*t[i]) 
    
    # Return the time points and solution values
    return t, y

