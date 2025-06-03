import numpy as np
import matplotlib.pyplot as pl



def FwEulerN(t0, te, h, Y0, ):

    # Time points
    t = np.arange(t0, te + h, h)
    
    # Create an array to store solutions, each row corresponds to a different y
    Y = np.zeros((len(t), 4))  # 4 columns for each y

    # Initial conditions
    Y[0, :] = Y0
    
    # Implement the Forward Euler method
    for i in range(len(t) - 1):
        P, N = Y[i, 0], Y[i, 1],
        
        # Update each component using the respective ODEs
        Y[i + 1, 0] = Y[i, 0] + h * Y[i, 1]  # Update y1
        Y[i + 1, 1] = Y[i, 1] + h * Y[i, 2] # Update y2
        Y[i + 1, 2] = Y[i, 2] + h * Y[i, 3]  # Update y3
        Y[i + 1, 3] = Y[i, 3] + h * (-1*Y[i,0]-2*Y[i,2]+3*np.sin(t[i]) -5*np.cos(t[i])) # Update y4
  
    
    # Return the time points and the solution (S, I, R)
    return t, Y

t0 = 0
te = 15
h= 0.01

Y0= [5,8,3,10]
t,Y = FwEulerN(t0,te,h,Y0)

pl.plot(t,Y[:,0],c='Red')
pl.grid()
pl.show()


pl.plot(t,Y[:,2],c='Red')
pl.grid()
pl.show()