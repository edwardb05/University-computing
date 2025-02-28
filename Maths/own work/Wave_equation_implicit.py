import numpy as np
import pandas as pd
from scipy.linalg import solve_banded
import matplotlib.pyplot as plt

def crank_nicolson_wave(L=1.0, Nx=10, T=2.0, Nt=11, c=1.0, ):
    dx = L / (Nx - 1)  # Space step
    dt = T / (Nt - 1)  # Time step
    r = (c * dt / dx) ** 2  # CFL condition
    print(r)
    x = np.linspace(0, L, Nx)  # Spatial grid
    u = np.zeros((Nx, Nt))  # Solution matrix
    
    # Initial condition: cos(pi * x)

    u[:, 0] = np.exp(-((x - L / 2) ** 2) / 0.01)
    
    # First time step using an explicit approach
    u[1:-1, 1] = 0.5 * (u[2:, 0] + u[:-2, 0])
    
    # Tridiagonal matrix setup
    lower_diag = -1* np.ones(Nx - 3)   # Lower diagonal
    main_diag = 4 * np.ones(Nx - 2)   # Main diagonal
    upper_diag = -1 * np.ones(Nx - 3)   # Upper diagonal

    ab = np.zeros((3, Nx - 2))  # Band matrix for solve_banded()
    ab[0, 1:] = upper_diag  # Upper diagonal
    ab[1, :] = main_diag    # Main diagonal
    ab[2, :-1] = lower_diag  # Lower diagonal
    
    # Time stepping
    for n in range(1, Nt - 1):
        # Right-hand side (known values from previous time steps)
        b = (1 - r) * u[1:-1, n] + (r / 2) * (u[2:, n] + u[:-2, n]) - u[1:-1, n-1]
        
        # Solve tridiagonal system for u at time n+1
        u[1:-1, n+1] = solve_banded((1, 1), ab, b)
        
        # Neumann boundary conditions (zero derivative at boundaries)
        u[0, n+1] = u[1, n+1]
        u[-1, n+1] = u[-2, n+1]
    
    # Convert results to DataFrame
    times = [f"{t:.1f}s" for t in np.linspace(0, T, Nt)]
    df = pd.DataFrame(u, columns=times)
    df["x"] = x  # Add spatial coordinate
    
    return df

# Run the simulation
df_wave = crank_nicolson_wave()

# Display results
print("Wave Equation (Crank-Nicolson) Solution:")
print(df_wave)

# Plot the wave evolution
def plot_wave(df):
    plt.figure(figsize=(8, 5))
    for col in df.columns[:-1]:  # Skip the last column (x-coordinates)
        plt.plot(df["x"], df[col], label=col)
    
    plt.xlabel("x")
    plt.ylabel("u(x, t)")
    plt.title("Crank-Nicolson Wave Equation Evolution")
    plt.legend()
    plt.show()

# Plot the wave motion
plot_wave(df_wave)
