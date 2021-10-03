
#https://community.plotly.com/t/populating-url-query-strings-based-on-dropdown-value-and-dropdown-value-based-on-query-string/14029

# initialise everything.


#create table.
import pandas as pd
# Category  | DRONE DROP | (1ST IN-VIVO) | ACCEL FIMI | ACCEL PORTEUR
# 0. [].csv |                                    *           * 
# 1. Vid    |                                    *           *
# 2. Layout |                                    *           *
# 3. Opts   |                                                *

df_dropdown = pd.DataFrame({


                        # CHOREOGRAPHY |
                        #
                        # DATA: .csv folder on Ggl Drive    -> LINK
                        # VID: .mp4 of CHORE                -> LINK
                        # LAYOUT: .jpg of the system        -> LINK
                        # OPTS:         / 2D XY TRAJ. / 

                        'CHOREOGRAPHY': [
                            '', 
                            #Chore Video
                            'https://drive.google.com/file/d/1tDETo4dPgGq81jFtJDxbsVOX12sX_0H2/preview', 
                            #State Machine.
                            'https://drive.google.com/file/d/1Zon_cCdtncfQGMEADcY6j_KMnNAVzX5T/preview', 
                            ''],

                        # PHOTOGRAMMETRY |

                        'PHOTOGRAMMETRY': [
                            '', 
                            '', 
                            '', 
                            ''],

                        # DRONE DROP |

                        'DRONE DROP': [
                            '', 
                            '', 
                            '', 
                            ''],

                        # ACCEL FIMI |
                        #
                        # DATA: .csv folder on Ggl Drive    -> LINK
                        # VID: .mp4 of What Drone Sees      -> LINK
                        # LAYOUT: .jpg of the system        -> LINK
                        # OPTS:         / ACCEL-DATA / 

                        'ACCEL FIMI': [
                            'a', 
                            'https://drive.google.com/file/d/1UBIq9C9hXVHWmlX53Shb1dI_FK83e5XU/preview', 
                            'https://drive.google.com/file/d/1UBIq9C9hXVHWmlX53Shb1dI_FK83e5XU/preview', 
                            'd'],

                        # ACCEL PORTEUR |
                        #
                        # DATA: .csv folder on Ggl Drive     -> LINK
                        # OUTSIDER VID: .mp4 of What We See  -> LINK
                        # LAYOUT: .jpg of the system        -> LINK
                        # OPTS: / BATTERY / RSSI / ACCEL-DATA / COMPASS / 

                        'ACCEL PORTEUR': [
                            'A', 
                            'https://drive.google.com/file/d/1xwuA-BSdjV0qM0Dv9P3mmf14OgaSeRhz/preview', 
                            'https://drive.google.com/file/d/1WVUky43TWml9K10CJlbQP-vIsZeVrS6O/preview', 
                            'D'],                        
                        })

# select from table.

print ("SHOULD BE", df_dropdown['ACCEL FIMI'][1])




# display.
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
app = dash.Dash(__name__)


df_chore= pd.read_csv('~/Downloads/tf_chore.csv')
df_chore_cmd= pd.read_csv('~/Documents/data/Fo8/fo8commands.csv')

# print(df_chore['field.transforms0.transform.translation.x'], df_chore['field.transforms0.transform.translation.y'])
# print (df_chore_cmd)


# traj_graph = px.scatter(df_chore, x=x_translation, y=y_translation, #z='field.transforms0.transform.translation.z', 
#                     title="Lighting levels on full path",
#                     #color_continuous_scale=px.colors.sequential.Rainbow[::],
#                     )

#find closest point to [df_chore_cmd['x^0'][0], df_chore_cmd['y^0'][0]]
#that belongs to [drone_traj_x, drone_traj_y]
drone_traj_pts = []
for i in range(len(df_chore)):
    drone_traj_pts.append([df_chore['field.transforms0.transform.translation.x'], df_chore['field.transforms0.transform.translation.y']])


######################### CRITERIA #############################
############################## DEVIATION !!!####################
# import math
# error_array = []
# for i in range(len(df_chore_cmd)):
#     error_min = -1000
#     for traj_x, traj_y in drone_traj_pts:
#         error_xy = [(traj_x - df_chore_cmd['x^0'][i]), (traj_y - df_chore_cmd['y^0'][i])]
#         error = math.sqrt(float(error_xy[0][0]**2) + float(error_xy[1][0]**2))
#         if abs(error) < abs(error_min):
#             error_min = error
#     print (error_min)
#     error_array.append(error_min)
# print (error_array)
# # [0.5407299812353649, 1.1142412927647118, 1.504703911051228, 1.4127250849561663, 0.9200836089237374, 
# # 0.5410086131332512, 0.6868321864977565, 0.6803779055220148, 0.4392062713886528, 0.23290298871791631]

# #using LMS estimate....
# final_residual = 0
# for residual in error_array:
#     final_residual=math.sqrt(final_residual**2 + residual**2)
# #RES: 2.848664820808726 
# print("RES:", final_residual)

# #using MEAN estimate....
# import numpy as np
# chore_average = np.mean(error_array)
# #AVG: 0.8072811844190799
# print("AVG:", chore_average)

############################## DEVIATION !!!####################




traj_graph = go.Figure()
for id in range(3):
    print (id+1) 

    drone_traj_x = []
    drone_traj_y = []
    for entry in range(len(df_chore)):
        if df_chore['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
            drone_traj_x.append(df_chore['field.transforms0.transform.translation.x'][entry])
            drone_traj_y.append(df_chore['field.transforms0.transform.translation.y'][entry])

    traj_graph.add_trace(go.Scatter(x=drone_traj_x, y=drone_traj_y,
                        mode='markers',
                        name='drone '+str(id+1)))



_3d_traj_graph = go.Figure()

for id in range(3):
    print (id+1) 

    drone_traj_x = []
    drone_traj_y = []
    drone_traj_z = []
    for entry in range(len(df_chore)):
        if df_chore['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
            drone_traj_x.append(df_chore['field.transforms0.transform.translation.x'][entry])
            drone_traj_y.append(df_chore['field.transforms0.transform.translation.y'][entry])
            drone_traj_z.append(df_chore['field.transforms0.transform.translation.z'][entry])

    _3d_traj_graph.add_trace(go.Scatter3d(x=drone_traj_x, y=drone_traj_y, z= drone_traj_z,
                        mode='markers',
                        name='drone '+str(id+1),
                        ),)

                        
    #PLEASE reduce the marker size. 
    _3d_traj_graph.update_traces(marker=dict(size=1),
                      selector=dict(mode='markers'))

# traj_graph.add_trace(go.Scatter(x=drone2_traj_x, y=drone2_traj_y,
#                     mode='markers',
#                     name='drone 2'))
# traj_graph.update_xaxes(title_text="Latitude", title_font=dict(
#         family="Courier New, monospace",
#         size=1,
#         color="#000000"))
# traj_graph.update_yaxes(title_text="Longitude", title_font=dict(
#         family="Courier New, monospace",
#         size=1,
#         color="#000000"))

# traj_graph.update_traces(marker=dict(size=1),
#                   selector=dict(mode='markers'))



app.layout = html.Div([

    html.Div(className='row', style={"margin-bottom": "30px"}, children=[
        html.Div([html.Button("➕", id="open2-add1")], style = {'width': '5%', 'display': 'inline-flex', 'align-items': 'left', 'justify-content': 'left'}),  
        html.Div([html.Button('Complete', id='open2-mark-done')], style = {'width': '80%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 
        html.Div([html.Button("Remove", id="open2-mark-remove")], style = {'width': '5%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}),  
    ]),
    
    html.Div(className='row', children = [

        html.Div([dcc.Graph(
            id='trajectory',
            figure=traj_graph,
        )], className='six columns'),

        html.Div([dcc.Graph(
            id='3d_traj',
            figure=_3d_traj_graph,
        )], className='six columns'),
        ]),

    html.Div(dcc.RangeSlider(
            id='traj-edit-tool',
            min=1,
            max=len(df_chore),
            step=1,
            value=[1, len(df_chore)]
        ), className='ten columns'),

    html.Div([ html.Iframe( id = 'external_video',
        src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
            style={"height": "450px", "width": "80%"}),
    ]),



    html.Div(className='row', children = [

        html.Div([

            html.H5('Equipment', style={"margin-bottom": "10px"}, className='four columns'),

            #html.H5('Sensor Data\n \n \n \nEquipment', style={"margin-bottom": "100px"}),
            html.H5('Sensors', style={"margin-top": "20px", "margin-bottom": "10px"}),
            dcc.RadioItems(
                id='sensor-select',
                options=[
                    {'label': 'ACCEL FIMI', 'value': 'ACCEL FIMI'},
                    {'label': 'ACCEL PORTEUR', 'value': 'ACCEL PORTEUR'},
                    {'label': 'CHOREOGRAPHY', 'value': 'CHOREOGRAPHY'},
                    #{'label': 'Timescale', 'value': 'Timescale'}
                ],
                value='ACCEL PORTEUR'
            ), 
        ], className='eight columns'), 

        # html.Div(dcc.Graph(
        #     id='number2',
        #     figure=scat
        # ), className='ten columns'),
    ]),

])

@app.callback(

    dash.dependencies.Output('trajectory', 'figure'),
    [dash.dependencies.Input('traj-edit-tool', 'value')])

def update_figure( traj_range):
    print("chosen range:", traj_range)
    _traj_data = df_chore[traj_range[0]:traj_range[1]]
    traj_graph = go.Figure()

    for id in range(3):
        print (id+1) 
        drone_traj_x = []
        drone_traj_y = []
        for entry in range(traj_range[0], traj_range[1]):
            if _traj_data['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
                drone_traj_x.append(_traj_data['field.transforms0.transform.translation.x'][entry])
                drone_traj_y.append(_traj_data['field.transforms0.transform.translation.y'][entry])

        traj_graph.add_trace(go.Scatter(x=drone_traj_x, y=drone_traj_y,
                            mode='markers',
                            name='drone '+str(id+1)))
    drone2_offset = [-0.3, -0.01]
    traj_graph.add_trace(go.Scatter(x=df_chore_cmd['x^0']+drone2_offset[0], y=df_chore_cmd['y^0']+drone2_offset[1],
                        mode='markers',
                        name='Fo8 '))
            

    return traj_graph


@app.callback(
    #dash.dependencies.Output('trajectory', 'figure'),
    #dash.dependencies.Output('trajectory', 'figure'),
    dash.dependencies.Output('external_video', 'src'),
    [dash.dependencies.Input('sensor-select', 'value')])
def update_figure( sensor):
    print("chosen sensor:", sensor)
    url_garage = df_dropdown[sensor][1]
    print(url_garage)

    video_garage = dict(
                src=url_garage,
                    style={"height": "450px", "width": "80%"}),
    # print("Cut down by", trim_step)
    # time_axis = local_time_timestamps[::trim_step]
    # if sensor == "Lightsensor":
    #     sensor_data = log_adc['raw_data[4]'][::trim_step]
    #     #sensor_data = log_adc_parking['raw_data[4]'][::trim_step] #Test from Garage
    #     sensor_colour = df_square['adc_report']
    # if sensor == "Accelerometer":
    #     print('sup')
    #     sensor_data = abs_acc[::trim_step]
    #     sensor_colour = df_square['absolute_accel']
    # if sensor == "Timescale":
    #     sensor_data = df_square['gps_lon']
    #     sensor_colour = df_square['timestamp']

    # scat.data = []
    # scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=sensor_data,
    #                     mode='lines+markers',
    #                     name='trim_step:%d'% trim_step)
    #  )


    # scat2 = px.scatter_3d(df_square, x='gps_lat', y='gps_lon', z='altitude', color= sensor_colour,
    #                     title=str(sensor_colour), ###FIX TITLE
    #                     color_continuous_scale=px.colors.sequential.Rainbow[::],
    #                     hover_data=["gps_lat", "timestamp"]
    #                     )

    # scat2.update_xaxes(title_text="Longitude", title_font=dict(
    #     family="Courier New, monospace",
    #     size=10,
    #     color="#000000"))
    # scat2.update_yaxes(title_text="Latitude", title_font=dict(
    #         family="Courier New, monospace",
    #         size=10,
    #         color="#000000"))

    # scat2.update_traces(marker=dict(size=1),
    #                 selector=dict(mode='markers'))

    # value = 13000
    # print(value, "x:", df_square['gps_lon'][value],
    #         "y:", df_square['gps_lat'][value],
    #             "z:", df_square['altitude'][value])


    # # Add range slider
    # scat.update_layout(
    #     xaxis=dict(
    #         type="date",
    #         #rangeslider_range = [time_axis[1], time_axis[50]],
    #         rangeslider_thickness = 0.07,
    #         rangeslider=dict(
    #             visible=True,
    #             #autorange=False,
    #             #fixedrange= False,
    #             range=[time_axis[1], time_axis[50]]
    #         ),

    # ))

    # return scat2, scat
    

    # traj_graph = px.scatter(df_chore, x=x_translation, y=y_translation, #z='field.transforms0.transform.translation.z', 
    #                     title="Lighting levels on full path",
    #                     #color_continuous_scale=px.colors.sequential.Rainbow[::],
    #                     )
    # traj_graph.add_trace(go.Scatter(x=x_translation, y=y_translation,
    #                     mode='lines+markers',
    #                     name='drone 2'))

    # traj_graph.update_xaxes(title_text="Latitude", title_font=dict(
    #         family="Courier New, monospace",
    #         size=1,
    #         color="#000000"))
    # traj_graph.update_yaxes(title_text="Longitude", title_font=dict(
    #         family="Courier New, monospace",
    #         size=1,
    #         color="#000000"))

    # traj_graph.update_traces(marker=dict(size=1),
    #                 selector=dict(mode='markers'))

    return url_garage



if __name__ == '__main__':
    app.run_server(debug=True)