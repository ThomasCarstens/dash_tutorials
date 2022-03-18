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


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#### VALUES OUTSIDE ALLIANTECH (WITH GPS)
log_adc = pd.read_csv("~//Documents/data/droneData_alliantech/square_alliantech/log_8_2021-6-18-12-37-18_adc_report_0.csv")
log_gps = pd.read_csv("~//Documents/data/droneData_alliantech/square_alliantech/log_8_2021-6-18-12-37-18_vehicle_local_position_0.csv")
log_acc = pd.read_csv("~//Documents/data/droneData_alliantech/square_alliantech/log_8_2021-6-18-12-37-18_sensor_accel_0.csv")

### VALUES IN PARKING LOT (NO GPS)
# log_69_2021-6-25-12-41-44_adc_report_0.csv    log_69_2021-6-25-12-41-44.ulg
# log_69_2021-6-25-12-41-44_sensor_accel_0.csv  log_69_2021-6-25-12-41-44_vehicle_gps_position_0.csv
# log_69_2021-6-25-12-41-44_sensor_accel_1.csv  log_69_2021-6-25-12-41-44_vehicle_local_position_0.csv
# log_69_2021-6-25-12-41-44_sensor_gps_0.csv
#log_adc_parking = pd.read_csv("~/Documents/data/square_parking/log_69_2021-6-25-12-41-44_adc_report_0.csv")

### VALUES IN FOREST CLEARING (WITH GPS)
# ~/Documents/data/ciel_nuagueux/
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
clearing01_log_adc = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_76_2021-6-25-14-51-38_adc_report_0.csv")
clearing02_log_adc = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_77_2021-6-25-15-00-26_adc_report_0.csv")
clearing03_log_adc = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_78_2021-6-25-15-23-54_adc_report_0.csv")

clearing01_log_gps = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_76_2021-6-25-14-51-38_vehicle_local_position_0.csv")
clearing02_log_gps = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_77_2021-6-25-15-00-26_vehicle_local_position_0.csv")
clearing03_log_gps = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_78_2021-6-25-15-23-54_vehicle_local_position_0.csv")

clearing01_log_acc01 = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_76_2021-6-25-14-51-38_sensor_accel_0.csv")
clearing01_log_acc02 = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_76_2021-6-25-14-51-38_sensor_accel_1.csv")
clearing02_log_acc01 = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_77_2021-6-25-15-00-26_sensor_accel_0.csv")
clearing02_log_acc02 = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_77_2021-6-25-15-00-26_sensor_accel_1.csv")
clearing03_log_acc01 = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_78_2021-6-25-15-23-54_sensor_accel_0.csv")
clearing03_log_acc02 = pd.read_csv("~/Documents/data/droneData_alliantech/ciel_nuageux/log_78_2021-6-25-15-23-54_sensor_accel_1.csv")

#label xaxis as (UTC(12-37-18) + timestamp// 10**9)
#then convert old timestamps to add to new dataframe.
local_time_timestamps = []
for timestamp in log_adc['timestamp']:
    local_time_timestamps.append(((timestamp+1624019838000000-2*3600*10**6)//(10**3)))
print(local_time_timestamps[0])
#initialise, callback will change this.
time_axis=local_time_timestamps[0::10]

#label xaxis as (UTC(12-37-18) + timestamp// 10**9)
#then convert old timestamps to add to new dataframe.
import datetime
dt = datetime.datetime(2021, 6, 25, 14, 51, 38)
print (dt)
start_timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
print(start_timestamp)

local_time_timestamps = []
for timestamp in clearing01_log_adc['timestamp']:
    local_time_timestamps.append(((timestamp+start_timestamp-2*3600*10**6)//(10**3)))
print(local_time_timestamps[0])
#initialise, callback will change this.
#time_axis=local_time_timestamps[0::10]


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
new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 405))
#new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 6))
#new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 4))
new_acc = new_acc[:-1:]
print("LENGTHS:", len(local_time_timestamps), len(new_acc), len(log_gps['x']), len(log_gps['y']),len(log_adc['raw_data[4]']))

new_adc = log_adc['raw_data[4]'][:-45:]
new_time = log_adc['timestamp'][:-45:]
new_alt = []
# for entry in log_gps['z']:
#     new_alt.append(-1* entry)
# beefup = 2 # add a value 
# for acc in abs_acc:
#     if abs_acc.index(acc)%beefup == 0:
#         addOne = (abs_acc[abs_acc.index(acc)-1]+abs_acc[abs_acc.index(acc)-1])/2
#         abs_acc.append(addOne)
#         print(len(abs_acc))

print("NEG:", -log_gps['z'])
print("POS:", log_gps['z'])
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

#SAVE FINAL DATABASE
#df_init.to_csv('~/Documents/DashBeginnerTutorials/df_init.csv', index=False)

# print (df_square)
# print(log_adc)

# print(list(log_adc))
# print(list(log_gps))

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
        #rangeslider_range = [time_axis[1], time_axis[50]],
        rangeslider_thickness = 0.1,
        rangeslider=dict(
            visible=True,
            #autorange=False,
            #fixedrange= False,
            range=[time_axis[1], time_axis[50]]
        ),
        type="date"
    )
)
# Set custom x-axis labels
scat.update_xaxes(
    #ticktext=["End of Q1", "End of Q2", "End of Q3", "End of Q4"],
    #tickvals=["2016-04-01", "2016-07-01", "2016-10-01", "me"],
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
                    color_continuous_scale=px.colors.sequential.Inferno[::-1],
                    )
#for Surface plots -- later.
# scat2.update_traces(contours_z=dict(show=True, usecolormap=True,
#                                   highlightcolor="limegreen", project_z=True))

#light_yellow = [[0, '#FFDB58'], [1, '#FFDB58']]
#scat2.add_trace(go.Surface(z=z.apply(lambda z: 0), colorscale=light_yellow,  showscale=False))

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
    html.Div(dcc.Graph(
        id='life-exp-vs-gdp',
        figure=scat2
    )),

    dcc.Slider(
        id='my-slider',
        min=1,
        max=100,
        step=1,
        value=10,
    ),
    dcc.RadioItems(
        id='sensor',
        options=[
            {'label': 'Accelerometer', 'value': 'Accelerometer'},
            {'label': 'Lightsensor', 'value': 'Lightsensor'},
            {'label': 'DistanceSensor', 'value': 'DistanceSensor'},
            {'label': 'Timescale', 'value': 'Timescale'}
        ],
        value='Lightsensor'
    ), 
    html.Div(dcc.Graph(
        id='number2',
        figure=scat
    )),
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
        sensor_data = abs_acc[::trim_step]
        sensor_colour = df_square['absolute_accel']
    if sensor == "Timescale":
        sensor_data = df_square['gps_lon']
        sensor_colour = df_square['timestamp']
    else:
        sensor_data = log_adc['raw_data[4]'][::trim_step]
        #sensor_data = log_adc_parking['raw_data[4]'][::trim_step]
        print("NO DATA FOR OPTION")
        #return scat
    scat.data = []
    scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=sensor_data,
                        mode='lines+markers',
                        name='trim_step:%d'% trim_step)
     )
    #log_adc = log_adc_parking

    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[0]'],
    #                     mode='lines+markers',
    #                     name='channel0'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[1]'],
    #                     mode='lines+markers',
    #                     name='channel1'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[2]'],
    #                     mode='lines+markers',
    #                     name='channel2'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[3]'],
    #                     mode='lines+markers',
    #                     name='channel3'))
    # scat.add_trace(go.Scatter(x=time_axis, y=log_adc['raw_data[4]'],
    #                     mode='lines+markers',
    #                     name='channel4'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[5]'],
    #                     mode='lines+markers',
    #                     name='channel5'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[6]'],
    #                     mode='lines+markers',
    #                     name='channel6'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[7]'],
    #                     mode='lines+markers',
    #                     name='channel7'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[8]'],
    #                     mode='lines+markers',
    #                     name='channel8'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[9]'],
    #                     mode='lines+markers', 
    #                     name='channel9'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[10]'],
    #                     mode='lines+markers',
    #                     name='channel10'))
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[11]'],
    #                     mode='lines+markers',
    #                     name='channel11'))


    # scat2 = px.scatter_3d(df_square, x='gps_lat', y='gps_lon', z='altitude', color= sensor_colour, template="plotly_dark", 
    #                     title=str(sensor_colour), ###FIX TITLE
    #                     color_continuous_scale=px.colors.sequential.Inferno[::-1],
    #                     hover_data=["gps_lat", "timestamp"]
    #                     )
    #scat.update_layout(template="plotly_dark")
    scat2 = px.scatter(df_square, x='gps_lon', y='gps_lat', color= sensor_colour, 
                        title=str(sensor_colour), ###FIX TITLE
                        color_continuous_scale=px.colors.sequential.Inferno[::-1],

                        )

    # scat2.add_annotation(x=df_square['gps_lon'][0], y=df_square['gps_lat'][0],#z=df_square['altitude'][0],
    #         text="Starting point",
    #         showarrow=True,
    #         yshift=10)
    # print("x:", df_square['gps_lon'][10],
    #         "y:", df_square['gps_lat'][10],
    #             "z:", df_square['altitude'][10])
    scat2.update_xaxes(title_text="Longitude", title_font=dict(
        family="Courier New, monospace",
        size=10,
        color="#000000"))
    scat2.update_yaxes(title_text="Latitude", title_font=dict(
            family="Courier New, monospace",
            size=10,
            color="#000000"))
    scat2.add_layout_image(
            dict(
                source = Image.open('/home/txa//Documents/data/droneData_alliantech/square_alliantech/alliantech_top10.png'),
                #source="/home/txa//Documents/data/droneData_alliantech/square_alliantech/alliantech_top.png",
                xref="x",
                yref="y",
                x=-47,
                sizex=60,
                y=30,
                sizey=40,
                #RadialAxis (orientation = 90,),
                #orientation = 90,
                sizing="fill",
                opacity=1,
                layer="below")
    )
    scat2.update_traces(marker=dict(size=1),
                    selector=dict(mode='markers'))

    value = 13000
    print(value, "x:", df_square['gps_lon'][value],
            "y:", df_square['gps_lat'][value],
                "z:", df_square['altitude'][value])

    # scat2.update_layout(
    #     scene=dict(
    #         annotations=[
    #                 dict(
    #                     showarrow=True,
    #                     x=df_square['gps_lon'][0],
    #                     y=df_square['gps_lat'][0],
    #                     z=df_square['altitude'][0],
    #                     text="START",
    #                     #xanchor="left",
    #                     #xshift=0.1,
    #                     opacity=1),

    #                 dict(
    #                     showarrow=True,
    #                     x=df_square['gps_lon'][12000],
    #                     y=df_square['gps_lat'][12000],
    #                     z=df_square['altitude'][12000],
    #                     text=str(df_square['timestamp'][12000]),
    #                     #xanchor="left",
    #                     #xshift=0.1,
    #                     opacity=1),

    #                 dict(
    #                     showarrow=True,
    #                     x=df_square['gps_lon'][17434],
    #                     y=df_square['gps_lat'][17434],
    #                     z=df_square['altitude'][17434],
    #                     text="END",
    #                     #xanchor="left",
    #                     #xshift=0.0,
    #                     opacity=1),
    #                     ] 
    #                 ),
                    
    #             )
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