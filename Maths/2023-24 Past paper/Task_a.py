import numpy as np 
import matplotlib.pyplot as pl


Nc = 10
w = np.linspace(1,10,10)
amplitudes = np.array([5,2,0,3,1,8,2,3,7,6])
phase = np.array([np.pi/2,np.pi,np.pi/2,0,3/2*np.pi,np.pi,0,3/2*np.pi,np.pi,0])

# a
dt = 0.01
t = np.arange(0,2*np.pi+dt,dt)

for i in range(Nc):
    yc = amplitudes[i]*np.sin(w[i]*t+phase[i])
    pl.plot(t,yc)
pl.grid()
pl.show()

# b
y= np.ndarray(len(t))
for j in range(0,len(t)):
    for i in range(Nc):
        y[j]+= amplitudes[i]*np.sin(w[i]*t[j]+phase[i])


pl.plot(t,y)
pl.grid()
pl.show()

# C

def DFT(yn):
    N= len(yn)
    FT = np.zeros(N)
    for k in range(0,N):
        FTk =0
        for n in range(0,N):
            FTk+= yn[n]*np.exp((-2*np.pi*1j*k*n)/N)
        FT[k] = FTk
    return FT

def DFT(yn):
    # y: values of the function, in time domain
    N = len(yn)
    w = 2*np.pi/N
    FTk = np.zeros(N,dtype=complex)
    for k in range(0,N):
        for n in range(0,N):
            FTk[k] += np.exp(-1j*k*w*n)*yn[n]
    return FTk


FT = DFT(y)
Nt = len(t)
df = 1/(Nt*dt) # frequency step
f = np.arange(0,1/dt,df)
pl.bar(f[:int(Nt/2)]*2*np.pi,abs(FT[:int(Nt/2)]),width=0.04,color='b')
pl.grid()
pl.axis([0,30,0,1000])
pl.show()
print("this is the result")
print(f[0],f[-1])
