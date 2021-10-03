#tensor([[0.9940, 0.0018, 0.0042]])
import numpy as np

import dash
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_gif_component as gif
from datetime import date, timedelta
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


try:
    diagram01 = np.load("/home/txa/Downloads/Matrice1100mediumblanc4.npy")
except:
    print("did not find DIAGRAM01")

# for each in diagram01:
#     print(each)
print(diagram01.shape)
x_current = list(range(600))
print(x_current)
vibration01_graph = go.Figure()
import os
print(os. getcwd())


try:
    diagram02 = np.load("/home/txa/Downloads/Matrice1100mediumblanc3.npy")
    diagram03 = np.load("/home/txa/Downloads/Matrice1100mediumblanc2.npy")
    diagram03 = np.load("/home/txa/Downloads/Matrice1100mediumblanc2.npy")
except:
    print("did not find The others")


# for each in diagram01:
#     print(each)
print(diagram01.shape)
x_current = list(range(600))
print(x_current)
vibration01_graph = go.Figure()

# for each in diagram01:
vibration01_graph.add_trace(go.Scatter(x=x_current, y=diagram01[10],
                            mode='lines',
                            name='THROW: VIBRATION'))

theme = {
    'dark': False,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E'
}


app.layout = html.Div([

                dcc.Store(id='current_tensor', data = [0,0]), #ensures rangeslider consistent 

                # html.Div(id='dark-theme-components', children=[
                #         daq.DarkThemeProvider(theme=theme)
                #     ], style={
                #         'border': 'solid 1px #A2B1C6',
                #         'border-radius': '5px',
                #         'padding': '50px',
                #         'margin-top': '20px'
                #     }),

                html.Div(className='row', children = [
                    html.Div([
                        html.Div([
                            html.H6(children='DTW', id='title_graph01', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                            html.Div(className='row', style={"margin-bottom": "30px"}, children=[
                                                    html.Div([daq.Indicator(
                                                                id='colour_algo01',
                                                                value=True,
                                                                color="#fcfd85",
                                                                size=300),  
                                                        ], style = {'width': '100%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 
                                                    #html.Div([html.Div("☑️ ", id="open01")], style = {'width': '100%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}),  

                                                ]),
                            dcc.RangeSlider(
                                id='algo01-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000]),

                            # daq.Indicator(
                            # id='my-daq-indicator',
                            # value=True,
                            # color="#00cc96"
                            # ),  

                            html.Div(dcc.Graph(
                                id='algo01',
                                figure=vibration01_graph
                            )),


                    ], className= 'four columns'),

                    ]),

                    html.Div([
                        html.Div([
                            html.H6(children='SVM', id='title_graph02', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                            html.Div(className='row', style={"margin-bottom": "30px"}, children=[
                                                    #html.Div([html.Div("☑️ ", id="open02")], style = {'width': '40%', 'display': 'inline-flex', 'align-items': 'right', 'justify-content': 'right'}),  
                                                    html.Div([daq.Indicator(
                                                                id='colour_algo02',
                                                                value=True,
                                                                color="#ff7400",
                                                                size = 300,
                                                                label = dict(
                                                                    label= "ORANGE",
                                                                ),
                                                                labelPosition = 'bottom',
                                                                ),  
                                                        ], style = {'width': '100%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 

                                                ]),
                            dcc.RangeSlider(
                                id='algo02-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000]),

                            html.Div(dcc.Graph(
                                id='algo02',
                                figure=vibration01_graph
                            )),


                    ], className= 'four columns'),

                    ]),


                    html.Div([
                        html.Div([
                            html.H6(children='CNN', id='title_graph03', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                            html.Div(className='row', style={"margin-bottom": "30px"}, children=[
                                                    #html.Div([html.Div("☑️ ", id="open03")], style = {'width': '40%', 'display': 'inline-flex', 'align-items': 'right', 'justify-content': 'right'}),  
                                                    html.Div([daq.Indicator(
                                                                id='colour_algo03',
                                                                value=True,
                                                                color="#d9dadc",
                                                                size = 300),  
                                                        ], style = {'width': '100%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 

                                                ]),
                            dcc.RangeSlider(
                                id='algo03-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000]),

                            html.Div(dcc.Graph(
                                id='algo03',
                                figure=vibration01_graph
                            )),


                    ], className= 'four columns'),

                    ])

                ])

            ])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')


                #         html.Div([
                #             html.H6(children='GRAPH02', id='small-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                #             dcc.RangeSlider(
                #                 id='algo02-edit-tool',
                #                 min=1,
                #                 max=100000,
                #                 step=1,
                #                 value=[1, 100000]),

                #             html.Div(dcc.Graph(
                #                 id='algo02',
                #                 figure=vibration01_graph
                #             )),

                #     ], className= 'four columns'),

                #         html.Div([
                #             html.H6(children='GRAPH03', id='small-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                #             dcc.RangeSlider(
                #                 id='algo03-edit-tool',
                #                 min=1,
                #                 max=100000,
                #                 step=1,
                #                 value=[1, 100000]),

                #         html.Div(dcc.Graph(
                #             id='algo03',
                #             figure=vibration01_graph
                #         )),

                #     ], className= 'four columns'),

                # ])