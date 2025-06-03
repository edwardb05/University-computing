import numpy as np
import matplotlib.pyplot as plt

# Part a
# Transfer fuction
def func1(omega):
    y =(1j*0.1*omega)/(1+1j*0.1*omega)
    return y


omega = np.arange(0.1,10000,1000)
omega = np.logspace(-1,4,1000) #For logarithmically spacing out nodes
H= func1(omega)

# Finding the amplitude
Hamp= abs(H)
# Converting amp to decibels
Hdecibel= 20* np.log10(H)
# Calculating phase
Hphase = np.arctan2(H.imag,H.real)*180/np.pi # phase of H, in degree

plt.subplot(3, 1, 1)
plt.semilogx(omega,H,'r') #plot with a logarithmic x -axis
plt.xlabel('w (rad/s)',fontsize=20)
plt.ylabel('|H|',fontsize=20)
plt.grid()
plt.subplot(3, 1, 2)
plt.semilogx(omega,Hdecibel,'r')
plt.xlabel('w (rad/s)',fontsize=20)
plt.ylabel('|H| dB',fontsize=20)
plt.grid()
plt.subplot(3, 1, 3)
plt.semilogx(omega,Hphase,'r')
plt.xlabel('w (rad/s)',fontsize=20)
plt.ylabel('Ph H',fontsize=20)
plt.grid()
plt.show()

# Part b
def funcpartb(t):
    y = np.exp(-((t-3)**2)/0.1)
    return y

# Setting time domain
dt= 0.01
t = np.arange(0,6+dt,dt)

# Discretizing y
yi = funcpartb(t)

# Plotting
plt.scatter(t,yi)
plt.xlabel('t (s)',fontsize=20)
plt.ylabel('yi',fontsize=20)
plt.grid()
plt.show()

###Part C

# Discrete fourier transform
def DFT(yn):
    N= len(yn)
    FT = np.zeros(N)
    for k in range(0,N):
        FTk =0
        for n in range(0,N):
            FTk+= yn[n]*np.exp((-2*np.pi*1j*k*n)/N)
        FT[k] = FTk
    return FT

yif = DFT(yi)

N = len(t)  # number of discrete points available
# build the frequency domain axis
df = 1/(N*dt) # frequency step
f = np.arange(0,1/dt,df)
plt.bar(f,abs(yif),width=0.04,color='b')
plt.axis([0,20,0,50])
plt.grid()
plt.xlabel('f (Hz)',fontsize=20)
plt.ylabel('FT',fontsize=20)
plt.show()

####Part D 
# Find omega for each frequancy 
w = 2*np.pi*f
# evaluate H(w) at these w
H = 1j*w*0.1 / (1+1j*w*0.1)

yof = H*yif

plt.bar(f,abs(yof),width=0.04,color='b')
plt.axis([0,20,0,20])
plt.grid()
plt.xlabel('f (Hz)',fontsize=20)
plt.ylabel('FT',fontsize=20)
plt.show()

####Part E 

def DFTinv(FT):
    N= len(FT)
    y = np.zeros(N)
    for n in range(0,N):
        Yn =0
        for k in range(0,N):
            Yn += FT[k]*np.exp((2*np.pi*1j*k*n)/N)
        y[n] = Yn
    return y

yo = DFTinv(yof)

plt.scatter(t,yo)
plt.xlabel('t (s)',fontsize=20)
plt.ylabel('yo',fontsize=20)
plt.grid()
plt.show()
