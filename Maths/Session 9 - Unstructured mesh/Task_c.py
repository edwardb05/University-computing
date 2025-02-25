import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from Task_a import TrNN
import plotly.graph_objects as go

def PlotMesh3D(nodes,elements,func):  

    fig = pl.figure()
    # ax = pl.axes(projection='3d')
    # ax.plot_trisurf(nodes[:,0], nodes[:,1], nodes[:,2], triangles = elements, edgecolor=[[0,0,0]], linewidth=1.0, alpha=0.0, shade=True)
    cntr1 = pl.tricontour(nodes[:,0],nodes[:,1],func, levels=14, cmap="RdBu_r")
    fig.colorbar(cntr1)
    pl.xlabel('x')
    pl.ylabel('y')
    # ax.view_init(elev=30, azim=80, roll=0)
    pl.show()

f = open('Hob.Elements.txt','r')
te = f.readlines()
f.close()
f = open('Hob.Nodes.txt','r')
tn = f.readlines()
f.close()

Ne = len(te)
Nn = len(tn)

elementshob = np.ndarray((Ne,3),dtype=int)
for i in range(len(te)):
    temp = te[i].split(',',3)
    elementshob[i,:] = [int(val) for val in temp]
    
nodeshob = np.ndarray((Nn,3),dtype=float)
for i in range(Nn):
    temp = tn[i].split(',',3)
    nodeshob[i,:] = [float(val) for val in temp]

f = open('Hob.Temperatures.txt','r')
t = f.readlines()
f.close()
Thob = np.ndarray(Nn,dtype=float)
for i in range(len(t)):
    Thob[i] = float(t[i])

PlotMesh3D(nodeshob,elementshob,Thob)

f = open('TeaPot.Elements.txt','r')
te = f.readlines()
f.close()
f = open('TeaPot.Nodes.txt','r')
tn = f.readlines()
f.close()

Ne = len(te)
Nn = len(tn)

elementspot = np.ndarray((Ne,3),dtype=int)
for i in range(len(te)):
    temp = te[i].split(',',3)
    elementspot[i,:] = [int(val)-1 for val in temp]
    
nodespot = np.ndarray((Nn,3),dtype=float)
for i in range(Nn):
    temp = tn[i].split(',',3)
    nodespot[i,:] = [float(val) for val in temp]

x = nodespot[:, 0]
y = nodespot[:, 1]
z = nodespot[:, 2]

# Extract the triangular faces for Mesh3D
i_faces = elementspot[:, 0]
j_faces = elementspot[:, 1]
k_faces = elementspot[:, 2]

# Create a 3D mesh plot using Plotly
fig = go.Figure(data=[
    go.Mesh3d(
        x=x, y=y, z=z,
        i=i_faces, j=j_faces, k=k_faces,
        color='lightblue', opacity=0.6
    )
])

fig.update_layout(
    title="3D TeaPot Mesh",
    width=600, height=600,
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1.5)
        )
    )
)

fig.show()

def AreaTriangle(A,B):
    # A and B are nodal points in R3
    # cross product A x B
    CP = np.cross(A,B) / 2
    A = np.sqrt(CP.dot(CP))
    return A

def FindInternal(A,B,C,P):
    # A, B, C and P are nodal points in R3
    A1 = AreaTriangle((B-P),(C-P))
    A2 = AreaTriangle((C-P),(A-P))
    A3 = AreaTriangle((A-P),(B-P))
    
    At = AreaTriangle((B-A),(C-A))
    
    if abs( (A1+A2+A3) - At ) < 0.1:
        res = True
    else:
        res = False
    return res

# scroll all nodal points at the base of the pot (y=0)
Nnp = len(nodespot)
Neh = len(elementshob)
BaseNodes = np.zeros(Nnp,dtype=int)
Inelement = np.zeros(Nnp,dtype=int)
Nb = 0
for i in range(Nnp):
    if nodespot[i,2] == 0:
        # this node is at the base of the pot
        P = nodespot[i,:]
        BaseNodes[Nb] = i
        # determine which element of the mesh hob contains it
        for j in range(Neh):
            # extract the nodes of this element
            A = nodeshob[elementshob[j,0]]
            B = nodeshob[elementshob[j,1]]
            C = nodeshob[elementshob[j,2]]
            # determine if P is internal to triangle ABC
            IsInternal = FindInternal(A,B,C,P)
            if IsInternal:
                Inelement[Nb] = j
        Nb += 1

Tpot = np.zeros(Nb)
for i in range(Nb):
    # set the triangle contributing to interpolation of node i
    el = elementshob[Inelement[i]]
    r = nodeshob[el]
    rp = nodespot[BaseNodes[i]]
    fr = np.array([Thob[el[0]],Thob[el[1]],Thob[el[2]]])
    Tpot[i] = TrNN(r,fr,rp)

PlotMesh3D(nodeshob,elementshob,Tpot)