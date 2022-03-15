import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

#import dash_bootstrap_components as dbc #not working.

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                            suppress_callback_exceptions=True)
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# INITIALIZE: memory database
import numpy as np
import pandas as pd
from dynamic_controls import DYNAMIC_CONTROLS
from dash import callback_context
import datetime

# RETRIEVE
#Dedicated time https://drive.google.com/file/d/1xwuA-BSdjV0qM0Dv9P3mmf14OgaSeRhz/view?usp=sharing
                #https://drive.google.com/file/d/1xwuA-BSdjV0qM0Dv9P3mmf14OgaSeRhz/preview       
url_DT = 'https://drive.google.com/file/d/1Dig40yP0swJMsYWvtXOQFnwnayEi6Lvx/view?usp=sharing'
#Upcoming events
url_UE = 'https://drive.google.com/file/d/1fO0-X1ImngZVF1AoBCpFdHJdzsnutdmL/view?usp=sharing'
#Week advancement
url_WA = 'https://drive.google.com/file/d/12195l299XJRsRYCpZ1FS1wGZTngHNeBE/view?usp=sharing'

repo_path = "~/Documents/DashBeginnerTutorials/multitask_app"
data_path = "~/Documents/data"

def convert2df(url):
    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    df = pd.read_csv(path)
    if df.empty:
        print('empty')
    return df

def save2file():
    #SAVE ALL...
    #df_dedicatedTime.to_csv("file_path\data.csv")
    #df_weekAdvance.to_csv('~/Documents/DashBeginnerTutorials/db_Week_advancement.csv', index=False)
    df_dedicatedTime.to_csv(repo_path+'/db_Dedicated_time.csv', index=False)
    df_Upcoming_events.to_csv(repo_path+'/db_Upcoming_events.csv', index=False)

def read_file():
    #RETRIEVE ALL...
    df_weekAdvance = pd.DataFrame()
    #df_weekAdvance= pd.read_csv('~/Documents/DashBeginnerTutorials/db_Week_advancement.csv', index=False)
    df_dedicatedTime= pd.read_csv(repo_path+'/db_Dedicated_time.csv')
    df_Upcoming_events= pd.read_csv(repo_path+'/db_Upcoming_events.csv')
    return df_dedicatedTime, df_Upcoming_events

def getDriveFile():
    df_dedicatedTime = convert2df(url_DT)
    df_Upcoming_events = convert2df(url_UE)

def remove_entry(df, entry):
    bb = df.drop(entry, axis = 1)
    print(bb)
    #bb.to_csv('~/Documents/DashBeginnerTutorials/db_Dedicated_time.csv', index=False)
    return bb

    df_dedicatedTime, df_Upcoming_events = read_file()

df_dedicatedTime, df_Upcoming_events = read_file()
#TEMPORARY
df_weekAdvance = pd.DataFrame()#df_weekAdvance = convert2df(url_WA)


# INITIALIZE: layout_list entries for graphs
xy_layouts = [[0, 0.45], [0.55, 1]]
graph_layout_left = [[xy_layouts[0], xy_layouts[1]],
                        [xy_layouts[1], xy_layouts[1]],
                        [xy_layouts[1], xy_layouts[0]],
                        [xy_layouts[0], xy_layouts[0]]]
                        # Currently for CRITERIA
                        # [ 0   1 
                        #   3   2  ]
                        # [ 1   0 
                        #   3   2  ]
                        # [ 2   0 
                        #   (4)   1  ]
graph_layout_right = [[xy_layouts[0], xy_layouts[1]],
                        [xy_layouts[1], xy_layouts[1]],
                        [xy_layouts[0], xy_layouts[0]],
                        [xy_layouts[1], xy_layouts[0]]]
                        # Currently for DEADLINES
                        # [ 0   1 
                        #   2   3  ]

xy_layouts = [[0, 0.30], [0.35, 0.65], [0.70, 1]]
graph_layout_left = [[xy_layouts[2], xy_layouts[2]],
                        [xy_layouts[2], xy_layouts[1]],
                        [xy_layouts[1], xy_layouts[2]],

                    [xy_layouts[2], xy_layouts[0]],
                        [xy_layouts[1], xy_layouts[1]],
                        [xy_layouts[0], xy_layouts[2]],

                    [xy_layouts[1], xy_layouts[0]],
                        [xy_layouts[0], xy_layouts[1]],
                        [xy_layouts[2], xy_layouts[2]]]
                        # [ 5   2   0
                        #   7   4   1
                        # (10)   6   3 ]

                        # [ 2   .   .
                        #   1   .   .]
                        # [ 0   1   2

graph_layout_right = [[xy_layouts[0], xy_layouts[2]],
                        [xy_layouts[0], xy_layouts[1]],
                        [xy_layouts[1], xy_layouts[2]],

                    [xy_layouts[0], xy_layouts[0]],
                        [xy_layouts[1], xy_layouts[1]],
                        [xy_layouts[2], xy_layouts[2]],

                    [xy_layouts[1], xy_layouts[0]],
                        [xy_layouts[2], xy_layouts[1]],
                        [xy_layouts[0], xy_layouts[2]]]
                        # [ 0   2   5
                        #   1   4   7
                        #  3   6   (10)]

                        # [ 2   .   .
                        #   1   .   .]
                        # [ 0   1   2

pyramid_layouts = [[0, 1], [0, 0.5], [0, 0.25], [0, 0.125], [0, 0.0625]]
graph_layout_pyramid = [[pyramid_layouts[0], pyramid_layouts[0]],
                        [pyramid_layouts[0], pyramid_layouts[1]],
                        [pyramid_layouts[0], pyramid_layouts[2]],
                        [pyramid_layouts[0], pyramid_layouts[3]],
                        [pyramid_layouts[0], pyramid_layouts[4]]]                 
# INITIALIZE: empty GAUGE trace
fig = go.Figure()
fig.add_trace(go.Indicator(
    mode = "gauge+number+delta",
    value = 0,
    #customdata=[200],
    #delta = {'reference': 100},
    gauge = {
        'axis': {'visible': False},
        'bar' : {'color' : 'grey'}},
    title = {'text': "+"},
    domain = {'x': [0,1], 'y': [0,1]}
    ))

# Override go.Figure() margins.
tightfit = dict(l=20, r=20, t=20, b=0)
fig.update_layout(
    margin=tightfit,
    paper_bgcolor="LightSteelBlue",
)

###### App Layout (all pages) #####################################

app.layout = html.Div([

    # Dropdown triggers a change in the Page Layout
    html.Div(dcc.Dropdown(
        id = 'pages-dropdown',
        options=[
            {'label': 'Machine Learning', 'value': 'Machine Learning'},
            {'label': 'Time Dashboard', 'value': 'Time Dashboard'},
            {'label': 'Crypto+Budget', 'value': 'Crypto'},
            {'label': 'Drone Dev', 'value': 'Drone Dev'}, #Onboarding Sensors
        ],
        value='Time Dashboard'
    )),

    html.H3('Outcomes of Drone Dev'),

    # (dcc.Dropdown(
    #     id = 'drone-dev-dropdown',
    #     options=[
    #         {'label': '1 July: Drone Photogrammetry', 'value': 'Drone Photogrammetry'},
    #         {'label': '5 July: Onboarding Sensors', 'value': 'Onboarding Sensors'},
    #         {'label': '20 July: Drone Drop', 'value': 'Drone Drop'},
    #     ],
    #     placeholder="Choose Section",
    # )),
    # Update interval of 1s for Graph Rendering
    html.Div(dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
    )),

    # content will be rendered in this element
    html.Div(id='page-content'),
    html.Div(id='page-content-more'),

    # Session tokens? (UNFINISHED)
    dcc.Store(id='session-nav'),                      #Linked to l.248/l.425
    dcc.Store(id='intermediate-value'),                      #!!! add here
    dcc.Store(id='warning-trigger'),          #window-trigger for warnings
    
    ])
        

###### Page Layout CALLBACK ####################################################

@app.callback(dash.dependencies.Output('page-content', 'children'),
              dash.dependencies.Input('pages-dropdown', 'value'),
              #[dash.dependencies.State('drone-dev-dropdown', 'value')],
              #dash.dependencies.Input('button+', 'n_clicks')
              #prevent_initial_call=True
              )
def display_page(value):
    if value == "Time Dashboard" :
        return html.Div([
            DYNAMIC_CONTROLS['timer-graphs'],
            #DYNAMIC_CONTROLS['edit-timers'],
            #DYNAMIC_CONTROLS['see-database']
            DYNAMIC_CONTROLS['open1-window'],
            DYNAMIC_CONTROLS['open2-window'],
            DYNAMIC_CONTROLS['edit1-window'],
            DYNAMIC_CONTROLS['edit2-window'],
        ])
    if value == "Photogrammetry":
        return html.Div([
            DYNAMIC_CONTROLS['general-photogrammetry'],
            DYNAMIC_CONTROLS['2-photos'],
        ])
    if value == "Machine Learning" :
        return html.Div([
            DYNAMIC_CONTROLS['drone-graphs'],
            #DYNAMIC_CONTROLS['timer-graphs']
        ])
    if value == "Drone Dev" :
        return html.Div([
            DYNAMIC_CONTROLS['drone-graphs'],
            #DYNAMIC_CONTROLS['timer-graphs']
        ])

@app.callback(dash.dependencies.Output('page-content-more', 'children'),
                dash.dependencies.Output('session-nav', 'data'),
              dash.dependencies.Input('drone-dev-dropdown', 'value'),
              )
def display_page(value):

    # {'label': '5 June | UAV Photogrammetry', 'value': 'Drone Photogrammetry'},
    # {'label': '15 June | DAQ System Design', 'value': 'DAQ System'},
    # {'label': '5 July  | In-vivo Data Collection Flight', 'value': 'In-vivo Data Collection Flight'},
    # {'label': '20 July | UAV Carrier System Design', 'value': 'Carrier System Design'},
    # {'label': '30 July | Drone Drop', 'value': 'Drone Drop'},

    # STORE DATA HERE
    session_page = value
    print(session_page)
    page_layout = html.Div([
        #DYNAMIC_CONTROLS['drone-graphs'],
    ])
    if value == "Drone Photogrammetry" :
        page_layout = html.Div([
            DYNAMIC_CONTROLS['drone-graphs'],
            DYNAMIC_CONTROLS['general-photogrammetry'],
            DYNAMIC_CONTROLS['2-photos'],
        ])
    if value == "Carrier System Design" :
        page_layout = html.Div([
            DYNAMIC_CONTROLS['drone-graphs'],
            DYNAMIC_CONTROLS['general-photogrammetry'],
        ])
    if value == "Drone Drop" :
        page_layout = html.Div([
            DYNAMIC_CONTROLS['drone-graphs'],
            DYNAMIC_CONTROLS['in-vivo'],
        ])

    if value == "DAQ System" :
        page_layout = html.Div([
            DYNAMIC_CONTROLS['drone-graphs'],
            DYNAMIC_CONTROLS['2-photos'],
        ])

    if value == "In-vivo Data Collection Flight" :
        page_layout = html.Div([
            DYNAMIC_CONTROLS['drone-graphs'],
            DYNAMIC_CONTROLS['in-vivo'],
        ])      

    return page_layout, session_page

# ##### DRONE DATA: in-vivo Callback ############


# log_adc = convert2df(url)
# #### SEE LIST OF FILES AT END OF THIS FILE.


# log_adc = pd.read_csv(data_path+"/square_alliantech/log_8_2021-6-18-12-37-18_adc_report_0.csv")
# log_gps = pd.read_csv(data_path+"/square_alliantech/log_8_2021-6-18-12-37-18_vehicle_local_position_0.csv")
# log_acc = pd.read_csv(data_path+"/square_alliantech/log_8_2021-6-18-12-37-18_sensor_accel_0.csv")

# clearingdata = "https://drive.google.com/drive/folders/1zhIqEN6gt2KINvJkDnXFayjJvm2dn0IP?usp=sharing"
# # not going to work: we need individual paths.
# clearing01_log_adc = pd.read_csv(data_path+"/ciel_nuageux/log_76_2021-6-25-14-51-38_adc_report_0.csv")
# clearing02_log_adc = pd.read_csv(data_path+"/ciel_nuageux/log_77_2021-6-25-15-00-26_adc_report_0.csv")
# clearing03_log_adc = pd.read_csv(data_path+"/ciel_nuageux/log_78_2021-6-25-15-23-54_adc_report_0.csv")

# clearing01_log_gps = pd.read_csv(data_path+"/ciel_nuageux/log_76_2021-6-25-14-51-38_vehicle_local_position_0.csv")
# clearing02_log_gps = pd.read_csv(data_path+"/ciel_nuageux/log_77_2021-6-25-15-00-26_vehicle_local_position_0.csv")
# clearing03_log_gps = pd.read_csv(data_path+"/ciel_nuageux/log_78_2021-6-25-15-23-54_vehicle_local_position_0.csv")

# clearing01_log_acc01 = pd.read_csv(data_path+"/ciel_nuageux/log_76_2021-6-25-14-51-38_sensor_accel_0.csv")
# clearing01_log_acc02 = pd.read_csv(data_path+"/ciel_nuageux/log_76_2021-6-25-14-51-38_sensor_accel_1.csv")
# clearing02_log_acc01 = pd.read_csv(data_path+"/ciel_nuageux/log_77_2021-6-25-15-00-26_sensor_accel_0.csv")
# clearing02_log_acc02 = pd.read_csv(data_path+"/ciel_nuageux/log_77_2021-6-25-15-00-26_sensor_accel_1.csv")
# clearing03_log_acc01 = pd.read_csv(data_path+"/ciel_nuageux/log_78_2021-6-25-15-23-54_sensor_accel_0.csv")
# clearing03_log_acc02 = pd.read_csv(data_path+"/ciel_nuageux/log_78_2021-6-25-15-23-54_sensor_accel_1.csv")

# # FIMI FLIGHT.
# log_adc = clearing03_log_adc
# log_gps = clearing03_log_gps
# log_acc = clearing03_log_acc01 + clearing03_log_acc02

# import datetime
# dt = datetime.datetime(2021, 6, 25, 14, 51, 38)
# start_timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
# print("START_TIME=", start_timestamp)
# local_time_timestamps = []
# for timestamp in log_adc['timestamp']:
#     local_time_timestamps.append(((timestamp+start_timestamp-2*3600*10**6)//(10**3)))
# print(local_time_timestamps[0])
# #initialise, callback will change this.
# time_axis=local_time_timestamps[0::10]


# import math
# abs_acc = []
# #Get absolute value of acceleration
# for i in range(len(log_acc['timestamp'])):
#     x = (log_acc['x'][i])
#     y = (log_acc['y'][i])
#     z = (log_acc['z'][i])
#     abs = math.sqrt(x**2 + y**2 + z**2)
#     # if i<len(log_adc['timestamp']):
#     #     if log_acc['timestamp'][i] == log_adc['timestamp'][i]:
#     #         print('keep this')
#     abs_acc.append(abs)
# print("LENGTHS:", len(abs_acc)/len(log_gps['x'])) #2.85...
# import numpy as np
# new_acc=abs_acc[::2]
# new_acc = np.array(new_acc)
# new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 8))
# new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 5))
# #new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 405))
# #new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 6))
# #new_acc = np.delete(new_acc, np.arange(0, new_acc.size, 4))
# new_acc = new_acc[:-41+4:]

# # TIME 30760 
# # ACC 30682 
# # GPS.x 30718 
# # GPS.y 30718 
# # ADC 30760

# new_adc = log_adc['raw_data[4]'][:-42+4:]
# #new_time = log_adc['timestamp'][:-42:]
# new_time = local_time_timestamps[:-42+4:]
# new_alt = []

# print("LENGTHS:", "\nTIME", len(new_time), 
#                     "\nACC", len(new_acc), "\nGPS.x", len(log_gps['x']), 
#                     "\nGPS.y",len(log_gps['y']), "\nADC", len(new_adc))

# df_square = pd.DataFrame({'timestamp':new_time, 
#                         'absolute_accel': new_acc,
#                             'adc_report': new_adc,
#                             'gps_lat': log_gps['x'],
#                             'gps_lon': log_gps['y'],
#                             'altitude': -log_gps['z'],
#                             })

# # INITIALIZE: empty SCATTERPLOT trace
# scat = go.Figure()
# scat.update_layout(
#     title="Lighting measurements over time",
#     title_x=0.2,
#     xaxis_title="Time (100 messages per second)",
#     yaxis_title="ADC values",
#     font=dict(
#         family="Courier New, monospace",
#         size=10,
#         color="#000000"
#     )
# )

# # Add range slider
# scat.update_layout(
#     xaxis=dict(
#         #rangeslider_range = [time_axis[1], time_axis[50]],
#         rangeslider_thickness = 0.1,
#         rangeslider=dict(
#             visible=True,
#             #autorange=False,
#             #fixedrange= False,
#             range=[time_axis[1], time_axis[50]]
#         ),
#         type="date"
#     )
# )
# # Set custom x-axis labels
# scat.update_xaxes(
#     type = 'date'
# )
# # Prefix y-axis tick labels with dollar sign
# scat.update_yaxes(ticksuffix="m")
# scat.add_trace(go.Scatter(x=time_axis, y=log_adc['raw_data[4]'],
#                     mode='lines+markers',
#                     name='channel4'))

# #adc_report                        0    2  101  1   96 #101Hz
# #vehicle_local_position            0   15  100  1  168 #100Hz
# #sensor_accel                      1    4  800  8   48 #800Hz
# #100Hz = 0.01s/message ==> timestamps go from ... to ... .


# scat2 = px.scatter_3d(df_square, x='gps_lat', y='gps_lon', z='altitude', color='adc_report', 
#                     title="Lighting levels on full path",
#                     color_continuous_scale=px.colors.sequential.Rainbow[::],
#                     )

# scat2.update_xaxes(title_text="Latitude", title_font=dict(
#         family="Courier New, monospace",
#         size=10,
#         color="#000000"))
# scat2.update_yaxes(title_text="Longitude", title_font=dict(
#         family="Courier New, monospace",
#         size=10,
#         color="#000000"))

# scat2.update_traces(marker=dict(size=1),
#                   selector=dict(mode='markers'))

# @app.callback(

#     dash.dependencies.Output('life-exp-vs-gdp', 'figure'),
#     dash.dependencies.Output('number2', 'figure'),
#     dash.dependencies.Output('equipment-image', 'children'),
    
#     [dash.dependencies.Input('my-slider', 'value')],
#     [dash.dependencies.Input('sensor', 'value')],
#     dash.dependencies.State('session-nav', 'data')
#     )
# def update_figure(trim_step, sensor, session_page):
#     print("We are now at", session_page)
#     if session_page == "In-vivo Data Collection Flight":
#         print("chosen sensor:", sensor)
#         print("Cut down by", trim_step)
#         time_axis = local_time_timestamps[::trim_step]
#         if sensor == "Lightsensor":
#             sensor_data = log_adc['raw_data[4]'][::trim_step]
#             sensor_colour = df_square['adc_report']
#         if sensor == "Accelerometer":
#             print('sup')
#             sensor_data = abs_acc[::trim_step]
#             sensor_colour = df_square['absolute_accel']
#         if sensor == "Timescale":
#             sensor_data = df_square['gps_lon']
#             sensor_colour = df_square['timestamp']

#         scat.data = []
#         scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=sensor_data,
#                             mode='lines+markers',
#                             name='trim_step:%d'% trim_step)
#         )

#         scat2 = px.scatter_3d(df_square, x='gps_lat', y='gps_lon', z='altitude', color= sensor_colour,
#                             title=str(sensor_colour), ###FIX TITLE
#                             color_continuous_scale=px.colors.sequential.Rainbow[::],
#                             hover_data=["gps_lat", "timestamp"]
#                             )

#         scat2.update_xaxes(title_text="Longitude", title_font=dict(
#             family="Courier New, monospace",
#             size=10,
#             color="#000000"))
#         scat2.update_yaxes(title_text="Latitude", title_font=dict(
#                 family="Courier New, monospace",
#                 size=10,
#                 color="#000000"))

#         scat2.update_traces(marker=dict(size=1),
#                         selector=dict(mode='markers'))

#         value = 13000
#         print(value, "x:", df_square['gps_lon'][value],
#                 "y:", df_square['gps_lat'][value],
#                     "z:", df_square['altitude'][value])

#         scat.update_layout(
#             xaxis=dict(
#                 type="date",
#                 #rangeslider_range = [time_axis[1], time_axis[50]],
#                 rangeslider_thickness = 0.07,
#                 rangeslider=dict(
#                     visible=True,
#                     #autorange=False,
#                     #fixedrange= False,
#                     range=[time_axis[1], time_axis[50]]
#                 ),

#         ))

#     #return scat2, scat

#     if session_page == "Drone Drop":
#             print("chosen sensor:", sensor)
#             print("Cut down by", trim_step)
#             time_axis = local_time_timestamps[::trim_step]
#             if sensor == "Lightsensor":
#                 sensor_data = log_adc['raw_data[4]'][::trim_step]
#                 sensor_colour = df_square['adc_report']
#             if sensor == "Accelerometer":
#                 print('sup')
#                 sensor_data = abs_acc[::trim_step]
#                 sensor_colour = df_square['absolute_accel']
#             if sensor == "Timescale":
#                 sensor_data = df_square['gps_lon']
#                 sensor_colour = df_square['timestamp']

#             scat.data = []
#             scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=sensor_data,
#                                 mode='lines+markers',
#                                 name='trim_step:%d'% trim_step)
#             )

#             scat2 = px.scatter_3d(df_square, x='gps_lat', y='gps_lon', z='altitude', color= sensor_colour,
#                                 title=str(sensor_colour), ###FIX TITLE
#                                 color_continuous_scale=px.colors.sequential.Rainbow[::],
#                                 hover_data=["gps_lat", "timestamp"]
#                                 )

#             scat2.update_xaxes(title_text="Longitude", title_font=dict(
#                 family="Courier New, monospace",
#                 size=10,
#                 color="#000000"))
#             scat2.update_yaxes(title_text="Latitude", title_font=dict(
#                     family="Courier New, monospace",
#                     size=10,
#                     color="#000000"))

#             scat2.update_traces(marker=dict(size=1),
#                             selector=dict(mode='markers'))

#             value = 13000
#             print(value, "x:", df_square['gps_lon'][value],
#                     "y:", df_square['gps_lat'][value],
#                         "z:", df_square['altitude'][value])

#             scat.update_layout(
#                 xaxis=dict(
#                     type="date",
#                     #rangeslider_range = [time_axis[1], time_axis[50]],
#                     rangeslider_thickness = 0.07,
#                     rangeslider=dict(
#                         visible=True,
#                         #autorange=False,
#                         #fixedrange= False,
#                         range=[time_axis[1], time_axis[50]]
#                     ),

#             ))
#     equipment_pic = html.Iframe(
#             src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
#                 style={"height": "450px", "width": "80%"})
#     return scat2, scat, equipment_pic

###### The Rest of the CALLBACKS ####################################################

#FUNCTION: Turn a go.Figure() into white with optional Title/Message.
#USAGE: blankSpace(priority_fig, "Logs", "No logs found.")

def blankSpace(figure, my_title, my_text):
    figure.update_layout(plot_bgcolor='rgb(255,255,255)',
                                            title=dict(
                                                    text=my_title,
                                                    font_size=30,
                                                    font_color='black',
                                                    x = 0.5,
                                                    xanchor = 'center'
                                                ),)
    figure.update_xaxes(visible= False)
    figure.update_yaxes(visible= False)

    # INTRO
    figure.add_annotation(text=my_text,
                    xref="paper", yref="paper",
                    font=dict(
                        family="Courier New, monospace",
                        size=16,
                        color="#000000"
                        ),
                    x=0, y=0.9, showarrow=False)

###### Dashboard Rendering ###########################
########## INITIALIZE: empty GAUGE trace
    #fig = go.Figure()
empty_trace_right = go.Indicator(
    mode = "gauge+number+delta",
    value = 0,
    #customdata=[200],
    #delta = {'reference': 100},
    gauge = {
        'axis': {'visible': False},
        'bar' : {'color' : 'grey'}},
    title = {'text': "+"},
    domain = {'x': graph_layout_right[0][0], 'y': graph_layout_right[0][1]},
    )

awkward_trace_right = go.Indicator(
    mode = "gauge+number+delta",
    value = 0,
    #customdata=[200],
    #delta = {'reference': 100},
    gauge = {
        'axis': {'visible': False},
        'bar' : {'color' : 'grey'}},
    title = {'text': "+"},
    domain = {'x': graph_layout_right[3][0], 'y': graph_layout_right[3][1]},
    )

# INITIALIZE: empty_trace @ Position 1
empty_trace_left = go.Indicator(
    mode = "gauge+number+delta",
    value = 0,
    #customdata=[200],
    #delta = {'reference': 100},
    gauge = {
        'axis': {'visible': False},
        'bar' : {'color' : 'grey'}},
    title = {'text': "+"},
    domain = {'x': graph_layout_left[0][0], 'y': graph_layout_left[0][1]},
    )

# INITIALIZE: awkward_trace @ Position 3
awkward_trace_left = go.Indicator(
    mode = "gauge+number+delta",
    value = 0,
    #customdata=[200],
    #delta = {'reference': 100},
    gauge = {
        'axis': {'visible': False},
        'bar' : {'color' : 'grey'}},
    title = {'text': "+"},
    domain = {'x': graph_layout_left[3][0], 'y': graph_layout_left[3][1]},
    )    

@app.callback( #speed-indicatorgraph1
    dash.dependencies.Output('graph1', 'figure'), #deadline-fig2graph2
    dash.dependencies.Output('graph2', 'figure'), #deadline-fig2graph2
    dash.dependencies.Output('speed-indicator', 'figure'),
    dash.dependencies.Output('next-indicator', 'figure'),
    dash.dependencies.Output('deadline-fig2', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')],
    [dash.dependencies.State('open1-dropdown', 'value')], 
    [dash.dependencies.State('priorities-dropdown', 'value')]) #INTERVAL has 2 purposes: UPDATE TIME or UPDATE GRAPH EDITS.
def update_output(n_intervals, checkedgraph, what2graph):
    if n_intervals % 2:
        print("Updating. /")
    else: 
        print("Updating. \ ")

    df_dedicatedTime, df_Upcoming_events = read_file()



    #recursive_fig2.update_layout(domain = {'x': [0,1], 'y': [0,0.5]})

    #df_week = pd.read_csv("~/Documents/DashBeginnerTutorials/db_"+dropdown_value+".csv")
    #df_week = pd.read_csv('~/Documents/DashBeginnerTutorials/db_Week_advancement.csv')

    # MIGRATION
    # df_dedicatedTime = pd.read_csv('~/Documents/DashBeginnerTutorials/db_Dedicated_time.csv')
    # df_Followups= pd.read_csv( '~/Documents/DashBeginnerTutorials/db_Followups.csv')
    # df_Upcoming_events= pd.read_csv('~/Documents/DashBeginnerTutorials/db_Upcoming_events.csv')

    #opts = list(df_week)
    #options=[{'label':opt, 'value':opt} for opt in opts]  


    ####################################
    ### RIGHT-SIDE Graph Rendering
    # DEADLINE FIG: (RIGHT) DEADLINE SECTION   
    # ################3

    deadline_fig = go.Figure()
    deadline_fig.data = []
    deadline_fig2 = go.Figure()
    deadline_fig2.data = []

    deadline_fig.update_layout(
        margin=tightfit,
    )
    deadline_fig2.update_layout(
        margin=tightfit,
    )

    
    ## According to values in Database.
    db_selected = df_Upcoming_events
    nb_graphs = len(list(db_selected.keys()))

    if nb_graphs == 0:
        deadline_fig.add_trace(empty_trace_right)
        deadline_fig2.add_trace(empty_trace_right)

    if nb_graphs == 3:
        deadline_fig.add_trace(awkward_trace_right)

    if nb_graphs < 5:
        deadline_fig2.add_trace(empty_trace_right)
        deadline_fig.data = [] #remove if we are adding.

    if nb_graphs> 4:
        deadline_fig2.data = [] #remove if we are adding.
    #####################################

    count = 0
    deadline_list = []
    reordered_deadlines = []
    fixed_deadlines = []

    #LOOP CONTAINS DEADLINE CALCS FOLLOWED BY DEADLINE GRAPHS.
    for i in db_selected.keys():
        #print("Here", db_selected[i][1].split(',')) #LOL WRONG GRAPH...

        # ALL TIMER VALUES
        d=[int(x) for x in db_selected[i][1].split(',')]
        #print(d)
        deadline = datetime.datetime(year=d[0], month=d[1], day=d[2], hour=d[3], minute=d[4], second=d[5])
        time_left=(deadline - datetime.datetime.now())
        deadline_list.append(time_left)
        fixed_deadlines.append(time_left)



        hours_left = time_left.seconds//3600
        minutes_left = time_left.seconds//60 #hierarchy here.
        minutes_clock = time_left.seconds//60 - time_left.seconds//3600

        #Set a Logical Gauge Value. MINUTES else HOURS else DAYS.
        # if time_left.seconds//60 > 180: #too many minutes
        #     if time_left.seconds//3600 > 24: #too many hours
        #         timer_value = time_left.days
        #         value_units = 'days'
        #         value_range = [0,30]
        #     else: 
        #         timer_value = time_left.seconds//3600
        #         value_units = 'h'
        #         value_range = [0,24]
        # else: 
        #     timer_value = time_left.seconds//60
        #     value_units = 'min'
        #     value_range = [0,180]

        prefix_time= 'in '
        if time_left.days > 0 and time_left.days < 7: #too many days
            timer_value = time_left.days
            value_units = ' day' if timer_value == 1 else ' days'
            value_range = [0,30]
            color_or_grey = db_selected[i][6]
        else:
            if time_left.days == 0:
                color_or_grey = db_selected[i][6]

                if time_left.seconds//60 > 180: #too many hours
                    timer_value = time_left.seconds//3600
                    value_units = 'h'
                    value_range = [0,24]
                else:  #in minutes
                    timer_value = time_left.seconds//60
                    value_units = 'min'
                    value_range = [0,180]

            else:
                if time_left.days > 7 and time_left.days < 21:
                    color_or_grey = db_selected[i][6] #in weeks.
                    timer_value = time_left.days // 7
                    value_units = ' week' if timer_value == 1 else ' weeks'
                    value_range = [0,3]     #currently max deadline...
                else:    
                    if time_left.days > 21:
                        color_or_grey = db_selected[i][6] #in weeks.
                        timer_value = time_left.days
                        value_units = ' days'
                        value_range = [0,time_left.days + 5]     #range is dependent...
                    else:
                        color_or_grey = 'grey' #last option: negative days.
                        timer_value = -time_left.days
                        value_units = (' day' if time_left.days == -1 else ' days')+(' late')
                        value_range = [0,-time_left.days+1]
                        prefix_time = ''


        #limitations: NO LABEL + MIGHT TRANSFER TO MAIN.

        #remove past deadlines AND record them
        # if time_left.days < 0: #Negative is past.
        #     df_weekAdvance[i]= db_selected[i]
        #     continue

        #print(db_selected[i])
        #df_weekAdvance.to_csv('~/Documents/DashBeginnerTutorials/db_Week_advancement.csv', index=False)
        if db_selected[i][10] != 'unfinished':
            print(db_selected[i])
            df_weekAdvance[i]= db_selected[i]
            continue #both late and complete are removed here.

        count+=1
        graph_position = graph_layout_right [(count-1)%4]
        ### ADDED 

        if count < 8:
            renderedGraph = deadline_fig
            graph_position = graph_layout_right [(count-1)]
        if count == 10:
            renderedGraph = deadline_fig
            graph_position = graph_layout_right [8]
        if count == 8 or count == 9:
            renderedGraph = deadline_fig2
            graph_position = graph_layout_right [count - 8]
        if count > 10:
            renderedGraph = deadline_fig2
            graph_position = graph_layout_right [count - 9]

        renderedGraph.add_trace(go.Indicator(
        mode = db_selected[i][0],
        value = timer_value,
        number = {
            'suffix': value_units,
            'valueformat': 'help',
            'prefix': prefix_time
        },
        customdata= list(db_selected[i][2]),
        delta = {'reference': int(db_selected[i][3]),},
        gauge = {
            'axis': {'visible': False, 'range': value_range,}, #axis visible: bool(db_selected[i][4])
            'bar' : {'color' : color_or_grey,}},
        title = {'text': db_selected[i][7], 'font': {'size': 20}},
        domain = {'x': graph_position[0], 'y': graph_position[1]}
                )) 
        ####

        # if count < 5:
        #     deadline_fig.add_trace(go.Indicator(
        #     mode = db_selected[i][0],
        #     value = timer_value,
        #     number = {
        #         'suffix': value_units,
        #         'valueformat': 'help'
        #     },
        #     customdata= list(db_selected[i][2]),
        #     delta = {'reference': int(db_selected[i][3]),},
        #     gauge = {
        #         'axis': {'visible': bool(db_selected[i][4]), 'range': value_range,},
        #         'bar' : {'color' : color_or_grey,}},
        #     title = {'text': db_selected[i][7], 'font': {'size': 20}},
        #     domain = {'x': graph_position[0], 'y': graph_position[1]} #[int(x) for x in (df_week[i][5]).split(',')]
        #         ))
        # if count > 4 and count < 9:

        #     deadline_fig2.add_trace(go.Indicator(
        #     mode = db_selected[i][0],
        #     value = timer_value,
        #     number = {
        #         'suffix': value_units,
        #         'valueformat': 'help'
        #     },
        #     customdata= list(db_selected[i][2]),
        #     delta = {'reference': int(db_selected[i][3]),},
        #     gauge = {
        #         'axis': {'visible': bool(db_selected[i][4]), 'range': value_range ,},
        #         'bar' : {'color' : db_selected[i][6],}},
        #     title = {'text': db_selected[i][7], 'font': {'size': 20}},
        #     domain = {'x': graph_position[0], 'y': graph_position[1]} #[int(x) for x in (df_week[i][5]).split(',')]
        #         )) 
    print("count is now", count)
    #REMOVE UNUSED SPACES.
    if count < 5:
    # WHITE LAYOUT
        deadline_fig2.update_layout(plot_bgcolor='rgb(255,255,255)',
                                        )
        deadline_fig2.update_xaxes(visible= False)
        deadline_fig2.update_yaxes(visible= False)
        blankSpace(deadline_fig2, "", "")
    #REMOVE UNUSED SPACES.
    if count == 0:
    # WHITE LAYOUT
        deadline_fig.update_layout(plot_bgcolor='rgb(255,255,255)',
                                        )
        deadline_fig.update_xaxes(visible= False)
        deadline_fig.update_yaxes(visible= False)
        blankSpace(deadline_fig, "", "Add some graphs :)")

    ### LEFT-SIDE
    # RECURSIVE FIG RENDER
    # ################3
    #####################################
    # SUCCESSRATE GRAPHS
    #############################################################################
    recursive_fig = go.Figure()
    recursive_fig.data = []
    recursive_fig2 = go.Figure()
    recursive_fig2.data = []

    recursive_fig.update_layout(
        margin=tightfit,
    )
    recursive_fig2.update_layout(
        margin=tightfit,
    )
    # [ 5   2   0
    #   7   4   1
    # (10)   6   3 ]

    # [ 2   .   .
    #   1   .   .]
    # [ 0   1   2

    ## Dynamic plug in: @ Pos 1/3 when insufficient graphs.
    db_selected = df_dedicatedTime
    nb_recursiveFigs = len(list(db_selected.keys()))

    if nb_recursiveFigs == 0:
        recursive_fig.add_trace(empty_trace_left)

    if nb_recursiveFigs < 6:
        blankSpace(recursive_fig2, "", "")

    if nb_recursiveFigs > 5 and nb_recursiveFigs < 8:
        recursive_fig2.add_trace(empty_trace_left)
        #recursive_fig.data = [] #remove empty graph in Figure 1 if we are adding.

    # if nb_recursiveFigs == 3:
    #     recursive_fig.add_trace(awkward_trace_left)

    count=0


    for i in df_dedicatedTime:
        timer_value = float(df_dedicatedTime[i][1])*100

        count+=1 

        if count < 8:
            renderedGraph = recursive_fig
            graph_position = graph_layout_left [(count-1)]
        if count == 10:
            renderedGraph = recursive_fig
            graph_position = graph_layout_left [8]
        if count == 8 or count == 9:
            renderedGraph = recursive_fig2
            graph_position = graph_layout_left [count - 8]
        if count > 10:
            renderedGraph = recursive_fig2
            graph_position = graph_layout_left [count - 9]

        renderedGraph.add_trace(go.Indicator(
        mode = db_selected[i][0],
        number = {
            'suffix': '%',
        },
        value = timer_value,
        customdata= list(db_selected[i][2]),
        delta = {'reference': int(db_selected[i][3]),},
        gauge = {
            'axis': {'visible': False, 'range': [int(x) for x in (db_selected[i][5]).split(',')] ,}, #visible: bool(db_selected[i][4])
            'bar' : {'color' : db_selected[i][6],}},
        title = {'text': db_selected[i][7], 'font': {'size': 20}},
        domain = {'x': graph_position[0], 'y': graph_position[1]} #[int(x) for x in (df_week[i][5]).split(',')]
            ))


        # if count < 6:
        #     renderedGraph.add_trace(go.Indicator(
        #     mode = db_selected[i][0],
        #     value = timer_value,
        #     customdata= list(db_selected[i][2]),
        #     delta = {'reference': int(db_selected[i][3]),},
        #     gauge = {
        #         'axis': {'visible': bool(db_selected[i][4]), 'range': [int(x) for x in (db_selected[i][5]).split(',')] ,},
        #         'bar' : {'color' : db_selected[i][6],}},
        #     title = {'text': db_selected[i][7],},
        #     domain = {'x': graph_position[0], 'y': graph_position[1]} #[int(x) for x in (df_week[i][5]).split(',')]
        #         ))

        # if count > 5 and count < 9:
        #     recursive_fig2.add_trace(go.Indicator(
        #     mode = db_selected[i][0],
        #     value = timer_value,
        #     customdata= list(db_selected[i][2]),
        #     delta = {'reference': int(db_selected[i][3]),},
        #     gauge = {
        #         'axis': {'visible': bool(db_selected[i][4]), 'range': [int(x) for x in (db_selected[i][5]).split(',')] ,},
        #         'bar' : {'color' : db_selected[i][6],}},
        #     title = {'text': db_selected[i][7],},
        #     domain = {'x': graph_position[0], 'y': graph_position[1]} #[int(x) for x in (df_week[i][5]).split(',')]
        #         ))

    #REMOVE UNUSED SPACES.
    if count < 5:
    # WHITE LAYOUT
        recursive_fig2.update_layout(plot_bgcolor='rgb(255,255,255)',
                                        )
        recursive_fig2.update_xaxes(visible= False)
        recursive_fig2.update_yaxes(visible= False)
        blankSpace(recursive_fig2, "", "")
    #REMOVE UNUSED SPACES.
    if count == 0:
    # WHITE LAYOUT
        recursive_fig.update_layout(plot_bgcolor='rgb(255,255,255)',
                                        )
        recursive_fig.update_xaxes(visible= False)
        recursive_fig.update_yaxes(visible= False)
        blankSpace(recursive_fig, "", "Add some graphs :)")
    ######################################
    # PRIORITY GRAPHS
    #############################################################################
    # Option List:
    # ROUTINE: Shows a scatter plot of a SuccessRate Graph.
    priority_fig = go.Figure()
    #priority_fig.data = []
    # Must select Graph from dropdown. If so, get pts and compute avg = [arithmetic mean over period, ...] 
    if what2graph == "ROUTINE":# and checkedgraph is not None:
        #priority_fig = go.Figure()
        #priority_fig.data = []
        for db_entry in df_dedicatedTime:
            #db_entry = df_dedicatedTime[checkedgraph]
            #print(db_entry)
            #print(db_entry[9])
            start_day = datetime.datetime.fromtimestamp(float(df_dedicatedTime[db_entry][9])) #!!! To add.
            #print("start_day is", start_day)
            success = [int(x) for x in (df_dedicatedTime[db_entry][13]).split(', ')]
            day= [start_day+datetime.timedelta(days=i) for i in range(len(success))]
            average = sum(success)/len(success)
            
            print (db_entry, "\nDAY", day, "\navg", average, "\nsuccess", success)

            priority_fig.add_trace(
                go.Scatter(x=day, y=success,
                                    mode='markers', name= db_entry)
            )
            priority_fig.add_trace(
                go.Scatter(x=[start_day, start_day+datetime.timedelta(days=len(success)-1)], y=[0,average],
                                    mode='markers+lines', name='avg '+db_entry)
            )
        priority_fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.0,
            xanchor="right",
            x=0.8
        ))
        print("HOOOOOHO")
        priority_fig.update_layout(
            xaxis=dict(
                type="date",
            ),
            # title=dict(
            #     text=checkedgraph,
            #     font_size=30,
            #     font_color='black',
            #     x = 0.5,
            #     xanchor = 'center'
            # ),
        )
        return  recursive_fig, recursive_fig2, priority_fig, deadline_fig, deadline_fig2


    # ROUTINE: Shows a scatter plot of a SuccessRate Graph. 
    # Must select Graph from dropdown. Otherwise GO WHITE and SHOW MESSAGE.

    if what2graph == "USAGE TIPS":
        priority_fig = go.Figure()
        priority_fig.data = []
        # WHITE LAYOUT
        priority_fig.update_layout(plot_bgcolor='rgb(255,255,255)',
                                    title=dict(
                                            text="What's up! Let's start",
                                            font_size=30,
                                            font_color='black',
                                            x = 0.5,
                                            xanchor = 'center'
                                        ),)
        priority_fig.update_xaxes(visible= False)
        priority_fig.update_yaxes(visible= False)

        # MESSAGE
        priority_fig.add_annotation(text="Select a Graph in the Dropdown",
                        xref="paper", yref="paper",
                        font=dict(
                            family="Courier New, monospace",
                            size=16,
                            color="#000000"
                            ),
                        x=0, y=0.3, showarrow=False)
        priority_fig.add_annotation(text="To Visualize Your Progress over time",
                        xref="paper", yref="paper",
                        font=dict(
                            family="Courier New, monospace",
                            size=16,
                            color="#000000"
                            ),
                        x=0, y=0.2, showarrow=False)

        priority_fig.add_annotation(text="Add Some Graphs with Below Button",
                        xref="paper", yref="paper",
                        font=dict(
                            family="Courier New, monospace",
                            size=16,
                            color="#000000"
                            ),
                        x=0, y=0.8, showarrow=False)
        return  recursive_fig, recursive_fig2, priority_fig, deadline_fig, deadline_fig2

    # Show PAST Deadlines / COMPLETE Tasks.
    if what2graph == "LOGS":
        priority_fig = go.Figure()
        priority_fig.data = []

        # if empty Dataframe, SHOW MESSAGE.
        if df_weekAdvance.empty: 
            # WHITE LAYOUT
            blankSpace(priority_fig, "Logs", "Not yet any logs.")
            return  recursive_fig, recursive_fig2, priority_fig, deadline_fig, deadline_fig2

        names = df_weekAdvance.keys()
        # Gather all names & deadlines -> ARRAYs names[...] & completeDate[...]
        completeDate = []
        startDate = []
        for i in df_weekAdvance:
            #Using timestamps: only one line (unverified)... #completeDate.append(datetime.datetime.fromtimestamp(float(df_weekAdvance[i][1])))

            d=[int(x) for x in df_weekAdvance[i][1].split(',')] #HARD DEADLINE
            deadline = datetime.datetime(year=d[0], month=d[1], day=d[2], hour=d[3], minute=d[4], second=d[5])
            # NEED DATASTRUCT CONSISTENCY BEFORE THIS
            #print(df_weekAdvance[i][10])
            if df_weekAdvance[i][10] == 'Late':
                completeDate.append('Late')
                startDate.append(deadline)  
            else: #completed by deadline
                start_D=datetime.datetime.fromtimestamp(float(df_weekAdvance[i][10])) # COMPLETION DATE
                #deadline = datetime.datetime(year=d[0], month=d[1], day=d[2], hour=d[3], minute=d[4], second=d[5])
                startDate.append(deadline)
                days_taken = deadline - start_D 
                completeDate.append(days_taken.days)

            
            

        # Trace a Table
        priority_fig.add_trace(go.Table(
            header=dict(values=['Task', 'Deadline', 'Days completed before deadline']),
            cells=dict(values=[names, startDate, completeDate]))
        )

        return  recursive_fig, recursive_fig2, priority_fig, deadline_fig, deadline_fig2


    

    # Append indices of countdown graphs from most to least urgent -> TO ARRAY reordered_deadlines
    db_selected = df_Upcoming_events

    while len(deadline_list)!=0:
        print("SIKE")
        closest = min(d for d in deadline_list)
        reordered_deadlines.append(fixed_deadlines.index(closest))
        deadline_list.remove(closest)
        print('ma boy', reordered_deadlines)
        #print('lisst is ', deadline_list)

    # Render URGENCY graphs (priority_fig): categories "HOY" and "NEXT UP" 
    if what2graph == "NEXT UP" or what2graph == "HOY" or what2graph == "WORK":
        priority_fig = go.Figure()
        priority_fig.data = []

    # If there are no graphs.
    if len(reordered_deadlines) == 0:
        blankSpace(priority_fig, "Upcoming: Today", "All finished for this timeframe.")

    # If there are graphs: MESSAGE
    for g in reordered_deadlines:
        if ((fixed_deadlines[g].days == 0) and (fixed_deadlines[g].seconds//3600 < 12)): #BUG: NOT TAKING THE OBVIOUS ONE.
            priority_key = db_selected.keys()[reordered_deadlines[g]]
            print(db_selected[str(priority_key)])
            priority_fig.add_annotation(text="Next one: "+ db_selected[priority_key][7],

                            xref="paper", yref="paper",
                            font=dict(
                                family="Courier New, monospace",
                                size=16,
                                color="#000000"
                                ),
                            x=0, y=-0.2, showarrow=False)         
            priority_fig.add_annotation(text=" ETA: " + str(fixed_deadlines[reordered_deadlines[g]]),
                            xref="paper", yref="paper",
                            font=dict(
                                family="Courier New, monospace",
                                size=16,
                                color="#000000"
                                ),
                            x=0, y=-0.27, showarrow=False)           
            break

    print(fixed_deadlines)
    count=0 #Used for Layout of selected graphs.
    visible = 0 #Used for Knowing if any will later be Rendered.
    for g in reordered_deadlines:
        db_selected = df_Upcoming_events
        g = int(g)
        if fixed_deadlines[g].days < 0: #while keeping the indices
            continue

        db_key, db_val = list(db_selected.items())[g]

        # "NEXT UP": Only graphs with a deadline within 3 hours
        if what2graph == "NEXT UP":
            # Timer value in minutes, with max range at 180 min
            db_val[5] = '0,180'
            timer_value = fixed_deadlines[g].seconds//60
            # When empty:
            if fixed_deadlines[g].seconds//60 > 180:
                if g == reordered_deadlines[-1]: 
                    # WHITE LAYOUT
                    blankSpace(priority_fig, "Upcoming", "Your next 3h are free.")
                    return  recursive_fig, recursive_fig2, priority_fig, deadline_fig, deadline_fig2
                continue
        # "HOY": Only graphs with a deadline within 1 day
        if what2graph == "HOY":
            # Timer value in hours, with max range at 12h
            db_val[5] = '0,12'
            timer_value = fixed_deadlines[g].seconds//3600
            # When empty:
            if (fixed_deadlines[g].seconds//3600 > 12) or (fixed_deadlines[g].days> 0): #if more than 12h OR day>0
                #skip, and if all skipped, add little comment.
                if g == reordered_deadlines[-1] and visible == 0: 
                    # WHITE LAYOUT
                    blankSpace(priority_fig, "Upcoming", "Nothing in the next day.")
                    return  recursive_fig, recursive_fig2, priority_fig, deadline_fig, deadline_fig2
                continue
            else:
                visible += 1

        # "WORK": Only graphs within category 1.
        if what2graph == "WORK":
            # Timer value in minutes, with max range at 180 min
            db_val[5] = '0,180'
            timer_value = fixed_deadlines[g].seconds//60
            # When empty:
            if db_val[11] != '1':
                if g == reordered_deadlines[-1]: 
                    # WHITE LAYOUT
                    blankSpace(priority_fig, "For work", "We're done here.")
                    return  recursive_fig, recursive_fig2, priority_fig, deadline_fig, deadline_fig2
                continue


        #Now that values are selected, place them in order of appearance.  
        count+=1
        #Limiting us to 3 urgent graphs.
        if count > 3:
            continue
        #Size&positioning of all three graphs.
        size_proportional = 27/(1+count/3)
        graph_position = graph_layout_pyramid [(count-1)%5]
        #Colour of all three graphs.
        colour_palette = ['#ff0000', '#970505', '#550505'] #red-darkening hues, taken from https://htmlcolorcodes.com/ 
        db_val[6] = colour_palette[count-1] #'red'

        priority_fig.add_trace(go.Indicator(
            mode = 'gauge',
            value = timer_value,
            customdata= list(db_val[2]),
            delta = {'reference': int(db_val[3]),},
            gauge = {
                'axis': {'visible': bool(db_val[4]), 'range': [int(x) for x in (db_val[5]).split(',')] ,},
                'bar' : {'color' : db_val[6],}},
            title = {'text': db_val[7], 'font': {'size': size_proportional}},
            domain = {'x': graph_position[0], 'y': graph_position[1]} #[int(x) for x in (df_week[i][5]).split(',')]
        ))


    return  recursive_fig, recursive_fig2, priority_fig, deadline_fig, deadline_fig2


# @app.callback( #speed-indicatorgraph1
#     #dash.dependencies.Output('graph1', 'figure'), #deadline-fig2graph2
#     #dash.dependencies.Output('graph2', 'figure'), #deadline-fig2graph2
#     dash.dependencies.Output('speed-indicator', 'figure'),
#     #dash.dependencies.Output('next-indicator', 'figure'),
#     #dash.dependencies.Output('deadline-fig2', 'figure'),
#     [dash.dependencies.Input('interval-component', 'n_intervals')],
#     [dash.dependencies.State('open1-dropdown', 'value')], 
#     [dash.dependencies.State('priorities-dropdown', 'value')]) #INTERVAL has 2 purposes: UPDATE TIME or UPDATE GRAPH EDITS.
# def update_output(n_intervals, checkedgraph, what2graph):



## UPDATE DROPDOWN OPTIONS ##############################################


@app.callback( #speed-indicator
    #dash.dependencies.Output('speed-indicator', 'figure'),
    dash.dependencies.Output('open1-dropdown', 'options'),
    dash.dependencies.Output('open2-dropdown', 'options'),

    #[dash.dependencies.Input('top-dropdown', 'value')], 
    dash.dependencies.Input('open1', 'n_clicks'),
    dash.dependencies.Input('intermediate-value', 'data'),)
    #dash.dependencies.Input('mark-done', 'n_clicks'))
def update_output(open1, trigger):

    df_dedicatedTime, df_Upcoming_events = read_file()

    db_selected = df_dedicatedTime
    opts = list(db_selected)
    print (opts)
    options=[{'label':opt, 'value':opt} for opt in opts]  

    db_selected = df_Upcoming_events
    options2=[]
    for i in db_selected:
        d=[int(x) for x in db_selected[i][1].split(',')]
        #print(d)
        deadline = datetime.datetime(year=d[0], month=d[1], day=d[2], hour=d[3], minute=d[4], second=d[5])
        time_left=(deadline - datetime.datetime.now())
        #print(time_left)

        if time_left.days < 0: #remove past deadlines
            print(i)
            #continue #keep old deadlines

        if db_selected[i][10] != 'unfinished': #remove Completed deadlines
            print(i)
            continue

        options2.append({'label':i, 'value':i})

    #opts2 = list(db_selected)
    #print (opts2)
    #options2=[{'label':opt, 'value':opt} for opt in opts2] 

    return options, options2

#    dash.dependencies.Input('save', 'n_clicks'),


# dash.dependencies.Input('open1-mark-remove', 'value'), #  LOG DEPENDS ON NATURE...
#                                                           df_weekAdvance[a] = db_selected[a]
#                                                           data = data.drop(a, axis = 0)

# dash.dependencies.Input('open2-add1', 'value'),
# dash.dependencies.Input('open2-mark-done', 'value'),  #  LOG DEPENDS ON NATURE...
# dash.dependencies.Input('open2-mark-remove', 'value'), 
# dash.dependencies.State('open2-dropdown', 'value'),

## IN ANOTHER CALLBACK
# dash.dependencies.Output('open2-dropdown', 'options'), #Update the options.

import math
@app.callback( #speed-indicator
    dash.dependencies.Output('intermediate-value', 'data'),
    dash.dependencies.Output('warning-trigger', 'data'),

    #save all graphs
    dash.dependencies.Input('save', 'n_clicks'),
    #remove a graph
    dash.dependencies.Input('open1-mark-remove', 'n_clicks'),
    dash.dependencies.Input('open2-mark-remove', 'n_clicks'),
    #accomplish existing graph

    dash.dependencies.Input('open1-dropdown', 'value'),
    dash.dependencies.Input('mark-done', 'n_clicks'), #  LOG DEPENDS ON NATURE...

    dash.dependencies.Input('open2-mark-done', 'n_clicks'), #  LOG DEPENDS ON NATURE...
    #edit existing graph
    dash.dependencies.Input('open1-edit', 'n_clicks'),

    #ADD SUCCESSRATE
    dash.dependencies.Input('add2', 'n_clicks'),

    #ADD COUNTDOWN
    #dash.dependencies.Input('add1', 'n_clicks'),
    dash.dependencies.Input('add1-countdown', 'n_clicks'),

    #edit existing graph
    [dash.dependencies.State('open1-name', 'value')], 
    [dash.dependencies.State('open1-current', 'value')],
    [dash.dependencies.State('open1-max', 'value')],

    #ADD COUNTDOWN
    # [dash.dependencies.State('countdown-name', 'value')],
    # [dash.dependencies.State('open1-date', 'value')],
    # [dash.dependencies.State('open1-time', 'value')],

    #ADD SUCCESSRATE

    [dash.dependencies.State('open1-success-interval', 'value')],
    [dash.dependencies.State('progress-dropdown', 'value')],
    [dash.dependencies.State('open1-rate-name', 'value')],
    [dash.dependencies.State('open1-add-current', 'value')],
    [dash.dependencies.State('open1-add-max', 'value')],

    # OPEN 2 VARIABLES
    
    [dash.dependencies.State('open2-dropdown', 'value')],

    [dash.dependencies.State('countdown-name', 'value')],
    [dash.dependencies.State('open2-date', 'start_date')],
    [dash.dependencies.State('open2-date', 'end_date')],
    [dash.dependencies.State('open2-time', 'value')],
    [dash.dependencies.State('open2-category', 'value')],
)
def update_output(save, remove_left, removeR, a, b, doneR, c, d, e, f, g, h, l, m, n, o, p, open2,
                        nameR, startR, endR, timeR, categoryR):
    #i, j, k,
    df_dedicatedTime, df_Upcoming_events = read_file()

    #need to check which button pressed.
    trigger = callback_context.triggered[0] 
    button_id = trigger["prop_id"].split(".")[0]
    #print( "You clicked button {}".format(trigger["prop_id"].split(".")[0]))
    print("BUTTON PRESSED WAS", button_id)

    #MIGRATION
    # df_dedicatedTime = pd.read_csv("~/Documents/DashBeginnerTutorials/db_Dedicated_time.csv")
    # df_Upcoming_events = pd.read_csv("~/Documents/DashBeginnerTutorials/db_Upcoming_events.csv")

    # SUCCESSRATE
    # df_dedicatedTime = pd.DataFrame({
    #     'Nb tickets resto': 
    # ["gauge+number+delta", '3', 200, 100, '', '0,150', 'green', "d replicated", '0.25,0.5'],
    #     'Nb exercise routines': 
    # ["gauge", '0.4', 200, 100, '', '0,1', 'blue', "d", '0.5,1'],
    #     'Nb potential sponsors': 
    # ["gauge", '27', 200, 100, '', '0,150', 'orange', "d deadline", '0,0.25'],                        
    #                     })

    #save all graphs
    if button_id == 'save':
        save2file()

    if button_id == 'open1-mark-remove':
        db_selected = df_dedicatedTime

        print(db_selected)
        #remove_entry(a)
        df_dedicatedTime=remove_entry(db_selected, a)
        df_dedicatedTime.to_csv(repo_path+'/db_Dedicated_time.csv', index=False)
        return 0, 4
            
    #check off existing graph: graph a, on click b
    #db_selected = df_dedicatedTime
    #df_dedicatedTime, df_Upcoming_events = read_file()


    if button_id == 'open1-edit':
        #edit existing graph: on click c, edit a with name f, current val g and max h
        db_selected = df_dedicatedTime

        print(c, a, f, g, h) #1 Lab responses ere 4 34
        db_selected[a][7] = f               #Title
        db_selected[a][1] = g               #Value
        #db_selected[a][5] = "0,"+str(h)     #Range (NOT a range value...)
        db_selected[a][14] = str(h)     #Range (NOT a range value...)
        print(db_selected[a])
        #MIGRATION
        db_selected.to_csv(repo_path+'/db_Dedicated_time.csv', index=False)
        return 0, 4




    if button_id == 'add2':
        #ADD SUCCESSRATE: on click d, CREATE NEW with name n, current val o and max p. 
        # also m days and l week

        df_dedicatedTime, df_Upcoming_events = read_file()

        now = datetime.datetime.today()
        timestamp = now.replace(tzinfo=datetime.timezone.utc).timestamp()
        
        db_selected = df_dedicatedTime 
        print(d, n, o, p, m, l) #1 Lab responses ere 4 34
        db_selected[str(n)] =  ["gauge+number+delta", '1.0', 200, 1, '', 
        '0,1', 'green', "d replicated", '0.25,0.5', '', '', '', '', '0']#str(["gauge+number+delta", str(o), 200, 100, '', "0,"+str(p), 'green', str(n), '0.25,0.5']),
        #["gauge+number+delta", '3', 200, 100, '', '0,150', 'green', "d replicated", '0.25,0.5'],
        db_selected[n][7] = n               #Title
        db_selected[n][1] = str(o)               #Value
        #db_selected[n][5] = "0,"+str(p)      #Range (NOT a range value...)
        #db_selected[n][14] = str(p)          #Range (NOT a range value...)
        db_selected[n][9] = timestamp
        db_selected[n][10] = m               #Perform - I wish to complete this every...
        db_selected[n][11] = l               #Rateme  - Rate my progress every...
        #db_selected[n][12] = (datetime.today())
        db_selected[n][13] = '0'

        #RANDOM COLOUR
        print("LEN IS", len(db_selected.keys()))
        colour_dict = {0: 'green', 1: 'blue', 2: 'orange', 3: 'pink'}
        colour = colour_dict [len(db_selected.keys()) % 4 ]
        print("COLOUR", colour)
        db_selected[n][6] = colour

        db_selected.to_csv(repo_path+'/db_Dedicated_time.csv', index=False)
        return 0, 4

    # if button_id == 'open2-add1':
    #     print("DETECTS. Not used here.")
    #     pass
# ["gauge+number+delta", '2021,6,29,17,20,24', 200, 100, '', '0,150', 'green', "Papeyy", '0,1']

    if button_id == 'open2-mark-done':
        print("REMOVER. non verified.")
        db_selected = df_Upcoming_events
        print(db_selected)
        #deadline = str(end_date_object.year)+','
        # +str(end_date_object.month)+','+str(end_date_object.day)
        # +','+hh+','+mm+','+'0'
        d = [int(x) for x in db_selected[open2][1].split(",")]
        deadline = datetime.datetime(year=d[0], month=d[1], day=d[2], hour=d[3], minute=d[4], second=d[5])
        if datetime.datetime.now().timestamp() < deadline.timestamp():
            db_selected[open2][10] = (datetime.datetime.now().timestamp())
        else: 
            db_selected[open2][10] = 'Late'

        #Watch out: we remain but 10 gets used.
        #df_Upcoming_events=remove_entry(db_selected, open2)
        df_Upcoming_events.to_csv(repo_path+'/db_Upcoming_events.csv', index=False)
        return 0, 4

    if button_id == 'open2-mark-remove':
        print("REMOVER. non verified.")
        db_selected = df_Upcoming_events
        print(db_selected)
        #remove_entry(a)
        df_Upcoming_events=remove_entry(db_selected, open2)
        df_Upcoming_events.to_csv(repo_path+'/db_Upcoming_events.csv', index=False)
        return 0, 4

    if button_id == 'mark-done':
        #ADD SUCCESSRATE: refresh every m intervals and calculate "succeeded intervals/sum(l intervals)"
        rate_dict = {'week': 1/7, 'day': 1, 'halfday': 2}

        db_selected = df_dedicatedTime 
        power_up = 1
        #rate_performance = rate_dict[db_selected[a][11]] #Default per week...

        #NON-UPDATED LIST.
        total = [int(x) for x in db_selected[a][13].split(", ")]

        # Set up 3 dates: start, last, and today.
        start_day = datetime.datetime.fromtimestamp(float(db_selected[a][9]))
        last_recorded = start_day + datetime.timedelta(days=len(total)-1)
        today = (datetime.datetime.today())
        # get unrecorded time: total and in days.
        duration_unrecorded = (today - last_recorded)
        print("####", duration_unrecorded.days)
        nb_unrecorded_days = duration_unrecorded.days

        #UPDATED LIST.
        if len(total) > 7:
            total_window = total[:-7]
        else: total_window = total

        # If unrecorded, fill in the missing values.
        if nb_unrecorded_days != 0:
            [total.append(0) for i in range(nb_unrecorded_days)] #APPEND TOMORROW
        #Block if exceeds max nb of ticks/week.
        max_performance = rate_dict[db_selected[a][10]]
        if sum(total_window) >= max_performance*len(total_window) +1:
            print('not happening because ', sum(total_window), 'bigger than',  max_performance*len(total_window) +1)
            Wtrig = 1
        #Else add to today.
        else: 
            total[-1]= total[-1] + power_up #APPEND TODAY
        
        print(total)
        
        # Save new total
        db_selected[a][13] = str(total)[1:-1]               #Value

        scatter_dict = {}
        each_graph = a
        max_performance = rate_dict[db_selected[each_graph][10]]
        print ("I'mma rate yoouuu") 
        effectiveness = sum(total)/(max_performance*len(total))
        

        effectiveness_window = sum(total_window)/(max_performance*len(total_window))
        #rate_success = effectiveness_window/effectiveness
        rate_dict[db_selected[each_graph][3]] = effectiveness          #Ref to compare it
        db_selected[each_graph][1] = effectiveness_window               #Value shown

        db_selected.to_csv(repo_path+'/db_Dedicated_time.csv', index=False)

        
        #if (datetime.date.today() - start_date) % rateme == 0 and (datetime.date.today() != start_date):
        scatter_points = []
        rateme = rate_dict[db_selected[each_graph][11]] 
        x_len = len(total) * rateme
        print(x_len)
        for i in range (int(math.ceil(x_len))):
            j=i+1 #starts at 1
            performance_per_interval = sum(total[(j-1)*(int(math.ceil(rateme))):j*(int(math.ceil(rateme))) ])
            scatter_points.append([i, performance_per_interval]) 
        print("PTS IS", scatter_points)
        scatter_dict[each_graph] = scatter_points
        db_selected[each_graph][12] = scatter_points
        return Wtrig, 4


    if button_id == 'add1-countdown':
        # countdown-name -> nameR
        # add1-countdown -> addR
        # open2-date -> dateR
        # open2-time -> timeR


        now = datetime.datetime.today()
        timestamp = now.replace(tzinfo=datetime.timezone.utc).timestamp()
        print("registered")
        db_selected = df_Upcoming_events 

        db_selected[nameR] = ['gauge+number', '2021,6,29,17,20,24', 
                                200, 100, '', '0,150', 'green', "Papeyy", '0,1', '', '', 0]
        print(db_selected)
        print(nameR, timeR, startR, endR) #MadalinaRER 08:00 2021-07-01 2021-07-02

        db_selected[nameR][7] = nameR               #Title
        hh, mm = timeR[:2], timeR[3:] 
        print(hh, ":", mm) #08 : :00
        #print(yy, ":", mo, ":", da) #08 : :00
        start_date_object = datetime.date.fromisoformat(startR)
        end_date_object = datetime.date.fromisoformat(endR)

        #yy, mo, da = start_date_object[:4], start_date_object[6:8], start_date_object[10:12],
        #print(yy, ":", mo, ":", da) #08 : :00
        start_time = str(start_date_object.year)+','+str(start_date_object.month)+','+str(start_date_object.day)+','+hh+','+mm+','+'0'
        deadline = str(end_date_object.year)+','+str(end_date_object.month)+','+str(end_date_object.day)+','+hh+','+mm+','+'0'

        print (deadline) #2021,7,1,08,0000
        # start_date_string = start_date_object.strftime('%B %d, %Y')
        # print(start_date_string) #July 01, 2021
        print(start_date_object)
        
        #y, mo, da = dateR
        #deadline = ...
        db_selected[nameR][1] = str(deadline)               #Deadline 

        # db_selected[n][3] = str(o)     #DISPLAY Guessing via a hierarchy?
        # #db_selected[n][5] = "0,"+str(p)      #Range (NOT a range value...)
        # #db_selected[n][14] = str(p)          #Range (NOT a range value...)
        db_selected[nameR][9] = start_time
        db_selected[nameR][10] = 'unfinished'               #COMPLETE TIME
        print("category is", categoryR)
        db_selected[nameR][11] = categoryR         #CATEGORY: Base is '0', Work is '1', DroneLab '2'.
        #db_selected[nameR][12] = ''      #R: COMPLETION TIME (Implemented)
        # db_selected[n][13] = '0'

        #RANDOM COLOUR
        print("LEN IS", len(db_selected.keys()))
        colour_dict = {0: 'green', 1: 'blue', 2: 'orange', 3: 'pink'}
        colour = colour_dict [len(db_selected.keys()) % 4 ]
        print("COLOUR", colour)
        db_selected[nameR][6] = colour


        db_selected.to_csv(repo_path+'/db_Upcoming_events.csv', index=False)
        return 0, 4

        # nameR, startR, endR, timeR

    #ADD COUNTDOWN: on click e, CREATE NEW with name i, date j and time k
    # #REMOVE COUNTDOWN: on click e, CREATE NEW with name i, date j and time k
    # db_selected = df_Upcoming_events


    return 0, 4
    #print ('dropdown update bug')

##########################################################################    

############### ADD VALUE TO CHART CALLBACK #######################

#ISSUE ###: duplicate callbacks requires intermediate-state
#FIX: multiple outputs...
# from dash import callback_context
# @app.callback( #speed-indicator
#     #dash.dependencies.Output('speed-indicator', 'figure'),
#     dash.dependencies.Output('output-container-button', 'children'),
#     [dash.dependencies.Input('button', 'n_clicks')],
#     [dash.dependencies.Input('add-button', 'n_clicks')],
#     [dash.dependencies.Input('top-dropdown', 'value')],
#     dash.dependencies.Input('sub-dropdown', 'value'),
#     [dash.dependencies.State('input-box', 'value')],
#     [dash.dependencies.State('title-box', 'value')])
# def update_output(edit_clicks, add, page, topic, value, title):

#     df_week = pd.read_csv("~/Documents/DashBeginnerTutorials/db_"+page+".csv")
#     #need to check which button pressed.
#     trigger = callback_context.triggered[0] 
#     button_id = trigger["prop_id"].split(".")[0]
#     #print( "You clicked button {}".format(trigger["prop_id"].split(".")[0]))
#     if button_id == "button":
#         print("hello")
#         df_week[topic][1] = value
#     if button_id == "add-button":
#         #add text field
#         print(title)
#         print("hello")
#         df_week[title] = ["gauge+number+delta", '2021,6,17,23,25,25', 200, 100, '', '0,150', 'green', "Papers replicated", '0.25,0.5']
#         print(df_week[title])

#     df_week.to_csv('~/Documents/DashBeginnerTutorials/db_'+page+'.csv', index=False)

#     return 'The input value was "{}" and the button has been clicked {} times'.format(
#         value,
#         add
#     )

################## SEPARATE BUTTONS. ##

@app.callback(dash.dependencies.Output('open1-modal', 'style'),
              dash.dependencies.Input('open1-modal-close-button', 'n_clicks'),
              dash.dependencies.Input('open1', 'n_clicks'))

def close_modal(close, open):

    if (close is None) and (open is None):
        return {"display": "none"}

    if (close is None) and (open is not None):
        return {"display": "block"}

    if (open == close + 1) and (open is not None) and (close is not None):
        return {"display": "block"}

    if (open == close) and (close is not None):
        return {"display": "none"}

    print("Modal window bug")

@app.callback(dash.dependencies.Output('open2-modal', 'style'),
              dash.dependencies.Input('open2-modal-close-button', 'n_clicks'),
              dash.dependencies.Input('open2-add1', 'n_clicks'))

def close_modal(close, open):

    if (close is None) and (open is None):
        return {"display": "none"}

    if (close is None) and (open is not None):
        return {"display": "block"}

    if (open == close + 1) and (open is not None) and (close is not None):
        return {"display": "block"}

    if (open == close) and (close is not None):
        return {"display": "none"}

    print("Modal window bug")

# @app.callback(dash.dependencies.Output('edit1-modal', 'style'),
#               dash.dependencies.Input('edit1-modal-close-button', 'n_clicks'),
#               dash.dependencies.Input('warning-trigger', 'data'),) #storage

# def close_modal(close, open):


#     if (close is None) and (open != 1):
#         return {"display": "none"}

#     # OPEN/CLOSE
#     if (close is None) and (open == 1):
#         return {"display": "block"}

#     if (open == 1) and (close is not None):
#         return {"display": "none"}

#     print("Modal window bug")

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8053')
