# Let's do a local graph of an existing circle.

# Then find how to update position in realtime on same graph.

# Then find how to trace position accurately.

# x and y given as array_like objects
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="scatter-plot"),
    # html.P("Petal Width:"),
    # dcc.RangeSlider(
    #     id='range-slider',
    #     min=0, max=2.5, step=0.1,
    #     marks={0: '0', 2.5: '2.5'},
    #     value=[0.5, 2]
    # ),
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
    ),
])
numRobots = 1
r = 0.8
height = 0.3
final_height = 1.0
w = 2 * np.pi / numRobots
T = 2* 2 * np.pi / w #txa: decreased it assuming it gives more  points.

spiral_points = []
spiral_absolute = []
phase =0
nb_points = 100
height_increment = height
for t in np.linspace(0, T, nb_points):
    height_increment += (final_height - height) / nb_points 
    absolute_pt = [r * np.cos(w * t + phase), r * np.sin(w * t + phase), height_increment]
    spiral_absolute.append (absolute_pt)
    if t != 0:
        t0=t-1
        relative_pt = []
        zip_object = zip(spiral_absolute[-1], spiral_absolute[-2])
        for now_i, before_i in zip_object:
            relative_pt.append(now_i-before_i)
        #relative_pt = spiral_absolute[-1] - spiral_absolute[-2]
        spiral_points.append (relative_pt)


import pandas as pd


spiral_points_x=[]
spiral_points_y=[]
spiral_points_z=[]
for vector3 in spiral_points:
    spiral_points_x.append(vector3[0])
    spiral_points_y.append(vector3[1])
    spiral_points_z.append(vector3[2]) 

data = {'x values':  spiral_points_x,
        'y values': spiral_points_y,
        }
df = pd.DataFrame (data, columns = ['x values','y values'])
print (df)


spiral_absolute_x=[]
spiral_absolute_y=[]
spiral_absolute_z=[]
for vector3 in spiral_absolute:
    spiral_absolute_x.append(vector3[0])
    spiral_absolute_y.append(vector3[1])
    spiral_absolute_z.append(vector3[2]) 

# spiral_increment_x=[]
# spiral_increment_y=[]
# spiral_increment_z=[]
# for vector3 in spiral_increment:
#     spiral_increment_x.append(vector3[0])
#     spiral_increment_y.append(vector3[1])
#     spiral_increment_z.append(vector3[2]) 

# fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
# fig.show()

#CHANGE THESE AND TRACE UPDATES.
spiral_increment_x = [0,1,1,3,2]
spiral_increment_y = [0,1,1,4,1.7]

@app.callback(
    Output("scatter-plot", "figure"), 
    [Input('interval-component', 'n_intervals')])
def update_bar_chart(n):
    #low, high = slider_range
    #mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    fig = px.scatter( df,
         x='x values', y='y values', color ='y values',         
            width=400, height=400)

    fig.update_traces(marker=dict(
        color='blue'))

    fig.add_scatter(x=spiral_increment_x, y=spiral_increment_y)

    fig.update_traces(marker=dict(
        color='red'))
    fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
    )
    return fig



app.run_server(debug=True)