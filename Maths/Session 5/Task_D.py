import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 1.0  # Length of the pendulum (m)
g = 9.81  # Acceleration due to gravity (m/s^2)
m = 0.5  # Mass of the pendulum (kg)
h = 0.005  # Time step (s)
t_end = 8 # Total time (s)

# Initial conditions
theta0 = np.pi / 4  # Initial angle (radians)
theta_dot0 = 0.0  # Initial angular velocity (rad/s)

# Time array
t = np.arange(0, t_end, h)

# Define the system of ODEs for forward Euler
def derivatives(t, Y, c):
    y1, y2 = Y  # y1 = theta, y2 = angular velocity
    dy1_dt = y2
    dy2_dt = - (c / (m)) * y2 - (g / L) * np.sin(y1)
    return np.array([dy1_dt, dy2_dt])

# Forward Euler Method for solving the system of ODEs
def FwEulerN(t0, te, h, Y0, c):
    t = np.arange(t0, te+0.0001, h)
    print(t)
    Y = np.zeros((len(t), 2))  # Array to store theta and angular velocity
    Y[0] = Y0  # Set initial conditions
    
    # Implement the Forward Euler method
    for i in range(1, len(t)):
        dydt = derivatives(t[i-1], Y[i-1], c)  # Get derivatives at current step
        Y[i] = Y[i-1] + h * dydt  # Update using Euler method
    
    return t, Y

# Initial condition vector [theta(0), angular velocity(0)]
Y0 = [theta0, theta_dot0]

# Simulate for dry and humid environments
c_dry = 0.05  # Damping coefficient for dry environment (N s/m)
c_humid = 0.18  # Damping coefficient for humid environment (N s/m)

# Solve for both cases
t_dry, Y_dry = FwEulerN(0, t_end, h, Y0, c_dry)
t_humid, Y_humid = FwEulerN(0, t_end, h, Y0, c_humid)

# Extract the results
theta_dry = Y_dry[:, 0]  # Angle for dry environment
theta_dot_dry = Y_dry[:, 1]  # Angular velocity for dry environment

theta_humid = Y_humid[:, 0]  # Angle for humid environment
theta_dot_humid = Y_humid[:, 1]  # Angular velocity for humid environment


print(theta_dot_dry)
