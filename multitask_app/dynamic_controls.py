
import sys
print(sys.executable)
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_gif_component as gif

#import dash_bootstrap_components as dbc
from datetime import date, timedelta

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

import numpy as np
import pandas as pd

# #RETRIEVE
# adc_water_log = pd.read_csv("11_09_32_adc_report_0.csv")
# params = list(adc_water_log)
# print(adc_water_log)
# max_length = len(adc_water_log)
# print(params, max_length)
# print(adc_water_log['timestamp'])

# INITIALIZE: empty GAUGE trace
fig = go.Figure()
fig.add_trace(go.Indicator(
    mode = "gauge+number+delta",
    value = 0,
    #customdata=[200],
    #delta = {'reference': 100},
    gauge = {
        'axis': {'visible': False},
        'bar' : {'color' : 'grey'}},
    title = {'text': "+"},
    domain = {'x': [0,0.4], 'y': [0,1]}
    ))

# # INITIALIZE: empty SCATTERPLOT trace
scat = go.Figure()

scat2 = go.Figure()

# # Add traces
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[0]'],
#                     mode='lines+markers',
#                     name='channel0'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[1]'],
#                     mode='lines+markers',
#                     name='channel1'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[2]'],
#                     mode='lines+markers',
#                     name='channel2'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[3]'],
#                     mode='lines+markers',
#                     name='channel3'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[4]'],
#                     mode='lines+markers',
#                     name='channel4'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[5]'],
#                     mode='lines+markers',
#                     name='channel5'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[6]'],
#                     mode='lines+markers',
#                     name='channel6'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[7]'],
#                     mode='lines+markers',
#                     name='channel7'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[8]'],
#                     mode='lines+markers',
#                     name='channel8'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[9]'],
#                     mode='lines+markers',
#                     name='channel9'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[10]'],
#                     mode='lines+markers',
#                     name='channel10'))
# scat.add_trace(go.Scatter(x=adc_water_log['timestamp'], y=adc_water_log['raw_data[11]'],
#                     mode='lines+markers',
#                     name='channel11'))

#scat.update_layout(clickmode='event+select') #election data also accumulates (or un-accumulates) 
                                              # selected data if you hold down the shift
                                              # button while clicking.
                                              
# INITIALIZE: tabular layout
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

#df_weekAdvance=pd.read_csv('~/Documents/DashBeginnerTutorials/db_Week_advancement.csv')


DYNAMIC_CONTROLS = {
            'see-database': html.Div(children=[
                    html.H4(children='Logs'),
                    
                    #generate_table(df_weekAdvance)
                ]),

            'edit-timers': html.Div([

                html.Div(dcc.Dropdown(
                    id = 'top-dropdown',
                    options=[
                        {'label': 'Week_advancement', 'value': 'Week_advancement'},
                        {'label': 'Dedicated_time', 'value': 'Dedicated_time'},
                        {'label': 'Followups', 'value': 'Followups'},
                        {'label': 'Upcoming_events', 'value': 'Upcoming_events'}
                    ],
                    value='Week_advancement'
                )),

                html.Div(className='row', children=[
                    html.Div([dcc.Dropdown(
                        id = 'sub-dropdown',
                        options=[
                            {'label': 'Memo Topics', 'value': 'MT'},
                            {'label': 'Crypto Earnings', 'value': 'CE'},
                            {'label': 'Radar Usefulness', 'value': 'RU'},
                            {'label': 'IMU Usefulness', 'value': 'IU'},
                            {'label': 'Papers replicated', 'value': 'PR'},
                            {'label': 'Hackathons', 'value': 'Hackathons'},
                            {'label': 'Published Content', 'value': 'PC'}
                        ],
                        value='PR'
                    )], className='three columns'),

                    html.Div([
                        (dcc.Input(id='title-box', type='text', value='Activity')),
                        ], className='three columns'),

                    html.Div([
                        (dcc.Input(id='input-box', type='number', value=0)),
                        ], className='three columns'),

                ]),
                #html.Div(dcc.Input(id='input-box', type='number', value=0)),
                html.Div(className='row', children=[
                    html.Button('Edit', id='button'),
                    html.Button('Add Graph', id='add-button'),
                ]),
                html.Div(id='output-container-button',
                        children='Enter a value and press submit'),
                        




            ]),


            'timer-graphs': html.Div([
                html.H3(children='Multitasker App', id='big-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

                #html.Div([
                # html.H1(["Example heading", dbc.Badge("New", className="ml-1")]),
                # dbc.Row(
                #     [
                #         dbc.Col(
                #             dbc.Row(
                #                 html.H3("Criteria"),
                #                 dbc.Col(graph1, width = 6
                #                 ),

                #                 dbc.Col(graph2, width = 6
                #                 ),
                #             ),
                #         ),
                #         dbc.Col(
                #             html.Div("One of three columns")),
                #         dbc.Col(
                #             html.Div("One of three columns")),
                #     ],
                #     no_gutters=True,
                # ), 
                # #]),

                html.Div(className='row', children=[

                    html.Div([
                        html.H3('Success Rate', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                        (dcc.Dropdown(
                            id = 'open1-dropdown',
                            options=[
                                {'label': 'No graphs yet!', 'value': 'No graphs yet!'},
                            ],
                            placeholder="Graph to Mark Off",
                        )),
                        html.Div(className='row', style={"margin-bottom": "30px"}, children=[
                            #html.Div(className='row', children=[
                            html.Div([html.Button("➕", id="open1")], style = {'width': '5%', 'display': 'inline-flex', 'align-items': 'left', 'justify-content': 'left'}),  
                            #html.Div([html.Button("➕", id="open2")], style = {'width': '50%', 'display': 'inline-flex', 'align-items': 'right', 'justify-content': 'right'}),  
                            #]),
                            #html.Div([html.Button("☰", id="edit1")], style = {'width': '50%', 'display': 'inline-flex', 'align-items': 'left', 'justify-content': 'left'}),  
                            html.Div([html.Button('Tick', id='mark-done')], style = {'width': '80%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 
                            html.Div([html.Button("Remove", id="open1-mark-remove")], style = {'width': '5%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}),  

                        ]),


                        dcc.Graph(figure=fig, id="graph1"),
                        dcc.Graph(figure=fig, id="graph2"),
                        # html.Div([
                        #     #html.Div([        
                        #     dcc.Graph(figure=fig, id="graph1"),# style={'display': 'inline-block'}),
                        #             #dcc.Graph(className='two columns', figure=fig, id="graph2", style={'display': 'inline-block'})
                        #     #], className='seven columns'),

                        #             #dcc.Graph(figure=fig, id="graph1", style={'display': 'inline-block'}),
                        #     #html.Div([   
                        #     dcc.Graph(figure=fig, id="graph2"),# style={'display': 'inline-block'})
                        #     #], className='seven columns'),

                        #     # html.Div([   
                        #     # dcc.Graph(figure=fig, id="graph3"),# style={'display': 'inline-block'})
                        #     # ], className='six columns'),
                        # ]),



                    ], className='four columns'),
                    # html.Div([
                    #     dcc.Graph(figure=fig,
                    #     id='criteria-indicator', 
                    #     ),
                    # ], className='four columns'),

                    # html.Div([
                    #     dcc.Graph(figure=fig,
                    #     id='criteria-indicator-02', 
                    #     ),
                    # ], className='six columns'),

                    # ]),

                    html.Div([                        

                        

                        html.H3(date.today(), style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

                        dcc.Dropdown(
                            id = 'priorities-dropdown',
                            options=[
                                {'label': 'NEXT UP', 'value': 'NEXT UP'},
                                {'label': 'HOY', 'value': 'HOY'},
                                {'label': 'ROUTINE', 'value': 'ROUTINE'},
                                {'label': 'WORK', 'value': 'WORK'},
                                {'label': 'LOGS', 'value': 'LOGS'},
                                {'label': 'USAGE TIPS', 'value': 'USAGE TIPS'},
                            ],
                            value='USAGE TIPS'
                        ),

                        dcc.Graph(figure=fig,
                        id='speed-indicator', 
                        ),
                        html.Div([html.Button("Save", id="save")], style = {'width': '100%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center', "margin-bottom": "60px"}),  
                         
                        gif.GifPlayer(
                            gif='assets/hack_time.gif',
                            still='assets/Rakotz.jpg',
                        ),


                    ], className='four columns'),
    
                    html.Div([
                        html.H3('Countdowns', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
                        (dcc.Dropdown(
                            id = 'open2-dropdown',
                            options=[
                                {'label': 'No graphs yet!', 'value': 'No graphs yet!'},
                            ],
                            placeholder="Graph to Mark Off",
                        )),
                        html.Div(className='row', style={"margin-bottom": "30px"}, children=[
                            html.Div([html.Button("➕", id="open2-add1")], style = {'width': '5%', 'display': 'inline-flex', 'align-items': 'left', 'justify-content': 'left'}),  
                            html.Div([html.Button('Complete', id='open2-mark-done')], style = {'width': '80%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}), 
                            html.Div([html.Button("Remove", id="open2-mark-remove")], style = {'width': '5%', 'display': 'inline-flex', 'align-items': 'center', 'justify-content': 'center'}),  

                        ]),
                        
                        dcc.Graph(figure=fig,
                        id='next-indicator', 
                        ),
                        # html.Div([dcc.Graph(figure=fig,
                        # id='deadline-figaro',
                        # )], style={'display': 'inline-block'}),
                        html.Div([dcc.Graph(figure=fig,
                        id='deadline-fig2',
                        )])
                    ], className='four columns'),

                    html.Div( className = "calendar-view", children = [
                    html.Iframe(src="https://calendar.google.com/calendar/embed?src=thomaxarstens%40gmail.com&ctz=Africa%2FJohannesburg", 
                            #style="border: 0" width="800" height="600" frameborder="0" scrolling="no"
                            style={"width":"100%", "border-width":"0", "frameborder": "0", "scrolling":"no"}),
                    ])

                    # <blockquote class="trello-board-compact">
                    #     <a href="{url to board}">Trello Board</a>
                    #     </blockquote>
                    #     <script src="https://p.trellocdn.com/embed.min.js"></script>
                    
                    #html.Button('Edit', id='button'),
                ]),
            ]),
            #### OPEN1: SUCCESS RATE POP UP ###   #############
            'open1-window': html.Div([  # modal div
         
            html.Div([  # content div
                html.Div(className='row', children=[
                    html.Div([


                        html.Div('Graph to EDIT'),
                        
                        

                        html.Div(className='row', children=[
                            html.Div([
                                (dcc.Input(id='open1-name', type='text', placeholder="Edit Title",)),
                                ], className='two columns'),

                            html.Div([
                                (dcc.Input(id='open1-current', type='number', placeholder="Current Value",)),
                                ], className='two columns'),

                            html.Div([
                                (dcc.Input(id='open1-max', type='number', placeholder="Max Range",)),
                                ], className='two columns'),
                        ]),

                        html.Button('Edit', id='open1-edit'),
                        html.Button('Remove', id='open1-remove'),
                    ], className='six columns'),

                    
            #]),

                    html.Div([

                        # html.Div(dcc.Dropdown(
                        #     id = 'top-dropdown',
                        #     options=[
                        #         {'label': 'Week_advancement', 'value': 'Week_advancement'},
                        #         {'label': 'Dedicated_time', 'value': 'Dedicated_time'},
                        #         {'label': 'Followups', 'value': 'Followups'},
                        #         {'label': 'Upcoming_events', 'value': 'Upcoming_events'}
                        #     ],
                        #     value='Week_advancement'
                        # )),
                        # html.Div('Either add a Countdown timer...'),
                        # html.Div(className='row', children=[
                        #     html.Div([(dcc.Input(id='countdown-name', type='text', placeholder="Edit Title",)),
                        #     ], className='two columns'),

                        #     html.Div([dcc.DatePickerRange(
                        #         id='open1-date',
                        #         min_date_allowed=date(1995, 8, 5),
                        #         max_date_allowed=date(2022, 9, 19),
                        #         initial_visible_month=date.today(),
                        #         start_date = date.today(),
                        #         end_date=date.today() + timedelta(days=1)

                        #     )], className='six columns'),

                        #     html.Div([(dcc.Input(id='open1-time', type='text', placeholder="HH:MM")),
                        #         ], className='two columns'),
                        # ]),
                        

                        # html.Div(className='row', children=[
                        #     #html.Button('Edit', id='button'),
                        #     html.Button('Add Graph', id='add1'),
                        # ]),

                        html.Div('Or you can add a SuccessRate graph...'),  

                        html.Div(className='row', children=[
                            html.Div((dcc.Dropdown(
                                placeholder="I wish to complete this every...",
                                id = 'open1-success-interval',
                                options=[
                                    {'label': 'halfday', 'value': 'halfday'},
                                    {'label': 'day', 'value': 'day'},
                                    {'label': 'week', 'value': 'week'},
                                ],
                                #value='day'
                            )), className='six columns'),

                            html.Div([dcc.Dropdown(
                                    id = 'progress-dropdown',
                                    options=[
                                        {'label': 'halfday', 'value': 'halfday'},
                                        {'label': 'day', 'value': 'day'},
                                        {'label': 'week', 'value': 'week'},
                                    ],
                                    placeholder="Rate my progress every...",
                                )], className='six columns' ),
                        ]),
                        #html.Div(dcc.Input(id='input-box', type='number', value=0)),

                        html.Div(className='row', children=[
                            html.Div([
                                (dcc.Input(id='open1-rate-name', type='text', placeholder="Edit Title",)),
                                ], className='two columns'),

                            html.Div([
                                (dcc.Input(id='open1-add-current', type='number', placeholder="Current Value",)),
                                ], className='two columns'),

                            html.Div([
                                (dcc.Input(id='open1-add-max', type='number', placeholder="Max Range",)),
                                ], className='two columns'),
                        ]),
                        html.Div(className='row', children=[
                            #html.Button('Edit', id='button'),
                            html.Button('Add Graph', id='add2'),
                        ]),
                    ], className='six columns'),
            ]),
                html.Hr(),
                html.Button('Close', id='open1-modal-close-button')
            ],
                style={'textAlign': 'center', },
                className='modal-content',
            ),
        ],
            id='open1-modal',
            className='modal',
            style={"display": "none"},
        ),

            #### OPEN2: SUCCESS RATE POP UP ###   #############
            'open2-window': html.Div([  # modal div
         
            html.Div([  # content div
                html.Div(className='row', children=[
                    html.Div([


                        html.Div('Graph to EDIT'),
                        
                        

                        html.Div(className='row', children=[
                            html.Div([
                                (dcc.Input(id='open1-name', type='text', placeholder="Edit Title",)),
                                ], className='two columns'),

                            html.Div([
                                (dcc.Input(id='open1-current', type='number', placeholder="Current Value",)),
                                ], className='two columns'),

                            html.Div([
                                (dcc.Input(id='open1-max', type='number', placeholder="Max Range",)),
                                ], className='two columns'),
                        ]),

                        html.Button('Edit', id='open1-edit'),
                        html.Button('Remove', id='open1-remove'),
                    ], className='six columns'),

                    
            #]),

                    html.Div([

                        # html.Div(dcc.Dropdown(
                        #     id = 'top-dropdown',
                        #     options=[
                        #         {'label': 'Week_advancement', 'value': 'Week_advancement'},
                        #         {'label': 'Dedicated_time', 'value': 'Dedicated_time'},
                        #         {'label': 'Followups', 'value': 'Followups'},
                        #         {'label': 'Upcoming_events', 'value': 'Upcoming_events'}
                        #     ],
                        #     value='Week_advancement'
                        # )),
                        html.Div('Either add a Countdown timer...'),
                        html.Div(className='row', children=[
                            html.Div([(dcc.Input(id='countdown-name', type='text', placeholder="Edit Title",)),
                            ], className='two columns'),

                            html.Div([dcc.DatePickerRange(
                                id='open2-date',
                                min_date_allowed=date(1995, 8, 5),
                                max_date_allowed=date(2022, 9, 19),
                                initial_visible_month=date.today(),
                                start_date = date.today(),
                                end_date=date.today() + timedelta(days=1)

                            )], className='six columns'),

                            html.Div([(dcc.Input(id='open2-time', type='text', placeholder="HH:MM")),
                                ], className='two columns'),
                        ]),
                        

                        html.Div(className='row', children=[
                            #(dcc.Input(id='open2-category', type='text', placeholder="HH:MM")),
                            html.Div([dcc.Dropdown(
                                    id = 'open2-category',
                                    options=[
                                        {'label': 'Work', 'value': 1},
                                        {'label': 'Crypto', 'value': 2},
                                        {'label': 'DroneLab', 'value': 3},
                                        {'label': 'Kickstarter', 'value': 4},
                                        {'label': 'Masters', 'value': 5},
                                        {'label': 'Employment', 'value': 6},
                                        {'label': 'Budget', 'value': 7},
                                        {'label': 'Hackathon', 'value': 8},
                                        {'label': 'Health', 'value': 9},

                                    ],
                                    placeholder="Optional Category for Viewing",
                                )], className='four columns' ),
                            #html.Button('Edit', id='button'),
                            html.Button('Add Graph', id='add1-countdown'),
                        ]),

                        # html.Div('Or you can add a SuccessRate graph...'),  

                        # html.Div(className='row', children=[
                        #     html.Div((dcc.Dropdown(
                        #         placeholder="I wish to complete this every...",
                        #         id = 'open1-success-interval',
                        #         options=[
                        #             {'label': 'halfday', 'value': 'halfday'},
                        #             {'label': 'day', 'value': 'day'},
                        #             {'label': 'week', 'value': 'week'},
                        #         ],
                        #         #value='day'
                        #     )), className='six columns'),

                        #     html.Div([dcc.Dropdown(
                        #             id = 'progress-dropdown',
                        #             options=[
                        #                 {'label': 'halfday', 'value': 'halfday'},
                        #                 {'label': 'day', 'value': 'day'},
                        #                 {'label': 'week', 'value': 'week'},
                        #             ],
                        #             placeholder="Rate my progress every...",
                        #         )], className='six columns' ),
                        # ]),
                        # #html.Div(dcc.Input(id='input-box', type='number', value=0)),

                        # html.Div(className='row', children=[
                        #     html.Div([
                        #         (dcc.Input(id='open1-rate-name', type='text', placeholder="Edit Title",)),
                        #         ], className='two columns'),

                        #     html.Div([
                        #         (dcc.Input(id='open1-add-current', type='number', placeholder="Current Value",)),
                        #         ], className='two columns'),

                        #     html.Div([
                        #         (dcc.Input(id='open1-add-max', type='number', placeholder="Max Range",)),
                        #         ], className='two columns'),
                        # ]),
                        # html.Div(className='row', children=[
                        #     #html.Button('Edit', id='button'),
                        #     html.Button('Add Graph', id='add22'),
                        # ]),
                    ], className='six columns'),
            ]),
                html.Hr(),
                html.Button('Close', id='open2-modal-close-button')
            ],
                style={'textAlign': 'center', },
                className='modal-content',
            ),
        ],
            id='open2-modal',
            className='modal',
            style={"display": "none"},
        ),
           #### EDIT1: SUCCESS RATE EDIT ###   #############
            'edit1-window': html.Div([  # modal div
         
            html.Div([  # content div
                html.Div(className='row', children=[
                    html.Div([


                        html.Div('Graph TYPE'),
                    
                        dcc.RadioItems(
                            id='graph-type',
                            options=[
                                {'label': 'Countdown', 'value': 'Countdown'},
                                {'label': 'SuccessRate', 'value': 'SuccessRate'},
                            ],
                            value='Countdown'
                        ), 

                        html.Div('Graph to ADD'),
                        #html.Div(className='row', children=[
                            (dcc.Input(id='new-title', type='text', placeholder="Name")),
                            (dcc.Dropdown(
                                placeholder="I wish to complete this every...",
                                id = 'new-success-interval',
                                options=[
                                    {'label': 'halfday', 'value': 'halfday'},
                                    {'label': 'day', 'value': 'day'},
                                    {'label': 'week', 'value': 'week'},
                                ],
                                #value='day'
                            )),
                        #]),
                        dcc.DatePickerRange(
                            id='dd-deadline',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2022, 9, 19),
                            initial_visible_month=date.today(),
                            start_date = date.today(),
                            end_date=date.today() + timedelta(days=1)

                        ),
                        (dcc.Input(id='new-deadline', type='text', placeholder="HH:MM")),
                        #(dcc.Input(id='new-success-interval', type='text', value="Title:")),


                        html.Div('Graph to EDIT'),
                        (dcc.Dropdown(
                            id = 'new-dropdown',
                            options=[
                                {'label': 'Choice1', 'value': 'Choice1'},
                                {'label': 'Choice2', 'value': 'Choice2'},
                                {'label': 'Choice3', 'value': 'Choice3'},
                            ],
                            placeholder="Graph to Mark Off",
                        )),
                        html.Button('Done', id='mark-done'),
                        html.Button('Edit', id='edit-graph'),


                    ], className='six columns'),

                    
            #]),

                    html.Div([

                        html.Div(dcc.Dropdown(
                            id = 'top-dropdown',
                            options=[
                                {'label': 'Week_advancement', 'value': 'Week_advancement'},
                                {'label': 'Dedicated_time', 'value': 'Dedicated_time'},
                                {'label': 'Followups', 'value': 'Followups'},
                                {'label': 'Upcoming_events', 'value': 'Upcoming_events'}
                            ],
                            value='Week_advancement'
                        )),

                        html.Div(className='row', children=[
                            html.Div([dcc.Dropdown(
                                id = 'sub-dropdown',
                                options=[
                                    {'label': 'Memo Topics', 'value': 'MT'},
                                    {'label': 'Crypto Earnings', 'value': 'CE'},
                                    {'label': 'Radar Usefulness', 'value': 'RU'},
                                    {'label': 'IMU Usefulness', 'value': 'IU'},
                                    {'label': 'Papers replicated', 'value': 'PR'},
                                    {'label': 'Hackathons', 'value': 'Hackathons'},
                                    {'label': 'Published Content', 'value': 'PC'}
                                ],
                                value='PR'
                            )], className='three columns'    ),

                            html.Div([
                                (dcc.Input(id='title-box', type='text', value='Activity')),
                                ], className='three columns'),

                            html.Div([
                                (dcc.Input(id='input-box', type='number', value=0)),
                                ], className='three columns'),

                        ]),
                        #html.Div(dcc.Input(id='input-box', type='number', value=0)),
                        html.Div(className='row', children=[
                            html.Button('Edit', id='button'),
                            html.Button('Add Graph', id='add-button'),
                        ]),
                        html.Div(id='output-container-button',
                                children='Enter a value and press submit'),
                    ], className='six columns'),
            ]),
                html.Hr(),
                html.Button('Close', id='edit1-modal-close-button')
            ],
                style={'textAlign': 'center', },
                className='modal-content',
            ),
        ],
            id='edit1-modal',
            className='modal',
            style={"display": "none"},
        ),
        #### EDIT2: SUCCESS RATE EDIT ###   #############
        'edit2-window': html.Div([  # modal div
        
        html.Div([  # content div
            html.Div(className='row', children=[
                html.Div([


                    html.Div('Graph TYPE'),
                
                    dcc.RadioItems(
                        id='graph-type',
                        options=[
                            {'label': 'Countdown', 'value': 'Countdown'},
                            {'label': 'SuccessRate', 'value': 'SuccessRate'},
                        ],
                        value='Countdown'
                    ), 

                    html.Div('Graph to ADD'),
                    #html.Div(className='row', children=[
                        (dcc.Input(id='new-title', type='text', placeholder="Name")),
                        (dcc.Dropdown(
                            placeholder="I wish to complete this every...",
                            id = 'new-success-interval',
                            options=[
                                {'label': 'halfday', 'value': 'halfday'},
                                {'label': 'day', 'value': 'day'},
                                {'label': 'week', 'value': 'week'},
                            ],
                            #value='day'
                        )),
                    #]),
                    dcc.DatePickerRange(
                        id='dd-deadline',
                        min_date_allowed=date(1995, 8, 5),
                        max_date_allowed=date(2022, 9, 19),
                        initial_visible_month=date.today(),
                        start_date = date.today(),
                        end_date=date.today() + timedelta(days=1)

                    ),
                    (dcc.Input(id='new-deadline', type='text', placeholder="HH:MM")),
                    #(dcc.Input(id='new-success-interval', type='text', value="Title:")),


                    html.Div('Graph to EDIT'),
                    (dcc.Dropdown(
                        id = 'new-dropdown',
                        options=[
                            {'label': 'Choice1', 'value': 'Choice1'},
                            {'label': 'Choice2', 'value': 'Choice2'},
                            {'label': 'Choice3', 'value': 'Choice3'},
                        ],
                        placeholder="Graph to Mark Off",
                    )),
                    html.Button('Done', id='mark-done'),
                    html.Button('Edit', id='edit-graph'),


                ], className='six columns'),
            ]),
                html.Hr(),
                html.Button('Close', id='edit2-modal-close-button')
            ],
                style={'textAlign': 'center', },
                className='modal-content',
            ),
        ],
            id='edit2-modal',
            className='modal',
            style={"display": "none"},
        ),
            #### DRONE PAGE ### (DISCONTINUED)   #############
            'drone-graphs': html.Div([
            # html.H3('Outcomes of Drone Dev'),

            (dcc.Dropdown(
                id = 'drone-dev-dropdown',
                options=[
                    {'label': '5 June | UAV Photogrammetry', 'value': 'Drone Photogrammetry'},
                    {'label': '15 June | DAQ System Design', 'value': 'DAQ System'},
                    {'label': '5 July  | In-vivo Data Collection Flight', 'value': 'In-vivo Data Collection Flight'},
                    {'label': '20 July | UAV Carrier System Design', 'value': 'Carrier System Design'},
                    {'label': '30 July | Drone Drop', 'value': 'Drone Drop'},
                ],
                placeholder="Choose Section",
            )),

            # dcc.Graph(figure=scat,
            # id='habit-tracker', 
            # ),

            ]),

            ### PHOTOGRAMMETRY WITH EMBEDDED SKETCHFABS  #####
            'general-photogrammetry': html.Div([
            html.H3('You are on Photogrammetry page'),

            html.H1(children='Panneau directionel'),

            html.Div(children='''
                28 mai 2021.
            '''),

            html.Div(className='row', children=[
                html.Div([
                    (html.Button('<', id='button-before')),
                    ], className='three columns'),

                html.Div([html.Iframe(src="https://sketchfab.com/models/a1b9a816010449c8bd18d22bf97e8097/embed",
                            # title="Panneau directionnel", frameborder="0", allowfullscreen, 
                            # mozallowfullscreen="true", webkitallowfullscreen="true", 
                            # allow="fullscreen; autoplay; vr", xr-spatial-tracking, execution-while-out-of-viewport, execution-while-not-rendered, web-share, 
                            style={"height": "500px", "width": "100%"}),
                    ], className='three columns'),

                html.Div([
                    (html.Button('>',id='button-after')),
                    ], className='three columns'),
                ]),
            ]),

            ### ADDING PICTURES FROM ASSET FOLDER.
            '2-photos': html.Div(className='row', children=[
                html.Div(html.Img(src=app.get_asset_url('../3-opt-dashboard/assets/relay-pic.jpeg'), width = 300), className='two columns'), 
                html.Div(html.Img(src=app.get_asset_url('detail-rocks.png'), width = 300), className='two columns') 
                ]),

            'in-vivo': html.Div([

                html.Div(className='row', children = [

                    html.Div(dcc.Graph(
                        id='life-exp-vs-gdp',
                        figure=scat2
                    ), className='six columns'),

                    html.Div( html.Iframe(
                        src="https://drive.google.com/file/d/1OzedkXFXX97PheU4dYVHQempUOxBx6X6/preview",
                            style={"height": "450px", "width": "80%"}),
                    className='six columns'),
                ]),

                html.Div(className='row', children = [
                    html.H5('Path Section', className='two columns'),
                    html.Div(dcc.RangeSlider(
                        id='my-range-slider',
                        min=0,
                        max=20,
                        step=0.5,
                        value=[5, 15]
                    ), className='ten columns'),
                ]),

                html.Div(className='row', children = [

                    html.Div([

                        html.H5('Equipment', style={"margin-bottom": "10px"}),
                        html.Div( html.Iframe(
                            src="https://drive.google.com/file/d/1g7t1ncppoytzptNjC7p4kFX5PXZblhkB/preview",
                                style={"height": "150px", "width": "80%"})),
                        html.Div(dcc.Dropdown(
                            id = 'pages-dropdown',
                            options=[
                                {'label': 'FIMI_XSE', 'value': 'FIMIXSE_CAMERA'},
                                {'label': 'FIMI_XSE+PIXHAWK', 'value': 'FIMIXSE+PIXHAWK'},
                                {'label': 'PIXHAWK', 'value': 'PIXHAWK'},
                            ],
                            value='FIMIXSE+PIXHAWK'
                        )),
                        #html.H5('Sensor Data\n \n \n \nEquipment', style={"margin-bottom": "100px"}),
                        html.H5('Sensors', style={"margin-top": "20px", "margin-bottom": "10px"}),
                        dcc.RadioItems(
                            id='sensor',
                            options=[
                                {'label': 'Accelerometer', 'value': 'Accelerometer'},
                                {'label': 'Lightsensor', 'value': 'Lightsensor'},
                                {'label': 'DistanceSensor', 'value': 'DistanceSensor'},
                                {'label': 'Timescale', 'value': 'Timescale'}
                            ],
                            value='Lightsensor'
                        ), 
                    ], className='two columns'), 

                    html.Div(dcc.Graph(
                        id='number2',
                        figure=scat
                    ), className='ten columns'),
                ]),
                html.H5('Frequency Reduction For Data Collection'),
                dcc.Slider(
                    id='my-slider',
                    min=1,
                    max=100,
                    step=1,
                    value=10,
                ),
            ])
            }



            # html.Div([

                    #     html.Div(dcc.Dropdown(
                    #         id = 'top-dropdown',
                    #         options=[
                    #             {'label': 'Week_advancement', 'value': 'Week_advancement'},
                    #             {'label': 'Dedicated_time', 'value': 'Dedicated_time'},
                    #             {'label': 'Followups', 'value': 'Followups'},
                    #             {'label': 'Upcoming_events', 'value': 'Upcoming_events'}
                    #         ],
                    #         value='Week_advancement'
                    #     )),

                    #     html.Div(className='row', children=[
                    #         html.Div([dcc.Dropdown(
                    #             id = 'sub-dropdown',
                    #             options=[
                    #                 {'label': 'Memo Topics', 'value': 'MT'},
                    #                 {'label': 'Crypto Earnings', 'value': 'CE'},
                    #                 {'label': 'Radar Usefulness', 'value': 'RU'},
                    #                 {'label': 'IMU Usefulness', 'value': 'IU'},
                    #                 {'label': 'Papers replicated', 'value': 'PR'},
                    #                 {'label': 'Hackathons', 'value': 'Hackathons'},
                    #                 {'label': 'Published Content', 'value': 'PC'}
                    #             ],
                    #             value='PR'
                    #         )], className='three columns'    ),

                    #         html.Div([
                    #             (dcc.Input(id='title-box', type='text', value='Activity')),
                    #             ], className='three columns'),

                    #         html.Div([
                    #             (dcc.Input(id='input-box', type='number', value=0)),
                    #             ], className='three columns'),

                    #     ]),
                    #     #html.Div(dcc.Input(id='input-box', type='number', value=0)),
                    #     html.Div(className='row', children=[
                    #         html.Button('Edit', id='button'),
                    #         html.Button('Add Graph', id='add-button'),
                    #     ]),
                    #     html.Div(id='output-container-button',
                    #             children='Enter a value and press submit'),
                    # ]),
