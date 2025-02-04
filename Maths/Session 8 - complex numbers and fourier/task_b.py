import numpy as np
import matplotlib.pyplot as plt
# # bode plots
# def func1(omega):
#     y =1/(1+0.1*1j*omega)
#     return y

# omega = np.linspace(0,10000,10000)
# H= func1(omega)
# Hamp= abs(H)
# Hdecibel= 20* np.log10(H)
# Hphase = np.arctan2(H.imag,H.real)*180/np.pi # phase of H, in degree

# plt.subplot(3, 1, 1)
# plt.semilogx(omega,H,'r') #plot with a logarithmic x -axis
# plt.xlabel('w (rad/s)',fontsize=20)
# plt.ylabel('|H|',fontsize=20)
# plt.grid()
# plt.subplot(3, 1, 2)
# plt.semilogx(omega,Hdecibel,'r')
# plt.xlabel('w (rad/s)',fontsize=20)
# plt.ylabel('|H| dB',fontsize=20)
# plt.grid()
# plt.subplot(3, 1, 3)
# plt.semilogx(omega,Hphase,'r')
# plt.xlabel('w (rad/s)',fontsize=20)
# plt.ylabel('Ph H',fontsize=20)
# plt.grid()
# plt.show()


# Electronic circuits
# def func1(omega):
#     y =1/(1+(1/2)*((1+1j*omega*2*2)/(1+1j*omega*1*1)))
#     return y

# omega = np.linspace(0.001,10,1000)
# H= func1(omega)
# Hamp= abs(H)
# Hdecibel= 20* np.log10(H)
# Hphase = np.arctan2(H.imag,H.real)*180/np.pi # phase of H, in degree
# plt.subplot(3, 1, 1)
# plt.semilogx(omega,H,'r') #plot with a logarithmic x -axis
# plt.xlabel('w (rad/s)',fontsize=20)
# plt.ylabel('|H|',fontsize=20)
# plt.grid()
# plt.subplot(3, 1, 2)
# plt.semilogx(omega,Hdecibel,'r')
# plt.xlabel('w (rad/s)',fontsize=20)
# plt.ylabel('|H| dB',fontsize=20)
# plt.grid()
# plt.subplot(3, 1, 3)
# plt.semilogx(omega,Hphase,'r')
# plt.xlabel('w (rad/s)',fontsize=20)
# plt.ylabel('Ph H',fontsize=20)
# plt.grid()
# plt.show()

# Cascading filters 
#H1
def func1(omega):
    y =1/(1+1j*0.01*omega)
    return y
# H2
def func2(omega):
    y =(1j*40*omega)/(1+1j*40*omega)
    return y

omega = np.linspace(0.0001,10000,1000)
H1= func1(omega)
H2 = func2(omega)
H = H1*H2
Hamp= abs(H)
Hdecibel= 20* np.log10(H)
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