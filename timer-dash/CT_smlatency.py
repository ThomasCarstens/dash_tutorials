import dash_gif_component as gif
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import datetime

app = dash.Dash(__name__)

df_collisions = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/hdi_2/collision_graphs.csv')

time_array = []
message_times = []
for i in (1, 2, 4):
    time = abs(df_collisions['heli timestamps'][i] - df_collisions['collision timestamp'][i])/10**9
    message_time = datetime.datetime.fromtimestamp(df_collisions['heli timestamps'][i]/10**9)
    time_array.append(time)
    message_times.append(message_time)

#make x axis as a ccounter.
x01 = np.linspace(0, len(time_array), len(time_array))


template_graph = go.Figure()
template_graph.add_trace(go.Bar(
        name='B', x = message_times,
         y=np.array(time_array),marker=dict(color='rgba(114, 186, 59, 0.5)')))

template_graph.update_traces(texttemplate=time_array, textposition='outside')
template_graph.update_yaxes(range=(0, 3.5))


# template_graph.add_trace(trace)
template_graph.update_layout(
    title="Latency in Message Transmission",
    title_x=0.5,
    xaxis_title="Time of Message",
    yaxis_title="Seconds of Latency",

)
############# Ideas
#AT THIS POINT: OVER 1, 2, 3 DRONES???
#could add a page title and change PUBLISHING FREQUENCY for each test.

app.layout = html.Div([

    html.Div(dcc.Graph(
        id='algo03',
        figure=template_graph
    )),
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')