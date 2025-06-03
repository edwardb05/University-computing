import numpy as np
def func1(t):
    y =np.exp(-((t-5)**2)/4)
    return y
    
def DFT(yn):
    # y: values of the function, in time domain
    N = len(yn)
    w = 2*np.pi/N
    FTk = np.zeros(N,dtype=complex)
    for k in range(0,N):
        for n in range(0,N):
            FTk[k] += np.exp(-1j*k*w*n)*yn[n]
    return FTk


# 
def DFTinv(FT):
    N= len(FT)
    y = np.zeros(N)
    for n in range(0,N):
        Yn =0
        for k in range(0,N):
            Yn += FT[k]*np.exp((2*np.pi*1j*k*n)/N)
        y[n] = Yn
    return y

t0 = 0
tend = 6*np.pi
dt = 0.1
t = np.arange(t0,tend+dt,dt)
N = len(t)  # number of discrete points available
# build the frequency domain axis
df = 1/(N*dt) # frequency step
f = np.arange(0,1/dt,df)

y = func1(t)

FTk = DFT(y)

print(f[7])
print(FTk[7])