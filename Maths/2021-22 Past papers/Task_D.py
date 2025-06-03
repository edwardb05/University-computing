# -*- coding: utf-8 -*-
import numpy as np

def trapz(x, y):
    # Trapezoidal integration
    N = len(x) - 1
    S = 0
    for i in range(N):
        S += 0.5 * (y[i+1] + y[i]) * (x[i+1] - x[i])
    return S

# Step sizes
dx = 0.05
dy = 0.05
dz=5
R = 30
H = 150

# Define z steps
z = np.arange(0 + dz, H, dz)
N = len(z)
G = np.zeros(N)

for i, zr in enumerate(z):
    mx = (R / H) * zr  # radius at height z
    x = np.arange(-mx , mx, dx)  # x range for this slice
    y_integrals = np.zeros(len(x))

    for j in range(len(x)):
        # For each x, determine valid y range within the circle
        val = mx**2 - x[j]**2
        my = np.sqrt(val)
        y_vals = np.arange(-my + dy, my, dy)
        f = np.ones_like(y_vals)  # function is just 1
        y_integrals[j] = trapz(y_vals, f)

    G[i] = trapz(x, y_integrals)

# Final integration over z
I = trapz(z, G)
print(f"Numerical Volume = {I:.2f} mm³")

# Analytical reference
V_exact = (1/3) * np.pi * R**2 * H
print(f"Exact Volume     = {V_exact:.2f} mm³")
