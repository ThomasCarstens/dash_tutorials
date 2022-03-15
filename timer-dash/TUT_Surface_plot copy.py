import plotly.graph_objects as go
import numpy as np
import math

a, b, c = 1.35, 0.85, 1.1 # edges of table.
sigmoid = lambda v : 1/(1+math.exp(-v))
distance_ellipsoid= lambda x,y,z : (x**2/a**2)+(y**2/b**2)+(z**2/c**2) 
#sigmoid(18*((1-distance_ellipsoid(xi,yi,zi))-0.3))
def final(x, y, z):
    vox = []
    for xi in x:
        grid = []
        for yi in y:
            line = []
            for zi in z:
                point = xi+yi+zi    #sigmoid(18*((1-distance_ellipsoid(xi,yi,zi))-0.3))
                line.append(point)
            grid.append(line)
        vox.append(grid)
    return vox

# x = np.linspace(1,a,int(a*100))
# y = np.linspace(1,b,int(b*100))
# z = np.linspace(1,c,int(c*100))
x = np.outer(np.linspace(1,100,100), np.ones(100))
y = np.outer(np.linspace(1,100,100), np.ones(100))
z = np.outer(np.linspace(1,100,100), np.ones(100))

surface_colour = np.array(final(x, y, z))


z1 = np.array([
    [8.83,8.89,8.81,8.87,8.9,8.87],
    [8.89,8.94,8.85,8.94,8.96,8.92],
    [8.84,8.9,8.82,8.92,8.93,8.91],
    [8.79,8.85,8.79,8.9,8.94,8.92],
    [8.79,8.88,8.81,8.9,8.95,8.92],
    [8.8,8.82,8.78,8.91,8.94,8.92],
    [8.75,8.78,8.77,8.91,8.95,8.92],
    [8.8,8.8,8.77,8.91,8.95,8.94],
    [8.74,8.81,8.76,8.93,8.98,8.99],
    [8.89,8.99,8.92,9.1,9.13,9.11],
    [8.97,8.97,8.91,9.09,9.11,9.11],
    [9.04,9.08,9.05,9.25,9.28,9.27],
    [9,9.01,9,9.2,9.23,9.2],
    [8.99,8.99,8.98,9.18,9.2,9.19],
    [8.93,8.97,8.97,9.18,9.2,9.18]
])

z2 = z1 + 1
z3 = z1 - 1

fig = go.Figure(data=[
    go.Surface(z=z1),
    go.Surface(z=z2, showscale=False, opacity=0.9),
    go.Surface(z=z3, showscale=False, opacity=0.9)

])

fig.show()