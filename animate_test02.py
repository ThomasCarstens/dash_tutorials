import numpy as np
import plotly.graph_objects as go
import random
#x,y,z = np.genfromtxt(r'dat.txt', unpack=True)

random_pts=np.arange(100)
velocity_data = [random.random() for _ in range(100)]   
print (random_pts)
# Create figure
fig = go.Figure(
    data=[go.Scatter3d(x=[], y=[], z=[],
                     mode="markers",marker=dict(color="red", size=10))])
    
fig.update_layout(
        title='Animation Test',
        title_x=0.5,
        width=600, height=600, 
        xaxis_title='Time', 
        yaxis_title='Test Points',

        scene = dict(
        
        xaxis=dict(range=[min(random_pts), max(random_pts)], autorange=False),
        yaxis=dict(range=[min(random_pts), max(random_pts)], autorange=False),
        zaxis=dict(range=[min(random_pts), max(random_pts)], autorange=False),
        ),
        # fig.update_layout(updatemenus=[dict(type="buttons",
        #                           buttons=[dict(label="Play",
        #                                         method="animate",
        #                                         args=[None, dict(frame=dict(redraw=True,fromcurrent=True, mode='immediate'))      ])])])

        updatemenus=[dict(buttons = [dict(
                                    args = [None, {"frame": {"duration": 50, 
                                                            "redraw": True},
                                                    "fromcurrent": True, 
                                                    "mode": "immediate",
                                                    "transition": {"duration": 0}}],
                                    label = "Play",
                                    method = "animate")],
                    type='buttons',
                    showactive=False,
                    y=1,
                    x=1.12,
                    xanchor='right',
                    yanchor='top')]

        ),

height=2
x= np.linspace(-1, 1, 75)
y= np.linspace(0, 2, 100)
z= height*np.ones((100,75))
mycolorscale = [[0, '#aa9ce2'],
                [1, '#aa9ce2']]

surf = go.Surface(x=x, y=y, z=z, colorscale=mycolorscale, showscale=False)
#fig = go.Figure(data=[surf], layout=layout)
fig.add_surface(surf)

# for i in range(len(data)):
#     time.sleep(0.3)
#     fig.data[0].y = data[:i] 


# frames = [go.Frame(data= [go.Scatter3d(
#                                     #    x = random_pts[[k]], 
#                                     #    y=random_pts[[k]],
#                                     #    z=random_pts[[k]],
#                                        x =random_pts[:k+1], 
#                                        y=random_pts[:k+1],
#                                        z=random_pts[:k+1],
#                                        )],
                   
#                    traces= [0],
#                    name=f'frame{k}'      
#                   )for k in range(1, len(random_pts))]

# fig.update_layout(updatemenus=[dict(
#                 buttons=[dict(args=[None, dict(frame=dict(duration = 20))      ])])])

# # with fig.batch_animate(duration=2000, easing='elastic-in-out'):
# #     fig.data[0].marker.color = 'green'
# #     fig.data[0].marker.size = 20

# fig.update(frames=frames),

fig.show()