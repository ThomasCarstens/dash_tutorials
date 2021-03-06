#THESIS
# Graph exploration + formatting page.

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import plotly.graph_objects as go
import dash_gif_component as gif
from datetime import date, timedelta
import pandas as pd
import datetime
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
import os
print(os. getcwd())


df_chore= pd.read_csv('~/Documents/data/droneData_alliantech/eval_tests/tf_chore.csv')
front_traj_graph = go.Figure()
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
    traj_graph.update_traces(marker=dict(size=1),
                    selector=dict(mode='markers'))

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
    #txa 30 Nov
    # _3d_traj_graph.update_traces(marker=dict(size=1),
    #                   selector=dict(mode='markers'))

with open("/home/txa/Documents/data/droneData_alliantech/in-vivo/analysis_notes.txt", "r") as f:
    notes = f.readlines()
#html.Br()#

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'dark': True,
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
    'detail': '#007439'
}
dark_layout = go.Layout(
    template= 'plotly_dark',
)

rootLayout = html.Div(style={ 'backgroundColor': colors['background'],}, children=[

                dcc.Store(id='current_df_traj', data = [0,0]), #ensures rangeslider consistent 

                html.Div(className='row', children = [
                    html.Div([
                        html.Div([
                            html.H6(children='CHOREOGRAPHY', id='small-title', style = {'color': colors['text'], 'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                            dcc.RangeSlider(
                                id='traj-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000])
                            ]),

                        html.Div(className='row', children = [
                            html.Div(dcc.Graph(
                                id='trajectory',
                                figure=traj_graph
                            ), className= 'six columns'),

                            html.Div(dcc.Graph(
                                id='front-trajectory',
                                figure=front_traj_graph
                            ), className= 'six columns'),
                        ]),

                    ], className= 'twelve columns'),
                    
                ]),

                html.Div(className='row', children = [

                    html.Div(dcc.Graph(
                        id='3d_traj',
                        figure=_3d_traj_graph,
                        
                    ), className='seven columns'),

 
                    html.Div([
                        html.H5(children='Trajectory Chooser', id='radio-2', style = {'color': colors['text'], 'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        dcc.RadioItems(
                            style = {'color': colors['text']},
                            id='trajectory-select',
                            options=[
                                {'label': 'CHOREOGRAPHY', 'value': 'CHOREOGRAPHY'},
                                {'label': 'CHORE_AND_XR', 'value': 'CHORE_AND_XR'},
                                {'label': 'HAND_COLLISIONS', 'value': 'COLLISIONS'},
                                {'label': 'BOT2BOT_COLLISIONS', 'value': 'BOT2BOT_COLLISIONS'},
                                {'label': 'HOVER WITH PUSH', 'value': 'HOVERTEST'},
                                {'label': 'HOVER WITH 2 DRONES', 'value': '2D1A'},
                                {'label': 'HOVER WITH 3 DRONES', 'value': 'HOVER WITH 3 DRONES'},
                                {'label': 'XREALITY_TEST1', 'value': 'XREALITY_TEST1'},
                                {'label': 'HAND_TEST', 'value': 'HAND_TEST'},

                            ],
                            value='COLLISIONS'),
                    ], className='two columns'),



                    html.Div([
                        html.H5(children='Available videos', id='radio-title', style = {'color': colors['text'],'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                        dcc.RadioItems(
                            style = {'color': colors['text']},
                            id='sensor-select',
                            options=[
                                {'label': 'ACCEL FIMI', 'value': 'ACCEL FIMI'},
                                {'label': 'ACCEL PORTEUR', 'value': 'ACCEL PORTEUR'},
                                {'label': 'CHOREOGRAPHY', 'value': 'CHOREOGRAPHY'},
                                {'label': 'HOVERTEST', 'value': 'HOVERTEST'},
                                {'label': 'HOVER WITH 2 DRONES', 'value': '2D1A'},
                                {'label': 'HOVER WITH 3 DRONES', 'value': 'HOVER WITH 3 DRONES'},
                                {'label': 'XREALITY_TEST1', 'value': 'XREALITY_TEST1'},
                                {'label': 'HAND_DEMO', 'value': 'HAND_DEMO'},
                            ],
                            value='CHOREOGRAPHY'),
                    ], className='two columns'),

                    # FOR IFRAME: see callback with 'parameters'
                    # html.Div([
                    #     html.H5(children='Config Dashboard', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                    #     dcc.Checklist(
                    #         id = 'parameters',
                    #         options=[
                    #             {'label': 'Display Relevant Vid', 'value': 'CB_LINK'},
                    #             {'label': '...', 'value': 'MTL'},
                    #             {'label': 'Show Picture Not Video', 'value': 'PIC'},
                    #             {'label': '...', 'value': 'SF'}
                    #         ],
                    #         value=['MTL'])  

                    # ], className='one columns'),


                ]),
            ])
app.layout = html.Div(id='dark-theme-container', style={ 'backgroundColor': colors['background'],}, children=[
                
                html.H1(children='HIDE TOP', id='hiddentopdiv', style = {'color': colors['background'], 'height': '100px', 'width': '100%', 'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),

                html.Div(id='dark-theme-components', children=[
                    daq.DarkThemeProvider(theme=colors, children=rootLayout)
                ]),
                
                html.H1(children='HIDE BOTTOM', id='hiddendiv', style = {'color': colors['background'], 'height': '1000px', 'width': '100%', 'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),

            ])

#################################### CALLBACK PREP ########################################33

df_dropdown = pd.DataFrame({


                        # CHOREOGRAPHY |
                        #
                        # DATA: .csv folder on Ggl Drive    -> LINK
                        # VID: .mp4 of CHORE                -> LINK
                        # LAYOUT: .jpg of the system        -> LINK
                        # OPTS:         / 2D XY TRAJ. / 

                        'CHOREOGRAPHY': [
                            #tf_chore.csv //ELSE https://drive.google.com/file/d/1x2qqvYr9H7e2I3EXjBfKjJrhaLqA59aA/preview
                            'df_chore', 
                            #Chore Video
                            'https://drive.google.com/file/d/1tDETo4dPgGq81jFtJDxbsVOX12sX_0H2/preview', 
                            #State Machine.
                            'https://drive.google.com/file/d/1Zon_cCdtncfQGMEADcY6j_KMnNAVzX5T/preview', 
                            ''],



                        'CHORE_AND_XR': [
                            #tf_chore.csv //ELSE https://drive.google.com/file/d/1x2qqvYr9H7e2I3EXjBfKjJrhaLqA59aA/preview
                            'df_xrchore', 
                            # VIRTUAL DATA. #/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/1630749025Dragon.txt
                            # /home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/1630749025Ninjask.txt
                            #Chore Video
                            'https://drive.google.com/file/d/1tDETo4dPgGq81jFtJDxbsVOX12sX_0H2/preview', 
                            #State Machine.
                            'https://drive.google.com/file/d/1Zon_cCdtncfQGMEADcY6j_KMnNAVzX5T/preview', 
                            ''],

                        'COLLISIONS': [
                            #tf_chore.csv //ELSE https://drive.google.com/file/d/1x2qqvYr9H7e2I3EXjBfKjJrhaLqA59aA/preview
                            'df_hdi_collisions', 
                            # VIRTUAL DATA. #/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/1630749025Dragon.txt
                            # /home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/1630749025Ninjask.txt
                            #Chore Video
                            'https://drive.google.com/file/d/1tDETo4dPgGq81jFtJDxbsVOX12sX_0H2/preview', 
                            #State Machine.
                            'https://drive.google.com/file/d/1Zon_cCdtncfQGMEADcY6j_KMnNAVzX5T/preview', 
                            ''],

                        'BOT2BOT_COLLISIONS': [
                            #tf_chore.csv //ELSE https://drive.google.com/file/d/1x2qqvYr9H7e2I3EXjBfKjJrhaLqA59aA/preview
                            'df_bot2bot', 
                            # VIRTUAL DATA. #/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/1630749025Dragon.txt
                            # /home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/1630749025Ninjask.txt
                            #Chore Video
                            'https://drive.google.com/file/d/1tDETo4dPgGq81jFtJDxbsVOX12sX_0H2/preview', 
                            #State Machine.
                            'https://drive.google.com/file/d/1Zon_cCdtncfQGMEADcY6j_KMnNAVzX5T/preview', 
                            ''],
                        
                        #txa@zone:/media/txa/94417688-c15e-4b3e-8f47-54f4082d6ab6/home/thomas/huge_rosbag$ rostopic echo -b hdi_2.bag -p /tf >> tf_hdi.csv

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
                            'https://drive.google.com/file/d/1H2B8SR7sN1_LktbV0fOycew8WMFforu2/preview', 
                            #virtual cam...
                            'cam3_xr1'],    

                        'HAND_TEST': [
                            'ht1', 
                            'https://drive.google.com/file/d/19EEnso1FfGfpwT5F_QrqJtgzBWAlYcsm/preview', 
                            'https://drive.google.com/file/d/1XgOdDW7FtxYn9KzCE1J4A7BtdUNFqtnt/preview', 
                            ''],    

                        'HAND_DEMO': [
                            'hd1', 
                            'https://drive.google.com/file/d/1FCkTinrghoR7sSgqa2LBetXFaIwZMrIb/preview', 
                            'https://drive.google.com/file/d/18Sz-dewPpHpTHiwC36bUuhkayXPiOxCk/preview', 
                            ''],                    
                        })

                                # {'label': 'CHOREOGRAPHY', 'value': 'CHOREOGRAPHY'},
                                # {'label': 'HOVER WITH PUSH', 'value': 'HOVERTEST'},
                                # {'label': 'HOVER WITH 2 DRONES', 'value': '2D1A'},
                                # {'label': 'HOVER WITH 3 DRONES', 'value': '3D1A'},
                                # {'label': 'XREALITY_TEST1', 'value': 'XR1'},
                                # {'label': 'HAND_TEST', 'value': 'HAND_TEST'},
                                # {'label': 'HAND_DEMO', 'value': 'HAND_DEMO'},

def convert2df(url):
    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    df = pd.read_csv(path)
    if df.empty:
        print('empty')
    return df
## TF
df_chore= pd.read_csv('~/Documents/data/droneData_alliantech/eval_tests/tf_chore.csv')
df_hover= pd.read_csv('~/Documents/data/droneData_alliantech/eval_tests/tf_hover.csv')
df_2d1a= pd.read_csv('~/Documents/data/droneData_alliantech/eval_tests/tf_2d1a.csv')
df_3d1a= pd.read_csv('~/Documents/data/droneData_alliantech/eval_tests/tf_3d1a.csv')
df_xr1= pd.read_csv('~/Documents/data/droneData_alliantech/eval_tests/tf_xr1.csv')

df_ht1= pd.read_csv('~/Documents/data/droneData_alliantech/eval_tests/tf_ht1.csv')
## CAMERA
url_cam3_xr1 = 'https://drive.google.com/file/d/1nMD1hMEF8oU3a3u71dxpSC-W8x1NmBvW/view?usp=sharing'
url_cam3_xr1 = 'https://drive.google.com/file/d/1GvaVIhLfAs4v_dQsZPFRvw5s5v5cq6xs/view?usp=sharing'
#df_cam3_xr1 = pd.read_csv('~/Documents/data/droneData_alliantech/eval_tests/cam3_xr1.csv')
#df_cam3_xr1 = convert2df(url_cam3_xr1)
url_xrchore = 'https://drive.google.com/file/d/1tDETo4dPgGq81jFtJDxbsVOX12sX_0H2/view?usp=sharing'
url_xrchore = 'https://drive.google.com/file/d/1GvaVIhLfAs4v_dQsZPFRvw5s5v5cq6xs/view?usp=sharing'
output_bot_path = 'https://drive.google.com/file/d/1GvaVIhLfAs4v_dQsZPFRvw5s5v5cq6xs/view?usp=sharing'
#df_xrchore = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/xr_chore.csv')
#df_xrchore = convert2df(url_xrchore)

## DATA INEXISTENT
#df_xr_version = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/demofile2.csv', sep=',')
#print(list(df_xr_version.columns.values))
#df_xr_drone = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/drone_xr_pos.csv', sep=',')

#df_hdi_collisions = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/df_hdi_collisions.csv', sep=',')
# df_hdi2_collisions = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/hdi_2/df_hdi2_collisions.csv', sep=',')

df_hdi_position = pd.read_csv("/home/txa/Documents/data/droneData_alliantech/xr_processing/df_drone_pos.txt", sep=',')
#df_dragon_position = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/df_dragon_position.csv', sep=',')
df_dragon_position = pd.read_csv("/home/txa/Documents/data/droneData_alliantech/xr_processing/df_bot_pos.txt", sep=',')
#df_hdibag_hand = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/tf_hdi.csv')
df_hdibag_hand = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/hdi_2/bag_tf.csv')

#df_bot2bot = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/tf_bot2bot.csv')
# TO BE ADDED


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
    dash.dependencies.Output('front-trajectory', 'figure'),
    [dash.dependencies.Input('traj-edit-tool', 'value')],
    
    [dash.dependencies.Input('trajectory-select', 'value')],
    #[dash.dependencies.Input('parameters', 'value')],
    [dash.dependencies.State('current_df_traj', 'data')])
    
def update_figure(traj_range, category, cb_trig): #params
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
    if csv_of_interest == 'df_xrchore':
        df_traj = df_xrchore
    if csv_of_interest == 'df_hdi_collisions':
        df_traj = df_hdibag_hand
    if csv_of_interest == 'df_bot2bot':
        df_traj = df_bot2bot     

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
    traj_graph = go.Figure(layout = dark_layout)
    front_traj = go.Figure(layout = dark_layout)
    _3d_traj_graph = go.Figure(layout = dark_layout)
    traj_graph.update_layout(
        title="Timeline View",
        title_x=0.5,
        #xaxis_title="",
        #yaxis_title="Gain",
    )
    # front_traj.update_layout(
    #     title="Front View",
    #     title_x=0.5,
    #     #xaxis_title="",
    #     #yaxis_title="Gain",
    # )
    # _3d_traj_graph.update_layout(
    #     title="3D Plot of Flight",
    #     title_x=0.5,
    #     #xaxis_title="",
    #     #yaxis_title="Gain",
    # )
    #graph as many drones as exists in the newly selected data
    for id in range(3):
        print (id+1) 
        if csv_of_interest == 'df_xrchore':
            df_traj = df_xrchore
        min_selected = int(traj_range[0]*len(df_traj)/100000)
        max_selected = int(traj_range[1]*len(df_traj)/100000)
        _traj_data = df_traj[min_selected:max_selected]
        drone_traj_x = []
        drone_traj_y = []
        drone_traj_z = []
        drone_traj_p = []
        drone_traj_r = []
        drone_traj_yaw = []
        drone_timestamp = []
        #print(traj_range[1])
        for entry in _traj_data.index:
            #print(entry)
            if _traj_data['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
                drone_traj_x.append(_traj_data['field.transforms0.transform.translation.x'][entry])
                drone_traj_y.append(_traj_data['field.transforms0.transform.translation.y'][entry])
                drone_traj_z.append(_traj_data['field.transforms0.transform.translation.z'][entry])
                drone_traj_p.append(_traj_data['field.transforms0.transform.rotation.x'][entry])
                drone_traj_r.append(_traj_data['field.transforms0.transform.rotation.y'][entry])
                drone_traj_yaw.append(_traj_data['field.transforms0.transform.rotation.z'][entry])
                drone_timestamp.append(datetime.datetime.fromtimestamp(_traj_data['%time'][entry]/10**9))
        # ## ADD TO GRAPHS.
        if csv_of_interest != 'df_hdi_collisions':
            traj_graph.add_trace(go.Scatter(x=drone_traj_x, y=drone_traj_y,
                            mode='markers',
                            name='drone '+str(id+1)))
        else: #for collision graph
            if id%2==0:
                myname='drone agent'
            else:
                myname='virtual bot'
            traj_graph.add_trace(go.Scatter(x=drone_timestamp, y=drone_traj_z[::],
                            mode='markers',
                            name=myname))        

        traj_graph.update_traces(marker=dict(size=1),
                        selector=dict(mode='markers'))
        # DO NOT HIDE LEGENDS.
        # traj_graph.update_layout(showlegend=False)
        # front_traj.update_layout(showlegend=False)
        # front_traj.add_trace(go.Scatter(x=drone_traj_x, y=drone_traj_z,  #x=drone_traj_x, y=drone_traj_z, 
        #                     mode='markers',
        #                     name='Z: drone '+str(id+1)))

        # front_traj.add_trace(go.Scatter(x=drone_timestamp, y=drone_traj_z,  #x=drone_traj_x, y=drone_traj_z, 
        #                     mode='markers',
        #                     name='Z: drone '+str(id+1)))

        # front_traj.add_trace(go.Scatter(x=drone_timestamp, y=drone_traj_y,  #x=drone_traj_x, y=drone_traj_z, 
        #                     mode='markers',
        #                     name='Y: drone '+str(id+1)))

        # front_traj.add_trace(go.Scatter(x=drone_timestamp, y=drone_traj_yaw,  #x=drone_traj_x, y=drone_traj_z, 
        #                     mode='markers',
        #                     name='YAW: drone '+str(id+1)))
        # front_traj.add_trace(go.Scatter(x=drone_timestamp, y=drone_traj_p,  #x=drone_traj_x, y=drone_traj_z, 
        #                     mode='markers',
        #                     name='PITCH: drone '+str(id+1)))
        # front_traj.add_trace(go.Scatter(x=drone_timestamp, y=drone_traj_r,  #x=drone_traj_x, y=drone_traj_z, 
        #                     mode='markers',
        #                     name='ROLL: drone '+str(id+1)))

        front_traj.update_traces(marker=dict(size=1),
                        selector=dict(mode='markers'))

        _3d_traj_graph.add_trace(go.Scatter3d(x=drone_traj_x, y=drone_traj_y, z= drone_traj_z,
                            mode='markers',
                            marker=dict(size=0.3),
                            name='drone '+str(id+1),
                            ),)           
        #PLEASE reduce the marker size. 
        # _3d_traj_graph.update_traces(marker=dict(size=0.3),
        #                 selector=dict(mode='markers'))

        ########################################
        ###########################################################
    drone_xr_x = []
    drone_xr_y = []
    drone_xr_z = []
    if csv_of_interest == 'df_xrchore':
        df_traj = df_xr_drone[50::]
        min_selected = int(traj_range[0]*len(df_traj)/100000)
        max_selected = int(traj_range[1]*len(df_traj)/100000)
        _traj_data = df_traj[min_selected:max_selected:]

        quotient = 3
        for entry in _traj_data.index:
            drone_xr_x.append(_traj_data[' x'][entry]/quotient)
            drone_xr_y.append(_traj_data[' z'][entry]/quotient)
            drone_xr_z.append(_traj_data[' y'][entry]/quotient)

            #print(drone_xr_x)

        traj_graph.add_trace(go.Scatter(x=drone_xr_x, y=drone_xr_y,
                            mode='lines',
                            name='XR drone 3'))

        front_traj.add_trace(go.Scatter(x=drone_xr_x, y=drone_xr_z,
                            mode='lines',
                            name='XR drone 3'))
        _3d_traj_graph.add_trace(go.Scatter3d(x=drone_xr_x, y=drone_xr_y, z= drone_xr_z,
                            mode='lines',
                            name='XR drone 3',
                            
                            ),)   
        # traj_graph.update_layout(showlegend=False)
        # front_traj.update_layout(showlegend=False)   
        # _3d_traj_graph.update_traces(marker=dict(size=0.3),
        #                 selector=dict(mode='lines'))
        _3d_traj_graph.update_xaxes(range=(-0.52, 0.52))
        _3d_traj_graph.update_yaxes(range=(-0.52, 0.52))
    drone_xr_x = []
    drone_xr_y = []
    drone_xr_z = []
    if csv_of_interest == 'df_xrchore':
        df_traj = df_xr_version[50::]
        min_selected = int(traj_range[0]*len(df_traj)/100000)
        max_selected = int(traj_range[1]*len(df_traj)/100000)
        _traj_data = df_traj[min_selected:max_selected:]

        quotient = 3
        for entry in _traj_data.index:
            drone_xr_x.append(_traj_data[' x'][entry]/quotient)
            drone_xr_y.append(_traj_data[' z'][entry]/quotient)
            drone_xr_z.append(_traj_data[' y'][entry]/quotient)

            #print(drone_xr_x)

        traj_graph.add_trace(go.Scatter(x=drone_xr_x, y=drone_xr_y,
                            mode='lines',
                            name='XR drone 4'))
        front_traj.add_trace(go.Scatter(x=drone_xr_x, y=drone_xr_z,
                            mode='lines',
                            name='XR drone 4'))
        _3d_traj_graph.add_trace(go.Scatter3d(x=drone_xr_x, y=drone_xr_y, z= drone_xr_z,
                            mode='lines',
                            marker=dict(size=0.1),
                            name='XR drone 4',
                            ),)   
        # traj_graph.update_layout(showlegend=False)
        # front_traj.update_layout(showlegend=False)   
        # _3d_traj_graph.update_traces(marker=dict(size=0.3),
        #                 selector=dict(mode='lines'))

        ###########################################


    # if csv_of_interest == 'df_hdi_collisions':
    #     traj_graph = go.Figure(layout = dark_layout)
    #     front_traj = go.Figure(layout = dark_layout)
    #     _3d_traj_graph = go.Figure(layout = dark_layout)
    #     traj_graph.update_layout(
    #         title="Top View",
    #         title_x=0.5,
    #         #xaxis_title="",
    #         #yaxis_title="Gain",
    #     )
    #     front_traj.update_layout(
    #         title="Front View",
    #         title_x=0.5,
    #         #xaxis_title="",
    #         #yaxis_title="Gain",
    #     )
    #     _3d_traj_graph.update_layout(
    #         title="3D Plot of Flight",
    #         title_x=0.5,
    #         #xaxis_title="",
    #         #yaxis_title="Gain",
    #     )
        # df_traj = df_hdi_position[::]
    
        # drone_xr_x = []
        # drone_xr_y = []
        # drone_xr_z = []
        # time_xr = []
        # min_selected = int(traj_range[0]*len(df_traj)/100000)
        # max_selected = int(traj_range[1]*len(df_traj)/100000)
        # _traj_data = df_traj[min_selected:max_selected:]

        # quotient = 3
        # for entry in _traj_data.index:
        #     drone_xr_x.append(_traj_data[' x'][entry]/quotient)
        #     drone_xr_y.append(_traj_data[' z'][entry]/quotient)
        #     drone_xr_z.append(_traj_data[' y'][entry]/quotient)
        #     time_xr.append(_traj_data['time'][entry])

        #     #print(drone_xr_x)

        # traj_graph.add_trace(go.Scatter(x=time_xr, y=drone_xr_y,
        #                     mode='markers',
        #                     name='XR poses'))
        # front_traj.add_trace(go.Scatter(x=drone_xr_x, y=drone_xr_z,
        #                     mode='markers',
        #                     name='XR poses'))
        # _3d_traj_graph.add_trace(go.Scatter3d(x=drone_xr_x, y=drone_xr_y, z= drone_xr_z,
        #                     mode='markers',
        #                     name='XR poses',
        #                     ),)   
        # traj_graph.update_layout(showlegend=False)
        # front_traj.update_layout(showlegend=False)   
        # _3d_traj_graph.update_traces(marker=dict(size=0.3),
        #                 selector=dict(mode='markers'))

    if csv_of_interest == 'df_hdi_collisions':

        #VIRTUAL: 3 GRAPHS: DRONE, HAND AND COLLISIONS
        #REAL: 3 GRAPHS: DRONE, HAND AND COLLISIONS.
        start_point = 4000
        print(len(df_hdi_position))
        for df_traj in [df_hdi_position[start_point::]]:#, df_dragon_position[start_point::], df_hdi2_collisions[::], df_hdi_collisions[::]]:
            drone_xr_x = []
            drone_xr_y = []
            drone_xr_z = []
            time_xr = []
            time_timestamps = []
            min_selected = int(traj_range[0]*len(df_traj)/100000)
            max_selected = int(traj_range[1]*len(df_traj)/100000)
            _traj_data = df_traj[min_selected:max_selected:]

            quotient = 3
            for entry in _traj_data.index:
                drone_xr_x.append(_traj_data[' x'][entry]/quotient)
                drone_xr_y.append(_traj_data[' z'][entry]/quotient)
                drone_xr_z.append(_traj_data[' y'][entry]/quotient)
                # time_xr = [datetime.datetime.fromtimestamp(element / 10**9) for element in _traj_data['time']]
                time_xr.append(datetime.datetime.fromtimestamp(1630745292)#1630745595#1630745390#1630745185
                                    +1.74*datetime.timedelta(seconds = _traj_data['time'][entry]))
                time_timestamps.append(_traj_data['time'][entry]) #initial at: 1630745292+
            # REMOVE ALL MENTION OF COLLISIONS ####
            # Choose custom size for collisions.
            # collision_from_vr = (drone_xr_x[0]*quotient == df_hdi_collisions[' x'][min_selected:max_selected:][0])
            # collision_from_monitor = (drone_xr_x[0]*quotient == df_hdi2_collisions[' x'][min_selected:max_selected:][0])
            # collision_data_selected = (collision_from_vr) or (collision_from_monitor)

            # if collision_from_monitor:
            #     title = 'trajectory execution'
            #     colorchoice = 'yellow'
            #     drone_xr_x = [element * quotient for element in drone_xr_x]
            #     new_drone_xr_y = [element * quotient for element in drone_xr_z] #unity coordinates different
            #     drone_xr_z = [element * quotient for element in drone_xr_y]
            #     drone_xr_y = new_drone_xr_y
            #     time_xr = [datetime.datetime.fromtimestamp(element / 10**9) for element in _traj_data['time']]

            # if collision_from_vr:
            #     title = 'collision detection'
            #     colorchoice = 'red'
            #     for entry in _traj_data.index:
            #         time_xr.append(datetime.datetime.fromtimestamp(1630745389)
            #         +datetime.timedelta(seconds = 1.5* _traj_data['time'][entry])
            #         +datetime.timedelta(seconds =-10.30))

            #     #1630745389
            #     #60* datetime.datetime.fromtimestamp(element // 10**9).minute
            # if collision_data_selected:
            #     print('detected')
            # traj_graph.add_trace(go.Scatter(x=time_xr, y=drone_xr_z,
            #                     mode='markers',
            #                     #name='title', 
            #                     marker=dict(size=10),
            #                     ))
            delays = []
            delays_time = []
            print(drone_traj_z)

            lower_bound = -13000 #start of analysis.
            #lower_bound = -1000
            for count_ros, ros_z in enumerate(drone_traj_z[lower_bound:]):
                if count_ros % 1000 == 0:
                    print(count_ros, '/', len(drone_traj_z[lower_bound:]))
                # if count_ros>5000:
                #     break
                for count, same_z in enumerate(drone_xr_z):
                    
                    if round(ros_z, 6) == round(same_z, 6):
                        time_delay = abs(time_xr[count] - drone_timestamp[lower_bound:][count_ros])
                        delays.append(time_delay.total_seconds())
                        delays_time.append(drone_timestamp[lower_bound:][count_ros])
                        break

            print(delays)

            df_smlatency = pd.DataFrame({
                                        'delays_time': (delays_time), # revert to timestamps. Mpl might have tools to read it
                                        'delays': (delays),
                                        })

            df_smvisual = pd.DataFrame({
                                        'sim_time': (time_timestamps)[lower_bound:],
                                        'x': (drone_xr_x)[lower_bound:], #lower bound useless here I reckon.
                                        'y': (drone_xr_y)[lower_bound:],
                                        'z': (drone_xr_z)[lower_bound:],
                                        # SUPERPOSITION REQUIRES NEW APPROACH.
                                        # 'xD': (drone_traj_x)[lower_bound:], 
                                        # 'yD': (drone_traj_y)[lower_bound:],
                                        # 'zD': (drone_traj_z)[lower_bound:],
                                        })
            # SAVED !
            # df_smlatency.to_csv("sensor_performance/smlatency.csv", index=False)
            df_smvisual.to_csv("sensor_performance/df_smvisual.csv", index=False)


            traj_graph.add_trace(go.Scatter(x=time_xr, y=drone_xr_z,
                                mode='markers',
                                #name=title,
                            
                                marker=dict(size=2),
                                ))
            front_traj.add_trace(go.Scatter(x=delays_time, y=delays ,
                                mode='markers',
                                #name=title,
                            
                                marker=dict(size=2),
                                ))
            _3d_traj_graph.add_trace(go.Scatter3d(x=drone_xr_x, y=drone_xr_y, z= drone_xr_z,
                                mode='markers',
                                marker=dict(size=2),
                                name = 'Simulator logs',
                                #name=title,
                                ),)
            # DELETE FOR NOW                     
            # else:
            #     traj_graph.add_trace(go.Scatter(x=time_xr, y=drone_xr_z,
            #                         mode='markers',
            #                         name='XR collisions', 
            #                         marker=dict(size=2),
            #                         ))
                                    
            #     front_traj.add_trace(go.Scatter(x=drone_xr_x, y=drone_xr_z,
            #                         mode='markers',
            #                         name='XR collisions',
            #                         marker=dict(size=2),
            #                         ))
            #     _3d_traj_graph.add_trace(go.Scatter3d(x=drone_xr_x, y=drone_xr_y, z= drone_xr_z,
            #                         mode='markers',
            #                         name='XR collisions',
            #                         ),)


        # traj_graph.update_layout(showlegend=False)
        # front_traj.update_layout(showlegend=False)   
        start_time = datetime.datetime.fromtimestamp(1630745389)
        time_move = datetime.timedelta(minutes = 10, seconds = 0)
        time_stop = datetime.timedelta(minutes = 12, seconds = 0)
        # traj_graph.update_xaxes(range=(start_time + time_move, start_time + time_stop))
        # traj_graph.update_yaxes(range=(0.0, 1.0))
        # txa edit 20 Nov
        # _3d_traj_graph.update_traces(marker=dict(size=0.5),
        #                 selector=dict(mode='markers'))
    # KEEPING THESE SEPARATE FOR NOW.
    #IDEA FOR PARAM: Display 3D Version. (trig next callback.)
    # _3d_traj_graph = go.Figure()

    # for id in range(6):
    #     print (id+1) 

    #     drone_traj_x = []
    #     drone_traj_y = []
    #     drone_traj_z = []
    #     for entry in _traj_data.index:
    #         if _traj_data['field.transforms0.child_frame_id'][entry] == 'cf'+str(id+1):
    #             drone_traj_x.append(_traj_data['field.transforms0.transform.translation.x'][entry])
    #             drone_traj_y.append(_traj_data['field.transforms0.transform.translation.y'][entry])
    #             drone_traj_z.append(_traj_data['field.transforms0.transform.translation.z'][entry])


                        
    # IN CASE YOU WANT TO SEE BASE COMMANDS.
    # drone2_offset = [-0.3, -0.01]
    # traj_graph.add_trace(go.Scatter(x=df_chore_cmd['x^0']+drone2_offset[0], y=df_chore_cmd['y^0']+drone2_offset[1],
    #                     mode='markers',
    #                     name='Fo8 '))

    #PARAM: Display Relevant Vid. (trig next callback.)
    # if 'CB_LINK' in params:
    #     cb_trig[0] = 1 # LINKED
    # else:
    #     cb_trig[0] = 0 #'UNLINKED'

    # if 'PIC' in params:
    #     cb_trig[1] = 1 # LINKED
    # else:
    #     cb_trig[1] = 0 #'UNLINKED'
    _3d_traj_graph.update_xaxes(range=(-0.52, 0.52))
    _3d_traj_graph.update_yaxes(range=(-0.52, 0.52))
    return traj_graph, _3d_traj_graph, cb_trig, title_edit, front_traj

## IFRAME
# @app.callback(
#     dash.dependencies.Output('external_video', 'src'),
#     [dash.dependencies.Input('sensor-select', 'value')],
#     [dash.dependencies.Input('current_df_traj', 'data')],
#     [dash.dependencies.State('trajectory-select', 'value')])
# def update_figure( sensor, cb_trig, traj_select):
#     print("chosen sensor:", sensor)
#     print(cb_trig)
#     url_garage = df_dropdown[sensor][1]
#     if cb_trig[0] == 1:
#         url_garage = df_dropdown[traj_select][1]
#     if cb_trig[1] == 1:
#         url_garage = df_dropdown[sensor][2]
#     return url_garage

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
