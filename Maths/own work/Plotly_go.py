import plotly.graph_objects as go
import pandas as pd
import numpy as np
# Using explicit method


def gen_wave_equation_data():
    # Define parameters
    L = 1.0     # Length of domain
    Nx = 8      # Number of spatial points
    T = 2.0     # Total time
    Nt = 11     # Number of time steps

    # Create space with ghost points
    x = np.linspace(-0.2, L+0.2, Nx)
    # Init the matrix
    u = np.zeros((Nx, Nt))

    # Init conditions 0 at edges and sine wave in mid
    u[1:-1, 0] = np.cos(np.pi * x[1:-1])

    u[0,0]= u[2,0]
    u[7,0]=u[5,0]

    for i in range(1, Nx - 1):
        u[i, 1] = 0.5 * (u[i+1, 0] + u[i-1, 0])  # Simplified for r = 1
    u[0,1]= u[2,1]
    u[7,1]=u[5,1]
    # Time stepping loop, simplified as r = 1 
    for j in range(1, Nt - 1):
        for i in range(1, Nx - 1):
            u[i, j+1] = u[i+1, j] + u[i-1, j] - u[i, j-1] 
            u[0,j+1]= u[2,j+1]
            u[7,j+1]=u[5,j+1]

    # Convert results to DataFrame
    times = [f"{t:.1f}s" for t in np.linspace(0, T, Nt)]
    df = pd.DataFrame(u, columns=times)
    df["x"] = x  # Add spatial coordinate

    return df, times

df, times = gen_wave_equation_data()



fig = go.Figure()
for i in range(len(times)):
    fig.add_trace(go.Scatter(
        x=df["x"], 
        y=df[times[i]], 
        name=f'{times[i]} profile',
        text=[f"t = {times[i]}"] * len(df),
        line_shape='spline'
    ))

fig.update_traces(hoverinfo='text+name', mode='lines+markers')
fig.update_layout(title="Wave Equation Solution Over Time",
                  xaxis_title="Position (x)",
                  yaxis_title="Wave Amplitude",
                  legend=dict(y=0.5, traceorder='reversed', font_size=16))

fig.show()
print(df)