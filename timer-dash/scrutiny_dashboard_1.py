import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_gif_component as gif
from datetime import date, timedelta
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
import os
print(os. getcwd())


df_chore= pd.read_csv('~/Documents/data/eval_tests/tf_chore.csv')

traj_graph = go.Figure()
for id in range(3):
    print (id+1) 

    drone_traj_x = []
    drone_traj_y = []
    for entry in range(len(df_chore)):
        if df_chore['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
            drone_traj_x.append(df_chore['field.transforms0.transform.translation.x'][entry])
            drone_traj_y.append(df_chore['field.transforms0.transform.translation.y'][entry])

    traj_graph.add_trace(go.Scatter(x=drone_traj_x, y=drone_traj_y,
                        mode='markers',
                        name='drone '+str(id+1)))


_3d_traj_graph = go.Figure()

for id in range(3):
    print (id+1) 

    drone_traj_x = []
    drone_traj_y = []
    drone_traj_z = []
    for entry in range(len(df_chore)):
        if df_chore['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
            drone_traj_x.append(df_chore['field.transforms0.transform.translation.x'][entry])
            drone_traj_y.append(df_chore['field.transforms0.transform.translation.y'][entry])
            drone_traj_z.append(df_chore['field.transforms0.transform.translation.z'][entry])

    _3d_traj_graph.add_trace(go.Scatter3d(x=drone_traj_x, y=drone_traj_y, z= drone_traj_z,
                        mode='markers',
                        name='drone '+str(id+1),
                        ),)           
    #PLEASE reduce the marker size. 
    _3d_traj_graph.update_traces(marker=dict(size=1),
                      selector=dict(mode='markers'))

with open("notes/notes_chore.txt", "r") as f:
    notes = f.readlines()
#html.Br()#

app.layout = html.Div([

                dcc.Store(id='current_df_traj', data = [0,0]), #ensures rangeslider consistent 

                html.Div(className='row', children = [
                    html.Div([
                        html.Div([
                            html.H6(children='CHOREOGRAPHY', id='small-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                            dcc.RangeSlider(
                                id='traj-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000])
                            ]),
                        html.Div(dcc.Graph(
                            id='trajectory',
                            figure=traj_graph
                        )),

                    ], className= 'five columns'),
                    
                    html.Div([
                        html.H3(children='Flight Analysis', id='big-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
                        html.Iframe(
                        id = 'external_video',
                        src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
                            style={"height": "300px", "width": "65%"}),
                    ], className='six columns'),

                    html.Div(html.H6(children=notes, id='text-div', 
                            style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}
                            ), className='six columns'),
                ]),

                html.Div(className='row', children = [
                    # html.Div((
                    #     <blockquote class="trello-board-compact">
                    #     <a href="{https://trello.com/b/ApWZRkQy/newsletter-articles}">Trello Board</a>
                    #     </blockquote>
                    #     <script src="https://p.trellocdn.com/embed.min.js"></script>
                    # ), className='six columns'),

                    html.Div(dcc.Graph(
                        id='3d_traj',
                        figure=_3d_traj_graph,
                        
                    ), className='five columns'),


                    html.Div([
                        html.H5(children='Trajectory Chooser', id='radio-2', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        dcc.RadioItems(
                            id='trajectory-select',
                            options=[
                                {'label': 'TEST_1', 'value': 'CHOREOGRAPHY'},
                                {'label': 'HOVER WITH PUSH', 'value': 'HOVERTEST'},
                                {'label': 'HOVER WITH 2 DRONES', 'value': '2D1A'},
                                {'label': 'HOVER WITH 3 DRONES', 'value': 'HOVER WITH 3 DRONES'},
                                {'label': 'XREALITY_TEST1', 'value': 'XREALITY_TEST1'},
                                {'label': 'HAND_TEST', 'value': 'HAND_TEST'},

                            ],
                            value='CHOREOGRAPHY'),
                    ], className='two columns'),



                    html.Div([
                        html.H5(children='Available videos', id='radio-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        dcc.RadioItems(
                            id='sensor-select',
                            options=[
                                {'label': 'VIDEO_1', 'value': 'VIDEO_1'},
                                {'label': 'VIDEO_2', 'value': 'VIDEO_2'},
                                {'label': 'VIDEO_3', 'value': 'VIDEO_3'},
                                {'label': 'VIDEO_4', 'value': 'VIDEO_4'},
                                {'label': 'VIDEO_5', 'value': 'VIDEO_5'},
                                {'label': 'VIDEO_6', 'value': 'VIDEO_6'},
                                {'label': 'VIDEO_7', 'value': 'VIDEO_7'},
                                {'label': 'VIDEO_8', 'value': 'VIDEO_8'},
                            ],
                            value='VIDEO_1'),
                    ], className='two columns'),

                    html.Div([
                        html.H5(children='Config Dashboard', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        dcc.Checklist(
                            id = 'parameters',
                            options=[
                                {'label': 'Display Relevant Vid', 'value': 'CB_LINK'},
                                {'label': '...', 'value': 'MTL'},
                                {'label': '...', 'value': 'SF'}
                            ],
                            value=['MTL'])  

                    ], className='two columns'),


                ]),
            ])
#################################### CALLBACK PREP ########################################33

df_dropdown = pd.DataFrame({


                        # CHOREOGRAPHY |
                        #
                        # DATA: .csv folder on Ggl Drive    -> LINK
                        # VID: .mp4 of CHORE                -> LINK
                        # LAYOUT: .jpg of the system        -> LINK
                        # OPTS:         / 2D XY TRAJ. / 

                        'VIDEO_1': [
                            #tf_chore.csv //ELSE https://drive.google.com/file/d/1x2qqvYr9H7e2I3EXjBfKjJrhaLqA59aA/preview
                            'df_chore', 
                            #Chore Video
                            'https://drive.google.com/file/d/1HeWXMxgwKOtvBLDW9Sbk1EvR832SeYmu/preview', 
                            #State Machine.
                            'https://drive.google.com/file/d/1Zon_cCdtncfQGMEADcY6j_KMnNAVzX5T/preview', 
                            ''],

                        # HOVERTEST |

                        'HOVERTEST': [
                            #ELSE https://drive.google.com/file/d/107Qt78KKNubyInvjrD7xD_4C4Z0lEi9V/preview
                            'df_hover', 
                            'https://drive.google.com/file/d/1GJBwi408tLAaQ2nTPaKib4t8WmOV6k9H/preview', 
                            '', 
                            ''],

                        # 2D1A |

                        '2D1A': [
                            #ELSE https://drive.google.com/file/d/107Qt78KKNubyInvjrD7xD_4C4Z0lEi9V/preview
                            '2d1a', 
                            'https://drive.google.com/file/d/1iDla3U-xtCS70qHxsmk_hnaWZL3d0dQA/preview', 
                            '', 
                            ''],                        
                        # PHOTOGRAMMETRY |

                        'PHOTOGRAMMETRY': [
                            '', 
                            '', 
                            '', 
                            ''],

                        # DRONE DROP |

                        'DRONE DROP': [
                            '', 
                            '', 
                            '', 
                            ''],

                        # ACCEL FIMI |
                        #
                        # DATA: .csv folder on Ggl Drive    -> LINK
                        # VID: .mp4 of What Drone Sees      -> LINK
                        # LAYOUT: .jpg of the system        -> LINK
                        # OPTS:         / ACCEL-DATA / 

                        'ACCEL FIMI': [
                            'a', 
                            'https://drive.google.com/file/d/1UBIq9C9hXVHWmlX53Shb1dI_FK83e5XU/preview', 
                            'https://drive.google.com/file/d/1UBIq9C9hXVHWmlX53Shb1dI_FK83e5XU/preview', 
                            'd'],

                        # ACCEL PORTEUR |
                        #
                        # DATA: .csv folder on Ggl Drive     -> LINK
                        # OUTSIDER VID: .mp4 of What We See  -> LINK
                        # LAYOUT: .jpg of the system        -> LINK
                        # OPTS: / BATTERY / RSSI / ACCEL-DATA / COMPASS / 

                        'ACCEL PORTEUR': [
                            'A', 
                            'https://drive.google.com/file/d/1xwuA-BSdjV0qM0Dv9P3mmf14OgaSeRhz/preview', 
                            'https://drive.google.com/file/d/1WVUky43TWml9K10CJlbQP-vIsZeVrS6O/preview', 
                            'D'],                        


                        'HOVER WITH 3 DRONES': [
                            #name of df     (!!!)
                            '3d1a', 
                            #vid of test    (!!!)
                            'https://drive.google.com/file/d/1eUOmMTest6wYAPVPiXZiqrNDiqo-5Em2/preview', 
                            #(optional) pic
                            '', 
                            #other
                            ''],      

                        'XREALITY_TEST1': [
                            'xr1', 
                            'https://drive.google.com/file/d/1yyKoBrG8ekTLZ1DHeskCvUCruumRcNAa/preview', 
                            '', 
                            #virtual cam...
                            'cam3_xr1'],    

                        'HAND_TEST': [
                            'ht1', 
                            'https://drive.google.com/file/d/19EEnso1FfGfpwT5F_QrqJtgzBWAlYcsm/preview', 
                            '', 
                            ''],    

                        'HAND_DEMO': [
                            'hd1', 
                            'https://drive.google.com/file/d/1FCkTinrghoR7sSgqa2LBetXFaIwZMrIb/preview', 
                            '', 
                            ''],                    
                        })

                                # {'label': 'CHOREOGRAPHY', 'value': 'CHOREOGRAPHY'},
                                # {'label': 'HOVER WITH PUSH', 'value': 'HOVERTEST'},
                                # {'label': 'HOVER WITH 2 DRONES', 'value': '2D1A'},
                                # {'label': 'HOVER WITH 3 DRONES', 'value': '3D1A'},
                                # {'label': 'XREALITY_TEST1', 'value': 'XR1'},
                                # {'label': 'HAND_TEST', 'value': 'HAND_TEST'},
                                # {'label': 'HAND_DEMO', 'value': 'HAND_DEMO'},


## TF
df_chore= pd.read_csv('~/Documents/data/eval_tests/tf_chore.csv')
df_hover= pd.read_csv('~/Documents/data/eval_tests/tf_hover.csv')
df_2d1a= pd.read_csv('~/Documents/data/eval_tests/tf_2d1a.csv')
df_3d1a= pd.read_csv('~/Documents/data/eval_tests/tf_3d1a.csv')
df_xr1= pd.read_csv('~/Documents/data/eval_tests/tf_xr1.csv')

df_ht1= pd.read_csv('~/Documents/data/eval_tests/tf_ht1.csv')
## CAMERA
df_cam3_xr1 = pd.read_csv('~/Documents/data/eval_tests/cam3_xr1.csv')

# df_traj = pd.DataFrame({

#                         'df_chore': [
#                             #x
#                             'field.transforms0.child_frame_id', 
#                             #y
#                             '', 
#                             #z
#                             '', 
#                             ''],
# })

# dict = {'chore': df_chore['field.transforms0.child_frame_id'], 'hover': df_hover['field.transforms0.child_frame_id'], '1': (224,224,3)}
# df = pd.DataFrame({'List_No':[1,15,11],'something':[4,5,2]})
# df['array'] = df['List_No'].apply(lambda x: dict[str(x)])

# #EDIT MAX RANGE BASED ON TRAJ.
# @app.callback(
#     [dash.dependencies.Output('current_df_traj', 'data')],
#     [dash.dependencies.Output('traj-edit-tool', 'min')],
#     [dash.dependencies.Output('traj-edit-tool', 'max')],
#     [dash.dependencies.Input('trajectory-select', 'value')])

# def update_range(category):

#     csv_of_interest = df_dropdown[category][0]
#     #print("CSV CHOSEN:", csv_of_interest)
#     df_traj= pd.read_csv(csv_of_interest)
#     #print(df_traj)
#     traj_range = [1, len(df_traj)]
#     print ("range is", traj_range)
#     print("we obtain: df:", df_traj)

#     #print ("but registered range is", my_range)
#     return , [1], [len(df_traj)]

#EDIT TRAJ GRAPH BASED ON TRAJ
@app.callback(
    dash.dependencies.Output('trajectory', 'figure'),
    dash.dependencies.Output('3d_traj', 'figure'),
    [dash.dependencies.Output('current_df_traj', 'data')],
    dash.dependencies.Output('small-title', 'children'),
    [dash.dependencies.Input('traj-edit-tool', 'value')],
    
    [dash.dependencies.Input('trajectory-select', 'value')],
    [dash.dependencies.State('parameters', 'value')],
    [dash.dependencies.State('current_df_traj', 'data')])
    
def update_figure(traj_range, category, params, cb_trig):
    csv_of_interest = df_dropdown[category][0]
    print("CSV CHOSEN:", csv_of_interest)

    if csv_of_interest == 'df_chore':
        df_traj = df_chore
    if csv_of_interest == 'df_hover':
        df_traj = df_hover
    if csv_of_interest == '2d1a':
        df_traj = df_2d1a
    if csv_of_interest == '3d1a':
        df_traj = df_3d1a
    if csv_of_interest == 'xr1':
        df_traj = df_xr1
    if csv_of_interest == 'ht1':
        df_traj = df_ht1

    # 'XR1': [
    # 'xr1', 
    # 'HAND_TEST': [
    #     'ht1', 
    # 'HAND_DEMO': [
    #     'hd1', 

    #print(df_traj)
    #traj_range = [1, len(df_traj)]

    #adapt .csv to slider range
    print("df:", df_traj)
    print("range is", traj_range, "and len is", len(df_traj))
    # 16638
    min_selected = int(traj_range[0]*len(df_traj)/100000)
    max_selected = int(traj_range[1]*len(df_traj)/100000)
    print(min_selected, max_selected)
    frequency = 237
    duration = (max_selected-min_selected)/frequency

    title_edit = category + '@ ['+str(min_selected)+':'+str(max_selected)+']    | '+str(round(duration, 2))+'s @'+str(frequency)+'Hz |'
    _traj_data = df_traj[min_selected:max_selected]
    print("data:", _traj_data)
    print("done")
    traj_graph = go.Figure()
    #graph as many drones as exists in the newly selected data
    for id in range(6):
        print (id+1) 
        
        drone_traj_x = []
        drone_traj_y = []
        #print(traj_range[1])
        for entry in _traj_data.index:
            #print(entry)
            if _traj_data['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
                drone_traj_x.append(_traj_data['field.transforms0.transform.translation.x'][entry])
                drone_traj_y.append(_traj_data['field.transforms0.transform.translation.y'][entry])

        traj_graph.add_trace(go.Scatter(x=drone_traj_x, y=drone_traj_y,
                            mode='markers',
                            name='drone '+str(id+1)))

    # KEEPING THESE SEPARATE FOR NOW.
    #IDEA FOR PARAM: Display 3D Version. (trig next callback.)
    _3d_traj_graph = go.Figure()

    for id in range(6):
        print (id+1) 

        drone_traj_x = []
        drone_traj_y = []
        drone_traj_z = []
        for entry in _traj_data.index:
            if _traj_data['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
                drone_traj_x.append(_traj_data['field.transforms0.transform.translation.x'][entry])
                drone_traj_y.append(_traj_data['field.transforms0.transform.translation.y'][entry])
                drone_traj_z.append(_traj_data['field.transforms0.transform.translation.z'][entry])

        _3d_traj_graph.add_trace(go.Scatter3d(x=drone_traj_x, y=drone_traj_y, z= drone_traj_z,
                            mode='markers',
                            name='drone '+str(id+1),
                            ),)           
        #PLEASE reduce the marker size. 
        _3d_traj_graph.update_traces(marker=dict(size=1),
                        selector=dict(mode='markers'))
                        
    # IN CASE YOU WANT TO SEE BASE COMMANDS.
    # drone2_offset = [-0.3, -0.01]
    # traj_graph.add_trace(go.Scatter(x=df_chore_cmd['x^0']+drone2_offset[0], y=df_chore_cmd['y^0']+drone2_offset[1],
    #                     mode='markers',
    #                     name='Fo8 '))

    #PARAM: Display Relevant Vid. (trig next callback.)
    if 'CB_LINK' in params:
        cb_trig[0] = 1 # LINKED
    else:
        cb_trig[0] = 0 #'UNLINKED'

    return traj_graph, _3d_traj_graph, cb_trig, title_edit

@app.callback(
    dash.dependencies.Output('external_video', 'src'),
    [dash.dependencies.Input('sensor-select', 'value')],
    [dash.dependencies.Input('current_df_traj', 'data')],
    [dash.dependencies.State('trajectory-select', 'value')])
def update_figure( sensor, cb_trig, traj_select):
    print("chosen sensor:", sensor)
    url_garage = df_dropdown[sensor][1]
    if cb_trig[0] == 1:
        url_garage = df_dropdown[traj_select][1]
    return url_garage

# @app.callback(
#     dash.dependencies.Output('text-div', 'children'),
#     [dash.dependencies.Input('sensor-select', 'value')],
#     [dash.dependencies.Input('current_df_traj', 'data')],
#     [dash.dependencies.State('trajectory-select', 'value')])
# def update_figure( sensor, cb_trig, traj_select):
#     print("chosen sensor:", sensor)
#     url_garage = df_dropdown[sensor][1]
#     if cb_trig == 'LINKED':
#         url_garage = df_dropdown[traj_select][1]
#     return url_garage










if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
