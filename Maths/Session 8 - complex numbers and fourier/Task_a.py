import numpy as np
import matplotlib.pyplot as plt

# # Plotting sine waves

# def func1 (x):
#     y = 10*np.sin(np.pi*x)
#     return y

# def func2(x):
#     y = 5*np.sin(np.pi*x + np.pi/2)
#     return y

# x = np.linspace(0,2*np.pi,1000)

# y1 = func1(x)
# y2 = 5 + func2(x) # Offsetting by 5 v, representing DC offset



# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.show()

# # Plotting cosine waves

# def func1 (x):
#     y = 10*np.cos(np.pi*x)
#     return y

# def func2(x):
#     y = 10*np.sin(2*np.pi*x )
#     return y

# x = np.linspace(0,np.pi,1000)

# y1 = func1(x)
# y2 = func2(x) 

# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.show()

# Plotting cosine waves with phas differences 

def func1 (x):
    y = 10*np.cos(np.pi*x)
    return y

def func2(x):
    y = 10*np.sin(2*np.pi*x + np.pi/4 )
    return y

x = np.linspace(0,np.pi,1000)

y1 = func1(x)
y2 = func2(x) 

plt.plot(x,y1)
plt.plot(x,y2)
plt.show()


# plotting imaginary numbers 

def funcim1(x):
    y = 10* np.exp(1j*(np.pi*x)) #Vm* np.exp(1j*(omega*t+phshift))
    return y

def funcim2(x):
    y = 10* np.exp(1j*(2*np.pi*x - np.pi/4)) #Vm* np.exp(1j*(omega*t+phshift))
    return y

yim1 = funcim1(x)
yim2 = funcim2(x)
yim3 = yim1+yim2 # adding phasors
print(abs(yim3))


# plot at t = 0 in the complex plane
plt.arrow(0,0,yim1[0].real,yim1[0].imag,width=0.5,color='r')
plt.arrow(0,0,yim2[0].real,yim2[0].imag,width=0.5,color='b')
plt.arrow(0,0,yim3[0].real,yim3[0].imag,width=0.5,color='g')
plt.axis([-20,20,-20,20])
plt.xlabel('Re',fontsize=20)
plt.ylabel('Im',fontsize=20)
plt.grid()


plt.show()

