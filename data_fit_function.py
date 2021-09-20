
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



import numpy as np

# FIRST TEST.
# values = np.linspace(1,10,10)
# print('values', values)
# print(len(values))
# for i in range(len(values)):
#     print(i)
# interp = np.interp(np.linspace(1,10,100), np.linspace(1,10,10), values )
# print(interp)


np.random.seed(344)


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
    print (interp)

fita2blen(log_adc, len(log_gps))


# INITIALIZE: empty SCATTERPLOT trace
scat = go.Figure()

scat.add_trace(go.Scatter(x=x_current, y=CURRENT_Y,
                    mode='lines+markers',
                    name='channel1'))
scat.add_trace(go.Scatter(x=x_final, y=interp,
                    mode='lines+markers',
                    name='channel4'))



app.layout = html.Div([

    html.Div(className='row', children = [

        html.Div(dcc.Graph(
            id='life-exp-vs-gdp',
            figure=scat
        ), className='six columns'),

    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
