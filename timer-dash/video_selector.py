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



app.layout = html.Div([
                html.H6(children='', id='random-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

                dcc.Store(id='current_df_traj', data = [[0,0,0]]), #ensures rangeslider consistent 

                html.Div(className='row', children = [

                    dcc.Interval(
                            id='interval-component',
                            interval=5000, # in milliseconds
                            n_intervals=0
                    ),
                    dcc.Store(id='intermediate-value', data = 0),

                    html.Div(children = [
                            html.Video(
                                controls = True,
                                id = 'movie_player',
                                src = "https://www.youtube.com/watch?v=gPtn6hD7o8g",
                                autoPlay=True,
                                height = 300
                            ),
                        ], className= 'six columns'),

                    html.Div(children = [
                            html.Video(
                                controls = True,
                                id = 'movie_player2',
                                src = "https://www.youtube.com/watch?v=gPtn6hD7o8g",
                                autoPlay=True
                            ),
                        ], className= 'six columns'),    
                ])

                
            ])


from dash.dependencies import Input, Output, State

@app.callback(
    Output('movie_player', 'src'),                  #video
    [Input('interval-component', 'n_intervals')],   #clock
    )
def update_vid(n):
    video_list = ["assets/DronedemofortheDVICwebsite.mp4", "/home/txa/Desktop/test_orbital.MP4", "/home/txa/Desktop/IMG_5830.MOV", "3"]
    colour_list = ["0", "1", "2", "3"]
    selected_colour = '0'
    if selected_colour in colour_list [0]:
        print( video_list [colour_list.index(selected_colour)])
        return video_list [colour_list.index(selected_colour)]


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
