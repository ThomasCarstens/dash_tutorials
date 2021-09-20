import numpy as np
import plotly.graph_objects as go
height=2
x= np.linspace(-1, 1, 75)
y= np.linspace(0, 2, 100)
z= height*np.ones((100,75))
mycolorscale = [[0, '#aa9ce2'],
                [1, '#aa9ce2']]

surf = go.Surface(x=x, y=y, z=z, colorscale=mycolorscale, showscale=False)
layout = go.Layout(width=600,
                  scene_camera_eye_z=0.75)
fig = go.Figure(data=[surf], layout=layout)
fig.show()