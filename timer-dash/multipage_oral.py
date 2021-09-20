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
from scipy.fft import fft, fftfreq
from scipy import signal

from scipy.signal import butter, sosfilt, sosfreqz

fusion_graph = go.Figure()
accT_graph = go.Figure()
psd_graph = go.Figure()
gain_graph = go.Figure()
arduino_graph = go.Figure()
humidity_graph = go.Figure()

app.layout = html.Div([

                dcc.Store(id='current_df_traj', data = [[0,0,0]]), #ensures rangeslider consistent 

                html.Div(className='row', children = [
                    html.Div([
                        html.Div([
                            html.H2(children='TITLE TO EDIT', id='top-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

                            dcc.RangeSlider(
                                id='traj-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000])
                            ]),

                        html.Div(html.Iframe(
                        id = 'iframe_1',
                        src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
                            style={"height": "300px", "width": "100%"}
                        ), className= 'four columns'),


                        html.Div(html.Iframe(
                        id = 'iframe_2',
                        src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
                            style={"height": "300px", "width": "100%"}
                        ), className= 'four columns'),

                    html.Div([
                        html.H5(children='Service Drones: Linking Research Approaches to Industrial Practitioners', id='radio-2', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        dcc.RadioItems(
                            id='trajectory-select',
                            options=[
                                {'label': 'Motivations', 'value': 'TITLE'},
                                {'label': '', 'value': '', 'disabled': True},
                                {'label': '', 'value': '', 'disabled': True},
                                {'label': '', 'value': '', 'disabled': True},


                                {'label': 'Section 1: A Testbed for Service Drones', 'value': 'SECTION1'},
                                
                                {'label': 'SERVICE DRONE RESEARCH', 'value': 'SERVICE'},
                                {'label': 'A. SYSTEM REQUIREMENTS', 'value': 'SYSTEM'},
                                {'label': 'B. EVALUATION', 'value': 'EVALUATION'},

                                {'label': '', 'value': '', 'disabled': True},
                                {'label': '', 'value': '', 'disabled': True},

                                {'label': 'Section 2: Experimentations for Human-Drone Interfaces', 'value': 'SECTION2', 'disabled': True},

                                {'label': 'HUMAN-DRONE RESEARCH', 'value': 'HDI'},
                                {'label': 'A. PILOTING VIA GESTURE', 'value': 'GESTURE'},
                                {'label': 'B. INTERACTING WITH MIXED REALITY', 'value': 'XR'},

                                {'label': '', 'value': '', 'disabled': True},
                                {'label': '', 'value': '', 'disabled': True},
                                
                                {'label': 'Section 3: Deployment of UAVs for Industrial Applications', 'value': 'SECTION3', 'disabled': True},
                                
                                {'label': 'SENSOR PLACEMENT RESEARCH', 'value': 'PLACEMENT'},
                                {'label': 'A. ENVIRONMENT MONITORING', 'value': 'SCAN'},
                                {'label': 'B. VIBRATION MONITORING', 'value': 'VIBRATION'},

                            ],
                            value='CHOREOGRAPHY'),
                    ], className='two columns'),

                    ]),


                    html.Div(className='row', children = [                    
                        html.Div(html.Iframe(
                        id = 'iframe_3',
                        src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
                            style={"height": "300px", "width": "65%"}
                        ), className= 'five columns'),

                        html.Div(html.Iframe(
                        id = 'iframe_4',
                        src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
                            style={"height": "300px", "width": "65%"}
                        ), className= 'five columns'),
                        # html.Div(dcc.Graph(
                        #     id='SPECTROGRAM',
                        #     figure=spectrogram_graph,
                        #     style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        # ), className= 'five columns'),

                        html.Div(dcc.Graph(
                            id='graph_1',
                            figure=gain_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                        html.Div(dcc.Graph(
                            id='graph_2',
                            figure=arduino_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                        html.Div(dcc.Graph(
                            id='graph_3',
                            figure=humidity_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),


                    ]),

                ]),
        ])
#REALTIIIME
#temperature_graph
df_dropdown = pd.DataFrame({


                        'CHOREOGRAPHY': [
                            #tf_chore.csv //ELSE https://drive.google.com/file/d/1x2qqvYr9H7e2I3EXjBfKjJrhaLqA59aA/preview
                            'df_chore', 
                            #Chore Video
                            'https://drive.google.com/file/d/1tDETo4dPgGq81jFtJDxbsVOX12sX_0H2/preview', 
                            #State Machine.
                            'https://drive.google.com/file/d/1Zon_cCdtncfQGMEADcY6j_KMnNAVzX5T/preview', 
                            ''],

                        'TITLE': [
                            #tf_chore.csv //ELSE https://drive.google.com/file/d/1x2qqvYr9H7e2I3EXjBfKjJrhaLqA59aA/preview
                            'df_chore', 
                            #Presentation Photo
                            'https://drive.google.com/file/d/1R1_fwH7cVrpjaBiJulyQo5Fo8kIBoRLv/preview', 
                            #Presentation Photo
                            'https://drive.google.com/file/d/1-psUHZRTesfKrxGVJufHIG5VXzJWJ2Fa/preview', 
                            ''],

                        'GESTURE': [
                            #tf_chore.csv //ELSE https://drive.google.com/file/d/1x2qqvYr9H7e2I3EXjBfKjJrhaLqA59aA/preview
                            'df_chore', 
                            #Presentation Photo
                            'https://drive.google.com/file/d/1XgOdDW7FtxYn9KzCE1J4A7BtdUNFqtnt/preview', 
                            #Presentation Photo
                            'https://drive.google.com/file/d/1-psUHZRTesfKrxGVJufHIG5VXzJWJ2Fa/preview', 
                            ''],
        })

@app.callback(
    dash.dependencies.Output('iframe_1', 'src'),
    dash.dependencies.Output('iframe_2', 'src'),
    [dash.dependencies.Output('top-title', 'children')],
    #[dash.dependencies.Input('current_df_traj', 'data')],
    [dash.dependencies.Input('trajectory-select', 'value')])
def update_figure( traj_select):
    iframe_1 = df_dropdown[traj_select][1]
    iframe_2 = df_dropdown[traj_select][2]

    top_title = traj_select
    return iframe_1, iframe_2, top_title
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
