import numpy as np
import plotly.graph_objects as go

x,y,z = np.genfromtxt(r'dat.txt', unpack=True)
#successfully converted to numpy
#print(x, y, z)

# # Generate curve data
# t = np.linspace(-1, 1, 100)
# x = t + t ** 2
# y = t - t ** 2
# z = 1
# xm = np.min(x) - 1.5
# xM = np.max(x) + 1.5
# ym = np.min(y) - 1.5
# yM = np.max(y) + 1.5
# N = 1000
# s = np.linspace(-1, 1, N)
# xx = s + s ** 2
# yy = s - s ** 2
# zz = 1


# Create figure
fig = go.Figure(
    data=[go.Scatter3d(x=[], y=[], z=[],
                     mode="markers",marker=dict(color="red", size=1))])
    
fig.update_layout(
        
         scene = dict(
        
        xaxis=dict(range=[min(x), max(x)], autorange=False),
        yaxis=dict(range=[min(y), max(y)], autorange=False),
        zaxis=dict(range=[min(z), max(z)], autorange=False),
        )),


frames = [go.Frame(data= [go.Scatter3d(
                                       x=x[:k+1], 
                                       y=y[:k+1],
                                       z=z[:k+1])],
                   
                   traces= [0],
                   name=f'frame{k}'      
                  )for k  in  range(len(x-1))]
fig.update(frames=frames)




fig.update_layout(updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None, dict(frame=dict(redraw=True,fromcurrent=True, mode='immediate'))      ])])])


fig.show()