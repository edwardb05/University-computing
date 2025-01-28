import numpy as np
import matplotlib.pyplot as pl

x=np.arange(0,10,1)
y=np.linspace(10,20,21)
z=np.ndarray(len(x)+len(y))
z[:len(x)]= x
z[len(x):] =y
print(z)