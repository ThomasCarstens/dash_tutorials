import plotly.graph_objects as go
import numpy as np
a, b, c = 1.32, 1., 0.8
X, Y, Z = np.mgrid[-2:2:40j, -2:2:40j, 0:2:40j]
#planar_Z = np.linspace(-8,8,40j)
Xt, Yt = np.mgrid[-1.5:1.5:40j, -1:1:40j]

import math
a, b, c = 1.35, 0.85, 1.1 # edges of table.
sigmoid = lambda V : 1/(1+np.exp(-V))
distance_ellipsoid= lambda x,y,z : (x**2/a**2)+(y**2/b**2)+(z**2/c**2) 
#sigmoid(18*((1-distance_ellipsoid(xi,yi,zi))-0.3))

values0 = distance_ellipsoid(X, Y, Z)
values1 = (18*((1-distance_ellipsoid(X, Y, Z))-0.3))
values = sigmoid(18*((1-distance_ellipsoid(X, Y, Z))-0.3))

#(X**2/a**2)+(Y**2/b**2)+(Z**2/c**2)

fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values1.flatten(),
    isomin=0.1,
    isomax=0.8,
    opacity=0.1, # needs to be small to see through all surfaces
    surface_count=21, # needs to be a large number for good volume rendering
    colorscale='speed'
    ))
z_plane_pos = 0*np.ones((len(X),len(Y)))
fig.add_trace(
    go.Surface(x=Xt, y=Yt, z=z_plane_pos, showscale=False, colorscale = [[0, '#000000'], [1, '#000000']], opacity=0.3)
)

#go.Surface(z=z2, showscale=False, opacity=0.9),
# fig.update_xaxes(range=(-5, 5)) 
# fig.update_yaxes(range=(-5, 5)) 
fig.show()