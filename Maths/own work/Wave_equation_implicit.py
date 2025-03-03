import numpy as np

import matplotlib.pyplot as plt

# defining the implicit method for solving wave equation
def crank_nicolson_wave(L=1.0, Nx=10, T=2.0, Nt=11, c=1.0, width=0.01,depth = 1) :
    dx = L / (Nx - 1)  # Length step
    dt = T / (Nt - 1)  # Time step
    r = (c * dt / dx) ** 2  # CFL condition
    print(r)
    x = np.linspace(0, L, Nx)  # Length of wave domain
    u = np.zeros((Nx, Nt))  # Solution matrix
    
    
    # Set Gaussian pulse initial conditions
    u[:, 0] = A * np.exp(-((x - 0)/2)**2 / (2 * width**2))
    
    # First time step using  explicit approach setting g(x) to 0 as no initial speed
    u[1:-1, 1] = u[1:-1, 0] + (r / 2) * (u[:-2, 0] - 2 * u[1:-1, 0] + u[2:, 0])
    
    # Solving for each time, setting up tridiag matrix
    A = np.zeros((Nx-2, Nx-2))  #Init matrix excluding BC
    np.fill_diagonal(A, (1+r))  #Fill Main diag
    np.fill_diagonal(A[:-1, 1:], -r/2)  #Fill upper and lower diag
    np.fill_diagonal(A[1:, :-1], -r/2)  
    

    # Time stepping
    for j in range(1, Nt - 1):
        # b is RHS matrix for non BC, calulated from previous time steps
        b = np.zeros(Nx-2)
        #b iniitial and final values are different to bc
        b[0]= r/2 * u[0,j+1] + r/2*(u[2,j]+u[0,j]) + (2+r)*(u[1,j])+u[1,j-1]
        b[Nx-3]= r/2 * u[Nx-1,j+1] + r/2*(u[Nx-3,j]+u[Nx-1,j]) + (2+r)*(u[Nx-2,j])+u[Nx-2,j-1]

        #b values for the rest of the matrix
        for i in range(1,Nx-3):
            b[i]= r/2*(u[i+2,j]+u[i,j]) + (2+r)*(u[i+1,j])+u[i+1,j-1]
        
        
        # Solve tridiagonal system for u at time n
        u[1:-1, j+1] = np.linalg.inv(A).dot(b)
    return u
    

# Defining the explicit method for solving wave equation
def explicit_wave_method(L=1.0, Nx=10, T=2.0, Nt=11, c=1.0, width=0.01,depth = 1):
    dx = L / (Nx - 1)  # Length step
    dt = T / (Nt - 1)  # Time step
    r = (c * dt / dx) ** 2  # CFL condition
    print(r)
    x = np.linspace(0, L, Nx)  # Length of wave domain
    u = np.zeros((Nx, Nt))  # Solution matrix
    
    
    # Set Gaussian pulse initial conditions
    u[:, 0] = A * np.exp(-((x - 0)/2)**2 / (2 * width**2))
    
    # First time step using  explicit approach setting g(x) to 0 as no initial speed
    u[1:-1, 1] = u[1:-1, 0] + (r / 2) * (u[:-2, 0] - 2 * u[1:-1, 0] + u[2:, 0])

    # Time stepping loop, simplified as r = 1 
    for j in range(1, Nt - 1):
        for i in range(1, Nx - 1):
            u[i, j+1] =  (r / 2) * (u[i+1, j] - 2 * u[i, j] + u[i-1, j])+2*u[i, j] - u[i, j-1]
    return u

class insect:
    def __init__(self,weight, width, speed) -> None:
        self.width = width
        self.KE = 0.5*weight*speed**2

