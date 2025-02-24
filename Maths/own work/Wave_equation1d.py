from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
# Using explicit method

app = Dash(__name__)

def gen_wave_equation_data():
    # Define parameters
    L = 1.0     # Length of domain
    Nx = 6      # Number of spatial points
    T = 2.0     # Total time
    Nt = 11     # Number of time steps

    # Create space
    x = np.linspace(0, L, Nx)

 

    # Init the matrix
    u = np.zeros((Nx, Nt))

    # Init conditions 0 at edges and sine wave in mid
    u[1:-1, 0] = np.sin(np.pi * x[1:-1])

    for i in range(1, Nx - 1):
        u[i, 1] = 0.5 * (u[i+1, 0] + u[i-1, 0])  # Simplified for r = 1

    # Time stepping loop, simplified as r = 1 
    for j in range(1, Nt - 1):
        for i in range(1, Nx - 1):
            u[i, j+1] = u[i+1, j] + u[i-1, j] - u[i, j-1] 

    # Convert results to DataFrame
    times = [f"{t:.1f}s" for t in np.linspace(0, T, Nt)]
    df = pd.DataFrame(u, columns=times)
    df["x"] = x  # Add spatial coordinate

    return df, times

df, times = gen_wave_equation_data()

app.layout = html.Div([
    html.H4('Wave equation in 1D'),
    dcc.Graph(id="graph"),
    html.H4('Select time stamps'),
    dcc.Checklist(
        id="checklist",
        options=[{"label": t, "value": t} for t in times],
        value=[times[0], times[2]],  # Default selection
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def update_line_chart(selected_times):
    fig = px.line(df, x="x", y=selected_times, labels={"x": "Position", "value": "Amplitude"},
                  title="1D Wave Equation Over Time")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
