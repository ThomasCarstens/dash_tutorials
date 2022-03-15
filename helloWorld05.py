

# EMBED SKETCHFAB
# 28 May 2021
# ISSUE  ### Public network blocks my access??
# TEST ### Back at home.

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div(dcc.Dropdown(
        id = 'top-dropdown',
        options=[
            {'label': 'Photogrammetry', 'value': 'PG'},
            {'label': 'Machine Learning', 'value': 'ML'},
            {'label': 'Time Dashboard', 'value': 'FU'},
        ],
        value='PG'
    )),

    html.H1(children='Panneau directionel'),

    html.Div(children='''
        28 mai 2021.
    '''),

    html.Div(className='row', children=[
        html.Div([
            (html.Button('<', id='button-before', n_clicks = 0)),
            ], className='three columns'),

        html.Div([html.Iframe(src="https://sketchfab.com/models/a1b9a816010449c8bd18d22bf97e8097/embed",
                    # title="Panneau directionnel", frameborder="0", allowfullscreen, 
                    # mozallowfullscreen="true", webkitallowfullscreen="true", 
                    # allow="fullscreen; autoplay; vr", xr-spatial-tracking, execution-while-out-of-viewport, execution-while-not-rendered, web-share, 
                    style={"height": "800px", "width": "80%"}),
            ], className='three columns'),

        html.Div([
            (html.Button('>',id='button-after', n_clicks = 0)),
            ], className='three columns'),
        ]),

    html.Div(id='output-container-button',
            children='Enter a value and press submit'),

    dcc.Graph(
        id='example-graph',
        # figure=fig  # commented out to make the example runnable
    ),


    ])

if __name__ == '__main__':
    app.run_server(debug=True, port=8049, host='0.0.0.0')

############ EMBED THE SKETCHFAB ON AN HTML ###
# <div class="sketchfab-embed-wrapper"> 
# 
# <iframe title="Panneau directionnel" frameborder="0" allowfullscreen 
# mozallowfullscreen="true" webkitallowfullscreen="true" 
# allow="fullscreen; autoplay; vr" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share 
# src="https://sketchfab.com/models/a1b9a816010449c8bd18d22bf97e8097/embed"> </iframe> 
# 
# <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/panneau-directionnel-a1b9a816010449c8bd18d22bf97e8097?utm_medium=embed&utm_campaign=share-popup&utm_content=a1b9a816010449c8bd18d22bf97e8097" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Panneau directionnel </a> by <a href="https://sketchfab.com/Thomas.Carstens?utm_medium=embed&utm_campaign=share-popup&utm_content=a1b9a816010449c8bd18d22bf97e8097" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Thomas.Carstens </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=a1b9a816010449c8bd18d22bf97e8097" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p></div>
