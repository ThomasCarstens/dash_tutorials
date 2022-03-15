import dash_gif_component as gif
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import datetime
import numpy as np
app = dash.Dash(__name__)

# issues???
# removed drone iterable
# removed colour.
# added safety rangemax at 1
# removed rates[], then graph.
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



# CALLBACK: xy graph of trajectory.
def template_graph_plot (rangemin, rangemax):
    all_tfs_path = '/home/txa/Documents/data/droneData_alliantech/eval_tests/ht1/ht1.csv'
    df_alltfs = pd.read_csv(all_tfs_path)
    #print (df_alltfs)
    tfs_cf1 = []
    tfs_cf2 = []
    # tfs_cf3 = np.array([])
    # tfs_cf4 = np.array([])
    
    tfs_cf3 = []
    tfs_cf4 = []
    print('before loop')
    #now separate the drones.
        #recreate dataframe name on the fly
    i = 4
    trajectory = []
    min_data = max(1, rangemin*len(df_alltfs['field.transforms0.child_frame_id'])//100000)
    max_data = max(1,rangemax*len(df_alltfs['field.transforms0.child_frame_id'])//100000)
    print(min_data, max_data)
    drone_data_clipped = df_alltfs[min_data:max_data] #every 100?
    for entry in range(1,len(drone_data_clipped)):
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
    #print(tf_log)

    template_graph = go.Figure()

    # SEPARATING tfs_cf4 INTO MODES.

    signal_delimiters = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/ht1/signalmodes.csv')
    xd_split = []
    yd_split = []
    zd_split = []
    td_split = []
    prev_delimiter = 0
    # print(signal_delimiters['time'][0])
    # 1.62755038582071e+18
    
    delimiter = xd.index(signal_delimiters['x'][0])
    xd_split.append(xd[:delimiter])
    xd_split.append(xd[delimiter:])
    yd_split.append(yd[:delimiter])
    yd_split.append(yd[delimiter:])
    zd_split.append(zd[:delimiter])
    zd_split.append(zd[delimiter:])
    td_split.append(td[:delimiter])
    td_split.append(td[delimiter:])
    # for each in (signal_delimiters['x'][0], signal_delimiters['x'][4]):
    #     delimiter = xd.index(each)
    #     print("LIMIT IS:", delimiter)
    #     xd_split.append(xd[prev_delimiter:delimiter])
    #     yd_split.append(yd[prev_delimiter:delimiter])
    #     zd_split.append(zd[prev_delimiter:delimiter])
    #     prev_delimiter = delimiter
    #print (len(xd_split))
    # xd_split.append(xd[prev_delimiter:])
    # yd_split.append(yd[prev_delimiter:])
    # zd_split.append(zd[prev_delimiter:])
    # # ADDING THE HZ :)
    # hz_path = '/home/txa/Documents/data/hz_testgraph.txt'
    # #read line by line.
    # with open(hz_path, "r") as f:
    #     notes = f.readlines()
    # rates = []
    # for line in notes:
    #     if 'rate' in line:
    #         rates.append(float(line.split(' ')[-1][:-2]))

    import numpy as np
    # THIS WONT WORK UNLESS DENSIFIED. TECHNICALLY BOTH SAME ROSBAG SOOO DENSIFIED IS FIABLE.
    # JUST A CRAZY LONG PROCESS...
    # densify points on graph

    #rates_cf4 = fita2blen(rates, len(xd))
    for i in range(len(xd_split)):
        if signal_delimiters['name'][i] == 'PEACE':
            print('peace') #go.Scatter3d(x=xd_split[i], y=yd_split[i], z=zd_split[i],
            template_graph.add_trace(go.Scatter(x=xd_split[i], y=zd_split[i],
                                        mode='markers',
                                        name='Velocity Update Mode',
                                        marker=dict(
                                            color='red',
                                            size = 1.5,
                                            #colorscale='BrBG',
                                            line_width=0.2,
                                            # showscale=True,
                                            # colorbar = dict(
                                            #         len=1,
                                            #         thickness=50.0,
                                            #         #tickangle=-90,
                                            #         x = -0.3,
                                            #         xanchor='right',
                                            #         outlinewidth=0.0
                                            #     ),
                                
                                )))
        else:
            print('index')#go.Scatter(x=yd_split[i], y=zd_split[i],
            template_graph.add_trace(go.Scatter(x=xd_split[i], y=zd_split[i],
                                        mode='markers',
                                        name='Position Update Mode',
                                        marker=dict(
                                            color='blue',
                                            size = 1.5,
                                            #colorscale='BrBG',
                                            line_width=0.2,
                                            # showscale=True,
                                            # colorbar = dict(
                                            #         len=1,
                                            #         thickness=50.0,
                                            #         #tickangle=-90,
                                            #         x = -0.3,
                                            #         xanchor='right',
                                            #         outlinewidth=0.0
                                            #     ),
                                
                                )))
    #for i in range(len(signal_delimiters)):
        # if signal_delimiters['name'][i] == 'GRAB':
        #     template_graph.add_annotation(x=signal_delimiters['x'][i], y=signal_delimiters['z'][i],
        #         text="GRAB",
        #         showarrow=True,
        #         arrowhead=1)
        # if signal_delimiters['name'][i] == 'THUMBUP':
        #     template_graph.add_annotation(x=signal_delimiters['x'][i], y=signal_delimiters['z'][i],
        #         text="LAND",
        #         showarrow=True,
        #         arrowhead=1)
        # if signal_delimiters['name'][i] == 'PEACE':
        #     template_graph.add_annotation(x=signal_delimiters['x'][i], y=signal_delimiters['z'][i],
        #         text="SIGNAL",
        #         showarrow=True,
        #         arrowhead=1)
        # if signal_delimiters['name'][i] == 'INDEX':
        #     template_graph.add_annotation(x=signal_delimiters['x'][i], y=signal_delimiters['z'][i],
        #         text="SIGNAL",
        #         showarrow=True,
        #         arrowhead=1)


    import math
    timeline_graph = go.Figure()

    abs_vel_array = []
    for i in range(len(xd_split)):
        prev_x = 0 #initially
        prev_y = 0 #initially
        prev_z = 0 #initially
        abs_velocities = []
        for j in range(len(xd_split[i])):
            abs_vel = math.sqrt((xd_split[i][j]-(prev_x))**2+(yd_split[i][j]-(prev_y))**2+(zd_split[i][j]-(prev_z))**2)
            #print(abs_vel)
            prev_x = xd_split[i][j]
            prev_y = yd_split[i][j]
            prev_z = zd_split[i][j]
            abs_velocities.append(abs_vel*120)
        abs_vel_array.append(abs_velocities)
    #print("TIME:",td_split)
    for i in range(len(xd_split)):

        timeline_graph.add_trace(go.Scatter(x=td_split[i], y=abs_vel_array[i],
                                    mode='markers',
                                    line_width=0.5,
                                    name='Position Update Mode' if i == 1 else 'Velocity Update Mode',
                                    marker=dict(
                                        #color='blue',
                                        size = 0.9,
                                        #colorscale='BrBG',
                                        line_width=0.1,
                                        # showscale=True,
                                        # colorbar = dict(
                                        #         len=1,
                                        #         thickness=50.0,
                                        #         #tickangle=-90,
                                        #         x = -0.3,
                                        #         xanchor='right',
                                        #         outlinewidth=0.0
                                        #     ),
                                    )
                                    )
                                    )
        # for count, val in enumerate(abs_vel_array[i]):
        #     if val == 0:
        #         timeline_graph.add_vline(x=td_split[i][count], line=dict(
        #             color="Black",
        #             width=1,
        #             dash="solid",
        #         ))


    template_graph.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=0.0,
        xanchor="right",
        x=1
    ))
    template_graph.update_layout(
        #title="Drone Positions: Front View",
        #title_x=0.5,
        #title_y=0.95,
        xaxis_title="X coordinates",
        yaxis_title="Z coordinates",

    )
    # TO ADD: EXPECTED VELOCITIES.

    timestamped_gestures = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/ht1/hand_test1_results/timestamped_gestures.csv')
    timestamped_gestures= timestamped_gestures.dropna().reset_index(drop=True)
    expected_vel_time = []
    expected_vel_val = []
    time_offset = datetime.timedelta(milliseconds=0) # apparently 250ms does the trick with commands at 1/2 their initial.
    for j in range(len(timestamped_gestures['hand_signal'])):
        if '0' in timestamped_gestures['hand_signal'][j] or '1' in timestamped_gestures['hand_signal'][j]:
            expected_vel_val.append(float(timestamped_gestures['hand_signal'][j]))
            expected_vel_time.append(datetime.datetime.fromtimestamp(float(timestamped_gestures['time'][j])/10**9)+time_offset)
        #print (j)
        #print(timestamped_gestures['hand_signal'][0])
    #print(expected_vel_time)
    #print(expected_vel_val)
    #print(float(expected_vel[::2]))
    timeline_graph.add_trace(go.Scatter(x=expected_vel_time, y=expected_vel_val,
                                mode='markers',
                                line_width=0.5,
                                name='Desired Speeds',
                                marker=dict(
                                    color='green',
                                    size = 1.5,
                                    #colorscale='BrBG',
                                    line_width=0.1,
                                    # showscale=True,
                                    # colorbar = dict(
                                    #         len=1,
                                    #         thickness=50.0,
                                    #         #tickangle=-90,
                                    #         x = -0.3,
                                    #         xanchor='right',
                                    #         outlinewidth=0.0
                                    #     ),
                                )
                                )
                                )
    # for i,val in enumerate(expected_vel_val):
    #     if val == 0 :
    #         timeline_graph.add_vline(x=expected_vel_time[i], line=dict(
    #             color="Red",
    #             width=1,
    #             dash="solid",
    #         ))


    hand_signals = []
    hand_signals_time = []
    downslide_time = []
    upslide_time = []
    leftslide_time = []
    rightslide_time = []    
    upslide_time = []
    downslide_time = []
    right_time = []
    left_time = []
    up_time = []
    down_time = []
    index_time = []
    thumbup_time = []
    print("append slides")
    for j in range(len(timestamped_gestures['hand_signal'])):
        j_datetime = datetime.datetime.fromtimestamp(float(timestamped_gestures['time'][j])/10**9)
        if ('0' not in timestamped_gestures['hand_signal'][j]) and ('1' not in timestamped_gestures['hand_signal'][j]):
            hand_signals.append(timestamped_gestures['hand_signal'][j])
            hand_signals_time.append(j_datetime)
            print("saw hand_signal")
            #print(hand_signals_time)
            if timestamped_gestures['hand_signal'][j] == 'DOWN SLIDE':
                downslide_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'UP SLIDE':
                upslide_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'LEFT SLIDE':
                leftslide_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'RIGHT SLIDE':
                rightslide_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'UP SLIDE':
                upslide_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'DOWN SLIDE':
                downslide_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'RIGHT':
                right_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'LEFT':
                left_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'UP':
                up_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'DOWN':
                down_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'INDEX':
                index_time.append(j_datetime)
            if timestamped_gestures['hand_signal'][j] == 'THUMBUP':
                thumbup_time.append(j_datetime)
            sign = timestamped_gestures['hand_signal'][j] 
            # if (sign != 'INDEX') and (sign != 'THUMBUP') and (sign != 'DOWN SLIDE') and (sign != 'UP SLIDE') and (sign != 'LEFT SLIDE') and (sign != 'RIGHT SLIDE') and (sign != 'UP') and (sign != 'DOWN') and (sign != 'LEFT') and (sign != 'RIGHT'):
            #     print (sign)
            print("stuck hand_signal")
    
    print("prepare")
    downslide = []
    upslide = []
    leftslide = []
    rightslide = []
    upslide = []
    downslide = []
    right = []
    left = []
    up = []
    down = []
    index = []
    thumbup = []
    for j in up_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                up.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    for j in down_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                down.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    for j in downslide_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                downslide.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    for j in upslide_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                upslide.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    for j in leftslide_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                leftslide.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    for j in rightslide_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                rightslide.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    for j in right_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                right.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    for j in left_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                left.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    for j in index_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                index.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    for j in thumbup_time:
        for t in td:
            diff = t - j
            if abs(t - j) < datetime.timedelta(seconds=0.01):
                #print ("found", diff)
                thumbup.append([xd[td.index(t)], yd[td.index(t)], zd[td.index(t)], t ])
                break
    xrr, yrr, zrr, trr = zip(*upslide) #
    cutoff = trr.index(datetime.datetime(2021, 7, 29, 11, 19, 45, 918890))
    print("len UPSLIDES:", len(trr[cutoff:]))
    #print ("upslides:", trr)
    template_graph.add_trace(go.Scatter(x=xrr[cutoff:], y=zrr[cutoff:],
                                mode='markers',
                                line_width=0.5,
                                name='Upslides',
                                marker=dict(
                                    color='yellow',
                                    size = 4.0,
                                    line_width=0.1,

                                )
                                )
                                )     

    xrr, yrr, zrr, trr = zip(*downslide)
    #print ("downslides:", trr)
    cutoff = trr.index(datetime.datetime(2021, 7, 29, 11, 19, 45, 818310))
    print("len DOWNSLIDES:", len(trr[cutoff:]))
    template_graph.add_trace(go.Scatter(x=xrr[cutoff:], y=zrr[cutoff:],
                                mode='markers',
                                line_width=0.5,
                                name='Downslides',
                                marker=dict(
                                    color='blue',
                                    size = 4.0,
                                    line_width=0.1,

                                )
                                )
                                )     

    xrr, yrr, zrr, trr = zip(*rightslide)
    cutoff = trr.index(datetime.datetime(2021, 7, 29, 11, 19, 47, 488750))
    print("len RIGHTSLIDES:", len(trr[cutoff:]))
    #print ("rightslides:", trr)
    template_graph.add_trace(go.Scatter(x=xrr[cutoff:], y=zrr[cutoff:],
                                mode='markers',
                                line_width=0.5,
                                name='Rightslides',
                                marker=dict(
                                    color='red',
                                    size = 4.0,
                                    line_width=0.1,

                                )
                                )
                                )     
    xrr, yrr, zrr, trr = zip(*leftslide)
    cutoff = trr.index(datetime.datetime(2021, 7, 29, 11, 19, 46, 958400))
    print("len LEFTSLIDES:", len(trr[cutoff:]))
    #print ("leftslides:", trr)
    template_graph.add_trace(go.Scatter(x=xrr[cutoff:], y=zrr[cutoff:],
                                mode='markers',
                                line_width=0.5,
                                name='Leftslides',
                                marker=dict(
                                    color='green',
                                    size = 4.0,
                                    line_width=0.1,

                                )
                                )
                                )             
    xrr, yrr, zrr, trr = zip(*right)
    # print(trr) #no cutoff needed
    print("len RIGHT:", len(trr))
    print("change at", datetime.datetime.fromtimestamp(1627550385)) #1.62755038582071e+18 # 1627550385 820710000
     
    template_graph.add_trace(go.Scatter(x=xrr, y=zrr,
                                mode='markers',
                                marker_symbol='arrow-left',
                                line_width=0.5,
                                name='Left',
                                marker=dict(
                                    color='blue',
                                    size = 6.0,
                                    line_width=0.1,

                                )
                                )
                                )             

    xrr, yrr, zrr, trr = zip(*left)
    #print(trr)
    
    cutoff = trr.index(datetime.datetime(2021, 7, 29, 11, 19, 43, 38700))
    print("len LEFT:", len(trr[:cutoff]))
    
    template_graph.add_trace(go.Scatter(x=xrr[:cutoff], y=zrr[:cutoff],
                                mode='markers',
                                marker_symbol='arrow-right',
                                line_width=0.5,
                                name='Right',
                                marker=dict(
                                    color='green',
                                    size = 6.0,
                                    line_width=0.1,

                                )
                                )
                                )      

    xrr, yrr, zrr, trr = zip(*up)
    # print("UP", trr)
    cutoff = trr.index(datetime.datetime(2021, 7, 29, 11, 19, 46, 788620))
    print("len UP:", len(trr[:cutoff]))
    template_graph.add_trace(go.Scatter(x=xrr[:cutoff], y=zrr[:cutoff],
                                mode='markers',
                                marker_symbol='arrow-up',
                                line_width=0.5,
                                name='Up',
                                marker=dict(
                                    color='red',
                                    size = 6.0,
                                    line_width=0.1,

                                )
                                )
                                )      

    xrr, yrr, zrr, trr = zip(*down)
    #print("DOWN", trr) #no cutoff needed
    # cutoff = trr.index(datetime.datetime(2021, 7, 29, 11, 19, 46, 788620))
    print("len DOWN:", len(trr))
    template_graph.add_trace(go.Scatter(x=xrr, y=zrr,
                                mode='markers',
                                marker_symbol='arrow-down',
                                line_width=0.5,
                                name='Down',
                                marker=dict(
                                    color='orange',
                                    size = 6.0,
                                    line_width=0.1,

                                )
                                )
                                )   

    xrr, yrr, zrr, trr = zip(*index)
    #print("index:", trr) #no cutoff needed
    template_graph.add_trace(go.Scatter(x=xrr, y=zrr,
                                mode='markers',
                                marker_symbol='square',
                                line_width=0.5,
                                name='Index',
                                marker=dict(
                                    color='pink',
                                    size = 6.0,
                                    line_width=0.1,

                                )
                                )
                                )  

    xrr, yrr, zrr, trr = zip(*thumbup)
    template_graph.add_trace(go.Scatter(x=xrr, y=zrr,
                                mode='markers',
                                marker_symbol='diamond',
                                line_width=0.2,
                                name='Thumbup',
                                marker=dict(
                                    color='purple',
                                    size = 6.0,
                                    line_width=0.1,

                                )
                                )
                                )  


    # TO ADD: LABELS
    # WITH BARS LIKE realtime_graph...


    # for i in range(len(hand_signals)):
    #     if hand_signals[i] == 'GRAB':
    #         timeline_graph.add_vline(x=hand_signals_time[i], line=dict(
    #             color="Red",
    #             #text="GRAB",
    #             width=0.1,
    #             dash="dot",
    #         ))


    template_graph.update_xaxes(range=(-1.3, 0))    
    #template_graph.update_yaxes(range=(0, 0.2))
    #timeline_graph.update_xaxes(range=(-1.3, 0))  
    timeline_graph.update_layout(
        title="Drone Velocities",
        title_x=0.5,
        #title_y=0.95,
        xaxis_title="Time",
        yaxis_title="Absolute Velocity",

    )

    timeline_graph.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=0.0,
        xanchor="right",
        x=1
    ))

    timeline_graph.update_yaxes(range=(-0.05, 0.5))  

    # tightfit = dict(l=20, r=20, t=50, b=100)
    # template_graph.update_layout(
    #     margin=tightfit,
    # )
    return template_graph, timeline_graph

############################## END OF CALLBACK
timeline_graph = go.Figure()
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
        value=[1, 100000]),

    html.Div(dcc.Graph(
        id='timeline_graph',
        figure=timeline_graph
    )),

])
@app.callback(
    dash.dependencies.Output('collision_graph', 'figure'),
    dash.dependencies.Output('timeline_graph', 'figure'),
    [dash.dependencies.Input('traj-edit-tool', 'value')], 
    )
def traj_edit(slider_range):
    print(slider_range)
    template_graph, timeline_graph = template_graph_plot(slider_range[0], slider_range[1])
    # lower_time = each['timestamp'][min_selected]
    # upper_time = each['timestamp'][max_selected]
    # #print("LOWER TIME:", lower_time//1000000)
    # duration = (max_selected-min_selected)/frequency
    return template_graph, timeline_graph



if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')