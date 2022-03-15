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
df_traj1= pd.read_csv('~/Documents/data/in-vivo/11_40/11_40_32_vehicle_local_position_0.csv')
df_traj2= pd.read_csv('~/Documents/data/in-vivo/11_56/11_56_06_vehicle_local_position_0.csv')
df_traj3= pd.read_csv('~/Documents/data/in-vivo/12_10/12_10_04_vehicle_local_position_0.csv')
df_traj4= pd.read_csv('~/Documents/data/in-vivo/12_22/12_22_20_vehicle_local_position_0.csv')

#TRAJ IS USELESS.
df_traj5= pd.read_csv('~/Documents/data/in-vivo/12_35/12_35_05_vehicle_local_position_0.csv')

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

path1 = '~/Documents/data/in-vivo/11_40/11_40_32_'
path2 = '~/Documents/data/in-vivo/11_56/11_56_06_'
path3 = '~/Documents/data/in-vivo/12_10/12_10_04_'
path4 = '~/Documents/data/in-vivo/12_22/12_22_20_'

df_mag1a = pd.read_csv(path1 + 'vehicle_magnetometer_0.csv')
df_mag1b = pd.read_csv(path1 + 'vehicle_magnetometer_1.csv')
df_mag1 = pd.concat([df_mag1a, df_mag1b])['magnetometer_ga[0]']
df_mag_time = pd.read_csv(path1 + 'vehicle_magnetometer_1.csv')['timestamp']
#print(df_mag1)

df_mag2a = pd.read_csv(path2 + 'vehicle_magnetometer_0.csv')
df_mag2b = pd.read_csv(path2 + 'vehicle_magnetometer_1.csv')
df_mag2 = pd.concat([df_mag2a, df_mag2b])['magnetometer_ga[0]']

df_mag3a = pd.read_csv(path3 + 'vehicle_magnetometer_0.csv')
df_mag3b = pd.read_csv(path3 + 'vehicle_magnetometer_1.csv')
df_mag3 = pd.concat([df_mag3a, df_mag3b])['magnetometer_ga[0]']

df_mag4a = pd.read_csv(path4 + 'vehicle_magnetometer_0.csv')
df_mag4b = pd.read_csv(path4 + 'vehicle_magnetometer_1.csv')
df_mag4 = pd.concat([df_mag4a, df_mag4b])['magnetometer_ga[0]']

df_baro1 = pd.read_csv(path1 + 'sensor_baro_0.csv')['pressure']
df_baro2 = pd.read_csv(path2 + 'sensor_baro_0.csv')['pressure']
df_baro3 = pd.read_csv(path3 + 'sensor_baro_0.csv')['pressure']
df_baro4 = pd.read_csv(path4 + 'sensor_baro_0.csv')['pressure']

df_tx1 = pd.read_csv(path1 + 'telemetry_status_0.csv')['tx_rate_avg']
df_tx2 = pd.read_csv(path2 + 'telemetry_status_0.csv')['tx_rate_avg']
df_tx3 = pd.read_csv(path3 + 'telemetry_status_0.csv')['tx_rate_avg']
df_tx4 = pd.read_csv(path4 + 'telemetry_status_0.csv')['tx_rate_avg']

df_acc1a = pd.read_csv(path1 + 'sensor_accel_0.csv')
df_acc1b = pd.read_csv(path1 + 'sensor_accel_1.csv')
df_acc1 = pd.concat([df_acc1a, df_acc1b])
#df_abs_acc1 = math.sqrt( df_acc1['x']**2 + df_acc1['y']**2 +df_acc1['z']**2 )

df_acc2a = pd.read_csv(path2 + 'sensor_accel_0.csv')
df_acc2b = pd.read_csv(path2 + 'sensor_accel_1.csv')
df_acc2 = pd.concat([df_acc2a, df_acc2b])

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

df_acc3a = pd.read_csv(path3 + 'sensor_accel_0.csv')
df_acc3b = pd.read_csv(path3 + 'sensor_accel_1.csv')
df_acc3 = pd.concat([df_acc3a, df_acc3b])

df_acc4a = pd.read_csv(path4 + 'sensor_accel_0.csv')
df_acc4b = pd.read_csv(path4 + 'sensor_accel_1.csv')
df_acc4 = pd.concat([df_acc4a, df_acc4b])

df_mini1 = pd.read_csv('~/Documents/data/in-vivo/11_56/Drone.csv', skiprows = 21)
#df_slice1 = pd.read_csv('~/Documents/data/in-vivo/11_56/Slice_1_1.csv', sep=';')

#FIRST FLIGHT
df_slice2 = pd.read_csv('~/Downloads/Test_Flight1_UNFILTERED.csv', decimal=",", sep=';', skiprows = 22)

#SECOND FLIGHT
df_slice1 = pd.read_csv('~/Downloads/Test_Flight2_altitude_UNFILTERED.csv', decimal=",", sep=';', skiprows = 22)

df_control1 = pd.read_csv(path1 + 'vehicle_control_mode_0.csv')['flag_control_position_enabled']
df_control2 = pd.read_csv(path2 + 'vehicle_control_mode_0.csv')['flag_control_position_enabled']
df_control3 = pd.read_csv(path3 + 'vehicle_control_mode_0.csv')['flag_control_position_enabled']
df_control4 = pd.read_csv(path4 + 'vehicle_control_mode_0.csv')['flag_control_position_enabled']


df_land1 = pd.read_csv(path1 + 'vehicle_land_detected_0.csv')['landed']
df_land2 = pd.read_csv(path2 + 'vehicle_land_detected_0.csv')['landed']
df_land3 = pd.read_csv(path3 + 'vehicle_land_detected_0.csv')['landed']
df_land4 = pd.read_csv(path4 + 'vehicle_land_detected_0.csv')['landed']

df_freefall1 = pd.read_csv(path1 + 'vehicle_land_detected_0.csv')['ground_contact']
df_freefall2 = pd.read_csv(path2 + 'vehicle_land_detected_0.csv')['ground_contact']
df_freefall3 = pd.read_csv(path3 + 'vehicle_land_detected_0.csv')['ground_contact']
df_freefall4 = pd.read_csv(path4 + 'vehicle_land_detected_0.csv')['ground_contact']

# import datetime
# dt = datetime.datetime(2021, 8, 6, 13, 24, 25)
# print("HERE DT IS", dt)
# start_timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
# print("START_TIME=", start_timestamp)
# df_mini1_timestamps = []
# for timestamp in df_mini1['Time'][::50]:
#     timestamp = datetime.datetime.fromtimestamp(timestamp//1000000000)
#     #print(timestamp)
#     df_mini1_timestamps.append(((timestamp)))


# ATTEMPT TO PUT EXACT TIMES.
import datetime
start_datetime = datetime.datetime(2021, 8, 6, 14, 1, 50)
start_datetime = datetime.datetime(2021, 8, 6, 14, 6, 8)

#start_timestamp = start_datetime.replace(tzinfo=datetime.timezone.utc).timestamp()
#print("START_TIME=", start_timestamp)
df_slice1_timestamps = []
for timestamp in df_slice1['Time'][::10]:
    #timestamp = datetime.datetime.fromtimestamp(timestamp//1)
    dt = datetime.timedelta(seconds = int(timestamp))#, microseconds = int((timestamp-int(timestamp))*1000)
    datetime_value = start_datetime + dt #lost microseconds
    df_slice1_timestamps.append(datetime_value)


# HANDLING TIMESTAMP VALUES # IN SECONDS+MILLI...
start_drone = datetime.datetime(2021, 8, 6, 13, 56, 6) #DRONE TAKEOFF.
start_slice_time = df_acc2['timestamp'][58442]

df_acc2_timestamps = []
print("starting aaat:", df_traj2['timestamp'].values[0])
print("starting aaat:", df_traj2['timestamp'].values[-1])

# for timestamp in df_acc2['timestamp'][58442:]:
#     #since_start = datetime.timedelta(microseconds = timestamp)
#     point_x = (timestamp - start_slice_time)//1000000
#     #print ("PT_WINDOW: ", point_x)
#     df_acc2_timestamps.append(point_x)
# print('this?')

#####  SLICE GRAPH 
time_graph = go.Figure()
time_graph.add_trace(
    go.Scattergl(
        x =  df_slice1_timestamps,
        y =  df_slice1['Chan 0:3225A'][::10],
        mode='markers',
        name= 'slice'
    ),
)

# FINDING FIRST POINT.
start_slice = datetime.datetime(2021, 8, 6, 14, 6, 8) #SLICE TAKEOFF
start_datetime = datetime.datetime(2021, 8, 6, 13, 56, 6) #DRONE TAKEOFF.

timestamp=df_slice1['Time'].values[0]
dt = datetime.timedelta(seconds = int(timestamp//1))
datetime_value = start_slice + dt 
print("START TIME: ", datetime_value)
# FIND slice[0] IN PATH
# for id_path, xy_timestamp in enumerate(df_acc2['timestamp']):
#     since_start = datetime.timedelta(seconds = int(xy_timestamp/1000000))
#     point_window = start_datetime + since_start
#     print(datetime_value, point_window)   

#     if datetime_value == point_window:
#         print(point_window)
#         print("AHA", id_path)
#         #167296
#         break
#     else:
#         continue

# FINDING LAST POINT.
xy_timestamp = df_traj2['timestamp'].values[-1]
acc_timestamp = df_acc2['timestamp'].values[-1]
print("One vs Other:", xy_timestamp, acc_timestamp)

since_start = datetime.timedelta(seconds = int(xy_timestamp//1000000))
point_window = start_datetime + since_start
print ("PT_WINDOW: ", point_window)
# # FIND path[-1] IN SLICE   
# for id_slice, slice_timestamp in enumerate(df_slice1['Time']):
#     dt = datetime.timedelta(seconds = int(slice_timestamp))
#     datetime_value = start_slice + dt
#     print(datetime_value, point_window)
#     if datetime_value == point_window:
#         print(point_window)
#         print("AHA", id_slice)
#         #380000
#         break
#     else:
#         continue
fusion_graph = go.Figure()
print("x values of df_acc2 is", len(df_acc2['x'].values[167296:]))
print("x values of df_traj is", len(df_traj2['timestamp'].values))

print("slice is", len(df_slice1['Time'].values[:380000]))
print("traj is", len(df_traj2['x'].values[58442:]))
# x values of df_acc2 is 188756
# slice is 380000
# traj is 3757


#pump up the xyz data to length of dataframe
# df_traj_new_x = fita2blen(each['x'], len(df_mag_i))[min_selected:max_selected]
# df_traj_new_y = fita2blen(each['y'], len(df_mag_i))[min_selected:max_selected]
# df_traj_new_z = fita2blen(each['z'], len(df_mag_i))[min_selected:max_selected]

# FIRST USE DATAFRAME.
# df_fusion = pd.DataFrame({
#                             'time': df_slice1['Time'][:380000],
#                             'x': df_traj2['x'][58442:],
#                             'y': df_traj2['y'][58442:],
#                             'z': df_traj2['z'][58442:],
#                             'acc_slice_x': df_slice1['Chan 0:3225A'][:380000],
#                             'acc_px4_x': df_acc2['x'][167296:],
#                             'acc_px4_xyz': df_acc2_abs[167296:],
#                             'acc_px4_xy': df_acc2_xy_abs[167296:]
#                             })



# fusion_graph.add_trace(
#     go.Scatter3d(
#         x =  df_fusion['x'],
#         y =  df_fusion['y'],
#         z =  df_fusion['z'],
#         mode='markers',
#         marker=dict(
#             color= df_fusion['acc_slice_x'],
#             colorscale='Viridis',
#             line_width=0.0,
#             colorbar = dict(
#                     len=1,
#                     thickness=50.0,
#                     x = -0.3,
#                     xanchor='right',
#                     outlinewidth=0.0
#                 ),
#             showscale=False,
#         )
#     ),
# )

# fusion_graph.add_trace(
#     go.Scattergl(
#         x =  df_slice1['Time'][:-453000:50],
#         y =  df_slice1['Chan 0:3225A'][:-453000:50],
#         mode='markers',
#         name=43
#     ),
# )

#167296
#test_window = [167296:334960]
# fusion_graph.add_trace(
#     go.Scattergl(
#         x =  df_acc2_timestamps,
#         y =  df_acc2['x'][58442:],
#         mode='markers',
#         name=554
#     ),
# )

fusion_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='markers'))

#####  MINI GRAPH 
# time_graph = go.Figure()
# time_graph.add_trace(
#     go.Scattergl(
#         x =  df_mini1_timestamps,
#         y =  df_mini1['28736:ch3'][::50],
#         mode='markers',
#         marker=dict(
#             color= df_mini1['28736:ch3'],
#             colorscale='Viridis',
#             line_width=1,
#             colorbar = dict(
#                     len=1,
#                     thickness=50.0,
#                     x = -0.3,
#                     xanchor='right',
#                     outlinewidth=0.0
#                 ),
#             showscale=False,
#         )
#     ),
# )


# df_date = pd.DataFrame({
#                             'date': local_time_timestamps,
#                             # 'y': df_traj_new_y[::trim_step],
#                             # 'z': df_traj_new_z[::trim_step],
#                             # 'mag': df_mag_i[::trim_step],
#                             })

# colour_test = True
traj_graph = go.Figure()
# count = 0
# for each in [df_traj1, df_traj2, df_traj3, df_traj4]:
#     #print (each)
#     #if colour_test == True:
#         # traj_graph = px.scatter(df_magnetometer, x='x', y='y',
#         #                     color = 'mag', color_continuous_scale=px.colors.sequential.Rainbow[::],
#         #                     )
#                 # break
#     count+=1
#     #recreate dataframe name on the fly
#     df_mag_i = vars()["df_mag"+str(count)]
#     #pump up the xyz data to length of dataframe
#     df_traj_new_x = fita2blen(each['x'], len(df_mag_i))
#     df_traj_new_y = fita2blen(each['y'], len(df_mag_i))
#     df_traj_new_z = fita2blen(each['z'], len(df_mag_i))
#     #optional data length check...
#     #print("CHECK:", len(df_mag1['magnetometer_ga[0]']), len(df_traj1_new_x), len(df_traj1_new_y), len(df_traj1_new_z))
#     #PASSED: 42634 42634 42634 42634
#     # Visibility/Loading. problem: gotta sample at lower frequency
#     trim_step = 15
#     df_magnetometer = pd.DataFrame({
#                                 'x': df_traj_new_x[::trim_step],
#                                 'y': df_traj_new_y[::trim_step],
#                                 'z': df_traj_new_z[::trim_step],
#                                 'mag': df_mag_i[::trim_step],
#                                 })

#     traj_graph.add_trace(
#         go.Scattergl(
#             x = df_magnetometer['x'],
#             y = df_magnetometer['y'],
#             mode='markers',
#             marker=dict(
#                 color=df_magnetometer['mag'],
#                 colorscale='Viridis',
#                 line_width=1,
#                 #showscale=True,
#                 colorbar = dict(
#                         len=1,
#                         thickness=50.0,
#                         #tickangle=-90,
#                         x = -0.3,
#                         xanchor='right',
#                         outlinewidth=0.0
#                     ),
#                 #line_width=1,
#                 showscale=False,
#             )
#         ),
#     )

    # traj_graph.add_trace(go.Scatter(x=each['y'][::15], y=each['x'][::15],
    #                     mode='markers',
    #                     name='df_traj'+str(count)))



traj_graph.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))

#adjust position
tightfit = dict(l=200, r=0, t=0, b=20)
traj_graph.update_layout(
    margin=tightfit,
)

_3d_traj_graph = go.Figure()


# count = 0
# for each in [df_traj1, df_traj2, df_traj3, df_traj4]:
#     #print (each)
#     count+=1   
#     # if colour_test == True:
#     #     _3d_traj_graph = px.scatter_3d(df_magnetometer, x='x', y='y', z= 'z',
#     #                         color = 'mag', color_continuous_scale=px.colors.sequential.Rainbow[::],
#     #                         )
#     #     break
#     # else:
#     #     _3d_traj_graph.add_trace(
#     #         go.Scatter3d(x=each['x'][::15], y=-each['y'][::15], z= -each['z'][::15],
#     #                         mode='markers',
#     #                         name='df_traj'+str(count))
#     #                         )
#     df_traj_new_x = fita2blen(each['x'], len(df_mag1))
#     df_traj_new_y = fita2blen(each['y'], len(df_mag1))
#     df_traj_new_z = fita2blen(each['z'], len(df_mag1))
#     #print("CHECK:", len(df_mag1['magnetometer_ga[0]']), len(df_traj1_new_x), len(df_traj1_new_y), len(df_traj1_new_z))
#     #PASSED: 42634 42634 42634 42634
#     trim_step = 15
#     df_magnetometer = pd.DataFrame({
#                                 'x': df_traj_new_x[::trim_step],
#                                 'y': df_traj_new_y[::trim_step],
#                                 'z': df_traj_new_z[::trim_step],
#                                 'mag': df_mag1[::trim_step],
#                                 })

#     _3d_traj_graph.add_trace(
#         go.Scatter3d(
#             x = df_magnetometer['x'],
#             y = df_magnetometer['y'],
#             z = -df_magnetometer['z'],
#             mode='markers',
#             marker=dict(
#                 color=df_magnetometer['mag'],
#                 colorscale='Viridis',
#                 colorbar = dict(
#                     #len=0.2,
#                     thickness=50.0,
#                     #tickangle=-90,
#                     x = -0.1,
#                     xanchor='center',
#                     outlinewidth=0.0
#                 ),
#                 line_width=1,
#                 showscale=True,
#             )
#         ),
#     )

_3d_traj_graph.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
#adjust position
tightfit = dict(l=20, r=20, t=0, b=100)
_3d_traj_graph.update_layout(
    margin=tightfit,
)

# z_data = 0
# z=[]

# # for i in range(100):
# #     z = z.append(z_data)
# z = np.zeros((10,10))
# #sh_0, sh_1 = z.shape
# x, y = np.linspace(-10, 50, 10), np.linspace(-30, 30, 10)
# # fijg = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

# _3d_traj_graph.add_trace(go.Surface(z=z, x=x, y=y, showscale=False, opacity=0.9, ),)

#PLEASE reduce the marker size. 
_3d_traj_graph.update_traces(marker=dict(size=5),
                    selector=dict(mode='markers'))


with open("notes/notes_crashland.txt", "r") as f:
    notes = f.readlines()
#html.Br()#
rangeval = 100

app.layout = html.Div([

                dcc.Store(id='current_df_traj', data = [[0,0,0]]), #ensures rangeslider consistent 

                html.Div(className='row', children = [


                    html.Div([
                        html.H6(children='DRONE PORTEUR: GPS+MAGNETO @'+str(rangeval)+'pts', id='small-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        html.Div(dcc.Graph(
                            id='3d_traj',
                            figure=_3d_traj_graph,
                            
                        )),

                    ], className= 'five columns'),
                    
                    html.Div([
                        html.H3(children='Flight Analysis', id='big-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
                        html.Iframe(
                        id = 'external_video',
                        src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
                            style={"height": "300px", "width": "100%"}),
                    ], className='three columns'),

                    html.Div([
                        html.Div(className='row', style={"margin-top": "30px"}, children=[
                            html.Div([html.Button("<", id="left_pic")], style = {'width': '5%', 'display': 'inline-flex', 'align-items': 'left', 'justify-content': 'left'}),  
                            html.Div([html.Button('GALLERY', id='tb_assigned')], style = {'width': '85%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 
                            html.Div([html.Button(">", id="right_pic")], style = {'width': '5%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}),  
                        ]),
                        #html.H3(children='', id='mini-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
                        html.Iframe(
                        id = 'external_gallery',
                        src="https://drive.google.com/file/d/1Zon_cCdtncfQGMEADcY6j_KMnNAVzX5T/preview",
                            style={"height": "300px", "width": "100%"}),
                    ], className='three columns'),

                    html.Div(html.H6(children=notes, id='text-div', 
                            style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}
                            ), className='six columns'),
                ]),

                html.Div(className='row', children = [
                    html.Div(dcc.Graph(
                        id='trajectory',
                        figure=traj_graph,
                        style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                    ), className='five columns'),

                        html.Div([
                            
                            html.Div(id='trim-slider-title', children='trim-slider'),
                            
                            dcc.Slider(
                                id='my-slider',
                                min=1,
                                max=20,
                                step=1,
                                value=10,
                            ),

                            html.Div(id='traj-rangeslider-title', children='traj-rangeslider'),
                            dcc.RangeSlider(
                                id='traj-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000])
            

                            ], className='six columns'),


                    html.Div([
                        html.H5(children='Sensor Chooser', id='radio-2', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        dcc.RadioItems(
                            id='trajectory-select',
                            options=[
                                {'label': 'MAGNETOMETER', 'value': 'MAGNETOMETER'},
                                {'label': 'BAROMETER', 'value': 'BAROMETER'},
                                {'label': 'PX4_ACCELEROMETER', 'value': 'PX4_ACCELEROMETER'},
                                {'label': 'SLICE_ACCELEROMETER', 'value': 'SLICE_ACCELEROMETER'},
                                {'label': 'POWER_SENSOR', 'value': 'POWER_SENSOR'},
                                {'label': 'SIGNAL_STRENGTH', 'value': 'SIGNAL_STRENGTH'},
                                {'label': 'CONTROLLER_PERIODS', 'value': 'CONTROLLER_PERIODS'},
                                {'label': 'DETECT_LAND', 'value': 'DETECT_LAND'},
                                {'label': 'WIRELESS_ACCEL', 'value': 'WIRELESS_ACCEL'},
                                {'label': 'FREEFALL', 'value': 'FREEFALL'},
                                {'label': '', 'value': ''},
                            ],
                            value='MAGNETOMETER'),
                    ], className='two columns'),



                    html.Div([
                        html.H5(children='Available videos', id='radio-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        dcc.RadioItems(
                            id='sensor-select',
                            options=[
                                {'label': 'ACCEL FIMI', 'value': 'ACCEL FIMI'},
                                {'label': 'ACCEL PORTEUR', 'value': 'ACCEL PORTEUR'},
                                {'label': 'DRONE DROP', 'value': 'DRONE_DROP'},
                                {'label': 'VIDEO_1_EXTERNE', 'value': 'VIDEO_1_EXTERNE'},
                                {'label': 'VIDEO_2_EXTERNE', 'value': 'VIDEO_2_EXTERNE'},
                                {'label': '', 'value': ''},
                                {'label': 'PICTURE_OF_INTEREST', 'value': 'PICTURE_OF_INTEREST'},
                                {'label': 'OLD_DRONE', 'value': 'OLD_DRONE'},
                                {'label': '', 'value': ''},
                            ],
                            value='ACCEL FIMI'),
                    ], className='two columns'),

                    html.Div([
                        html.H5(children='Advanced Configuration', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        dcc.Checklist(
                            id = 'parameters',
                            options=[
                                {'label': 'Display Relevant Vid', 'value': 'CB_LINK'},
                                {'label': 'Timescale Mode', 'value': 'MTL'},
                                {'label': 'Search-and-Rescue Galleries', 'value': 'GALLERY_CB'},
                                {'label': 'Photogrammetry Galleries', 'value': 'PG_CB'},
                                {'label': '...', 'value': 'SF'},
                                {'label': '...', 'value': 'SF'},
                                {'label': '...', 'value': 'SF'},

                            ],
                            value=[''])  

                    ], className='two columns'),

                    html.Div(dcc.Graph(
                        id='timeplot',
                        figure=time_graph,
                        style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                    ), className='twelve columns'),

                    html.Div(dcc.Graph(
                        id='sensorfusion',
                        figure=fusion_graph,
                        style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                    ), className='twelve columns'),
                ]),
            ])
#################################### CALLBACK PREP ########################################33

df_dropdown = pd.DataFrame({
                   
                        # PHOTOGRAMMETRY |

                        'PANNEAU_PICS': [
                            'https://drive.google.com/file/d/1YUL7MF4tbzU4DWa73rYeXCXPV-widEUD/preview', 
                            'https://drive.google.com/file/d/1U0WHI7vRvatlIXWEMhw7REO17Pm55iv7/preview', 
                            'https://drive.google.com/file/d/1FcW8lxtlIqtJ5-ja8_Ho-19WBhJhj666/preview', 
                            'https://drive.google.com/file/d/1O1Pi17PzOXSC0TO_U2cnetYRKJQmtu0U/preview'],

                        'PANNEAU_RECONSTRUCTION': [
                            'https://drive.google.com/file/d/1McrX8u598YEEO93O9eVeA3iAeZs0-Iod/preview', 
                            'https://drive.google.com/file/d/1nluYwjjjm0bzbJR5VBNBy24oXbOuvHCt/preview', 
                            'https://drive.google.com/file/d/1nfqxeZYNRuI4Bj2MQcdrGQtiYbII91MN/preview', 
                            'https://sketchfab.com/models/a1b9a816010449c8bd18d22bf97e8097/embed'],

                        # SEARCH-AND-RESCUE |

                        'SEARCH-AND-RESCUE': [
                            'https://drive.google.com/file/d/19wgkDTYNVA4A_fmpMz-WmHqTB2R5bk_C/preview', 
                            'https://drive.google.com/file/d/19MasuPm3lsEmjsTILxUMVIKGOahaBItV/preview', 
                            'https://drive.google.com/file/d/1mTYR06HHS_9bhYe9-izjHSksmgRvhBmO/preview', 
                            'https://drive.google.com/file/d/1jWz16KUNf8hY-u4aP1_KZQhyjwBLkt0w/preview'],    

                        'PICTURE_OF_INTEREST': [
                            'https://drive.google.com/file/d/1dyWZiNHd1I1ovZ-IGBW9g4VVXvbGsAfm/preview', 
                            'https://drive.google.com/file/d/1DPsOX69232mCBACYPiVrIoayoGslHgpZ/preview', 
                            'https://drive.google.com/file/d/1V04kX__1c3OFFOtxwieQof1PqbMP_Gnd/preview', 
                            'https://drive.google.com/file/d/1u9rFmVGn8--bBiBmqwHaCSxWxmfVWn6u/preview'], 


                        # DRONE DROP |

                        'DRONE_DROP': [
                            '', 
                            'https://drive.google.com/file/d/1PqFE7UYoIGfDvFO3icczkIDlsqC0ADTe/preview', 
                            'https://drive.google.com/file/d/1MiYu6TmpzqDHRpUMnP53uU28SoLupY-0/preview', 
                            ''],

                        'ACCEL FIMI': [
                            'a', 
                            'https://drive.google.com/file/d/1DTVdkQwDl5XYryyXCSm8t9W9oyFsKeRi/preview', 
                            'https://drive.google.com/file/d/1UBIq9C9hXVHWmlX53Shb1dI_FK83e5XU/preview', 
                            'd'],


                        'ACCEL PORTEUR': [
                            'A', 
                            'https://drive.google.com/file/d/1xwuA-BSdjV0qM0Dv9P3mmf14OgaSeRhz/preview', 
                            'https://drive.google.com/file/d/1WVUky43TWml9K10CJlbQP-vIsZeVrS6O/preview', 
                            'D'],            

                        'OLD_DRONE': [
                            'https://drive.google.com/file/d/1n9hQwDYw2mtS1uIkyDlQ642rOWrbFJt0/preview', 
                            'https://drive.google.com/file/d/1n9hQwDYw2mtS1uIkyDlQ642rOWrbFJt0/preview', 
                            '', 
                            ''],    
})

                                # {'label': 'PHOTOGRAMMETRY', 'value': 'PHOTOGRAMMETRY'},
                                # {'label': 'DRONE DROP', 'value': 'DRONE DROP'},
                                # {'label': 'ACCEL FIMI', 'value': 'ACCEL FIMI'},
                                # {'label': 'ACCEL PORTEUR', 'value': 'ACCEL PORTEUR'},


## TF
df_chore= pd.read_csv('~/Documents/data/eval_tests/tf_chore.csv')
df_hover= pd.read_csv('~/Documents/data/eval_tests/tf_hover.csv')
df_2d1a= pd.read_csv('~/Documents/data/eval_tests/tf_2d1a.csv')
df_3d1a= pd.read_csv('~/Documents/data/eval_tests/tf_3d1a.csv')
df_xr1= pd.read_csv('~/Documents/data/eval_tests/tf_xr1.csv')

df_ht1= pd.read_csv('~/Documents/data/eval_tests/tf_ht1.csv')
## CAMERA
df_cam3_xr1 = pd.read_csv('~/Documents/data/eval_tests/cam3_xr1.csv')


#EDIT TRAJ GRAPH BASED ON TRAJ
@app.callback(
    dash.dependencies.Output('trajectory', 'figure'),
    dash.dependencies.Output('3d_traj', 'figure'),
    [dash.dependencies.Output('current_df_traj', 'data')],
    dash.dependencies.Output('small-title', 'children'),
    [dash.dependencies.Input('my-slider', 'value')],
    [dash.dependencies.Input('traj-edit-tool', 'value')],
    
    [dash.dependencies.Input('trajectory-select', 'value')],
    [dash.dependencies.Input('parameters', 'value')],
    [dash.dependencies.State('current_df_traj', 'data')])
    
def update_figure(trim_selected, traj_range, category, params, cb_trig):
    #print(traj_range)
    sensor_data = 'df_mag'
    if category == 'MAGNETOMETER':
        sensor_data = "df_mag"
        frequency = 237
    if category == 'BAROMETER':
        sensor_data = "df_baro"
        frequency = 237
    if category == 'SIGNAL_STRENGTH':
        sensor_data = "df_tx"
        frequency = 237

    if category == 'CONTROLLER_PERIODS':
        sensor_data = "df_control"
        frequency = 237
    if category == 'DETECT_LAND':
        sensor_data = "df_land"
        frequency = 237
    if category == 'FREEFALL':
        sensor_data = "df_freefall"
        frequency = 237
    # if category == 'SLICE_ACCELEROMETER':
    #     sensor_data = "df_slice"
    #     frequency = 237

    frequency = 237

    # 2D
    traj_graph = go.Figure()
    traj_graph.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=0.0,
        xanchor="right",
        x=1
    ))
    #adjust position
    tightfit = dict(l=200, r=0, t=0, b=40)
    traj_graph.update_layout(
        margin=tightfit,
    )
    # 3D
    _3d_traj_graph = go.Figure()

    #start_datetime = datetime.datetime(2021, 8, 6, 13, 24, 25)
    start_datetime = datetime.datetime(2021, 8, 6, 13, 40, 32)
    start_datetime2 = datetime.datetime(2021, 8, 6, 13, 56, 6)
    start_datetime3 = datetime.datetime(2021, 8, 6, 14, 10, 4)
    start_datetime4 = datetime.datetime(2021, 8, 6, 14, 22, 20)
    #start_datetime5 = datetime.datetime(2021, 8, 6, 14, 35, 5)

    count = 0
    for each in [df_traj1, df_traj2, df_traj3, df_traj4]:
        count+=1
        #recreate dataframe name on the fly
        df_mag_i = globals()[str(sensor_data)+str(count)]
        print(df_mag_i)

        #print("range is", traj_range, "and len is", len(df_mag_i))
        # 16638
        min_selected = int(traj_range[0]*len(df_mag_i)/100000)
        max_selected = int(traj_range[1]*len(df_mag_i)/100000)
        #print(min_selected, max_selected)
        lower_time = each['timestamp'][min_selected]
        upper_time = each['timestamp'][max_selected]
        #print("LOWER TIME:", lower_time//1000000)
        duration = (max_selected-min_selected)/frequency
        
        since_start = datetime.timedelta(seconds = int(lower_time//1000000))
        point_a = start_datetime + since_start
        since_start = datetime.timedelta(seconds = int(upper_time//1000000))
        point_b = start_datetime + since_start
        duration = point_b - point_a
        #6385801

        small_title = category + '@ ['+str(point_a)+'|'+str(point_b)+'] | '+str(duration)+'s'
        
        _sensor_readjust = df_mag_i[min_selected:max_selected]


        #pump up the xyz data to length of dataframe
        df_traj_new_x = fita2blen(each['x'], len(df_mag_i))[min_selected:max_selected]
        df_traj_new_y = fita2blen(each['y'], len(df_mag_i))[min_selected:max_selected]
        df_traj_new_z = fita2blen(each['z'], len(df_mag_i))[min_selected:max_selected]
        # Visibility/Loading. problem: gotta sample at lower frequency
        trim_step = trim_selected
        df_magnetometer = pd.DataFrame({
                                    'x': df_traj_new_x[::trim_step],
                                    'y': df_traj_new_y[::trim_step],
                                    'z': df_traj_new_z[::trim_step],
                                    'mag': _sensor_readjust[::trim_step],
                                    })

        traj_graph.add_trace(
            go.Scattergl(
                x = df_magnetometer['x'],
                y = df_magnetometer['y'],
                mode='markers',
                marker=dict(
                    size=2,
                    color=df_magnetometer['mag'],
                    colorscale='Viridis',
                    line_width=0.3,
                    colorbar = dict(
                            len=1,
                            thickness=50.0,
                            x = -0.3,
                            xanchor='right',
                            outlinewidth=0.0
                        ),
                    showscale=False,
                )
            ),
        ),
        _3d_traj_graph.add_trace(
            go.Scatter3d(
                x = df_magnetometer['x'],
                y = df_magnetometer['y'],
                z = -df_magnetometer['z'],
                mode='markers',
                marker=dict(
                    color=df_magnetometer['mag'],
                    colorscale='Viridis',
                    size = 4,

                    colorbar = dict(
                        #len=0.2,
                        thickness=50.0,
                        #tickangle=-90,
                        x = -0.1,
                        xanchor='center',
                        outlinewidth=0.0
                    ),
                    line_width=1,
                    showscale=True,
                )
            ),
        )


    _3d_traj_graph.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=0.0,
        xanchor="right",
        x=1
    ))

    # _3d_traj_graph.update_layout(legend=dict(
    #     orientation="h",
    #     yanchor="bottom",
    #     y=1.02,
    #     xanchor="right",
    #     x=1
    # ))
    #adjust position
    tightfit = dict(l=20, r=20, t=0, b=100)
    _3d_traj_graph.update_layout(
        margin=tightfit,
    )

    z_data = 0
    z=[]

    # for i in range(100):
    #     z = z.append(z_data)
    z = np.zeros((10,10))
    #sh_0, sh_1 = z.shape
    x, y = np.linspace(-10, 50, 10), np.linspace(-30, 30, 10)
    # fijg = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

    _3d_traj_graph.add_trace(go.Surface(z=z, x=x, y=y, showscale=False, opacity=0.9, ),)

    #PLEASE reduce the marker size. 


    # _3d_traj_graph.update_traces(marker=dict(size=1),
    #                     selector=dict(mode='markers'))    
    # #print(df_traj)
    # #traj_range = [1, len(df_traj)]

    # #adapt .csv to slider range
    # print("df:", df_traj)
    # print("range is", traj_range, "and len is", len(df_traj))
    # # 16638
    # min_selected = int(traj_range[0]*len(df_traj)/100000)
    # max_selected = int(traj_range[1]*len(df_traj)/100000)
    # print(min_selected, max_selected)
    # frequency = 237
    # duration = (max_selected-min_selected)/frequency

    # title_edit = category + '@ ['+str(min_selected)+':'+str(max_selected)+']    | '+str(round(duration, 2))+'s @'+str(frequency)+'Hz |'
    # _traj_data = df_traj[min_selected:max_selected]
    # print("data:", _traj_data)
    # print("done")
    # traj_graph = go.Figure()
    # #graph as many drones as exists in the newly selected data
    # for id in range(6):
    #     print (id+1) 
        
    #     drone_traj_x = []
    #     drone_traj_y = []
    #     #print(traj_range[1])
    #     for entry in _traj_data.index:
    #         #print(entry)
    #         if _traj_data['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
    #             drone_traj_x.append(_traj_data['field.transforms0.transform.translation.x'][entry])
    #             drone_traj_y.append(_traj_data['field.transforms0.transform.translation.y'][entry])

    #     traj_graph.add_trace(go.Scatter(x=drone_traj_x, y=drone_traj_y,
    #                         mode='markers',
    #                         name='drone '+str(id+1)))

    # # KEEPING THESE SEPARATE FOR NOW.
    # #IDEA FOR PARAM: Display 3D Version. (trig next callback.)
    # _3d_traj_graph = go.Figure()

    # for id in range(6):
    #     print (id+1) 

    #     drone_traj_x = []
    #     drone_traj_y = []
    #     drone_traj_z = []
    #     for entry in _traj_data.index:
    #         if _traj_data['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
    #             drone_traj_x.append(_traj_data['field.transforms0.transform.translation.x'][entry])
    #             drone_traj_y.append(_traj_data['field.transforms0.transform.translation.y'][entry])
    #             drone_traj_z.append(_traj_data['field.transforms0.transform.translation.z'][entry])

    #     _3d_traj_graph.add_trace(go.Scatter3d(x=drone_traj_x, y=drone_traj_y, z= drone_traj_z,
    #                         mode='markers',
    #                         name='drone '+str(id+1),
    #                         ),)           
    #     #PLEASE reduce the marker size. 
    #     _3d_traj_graph.update_traces(marker=dict(size=1),
    #                     selector=dict(mode='markers'))
                        
    # # IN CASE YOU WANT TO SEE BASE COMMANDS.
    # # drone2_offset = [-0.3, -0.01]
    # # traj_graph.add_trace(go.Scatter(x=df_chore_cmd['x^0']+drone2_offset[0], y=df_chore_cmd['y^0']+drone2_offset[1],
    # #                     mode='markers',
    # #                     name='Fo8 '))

    #PARAM: Display Relevant Vid. (trig next callback.)
    print(params)
    cb_trig = [0,0,0]
    if 'CB_LINK' in params:
        cb_trig[0] = 1 # LINKED
    else:
        cb_trig[0] = 0 #'UNLINKED'

    if 'GALLERY_CB' in params:
        cb_trig[1] = 1 # LINKED
    else:
        cb_trig[1] = 0 #'UNLINKED'

    if 'PG_CB' in params:
        cb_trig[2] = 1 # LINKED
    else:
        cb_trig[2] = 0 #'UNLINKED'

    return traj_graph, _3d_traj_graph, [cb_trig], small_title#traj_graph, _3d_traj_graph, cb_trig, title_edit

@app.callback(
    dash.dependencies.Output('external_gallery', 'src'),
    dash.dependencies.Output('external_video', 'src'),
    [dash.dependencies.Input('sensor-select', 'value')],
    [dash.dependencies.Input('current_df_traj', 'data')],
    [dash.dependencies.Input('right_pic', 'n_clicks')],
    [dash.dependencies.Input('left_pic', 'n_clicks')],
    [dash.dependencies.State('trajectory-select', 'value')])
def update_figure( sensor, cb_trig, right, left, traj_select):
    print("chosen sensor:", sensor)

    if (right is None):
        right = 0
    if (left is None):
        left = 0
    pic_id = (right - left)%len(df_dropdown['SEARCH-AND-RESCUE'])

    print("max nb of options:", len(df_dropdown['SEARCH-AND-RESCUE']))
    gallery_src = df_dropdown[sensor][2]
    url_garage = df_dropdown[sensor][1]

    #Advanced Configuration:
    print (cb_trig)
    if cb_trig[0][0] == 1:
        url_garage = df_dropdown[traj_select][1]

    if cb_trig[0][1] == 1:
        gallery_src = df_dropdown['SEARCH-AND-RESCUE'][pic_id]
        url_garage = df_dropdown['PICTURE_OF_INTEREST'][pic_id]

    if cb_trig[0][2] == 1:
        url_garage = df_dropdown['PANNEAU_PICS'][pic_id]
        gallery_src = df_dropdown['PANNEAU_RECONSTRUCTION'][pic_id]

    # if cb_trig[0][3] == 1:
    #     url_garage = df_dropdown['DRONE_DROP'][1]
    #     gallery_src = df_dropdown['DRONE_DROP'][2]

    return gallery_src, url_garage

# @app.callback(
#     dash.dependencies.Output('external_gallery', 'src'),
#     [dash.dependencies.Input('right_pic', 'n_clicks')],
#     [dash.dependencies.Input('left_pic', 'n_clicks')])
# def update_figure(right, left):
#     pic_id = (right - left)%len(df_dropdown['SEARCH-AND-RESCUE'])
#     print("seen as...", len(df_dropdown['SEARCH-AND-RESCUE']))
#     gallery_src = df_dropdown['SEARCH-AND-RESCUE'][pic_id]
#     if 'GALLERY_CB' in cb_trig:
#         url_garage = df_dropdown[traj_select][pic_id]
#     return gallery_src

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')


