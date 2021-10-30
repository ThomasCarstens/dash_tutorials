import dash_gif_component as gif
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import datetime
import numpy as np
app = dash.Dash(__name__)

# x1 = #plot xyz position of a single drone.
# line01 = # included.
# #colour included for hz!! 
template_graph = go.Figure()
global tfs_cf3
global tfs_cf4
tfs_cf3 = []
tfs_cf4 = []
tf_log = {}
global x_cf3, y_cf3, z_cf3, time_cf3
global x_cf4, y_cf4, z_cf4, time_cf4
###########################################

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

# CALLBACK: ALL DRONES.
def template_graph_plot (rangemin, rangemax):
    all_tfs_path = '/home/txa/Documents/data/droneData_alliantech/eval_tests/hdi_2/bag_tf.csv'
    df_alltfs = pd.read_csv(all_tfs_path)
    tfs_cf1 = []
    tfs_cf2 = []
    # tfs_cf3 = np.array([])
    # tfs_cf4 = np.array([])
    
    tfs_cf3 = []
    tfs_cf4 = []
    print('before loop')
    #now separate the drones.
    for i in range(3,5):
        #recreate dataframe name on the fly
        trajectory = []
        min_data = max(1, rangemin*len(df_alltfs['field.transforms0.child_frame_id'])//100000)
        max_data = rangemax*len(df_alltfs['field.transforms0.child_frame_id'])//100000
        print(min_data, max_data)
        drone_data_clipped = df_alltfs[min_data:max_data:100]
        for entry in range(len(drone_data_clipped)):
            #print(df_alltfs['field.transforms0.child_frame_id'][entry])
            if drone_data_clipped['field.transforms0.child_frame_id'][entry] == 'cf'+str(i):
                print("YES")
                pos = []
                pos.append(drone_data_clipped['field.transforms0.transform.translation.x'][entry])
                pos.append(drone_data_clipped['field.transforms0.transform.translation.y'][entry])
                pos.append(drone_data_clipped['field.transforms0.transform.translation.z'][entry])
                pos.append(datetime.datetime.fromtimestamp(drone_data_clipped['%time'][entry]/10**9))
                trajectory.append(pos)
            print('with all poses')
            tf_log['tfs_cf'+str(i)]=(trajectory)
        print('with specific drone')
        #unzip into respective axis.
        xd, yd, zd, td = zip(*tf_log['tfs_cf'+str(i)])
        print('with separated coordinate')
        print(tf_log)
    
        template_graph = go.Figure()


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

        rates_cf4 = fita2blen(rates, len(xd))

        template_graph.add_trace(go.Scatter(x=xd, y=yd,
                                    mode='markers',
                                    name='Trace cf'+str(i),
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

        # rates_cf3 = fita2blen(rates, len(x_cf3))

        # template_graph.add_trace(go.Scatter(x=x_cf3, y=y_cf3,
        #                             mode='markers',
        #                             name='Trace cf3',
        #                             marker=dict(
        #                                 color=rates_cf3,
        #                                 size = 1.5,
        #                                 colorscale='BrBG',
        #                                 line_width=0.2,
        #                                 showscale=True,
        #                                 colorbar = dict(
        #                                         len=1,
        #                                         thickness=50.0,
        #                                         #tickangle=-90,
        #                                         x = -0.3,
        #                                         xanchor='right',
        #                                         outlinewidth=0.0
        #                                     ),
                            
        #                     )))

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


    tightfit = dict(l=20, r=20, t=50, b=100)
    template_graph.update_layout(
        margin=tightfit,
    )
    return template_graph

############################## END OF CALLBACK
                
app.layout = html.Div([

    html.Div(dcc.Graph(
        id='collision_graph',
        figure=template_graph
    )),

    html.Div(id='traj-rangeslider-title', children='traj-rangeslider'),
    dcc.RangeSlider(
        id='traj-edit-tool',
        min=1,
        max=100000,
        step=1,
        value=[1, 100000])

])
@app.callback(
    dash.dependencies.Output('collision_graph', 'figure'),
    [dash.dependencies.Input('traj-edit-tool', 'value')], 
    )
def traj_edit(slider_range):
    print(slider_range)
    template_graph = template_graph_plot(slider_range[0], slider_range[1])
    # lower_time = each['timestamp'][min_selected]
    # upper_time = each['timestamp'][max_selected]
    # #print("LOWER TIME:", lower_time//1000000)
    # duration = (max_selected-min_selected)/frequency
    return template_graph



if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')