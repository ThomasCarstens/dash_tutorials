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

#### VALUES OUTDOORS (WITH GPS)
log_adc = pd.read_csv("~//Documents/data/droneData_alliantech/square_alliantech/log_8_2021-6-18-12-37-18_adc_report_0.csv")
log_gps =pd.read_csv("~//Documents/data/droneData_alliantech/square_alliantech/log_8_2021-6-18-12-37-18_vehicle_local_position_0.csv")
log_acc = pd.read_csv("~//Documents/data/droneData_alliantech/square_alliantech/log_8_2021-6-18-12-37-18_sensor_accel_0.csv")

print(list(log_acc))
print(list(log_acc))
print(list(log_acc))

#label xaxis as (UTC(12-37-18) + timestamp// 10**9)
#then convert old timestamps to add to new dataframe.
local_time_timestamps = []
for timestamp in log_adc['timestamp']:
    local_time_timestamps.append(((timestamp+1624019838000000-2*3600*10**6)//(10**3)))
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
new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 405))
#new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 6))
#new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 4))
new_acc = new_acc[:-1:]
print("LENGTHS:", len(new_acc), len(log_gps['x']), len(log_gps['y']),len(log_adc['raw_data[4]']))

new_adc = log_adc['raw_data[4]'][:-45:]
# beefup = 2 # add a value 
# for acc in abs_acc:
#     if abs_acc.index(acc)%beefup == 0:
#         addOne = (abs_acc[abs_acc.index(acc)-1]+abs_acc[abs_acc.index(acc)-1])/2
#         abs_acc.append(addOne)
#         print(len(abs_acc))






df_square = pd.DataFrame({'absolute_accel': new_acc,
                            'adc_report': new_adc,
                            'gps_lat': log_gps['x'],
                            'gps_lon': log_gps['y'],
                            'altitude': log_gps['z'],
                            })
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
            {'label': 'DistanceSensor', 'value': 'DistanceSensor'}
        ],
        value='Lightsensor'
    ), 
    html.Div(dcc.Graph(
        id='number2',
        figure=scat
    )),
])

## NEARLY DONE. returns array, needs to be the correct one+method to attach to graph.
@app.callback(
    dash.dependencies.Output('life-exp-vs-gdp', 'figure'),
    dash.dependencies.Output('number2', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')],
    [dash.dependencies.Input('sensor', 'value')])
def update_figure(trim_step, sensor):
    print("hello")
    print(trim_step)
    time_axis = local_time_timestamps[::trim_step]
    if sensor == "Lightsensor":
        sensor_data = log_adc['raw_data[4]'][::trim_step]
        sensor_colour = df_square['adc_report']
    if sensor == "Accelerometer":
        sensor_data = abs_acc[::trim_step]
        sensor_colour = df_square['absolute_accel']
    else:
        sensor_data = log_adc['raw_data[4]'][::trim_step]
        print("NO DATA FOR OPTION")
        #return scat
    scat.data = []
    scat.add_trace(go.Scatter(x=time_axis, y=sensor_data,
                        mode='lines+markers',
                        name='trim_step:%d'% trim_step)
    )
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

    # Create figure
    scat2 = go.Figure()

    # # Add trace
    # scat2.add_trace(
    #     go.Scatter(x=[0, 0.5, 1, 2, 2.2], y=[1.23, 2.5, 0.42, 3, 1])
    # )

    # Add images
    scat2.add_layout_image(
            dict(
                source="https://images.plot.ly/language-icons/api-home/python-logo.png",
                xref="x",
                yref="y",
                x=0,
                y=3,
                sizex=2,
                sizey=2,
                sizing="stretch",
                opacity=0.5,
                layer="below")
    )

    scat.add_trace(go.Scatter(x=time_axis, y=sensor_data,
                        mode='lines+markers',
                        name='trim_step:%d'% trim_step)
    )
        # Add range slider

    # Set templates
    scat2.update_layout(template="plotly_dark")
    # scat2 = px.scatter_3d(df_square, x='gps_lat', y='gps_lon', z='altitude', color= sensor_colour, template="plotly_dark", 
    #                     title=str(sensor_colour), ###FIX TITLE
    #                     color_continuous_scale=px.colors.sequential.Inferno[::-1],

    #                     )
    # scat2.update_xaxes(title_text="Latitude", title_font=dict(
    #     family="Courier New, monospace",
    #     size=10,
    #     color="#000000"))
    # scat2.update_yaxes(title_text="Longitude", title_font=dict(
    #         family="Courier New, monospace",
    #         size=10,
    #         color="#000000"))

    # scat2.update_traces(marker=dict(size=1),
    #                 selector=dict(mode='markers'))


    # ))

    return scat2, scat

if __name__ == '__main__':
    app.run_server(debug=True)