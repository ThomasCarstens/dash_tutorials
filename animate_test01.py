import sys
print(sys.executable)
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_gif_component as gif
import numpy as np
import plotly.express as px


random_pts=np.arange(100)     
fig=go.Figure(go.Scatter3d(x = random_pts[:1], y = random_pts[:1], z =random_pts[:1], mode='lines', name='Testing Points'))
fig.update_layout(title='Animation Test',
                  title_x=0.5,
                  width=600, height=600, 
                  xaxis_title='Time', 
                  yaxis_title='Test Points',
                  yaxis_range=(0,99),
                  xaxis_range=(0,99), #you generate y-values for i =0, ...99, 
                                      #that are assigned, by default, to x-values 0, 1, ..., 99
                  
                  updatemenus=[dict(buttons = [dict(
                                               args = [None, {"frame": {"duration": 50, 
                                                                        "redraw": False},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 0}}],
                                               label = "Play",
                                               method = "animate")],
                                type='buttons',
                                showactive=False,
                                y=1,
                                x=1.12,
                                xanchor='right',
                                yanchor='top')])
                                          
                    
frames= [go.Frame(data=[go.Scatter3d(x = random_pts[[i]], y=random_pts[[i]], z= random_pts[[i]])]) for i in range(1, 100)]
fig.update(frames=frames)

fig.show()