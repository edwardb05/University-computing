import numpy as np
# Interpolating with inverse distance weightings


def TrNN(r,f,rp):
    # initialize d and w
    d = np.ndarray(3)
    w = np.ndarray(3)
    # Calculate weightings
    for i in range(3):
        d[i]= ((r[i][0]-rp[0])**2 + (r[i][1]-rp[1])**2)**(1/2)
        w[i]= 1/d[i]
    # return the value of the function at this point
    frp = (w[0]*f[0]+w[1]*f[1]+w[2]*f[2])/(w[0]+w[1]+w[2])
    return frp

r = ((0,0),(1,2),(2,0.5))
f= (1,1.5,3)
rp= (1,0.5)

print(TrNN(r,f,rp))