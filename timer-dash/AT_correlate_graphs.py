# Alliantech.
# FOCUS on graphing Vibration Data.

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_gif_component as gif

import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
import os
print(os. getcwd())
import numpy as np
import math
import plotly.express as px

#np.where(a < 5, a, 10*a)

path1 = '~/Documents/data/in-vivo/11_40/11_40_32_'
path2 = '~/Documents/data/in-vivo/11_56/11_56_06_'
path3 = '~/Documents/data/in-vivo/12_10/12_10_04_'
path4 = '~/Documents/data/in-vivo/12_22/12_22_20_'

df_traj1= pd.read_csv('~/Documents/data/in-vivo/11_40/11_40_32_vehicle_local_position_0.csv')
df_traj2= pd.read_csv('~/Documents/data/in-vivo/11_56/11_56_06_vehicle_local_position_0.csv')
df_traj3= pd.read_csv('~/Documents/data/in-vivo/12_10/12_10_04_vehicle_local_position_0.csv')
df_traj4= pd.read_csv('~/Documents/data/in-vivo/12_22/12_22_20_vehicle_local_position_0.csv')

df_control1 = pd.read_csv(path1 + 'vehicle_control_mode_0.csv')['flag_control_position_enabled']
df_control2 = pd.read_csv(path2 + 'vehicle_control_mode_0.csv')['flag_control_position_enabled']
df_control3 = pd.read_csv(path3 + 'vehicle_control_mode_0.csv')['flag_control_position_enabled']
df_control4 = pd.read_csv(path4 + 'vehicle_control_mode_0.csv')['flag_control_position_enabled']

####################
# PX4 ACCELERATION #
####################
df_acc2a = pd.read_csv(path2 + 'sensor_accel_0.csv')
df_acc2b = pd.read_csv(path2 + 'sensor_accel_1.csv')
df_acc2 = pd.concat([df_acc2a, df_acc2b])
# Get absolute values
df_acc2_abs = []
df_acc2_xy_abs = []
for i in range(len(df_acc2['x'])):#range(len(log_acc['timestamp']))
    # print(df_acc2['x'])
    # print("Here is", (df_acc2['x'].values[i])**2)
    # print("done")
    x = df_acc2['x'].values[i]
    y = df_acc2['y'].values[i]
    z = df_acc2['z'].values[i]
    acc_abs = math.sqrt(x**2 + y**2 + z**2)
    acc_abs_xy = math.sqrt(x**2 + y**2)
    df_acc2_abs.append(acc_abs)
    df_acc2_xy_abs.append(acc_abs_xy)

######################
# SLICE ACCELERATION #
######################
df_slice1 = pd.read_csv('~/Downloads/Test_Flight2_altitude_UNFILTERED.csv', decimal=",", sep=';', skiprows = 22)

# ATTEMPT TO PUT EXACT TIMES.
import datetime
start_datetime = datetime.datetime(2021, 8, 6, 14, 1, 50)
start_datetime = datetime.datetime(2021, 8, 6, 14, 6, 8)

# Slice ==> ABSOLUTE TIME: df_slice1_timestamps
start_slice = datetime.datetime(2021, 8, 6, 14, 6, 8) #SLICE TAKEOFF

df_slice1_timestamps = []
for timestamp in df_slice1['Time']:
    #print(timestamp)
    dt = datetime.timedelta(microseconds = timestamp*1000000) 
    datetime_value = start_slice + dt 
    #print(datetime_value)
    df_slice1_timestamps.append(datetime_value)
print("len of slice", len(df_slice1_timestamps) )

# PX4 ==> ABSOLUTE TIME: df_acc2_timestamps
start_drone = datetime.datetime(2021, 8, 6, 13, 56, 6) #DRONE TAKEOFF.

df_acc2_timestamps = []
for timestamp in df_traj2['timestamp']:
    since_start = datetime.timedelta(microseconds = timestamp)
    point_x = since_start + start_drone
    df_acc2_timestamps.append(point_x)
print("len of acc2", len(df_acc2_timestamps) )

## TEST
difference = df_slice1_timestamps [0] - df_acc2_timestamps[0]
print("fist is", df_slice1_timestamps [0])
print("starting at", difference )
print("equivalent to", difference.microseconds )
difference = df_slice1_timestamps [0] - df_acc2_timestamps[58442]   #START POINT
print("starting at", difference )
print("last is", df_slice1_timestamps [-1])
print("end at", df_slice1_timestamps [-453000] - df_acc2_timestamps[62198] )


######################
# ALL MY PLOTS       #
######################


fusion_graph = go.Figure()

fusion_graph.add_trace(
    go.Scattergl(
        x =  df_slice1_timestamps[:-453000:50],
        y =  df_slice1['Chan 0:3225A'][:-453000:50],
        mode='markers',
        name='SLICE DATA'
    ),
)

fusion_graph.add_trace(
    go.Scattergl(
        x =  df_acc2_timestamps[58442:],
        y =  df_acc2['x'][58442:],
        mode='markers',
        name='PIXHAWK DATA'
    ),
)

fusion_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='markers'))


app.layout = html.Div([

                dcc.Store(id='current_df_traj', data = [[0,0,0]]), #ensures rangeslider consistent 

                html.Div(className='row', children = [
                    html.Div([
                        html.Div([
                            html.H6(children='DRONE PORTEUR: GPS+MAGNETO @pts', id='small-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                            dcc.RangeSlider(
                                id='traj-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000])
                            ]),

                        html.Div(dcc.Graph(
                            id='trajectory',
                            figure=fusion_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        )),

                    ], className= 'five columns'),
                ]),
        ])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
