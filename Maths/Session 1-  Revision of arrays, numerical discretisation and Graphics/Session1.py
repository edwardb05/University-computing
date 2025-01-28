# # -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pl

# task a ----------------
Dx = 0.5
x1 = np.arange(-5,-2+Dx,Dx)


Dx = 0.05
x2 = np.arange(-2+Dx,3,Dx)


Dx = 0.5
x3= np.arange(3,5+Dx,Dx)

x = np.hstack((x1,x2,x3))

f =np.sin(x)

g= np.sin(x**2+np.pi)
print(g[21])
pl.scatter(x,f,c='red',marker='d')
pl.scatter(x,g,c='magenta',marker='o')
pl.show()
#task b-----------
Dx = 0.1
x1 = np.arange(-2*np.pi,2*np.pi+Dx,Dx)

Dy = 0.1
y1 = np.arange(-np.pi,2*np.pi+Dy,Dy)


(Xg, Yg) = np.meshgrid(x1,y1)

f = np.sin(Xg)*np.cos(Yg)
g = np.cos(Xg)*np.sin(Yg)

s = f+g
p = f*g
print(p[10,10])
# # Task c -----------------------------------
from mpl_toolkits import mplot3d
import plotly.graph_objects as go

ax = pl.axes(projection='3d')
# plot surface
ax.plot_surface(Xg,Yg,s)
pl.show
# plot contour of s
# make a new window plot

pl.contour(Xg, Yg, p)
pl.title('Contour Plot of s')
pl.xlabel('X axis')
pl.ylabel('Y axis')
pl.show()

t = np.arange(0,10.05,0.05)
(Yg, Xg, Tg) = np.meshgrid(y1,x1,t)
print(Tg)
r = np.sin(Xg)*np.cos(Yg) * np.exp(-0.5*Tg)


ax = pl.axes(projection='3d')
ax.plot_surface(Xg[:,:,0],Yg[:,:,0],r[:,:,0])
pl.show()

ax = pl.axes(projection='3d')
ax.plot_surface(Xg[:,:,5],Yg[:,:,5],r[:,:,5])
pl.show()
# taskd ----
x = np.arange(-5,5+0.1,0.1)
y = x
(Xg, Yg) = np.meshgrid(x,y)
Nx = len(x)

F = np.ndarray( (Nx,Nx,2) )

# (a)
#F[:,:,0] = Xg
#F[:,:,1] = Yg

# (b)
F[:,:,0] = Yg
F[:,:,1] = -Xg
pl.streamplot(Xg,Yg,F[:,:,0],F[:,:,1])
pl.show()

# task e --

with open('Maths.txt') as f:
    Mt = [line.strip() for line in f]
with open('Computing.txt') as f:
    Ct = [line.strip() for line in f]

# convert string into floating numbers and then round to the nearest integer
Mm = [round(float(value)) for value in Mt]
Cm = [round(float(value)) for value in Ct]

Mm = np.array(Mm)
Cm = np.array(Cm) 

marks = np.linspace(0,100,101)
Md = np.zeros(len(marks)) 
Cd = np.zeros(len(marks)) 
for value in Mm:
    Md[value] += 1
for value in Cm:
    Cd[value] += 1   

print(Md[62])
    
pl.subplot(1,2,1)
pl.bar(marks,Md,color='red')
pl.bar(marks,Cd,color='blue')
pl.grid()
pl.xlabel('Marks')
pl.ylabel('Occurrences')
pl.legend(['Maths','Computing'])

pl.subplot(1,2,2)
pl.scatter(Cm,Mm,c='blue')
pl.axis('equal')
pl.grid()
pl.plot([0,100],[0,100],c='red',lw=8)
pl.xlabel('Computing')
pl.ylabel('Maths')

pl.show()


