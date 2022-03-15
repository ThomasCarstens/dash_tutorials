import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Equation of ring cyclide
# see https://en.wikipedia.org/wiki/Dupin_cyclide
import numpy as np

a, b, d = 1.32, 1., 0.8
c = a**2 - b**2

u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j]

x = (d * (c - a * np.cos(u) * np.cos(v)) + b**2 * np.cos(u)) / (a - c * np.cos(u) * np.cos(v))

y = b * np.sin(u) * (a - d*np.cos(v)) / (a - c * np.cos(u) * np.cos(v))
z = b * np.sin(v) * (c*np.cos(u) - d) / (a - c * np.cos(u) * np.cos(v))

fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Color corresponds to z', 
                    'Color corresponds to distance to origin'],
                    )
import math
m, n, o = 1.35, 0.85, 1.1 # edges of table.
sigmoid = lambda v : 1/(1+math.exp(-v))
# distance_ellipsoid= lambda x,y,z : (x**2/a**2)+(y**2/b**2)+(z**2/c**2) 
fig.add_trace(go.Surface(x=x, y=y, z=z, colorbar_x=-0.07), 1, 1)
fig.add_trace(go.Surface(x=x, y=y, z=z, surfacecolor=(x**2/m**2)+(y**2/n**2)+(z**2/o**2)), 1, 2)
fig.update_layout(title_text="Ring cyclide")
fig.show()
# import math
# a, b, c = 1.35, 0.85, 1.1 # edges of table.
# sigmoid = lambda v : 1/(1+math.exp(-v))
# distance_ellipsoid= lambda x,y,z : (x**2/a**2)+(y**2/b**2)+(z**2/c**2) 

# u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j]

# # y = b * np.sin(u) * (a - d*np.cos(v)) / (a - c * np.cos(u) * np.cos(v))
# # z = b * np.sin(v) * (c*np.cos(u) - d) / (a - c * np.cos(u) * np.cos(v))
# def final(x, y, z):
#     vox = []
#     for xi in x:
#         grid = []
#         for yi in y:
#             line = []
#             for zi in z:
#                 point = xi+yi+zi#sigmoid(18*((1-distance_ellipsoid(xi,yi,zi))-0.3))
#                 line.append(point)
#             grid.append(line)
#         vox.append(grid)
#     return vox
# x = np.linspace(1,a,int(a*100))
# y = np.linspace(1,b,int(b*100))
# z = np.linspace(1,c,int(c*100))
# surface_colour = final(x, y, z)
# #print(surface_colour)


# # fig = make_subplots(rows=1, cols=2,
# #                     specs=[[{'is_3d': True}, {'is_3d': True}]],
# #                     subplot_titles=['Color corresponds to z', 
# #                     'Color corresponds to distance to origin'],
# #                     )

# # fig.add_trace(go.Surface(x=x, y=y, z=z, colorbar_x=-0.07), 1, 1)
# # fig.add_trace(go.Surface(x=x, y=y, z=z, surfacecolor=surface_colour), 1, 2)
# # fig = go.Figure(data=[
# #     go.Surface(z=z, showscale=False, opacity=0.9)
# # ])
# # fig.update_layout(title_text="Ring cyclide")
# # fig.show()


# import plotly.graph_objects as go
# import numpy as np
  
# x = np.outer(np.linspace(1,a,int(a*100)), np.ones(int(a*100)))
# y = x
# #np.outer(np.linspace(1,b,int(a*100)), np.ones(int(a*100)))
# z = np.cos(x)
# print (z)
# fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
  
# fig.show()


