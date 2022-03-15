import dash_gif_component as gif
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import numpy as np

app = dash.Dash(__name__)

hz_path = '/home/txa/Documents/data/hz_testgraph.txt'
feedbacktopic_path = '/home/txa/Documents/data/hz_feedback.txt'
#read line by line.
with open(feedbacktopic_path, "r") as f:
    notes = f.readlines()

rates = []
min = []
max = []
stddev = []

for line in notes:
    if 'rate' in line:
        rates.append(float(line.split(' ')[-1][:-2]))
print( rates )
#make x axis as a ccounter.
x01 = np.linspace(0, len(rates), len(rates))
template_graph = go.Figure()
template_graph.add_trace(go.Bar(
        name='B',
         y=np.array(rates),marker=dict(color='rgba(114, 186, 59, 0.5)')))

template_graph.update_yaxes(range=(118, 122))
# trace = go.Histogram(x=rates,
#                         name='spread',
#                         marker=dict(color='rgba(114, 186, 59, 0.5)'))

# template_graph.add_trace(trace)
template_graph.update_layout(
    title="Publishing Frequency of Drone Poses",
    title_x=0.5,
    xaxis_title="Frequency measured over batches of 100 messages",
    yaxis_title="Hz",

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