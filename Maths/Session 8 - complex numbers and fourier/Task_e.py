import numpy as np
import matplotlib.pyplot as plt

def DFT(yn):
    N= len(yn)
    FT = np.zeros(N)
    for k in range(0,N):
        FTk =0
        for n in range(0,N):
            FTk+= yn[n]*np.exp((-2*np.pi*1j*k*n)/N)
        FT[k] = FTk
    return FT

## Natural resonating frequency 
# with open('Session 8 - complex numbers and fourier/Vibration.txt','r') as file:
#     y = [float(line.strip()) for line in file]
# print(y)
# y = np.array(y)
# tend = len(y)*0.01
# time = np.arange(0, tend, 0.01)
# N= len(y)

# df = 1/(N*0.01) # frequency step
# f = np.arange(0,1/0.01,df)

# # DFT
# FTk = DFT(y)

# plt.plot(time,y,'b')
# plt.xlabel('time (s)',fontsize=20)
# plt.ylabel('Displacement',fontsize=20)
# plt.grid()
# plt.show()
# # spectrum
# plt.plot(f[:int(N/2)]*2*np.pi,20*np.log10(abs(FTk[:int(N/2)])),color='r')
# plt.grid()
# plt.axis([0,f[int(N/2)]/2,0,50])
# plt.xlabel('omega (rad/s)',fontsize=20)
# plt.ylabel('|Vo|',fontsize=20)
# plt.show()

#Gaussian signal