# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from logging import log
from typing import Any
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#TO DO: 
#SURFACE PLOT INSIDE graph_object ALONGSIDE SCATTER PLOT.
# RANGEBAR TO EXAMINE ITS DATA
# 2ND TOP SCREEN: VIDEO RENDER *IS IT POSSIBLE
# 2ND TOP SCREEN SYNC WITH RANGEBAR

def fita2blen(f_val, x_desired):
    MAX_X = len(f_val)
    FINALLEN_X = x_desired
    CURRENTLEN_X = len(f_val)
    #x on 10 points, then 100 points
    x_current = list(np.linspace(1,MAX_X,CURRENTLEN_X))
    x_final = list(np.linspace(1,MAX_X,FINALLEN_X))
    # now function y
    # #random y
    # rrange = np.random.randint(1, 100, size=(1, CURRENTLEN_X))
    # CURRENT_Y = list(rrange[0, :])
    # func = CURRENT_Y
    # interpolate on 100 values.
    interp = np.interp(x_final, x_current, f_val )
    interp = list(interp)
    #print (interp)
    return interp

########### DATA ######################3
# ~/Documents/data/vendredi_auto$ ls

# @ 16:02                                                  # @ 16:13 # Drone flown straight, weak, drops gradually.

# log_182_2021-7-23-16-02-04_adc_report_0.csv              log_185_2021-7-23-16-13-28_adc_report_0.csv
# log_182_2021-7-23-16-02-04_sensor_accel_0.csv            log_185_2021-7-23-16-13-28_sensor_accel_0.csv
# log_182_2021-7-23-16-02-04_sensor_accel_1.csv            log_185_2021-7-23-16-13-28_sensor_accel_1.csv
# log_182_2021-7-23-16-02-04_sensor_gps_0.csv              log_185_2021-7-23-16-13-28_sensor_gps_0.csv
# log_182_2021-7-23-16-02-04_vehicle_gps_position_0.csv    log_185_2021-7-23-16-13-28_vehicle_gps_position_0.csv
# log_182_2021-7-23-16-02-04_vehicle_local_position_0.csv  log_185_2021-7-23-16-13-28_vehicle_local_position_0.csv

# @ 16:06                                                  # @ 16:14 # Drone flown straight, Lockdown, stunned.

# log_183_2021-7-23-16-06-18_adc_report_0.csv              log_186_2021-7-23-16-14-40_adc_report_0.csv
# log_183_2021-7-23-16-06-18_sensor_accel_0.csv            log_186_2021-7-23-16-14-40_sensor_accel_0.csv
# log_183_2021-7-23-16-06-18_sensor_accel_1.csv            log_186_2021-7-23-16-14-40_sensor_accel_1.csv
# log_183_2021-7-23-16-06-18_sensor_gps_0.csv              log_186_2021-7-23-16-14-40_sensor_gps_0.csv
# log_183_2021-7-23-16-06-18_vehicle_gps_position_0.csv    log_186_2021-7-23-16-14-40_vehicle_gps_position_0.csv
# log_183_2021-7-23-16-06-18_vehicle_local_position_0.csv  log_186_2021-7-23-16-14-40_vehicle_local_position_0.csv

# @ 16:11 # Drone flown straight, weak, sudden drop.       # @ 16:24 # Drone goes up, freaks out, killed.

# log_184_2021-7-23-16-11-24_adc_report_0.csv              log_187_2021-7-23-16-24-58_adc_report_0.csv
# log_184_2021-7-23-16-11-24_sensor_accel_0.csv            log_187_2021-7-23-16-24-58_sensor_accel_0.csv
# log_184_2021-7-23-16-11-24_sensor_accel_1.csv            log_187_2021-7-23-16-24-58_sensor_accel_1.csv
# log_184_2021-7-23-16-11-24_sensor_gps_0.csv              log_187_2021-7-23-16-24-58_sensor_gps_0.csv
# log_184_2021-7-23-16-11-24_vehicle_gps_position_0.csv    log_187_2021-7-23-16-24-58_vehicle_gps_position_0.csv
# log_184_2021-7-23-16-11-24_vehicle_local_position_0.csv  log_187_2021-7-23-16-24-58_vehicle_local_position_0.csv

crashfile_1_adc = pd.read_csv("~/Documents/data/vendredi_auto/log_182_2021-7-23-16-02-04_adc_report_0.csv")


crashfile_1_gps = pd.read_csv("~/Documents/data/vendredi_auto/log_182_2021-7-23-16-02-04_vehicle_local_position_0.csv")
crashfile_2_gps = pd.read_csv("~/Documents/data/vendredi_auto/log_183_2021-7-23-16-06-18_vehicle_local_position_0.csv")
crashfile_3_gps = pd.read_csv("~/Documents/data/vendredi_auto/log_184_2021-7-23-16-11-24_vehicle_local_position_0.csv")
crashfile_4_gps = pd.read_csv("~/Documents/data/vendredi_auto/log_185_2021-7-23-16-13-28_vehicle_local_position_0.csv")
crashfile_5_gps = pd.read_csv("~/Documents/data/vendredi_auto/log_186_2021-7-23-16-14-40_vehicle_local_position_0.csv")
crashfile_6_gps = pd.read_csv("~/Documents/data/vendredi_auto/log_187_2021-7-23-16-24-58_vehicle_local_position_0.csv")

crashfile_1_acc_0 = pd.read_csv("~/Documents/data/vendredi_auto/log_182_2021-7-23-16-02-04_sensor_accel_0.csv")
crashfile_2_acc_0 = pd.read_csv("~/Documents/data/vendredi_auto/log_183_2021-7-23-16-06-18_sensor_accel_0.csv")
crashfile_3_acc_0 = pd.read_csv("~/Documents/data/vendredi_auto/log_184_2021-7-23-16-11-24_sensor_accel_0.csv")
crashfile_4_acc_0 = pd.read_csv("~/Documents/data/vendredi_auto/log_185_2021-7-23-16-13-28_sensor_accel_0.csv")
crashfile_5_acc_0 = pd.read_csv("~/Documents/data/vendredi_auto/log_186_2021-7-23-16-14-40_sensor_accel_0.csv")
crashfile_6_acc_0 = pd.read_csv("~/Documents/data/vendredi_auto/log_187_2021-7-23-16-24-58_sensor_accel_0.csv")

crashfile_1_acc_1 = pd.read_csv("~/Documents/data/vendredi_auto/log_182_2021-7-23-16-02-04_sensor_accel_1.csv")
crashfile_2_acc_1 = pd.read_csv("~/Documents/data/vendredi_auto/log_183_2021-7-23-16-06-18_sensor_accel_1.csv")
crashfile_3_acc_1 = pd.read_csv("~/Documents/data/vendredi_auto/log_184_2021-7-23-16-11-24_sensor_accel_1.csv")
crashfile_4_acc_1 = pd.read_csv("~/Documents/data/vendredi_auto/log_185_2021-7-23-16-13-28_sensor_accel_1.csv")
crashfile_5_acc_1 = pd.read_csv("~/Documents/data/vendredi_auto/log_186_2021-7-23-16-14-40_sensor_accel_1.csv")
crashfile_6_acc_1 = pd.read_csv("~/Documents/data/vendredi_auto/log_187_2021-7-23-16-24-58_sensor_accel_1.csv")

#SELECT DATA
# FIMI FLIGHT.
# log_adc = clearing03_log_adc
# log_gps = clearing03_log_gps
# log_acc = clearing03_log_acc01 + clearing03_log_acc02

# PIXHAWK FLIGHT.
log_adc = crashfile_1_adc
print('LEN OF ADC IS:', len(log_adc))
log_gps = crashfile_1_gps
print('LEN OF GPS IS:', len(log_gps))
# frames = [crashfile_1_acc_0,crashfile_1_acc_1]
# log_acc = pd.concat(frames)

log_acc_2 = crashfile_2_acc_0 + crashfile_2_acc_1
log_acc_3 = crashfile_3_acc_0 + crashfile_3_acc_1
log_acc_4 = crashfile_4_acc_0 + crashfile_4_acc_1
log_acc_5 = crashfile_5_acc_0 + crashfile_5_acc_1
log_acc_6 = crashfile_6_acc_0 + crashfile_6_acc_1


log_acc = pd.concat([crashfile_6_acc_0, crashfile_6_acc_1])
print('LEN OF ACC IS:', len(log_acc))

log_adc2 = fita2blen(log_adc['raw_data[4]'], len(log_gps['x']))
print('LEN OF ADC2 IS:', len(log_adc2))
log_acc2 = fita2blen(log_acc['x'], len(log_gps['x']))
print('LEN OF ACC2 IS:', len(log_acc2))
##################################### DATA TO BE PREPROCESSED NOW ##################################3
# TIME
#label xaxis as (UTC(12-37-18) + timestamp// 10**9)
#then convert old timestamps to add to new dataframe.
import datetime
dt = datetime.datetime(2021, 6, 25, 14, 51, 38)
start_timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
print("START_TIME=", start_timestamp)
local_time_timestamps = []
for timestamp in log_acc['timestamp']:
    local_time_timestamps.append(((timestamp+start_timestamp-2*3600*10**6)//(10**3)))
print(local_time_timestamps[0])
#initialise, callback will change this.
time_axis=local_time_timestamps[0::10]


import math
abs_acc = []
#Get absolute value of acceleration
for i in range(len(log_acc['timestamp'])):
    x = (log_acc['x'][i])
    y = (log_acc['y'][i])
    z = (log_acc['z'][i])
    abs = math.sqrt(x**2 + y**2 + z**2)
    # if i<len(log_adc['timestamp']):
    #     if log_acc['timestamp'][i] == log_adc['timestamp'][i]:
    #         print('keep this')
    abs_acc.append(abs)


    
print("LENGTHS:", len(abs_acc)/len(log_gps['x'])) #2.85...
import numpy as np
new_acc=abs_acc[::2]
new_acc = np.array(new_acc)
new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 8))
new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 5))
#new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 405))
#new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 6))
#new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 4))

#1
#new_acc = new_acc[:-41+4-44:]

#6
new_acc = new_acc[::]

# TIME 30760 
# ACC 30682 
# GPS.x 30718 
# GPS.y 30718 
# ADC 30760

new_adc = log_adc['raw_data[4]'][:-42+4:]
#new_time = log_adc['timestamp'][:-42:]
new_time = local_time_timestamps[:-42+4-88317-44:]
new_alt = []

print("LENGTHS:", "\nTIME", len(new_time), 
                    "\nACC", len(new_acc), "\nGPS.x", len(log_gps['x']), 
                    "\nGPS.y",len(log_gps['y']), "\nADC", len(new_adc))
# TIME 30718 
# ACC 30718 
# GPS.x 30718 
# GPS.y 30718 
# ADC 30718
# for entry in log_gps['z']:
#     new_alt.append(-1* entry)
# beefup = 2 # add a value 
# for acc in abs_acc:
#     if abs_acc.index(acc)%beefup == 0:
#         addOne = (abs_acc[abs_acc.index(acc)-1]+abs_acc[abs_acc.index(acc)-1])/2
#         abs_acc.append(addOne)
#         print(len(abs_acc))


# vehicle_local_position.msg
# # Position in local NED frame
# float32 x				# North position in NED earth-fixed frame, (metres)
# float32 y				# East position in NED earth-fixed frame, (metres)
# float32 z				# Down position (negative altitude) in NED earth-fixed frame, (metres)
# from https://github.com/PX4/PX4-Autopilot/blob/master/msg/vehicle_local_position.msg

df_square = pd.DataFrame({'timestamp':new_time, 
                        'absolute_accel': new_acc,
                            'adc_report': new_adc,
                            'gps_lat': log_gps['x'],
                            'gps_lon': log_gps['y'],
                            'altitude': -log_gps['z'],
                            })

#FIRST VALUE IS:
print("x:", df_square['gps_lon'][10],
        "y:", df_square['gps_lat'][10],
            "z:", df_square['altitude'][10])


# INITIALIZE: empty SCATTERPLOT trace
scat = go.Figure()
scat.update_layout(
    title="Lighting measurements over time",
    title_x=0.2,
    xaxis_title="Time (100 messages per second)",
    yaxis_title="ADC values",
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="#000000"
    )
)

# Add range slider
scat.update_layout(
    xaxis=dict(
        rangeslider_thickness = 0.1,
        rangeslider=dict(
            visible=True,

            range=[time_axis[1], time_axis[50]]
        ),
        type="date"
    )
)
# Set custom x-axis labels
scat.update_xaxes(
    type = 'date'
)
# Prefix y-axis tick labels with dollar sign
scat.update_yaxes(ticksuffix="m")
scat.add_trace(go.Scatter(x=time_axis, y=log_adc['raw_data[4]'],
                    mode='lines+markers',
                    name='channel4'))

#adc_report                        0    2  101  1   96 #101Hz
#vehicle_local_position            0   15  100  1  168 #100Hz
#sensor_accel                      1    4  800  8   48 #800Hz
#100Hz = 0.01s/message ==> timestamps go from ... to ... .


scat2 = px.scatter_3d(df_square, x='gps_lat', y='gps_lon', z='altitude', color='adc_report', 
                    title="Lighting levels on full path",
                    color_continuous_scale=px.colors.sequential.Rainbow[::],
                    )

scat2.update_xaxes(title_text="Latitude", title_font=dict(
        family="Courier New, monospace",
        size=10,
        color="#000000"))
scat2.update_yaxes(title_text="Longitude", title_font=dict(
        family="Courier New, monospace",
        size=10,
        color="#000000"))

scat2.update_traces(marker=dict(size=1),
                  selector=dict(mode='markers'))


app.layout = html.Div([

    html.Div(className='row', children = [

        html.Div(dcc.Graph(
            id='life-exp-vs-gdp',
            figure=scat2
        ), className='six columns'),

        html.Div( html.Iframe(
            src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
                style={"height": "450px", "width": "80%"}),
        className='six columns'),
    ]),

    html.Div(className='row', children = [
        html.H5('Path Section', className='two columns'),
        html.Div(dcc.RangeSlider(
            id='my-range-slider',
            min=0,
            max=20,
            step=0.5,
            value=[5, 15]
        ), className='ten columns'),
    ]),

    html.Div(className='row', children = [

        html.Div([

            html.H5('Equipment', style={"margin-bottom": "10px"}),
            html.Div( html.Iframe(
                src="https://drive.google.com/file/d/1g7t1ncppoytzptNjC7p4kFX5PXZblhkB/preview",
                    style={"height": "150px", "width": "80%"})),
            html.Div(dcc.Dropdown(
                id = 'pages-dropdown',
                options=[
                    {'label': 'FIMI_XSE', 'value': 'FIMIXSE_CAMERA'},
                    {'label': 'FIMI_XSE+PIXHAWK', 'value': 'FIMIXSE+PIXHAWK'},
                    {'label': 'PIXHAWK', 'value': 'PIXHAWK'},
                ],
                value='FIMIXSE+PIXHAWK'
            )),
            #html.H5('Sensor Data\n \n \n \nEquipment', style={"margin-bottom": "100px"}),
            html.H5('Sensors', style={"margin-top": "20px", "margin-bottom": "10px"}),
            dcc.RadioItems(
                id='sensor',
                options=[
                    {'label': 'Accelerometer', 'value': 'Accelerometer'},
                    {'label': 'Lightsensor', 'value': 'Lightsensor '},
                    {'label': 'DistanceSensor', 'value': 'DistanceSensor'},
                    {'label': 'Timescale', 'value': 'Timescale'}
                ],
                value='Lightsensor'
            ), 
        ], className='two columns'), 

        html.Div(dcc.Graph(
            id='number2',
            figure=scat
        ), className='ten columns'),
    ]),
    html.H5('Frequency Reduction For Data Collection'),
    dcc.Slider(
        id='my-slider',
        min=1,
        max=100,
        step=1,
        value=10,
    ),
])

from PIL import Image


## NEARLY DONE. returns array, needs to be the correct one+method to attach to graph.
@app.callback(
    dash.dependencies.Output('life-exp-vs-gdp', 'figure'),
    dash.dependencies.Output('number2', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')],
    [dash.dependencies.Input('sensor', 'value')])
def update_figure(trim_step, sensor):
    print("chosen sensor:", sensor)
    print("Cut down by", trim_step)
    time_axis = local_time_timestamps[::trim_step]
    if sensor == "Lightsensor":
        sensor_data = log_adc['raw_data[4]'][::trim_step]
        #sensor_data = log_adc_parking['raw_data[4]'][::trim_step] #Test from Garage
        sensor_colour = df_square['adc_report']
    if sensor == "Accelerometer":
        print('sup')
        sensor_data = abs_acc[::trim_step]
        sensor_colour = df_square['absolute_accel']
    if sensor == "Timescale":
        sensor_data = df_square['gps_lon']
        sensor_colour = df_square['timestamp']

    scat.data = []
    scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=sensor_data,
                        mode='lines+markers',
                        name='trim_step:%d'% trim_step)
     )


    scat2 = px.scatter_3d(df_square, x='gps_lat', y='gps_lon', z='altitude', color= sensor_colour,
                        title=str(sensor_colour), ###FIX TITLE
                        color_continuous_scale=px.colors.sequential.Rainbow[::],
                        hover_data=["gps_lat", "timestamp"]
                        )

    scat2.update_xaxes(title_text="Longitude", title_font=dict(
        family="Courier New, monospace",
        size=10,
        color="#000000"))
    scat2.update_yaxes(title_text="Latitude", title_font=dict(
            family="Courier New, monospace",
            size=10,
            color="#000000"))

    scat2.update_traces(marker=dict(size=1),
                    selector=dict(mode='markers'))

    value = 13000
    print(value, "x:", df_square['gps_lon'][value],
            "y:", df_square['gps_lat'][value],
                "z:", df_square['altitude'][value])


    # Add range slider
    scat.update_layout(
        xaxis=dict(
            type="date",
            #rangeslider_range = [time_axis[1], time_axis[50]],
            rangeslider_thickness = 0.07,
            rangeslider=dict(
                visible=True,
                #autorange=False,
                #fixedrange= False,
                range=[time_axis[1], time_axis[50]]
            ),

    ))

    return scat2, scat

if __name__ == '__main__':
    app.run_server(debug=True)


### VALUES IN PARKING LOT (NO GPS)
# log_69_2021-6-25-12-41-44_adc_report_0.csv    log_69_2021-6-25-12-41-44.ulg
# log_69_2021-6-25-12-41-44_sensor_accel_0.csv  log_69_2021-6-25-12-41-44_vehicle_gps_position_0.csv
# log_69_2021-6-25-12-41-44_sensor_accel_1.csv  log_69_2021-6-25-12-41-44_vehicle_local_position_0.csv
# log_69_2021-6-25-12-41-44_sensor_gps_0.csv
#log_adc_parking = pd.read_csv("~/Documents/data/square_parking/log_69_2021-6-25-12-41-44_adc_report_0.csv")

### VALUES IN FOREST CLEARING (WITH GPS)
# ~/Documents/data/ciel_nuageux/
# log_76_2021-6-25-14-51-38_adc_report_0.csv              log_77_2021-6-25-15-00-26.ulg
# log_76_2021-6-25-14-51-38_sensor_accel_0.csv            log_77_2021-6-25-15-00-26_vehicle_gps_position_0.csv
# log_76_2021-6-25-14-51-38_sensor_accel_1.csv            log_77_2021-6-25-15-00-26_vehicle_local_position_0.csv
# log_76_2021-6-25-14-51-38_sensor_gps_0.csv              log_78_2021-6-25-15-23-54_adc_report_0.csv
# log_76_2021-6-25-14-51-38.ulg                           log_78_2021-6-25-15-23-54_sensor_accel_0.csv
# log_76_2021-6-25-14-51-38_vehicle_gps_position_0.csv    log_78_2021-6-25-15-23-54_sensor_accel_1.csv
# log_76_2021-6-25-14-51-38_vehicle_local_position_0.csv  log_78_2021-6-25-15-23-54_sensor_gps_0.csv
# log_77_2021-6-25-15-00-26_adc_report_0.csv              log_78_2021-6-25-15-23-54.ulg
# log_77_2021-6-25-15-00-26_sensor_accel_0.csv            log_78_2021-6-25-15-23-54_vehicle_gps_position_0.csv
# log_77_2021-6-25-15-00-26_sensor_accel_1.csv            log_78_2021-6-25-15-23-54_vehicle_local_position_0.csv
# log_77_2021-6-25-15-00-26_sensor_gps_0.csv