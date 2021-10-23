import dash_gif_component as gif
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import datetime
app = dash.Dash(__name__)

# x1 = #plot xyz position of a single drone.
# line01 = # included.
# #colour included for hz!! 

all_tfs_path = '/home/txa/Documents/data/droneData_alliantech/eval_tests/hdi_2/bag_tf.csv'
df_alltfs = pd.read_csv(all_tfs_path)
tfs_cf1 = []
tfs_cf2 = []
tfs_cf3 = []
tfs_cf4 = []
#now separate the drones.
for i in range(1,5):
    #recreate dataframe name on the fly
    tf_log = globals()['tfs_cf'+str(i)]
    for entry in range(len(df_alltfs['field.transforms0.child_frame_id'])):
        #print(df_alltfs['field.transforms0.child_frame_id'][entry])
        if df_alltfs['field.transforms0.child_frame_id'][entry] == 'cf'+str(i):
            print("YES")
            pos = []
            pos.append(df_alltfs['field.transforms0.transform.translation.x'][entry])
            pos.append(df_alltfs['field.transforms0.transform.translation.y'][entry])
            pos.append(df_alltfs['field.transforms0.transform.translation.z'][entry])
            pos.append(datetime.datetime.fromtimestamp(df_alltfs['%time'][entry]/10**9))

            tf_log.append(pos)

#unzip into respective axis.
print(len(tfs_cf1), len(tfs_cf2), len(tfs_cf3))
x_cf3, y_cf3, z_cf3, time_cf3 = zip(*tfs_cf3)
x_cf4, y_cf4, z_cf4, time_cf4 = zip(*tfs_cf4)
template_graph = go.Figure()
# template_graph.add_trace(go.Scatter(x=x_cf3, y=y_cf3,
#                             mode='lines',
#                             name='Trace 1',
#                             marker=dict( color='#ff7400')))

# template_graph.add_trace(go.Scatter(x=x_cf4, y=y_cf4,
#                             mode='lines',
#                             name='Trace 2',
#                             marker=dict( color='#d9dadc')))


# ADDING THE HZ :)
hz_path = '/home/txa/Documents/data/hz_testgraph.txt'
#read line by line.
with open(hz_path, "r") as f:
    notes = f.readlines()
rates = []
for line in notes:
    if 'rate' in line:
        rates.append(float(line.split(' ')[-1][:-2]))

import numpy as np
# THIS WONT WORK UNLESS DENSIFIED. TECHNICALLY BOTH SAME ROSBAG SOOO DENSIFIED IS FIABLE.
# JUST A CRAZY LONG PROCESS...
# densify points on graph
def fita2blen(f_val, x_desired):
    MAX_X = len(f_val)
    FINALLEN_X = x_desired
    CURRENTLEN_X = len(f_val)
    #x on 10 points, then 100 points
    x_current = list(np.linspace(1,MAX_X,CURRENTLEN_X))
    x_final = list(np.linspace(1,MAX_X,FINALLEN_X))
    # interpolate on 100 values.
    interp = np.interp(x_final, x_current, f_val )
    interp = list(interp)
    return interp

rates_cf4 = fita2blen(rates, len(x_cf4))

template_graph.add_trace(go.Scatter(x=x_cf4, y=y_cf4,
                            mode='markers',
                            name='Trace cf4',
                            marker=dict(
                                color=rates_cf4,
                                size = 1.5,
                                colorscale='BrBG',
                                line_width=0.2,
                                showscale=True,
                                colorbar = dict(
                                        len=1,
                                        thickness=50.0,
                                        #tickangle=-90,
                                        x = -0.3,
                                        xanchor='right',
                                        outlinewidth=0.0
                                    ),
                    
                    )))

rates_cf3 = fita2blen(rates, len(x_cf3))

template_graph.add_trace(go.Scatter(x=x_cf3, y=y_cf3,
                            mode='markers',
                            name='Trace cf3',
                            marker=dict(
                                color=rates_cf3,
                                size = 1.5,
                                colorscale='BrBG',
                                line_width=0.2,
                                showscale=True,
                                colorbar = dict(
                                        len=1,
                                        thickness=50.0,
                                        #tickangle=-90,
                                        x = -0.3,
                                        xanchor='right',
                                        outlinewidth=0.0
                                    ),
                    
                    )))

template_graph.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=0.0,
    xanchor="right",
    x=1
))
template_graph.update_layout(
    title="Publishing Frequency over Drone Positions",
    title_x=0.7,
    title_y=0.95,
    xaxis_title="X coordinates",
    yaxis_title="Y coordinates",

)
template_graph.update_xaxes(range=(-1, 1))



# template_graph.update_layout(marker=dict(
#                 color=rates,
#                 colorscale='Viridis',
#                 line_width=1,
#                 #showscale=True,
#                 colorbar = dict(
#                         len=1,
#                         thickness=50.0,
#                         #tickangle=-90,
#                         x = -0.3,
#                         xanchor='right',
#                         outlinewidth=0.0
#                     ),
#             ))


tightfit = dict(l=20, r=20, t=0, b=100)
template_graph.update_layout(
    margin=tightfit,
)

                
app.layout = html.Div([

    html.Div(dcc.Graph(
        id='algo03',
        figure=template_graph
    )),
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')