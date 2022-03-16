
import dash_gif_component as gif
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import datetime
from dash.exceptions import PreventUpdate
# from flask_caching import Cache
import os

app = dash.Dash(__name__)
# cache = Cache(app.server, config={
#     # try 'filesystem' if you don't want to setup redis
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://localhost:8050')
# })
# works now albeit jumpy
# fixing the ranges of the graphs.
# removing the colour bar
# 2 / 20 / 500 works well
# 3 / 20 / 500 better for acceleration
# 3 / 50 / 200 slows down
# trimby is creating a weird pattern
# that's the colour's fault. needs consistency.

all_tfs_path = '/home/txa/Documents/data/droneData_alliantech/eval_tests/hdi_2/bag_tf.csv'
df_alltfs = pd.read_csv(all_tfs_path)
global tf_log, tfs_cf3, tfs_cf4
tf_log = []
tfs_cf1 = []
tfs_cf2 = []
tfs_cf3 = []
tfs_cf4 = []
#now separate the drones.
for i in range(1,5):
    #recreate dataframe name on the fly
    tf_log = globals()['tfs_cf'+str(i)]
    for entry in range(len(df_alltfs['field.transforms0.child_frame_id'])):
        #print(df_alltfs['field.transforms0.child_frame_id'][entry])
        if df_alltfs['field.transforms0.child_frame_id'][entry] == 'cf'+str(i):
            print("YES")
            pos = []
            pos.append(df_alltfs['field.transforms0.transform.translation.x'][entry])
            pos.append(df_alltfs['field.transforms0.transform.translation.y'][entry])
            pos.append(df_alltfs['field.transforms0.transform.translation.z'][entry])
            pos.append(datetime.datetime.fromtimestamp(df_alltfs['%time'][entry]/10**9))

            tf_log.append(pos)

#unzip into respective axis.
print(len(tfs_cf1), len(tfs_cf2), len(tfs_cf3), len(tfs_cf4))
#print(tfs_cf4)



# ADDING THE HZ :)
hz_path = '/home/txa/Documents/data/hz_testgraph.txt'
#read line by line.
with open(hz_path, "r") as f:
    notes = f.readlines()
rates = []
for line in notes:
    if 'rate' in line:
        rates.append(float(line.split(' ')[-1][:-2]))


template_graph = go.Figure()

import numpy as np
# THIS WONT WORK UNLESS DENSIFIED. TECHNICALLY BOTH SAME ROSBAG SOOO DENSIFIED IS FIABLE.
# JUST A CRAZY LONG PROCESS...
# densify points on graph
def fita2blen(f_val, x_desired):
    MAX_X = len(f_val)
    FINALLEN_X = x_desired
    CURRENTLEN_X = len(f_val)
    #x on 10 points, then 100 points
    x_current = list(np.linspace(1,MAX_X,CURRENTLEN_X))
    x_final = list(np.linspace(1,MAX_X,FINALLEN_X))
    # interpolate on 100 values.
    interp = np.interp(x_final, x_current, f_val )
    interp = list(interp)
    return interp

def template_graph_plot (minval, maxval, trimby):
    clipped_cf3= tfs_cf3[::trimby]
    clipped_cf4= tfs_cf4[::trimby]

    range_cf3 = [ max(1, minval*len(clipped_cf3)//100000), maxval*len(clipped_cf3)//100000 ]
    range_cf4 = [ max(1, minval*len(clipped_cf4)//100000), maxval*len(clipped_cf4)//100000 ]

    x_cf3, y_cf3, z_cf3, time_cf3 = zip(*clipped_cf3[range_cf3[0]:range_cf3[1]])
    x_cf4, y_cf4, z_cf4, time_cf4 = zip(*clipped_cf4[range_cf4[0]:range_cf4[1]])
    # print("len", len(x_cf4))
    #x_cf4 = x_cf4[min_data:max_data]
    
    template_graph = go.Figure()
    rates_cf4 = fita2blen(rates, len(x_cf4))

    template_graph.add_trace(go.Scatter(x=x_cf4, y=y_cf4,
                                mode='markers',
                                name='Trace cf4',
                                marker=dict(
                                    color=rates_cf4,
                                    size = 1.5,
                                    colorscale='BrBG',
                                    line_width=0.2,
                                    showscale=False,
                                    # colorbar = dict(
                                    #         len=1,
                                    #         thickness=50.0,
                                    #         #tickangle=-90,
                                    #         x = -0.3,
                                    #         xanchor='right',
                                    #         outlinewidth=0.0
                                    #     ),
                        
                        )))

    rates_cf3 = fita2blen(rates, len(x_cf3))

    template_graph.add_trace(go.Scatter(x=x_cf3, y=y_cf3,
                                mode='lines',
                                name='Trace cf3',
                                marker=dict(
                                    color=rates_cf3,
                                    size = 1.5,
                                    colorscale='BrBG',
                                    line_width=0.2,
                                    showscale=False,
                                    # colorbar = dict(
                                    #         len=1,
                                    #         thickness=50.0,
                                    #         #tickangle=-90,
                                    #         x = -0.3,
                                    #         xanchor='right',
                                    #         outlinewidth=0.0
                                    #     ),
                        
                        )))

    template_graph.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=0.0,
        xanchor="right",
        x=1
    ))
    template_graph.update_layout(
        title="Publishing Frequency over Drone Positions",
        title_x=0.7,
        title_y=0.95,
        xaxis_title="X coordinates",
        yaxis_title="Y coordinates",

    )
    template_graph.update_xaxes(range=(-1, 1))
    template_graph.update_yaxes(range=(-1, 0.8))


    tightfit = dict(l=20, r=20, t=0, b=100)
    template_graph.update_layout(
        margin=tightfit,
    )

    return template_graph

clock_ms = 2000                
app.layout = html.Div([
    #realtime interval
    dcc.Interval(
            id='interval-component',
            interval=1*clock_ms, # in milliseconds
            n_intervals=0
    ),
    #update_range: counter storage (init at 1)
    dcc.Store(id='intermediate-value', data = 1),


    html.Div(dcc.Graph(
        id='collision_graph',
        figure=template_graph
    )),

    html.Div(id='traj-rangeslider-title', children='traj-rangeslider'),
    dcc.RangeSlider(
        id='traj-edit-tool',
        min=1,
        max=100000,
        step=1,
        value=[1, 100000]),

    html.Div(id='trim-title', children='trim-factor'),
    dcc.Input(
                id="trim_window",
                type="number",
                #placeholder="trim factor",
                value= 3
            ),
    html.Div(id='speed-title', children='speed_factor'),
    dcc.Input(
                id="speed_window",
                type="number",
                #placeholder="trim factor",
                value= 20
            ),
    html.Div(id='clock-title', children='clock_factor'),
    dcc.Input(
                id="clock_window",
                type="number",
                #placeholder="trim factor",
                value= 500
            ),
    html.Button('start', id='button-n'),
])

@app.callback(
    dash.dependencies.Output('collision_graph', 'figure'),
    dash.dependencies.Output('intermediate-value', 'data'),
    #[dash.dependencies.Input('traj-edit-tool', 'value')], 
    [dash.dependencies.Input('speed_window', 'value')], 
    #[dash.dependencies.Input('clock_window', 'value')], 
    [dash.dependencies.Input('interval-component', 'n_intervals')], 
    [dash.dependencies.Input('trim_window', 'value')], 
    [dash.dependencies.State('intermediate-value', 'data')], 
    [dash.dependencies.State('button-n', 'n_clicks')], 
    )
def traj_edit(speed, n, trim_factor, counter, button_clicked):
    if button_clicked is None:
        raise PreventUpdate
    else:
        # print (n)
        
        takeoff_val = 77441
        counter=takeoff_val+n*speed
        update_range = [takeoff_val, counter]
        template_graph = template_graph_plot(update_range[0], update_range[1], trim_factor)
        # lower_time = each['timestamp'][min_selected]
        # upper_time = each['timestamp'][max_selected]
        # #print("LOWER TIME:", lower_time//1000000)
        # duration = (max_selected-min_selected)/frequency
        return template_graph, counter

@app.callback(
    [dash.dependencies.Output('interval-component', 'interval')],
    [dash.dependencies.Input('clock_window', 'value')], 
    )
def clock_edit(clock_factor):
        return [clock_factor]

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
