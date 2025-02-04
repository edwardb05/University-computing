import numpy as np
import matplotlib.pyplot as plt

# fourier series 

# Saw wave
def func1(N,T,t):
    Nt = len(t)
    y = np.zeros(Nt)
    for n in range(1,N+1):
        y += 1/n*np.sin((2*n*np.pi)/T*t)
    y = 0.5 - y/np.pi
    return y

# Sqaure wave
def Square(t,N,T):
    # t: time axis
    # N: number of terms from the series
    # T: period of the function
    Nt = len(t)
    L = T/2
    y = np.zeros(Nt)
    for n in range(1,N+1,2): #Odd numbers only
        y += 1/n*np.sin(n*np.pi/L*t)
    y = 4*y/np.pi
    return y

T= 5
N =8
t= np.linspace(0,2*T,1000)
y= Square(t,N,T)
plt.plot(t,y)
plt.show()
print(t[20])
print(y[20])