

#imports
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=False)

# INITIALIZE: memory database
import numpy as np
import pandas as pd
df = pd.read_csv("list_points.csv")
source = df
def frameMaker(i):
    """
    returns x,y,z dict of currently indexed frame by vector component key
    """
    scale = 2
    current_dict = dict({
        "x": [[source["X"][i], scale * source["X"][i+1]], [source["Y"][i], source["Y"][i]], [source["Z"][i], source["Z"][i]]],
        "y": [[source["X"][i], source["X"][i]], [source["Y"][i], scale * source["Y"][i+1]], [source["Z"][i], source["Z"][i]]],
        "z": [[source["X"][i], source["X"][i]], [source["Y"][i], source["Y"][i]], [source["Z"][i], scale * source["Z"][i+1]]]
    })
    return current_dict

def animateDataSource(time_series_source):
    """
    Takes lists of x,y,z data and returns a list of plotly frames through the frameMaker function. 
    """
    list_of_frames = []
    for k in range(time_series_source.shape[0]-1):
        current_vector_data = frameMaker(k)
        list_of_frames.append(
            go.Frame(
                data=[go.Scatter3d(
                    x = [time_series_source["X"][k]],
                    y = [time_series_source["Y"][k]],
                    z = [time_series_source["Z"][k]],
                    name = "target",
                    mode = "markers",
                    marker=dict(color="red",size=10,opacity=0.5)),
                go.Scatter3d(
                    x=time_series_source["X"],
                    y=time_series_source["Y"],
                    z=time_series_source["Z"],
                    name="path",
                    mode="lines",
                    line=dict(color="black",  width=1)),    
                go.Scatter3d(
                    x=current_vector_data["x"][0],
                    y=current_vector_data["x"][1],
                    z=current_vector_data["x"][2],
                    name = "x",
                    line=dict(color='blue',width=3)),
                go.Scatter3d(
                    x=current_vector_data["y"][0],
                    y=current_vector_data["y"][1],
                    z=current_vector_data["y"][2],
                    name = "y",
                    line=dict(color='green',width=3)),
                go.Scatter3d(
                    x=current_vector_data["z"][0],
                    y=current_vector_data["z"][1],
                    z=current_vector_data["z"][2],
                    name = "z",
                    line=dict(color='red',width=3))
                ],
                traces =[0,1,2,3,4] ####THIS IS THE LINE THAT MUST BE INSERTED
            )
        )
    return list_of_frames

vect = frameMaker(0)
plt = go.Figure(
    data=[go.Scatter3d(
            x=[df["X"].iloc[0]],
            y=[df["Y"].iloc[0]],
            z=[df["Z"].iloc[0]],
            name="target",
            mode="markers",
            marker=dict(
                color="red",
                size=10,
                opacity=0.5)),
        go.Scatter3d(
            x=df["X"].values,
            y=df["Y"].values,
            z=df["Z"].values,
            name="path",
            mode="lines",
            line=dict(
                color="black",
                width=1)),
        go.Scatter3d(
            x = vect["x"][0],
            y = vect["x"][1],
            z = vect["x"][2],
            name = "x",
            mode = "lines",
            line = dict(color='blue', width=3)),
        go.Scatter3d(
            x = vect["y"][0],
            y = vect["y"][1],
            z = vect["y"][2],
            name = "y",
            mode = "lines",
            line = dict(color='green', width=3)),
        go.Scatter3d(
            x=vect["z"][0],
            y=vect["z"][1],
            z=vect["z"][2],
            name = "z",
            mode = "lines",
            line = dict(color='red', width=3))],
    layout = 
        go.Layout(
            title = go.layout.Title(text="Movement"),
            scene_aspectmode="cube",
            scene = dict(
                xaxis = dict(range=[-5,5], nticks=10, autorange=False),
                yaxis = dict(range=[-5,5], nticks=10, autorange=False),
                zaxis = dict(range=[-5,5], nticks=10, autorange=False)),
            updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    frames = animateDataSource(df)
)
plt.show()


