
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import dash_daq as daq

import json
import plotly.graph_objects as go
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, show_undo_redo=True)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

fig = go.Figure()
    
fig.add_trace(go.Indicator(
    mode = "gauge+number+delta",
    value = 40,
    customdata=[200],
    delta = {'reference': 100},
    gauge = {
        'axis': {'visible': False}},
    title = {'text': "The timer"},
    domain = {'x': [0,1], 'y': [0,1]}))

fig.update_layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)


app.layout = html.Div([

    html.Div(id='output'),

    dcc.Graph(figure=fig,
            id='speed-indicator'),
    # dcc.Interval(
    #     id='interval-component',
    #     interval=1*1000, # in milliseconds
    #     n_intervals=0
    # ),

    # # dcc.Store inside the app that stores the intermediate value
    # dcc.Store(id='timer-decrements', storage_type='local', data=200),
    html.Div(id='deadline-approaching',
             style={'font-size': '40px'}),
    html.Div(id='earliest-deadline',
             style={'font-size': '60px'}),
    html.Div(id='live-update-text',
             style={'font-size': '10px'}),

    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
    ),
    # dcc.Store inside the app that stores the intermediate value
    dcc.Store(id='comparing-deadlines')
])

@app.callback(
            Output('comparing-deadlines', 'data'),
            Output('speed-indicator', 'figure'),
            Output('live-update-text', 'children'),
            Output('deadline-approaching', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_date(n):

    deadline = datetime.datetime(year=2021, month=6, day=16, hour=23, minute=25, second=25)
    new_fig = go.Figure()
    #convert to hours...
    time_left=(deadline - datetime.datetime.now())
    hours_left = time_left.seconds//3600
    minutes_left = time_left.seconds//60
    minutes_clock = time_left.seconds//60 - time_left.seconds//3600


    new_fig.add_trace(go.Indicator(
        mode = "gauge+delta+number",
        value = minutes_left,
        customdata=[200],
        number = {
            'prefix': '%d:%d/'% (hours_left, minutes_clock),
            'valueformat': 'help'
        },
        delta = {'reference': 100},
        gauge = {
            'axis': {'visible': True, 'range':[0,60]}},
        title = {'text': "The timer"},
        domain = {'x': [0,1], 'y': [0,1]}))

    Stored_Dict = {} #probably needs init at construction...
    Stored_Dict['timer-1'] = time_left.seconds
    print(Stored_Dict)

    # fig.add_annotation(x=0, y=0,
    #             text='dhi',
    #             font={'size': 50},
    #             showarrow=True)

    return [    
                Stored_Dict,
                new_fig,
                html.P('Last updated ' +str(datetime.datetime.now())), 
                html.P('Time left: ' +str(deadline - datetime.datetime.now()))]

# CODE BELOW IS USELESS IF we can do it all in one callback.

@app.callback(
            Output('earliest-deadline', 'children'),
            Input('comparing-deadlines', 'data'))
def earliest_deadlines(data):
    print(data)


# WITH DECREMENTING VALUES.

# @app.callback(  Output('speed-indicator', 'figure'),
#                 Output('timer-decrements', 'data'),
#                 Input('interval-component', 'n_intervals'),
#                 Input('timer-decrements', 'data'))
# def update_metrics(n, time):
#     newfig = go.Figure()
    
#     newfig.add_trace(go.Indicator(
#         mode = "gauge+number+delta",
#         value = time,
#         customdata=[100],
#         delta = {'reference': 100},
#         gauge = {
#             'axis': {'visible': False}},
#         title = {'text': "The timer"},
#         domain = {'x': [0,1], 'y': [0,1]}))

#     time = time - 1

#     return newfig, time




if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')

