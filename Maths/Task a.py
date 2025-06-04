import numpy as np
import matplotlib.pyplot as pl

amplitude = [5, 2, 0, 3, 1, 8, 2, 3, 7, 6]
shift = [1/2, 1, 1/2, 0, 3/2, 1, 0, 3/2, 1, 0]
dt = 0.01
t = np.arange(0, 2*np.pi, dt)

# Plot individual sine waves
for i in range(len(amplitude)):
    y = amplitude[i] * np.sin((i+1) * t + np.pi * shift[i])
    pl.plot(t, y)
pl.title("Individual Sine Components")
pl.show()

# Sum of all sine waves
ytotal = np.zeros(len(t))
for i in range(len(amplitude)):
    y = amplitude[i] * np.sin((i+1) * t + np.pi * shift[i])
    ytotal += y

pl.plot(t, ytotal)
pl.title("Sum of All Sine Components")
pl.grid()
pl.show()

def DFT(yn):
    # y: values of the function, in time domain
    N = len(yn)
    w = 2*np.pi/N
    FTk = np.zeros(N,dtype=complex)
    for k in range(0,N):
        for n in range(0,N):
            FTk[k] += np.exp(-1j*k*w*n)*yn[n]
    return FTk

FTk = DFT(ytotal)
Nt = len(t)
df = 1/(Nt*dt) # frequency step
f = np.arange(0,1/dt,df)
pl.bar(f[:int(Nt/2)]*2*np.pi,abs(FTk[:int(Nt/2)]),width=0.04,color='b')
pl.grid()
pl.axis([0,30,0,1000])
pl.show()