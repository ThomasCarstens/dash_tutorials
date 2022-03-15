import dash
import dash_core_components as dcc
import dash_html_components as html

print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


## HELLO WORLD: RENDERING MULTIPLE PAGES. VIA A DROPDOWN.
app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    html.Div(dcc.Dropdown(
        id = 'top-dropdown',
        options=[
            {'label': 'Photogrammetry', 'value': 'PG'},
            {'label': 'Machine Learning', 'value': 'ML'},
            {'label': 'Time Dashboard', 'value': 'FU'},
        ],
        value='PG'
    )),

    #### CHANGING URL IS FOR LATER. ##
    # dcc.Link('Navigate to "/"', href='/'),
    # html.Br(),
    # dcc.Link('Navigate to "/page-2"', href='/page-2'),

    # content will be rendered in this element
    html.Div(id='page-content'),

    html.Div(className='row', children=[
        html.Div([
            (html.Button('<', id='button-')),
            ], className='two columns'),
        html.Div([
            (html.Button('>', id='button+')),
            ], className='two columns'),
    ])
])

DYNAMIC_CONTROLS = {
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
                html.Div(html.Img(src=app.get_asset_url('detail-post.png'), width = 300), className='two columns'), 
                html.Div(html.Img(src=app.get_asset_url('detail-rocks.png'), width = 300), className='two columns') 
                ])

            }

# @app.callback(dash.dependencies.Output('page-content', 'children'),
#               [dash.dependencies.Input('url', 'pathname')],
#               dash.dependencies.Input('button-before', 'n_clicks'))
# def display_page(pathname, click_nb):


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')],
              dash.dependencies.Input('top-dropdown', 'value'),
              dash.dependencies.Input('button+', 'n_clicks'))
def display_page(pathname, value, n_clicks):
    if value == "PG" and n_clicks != 1:
        return html.Div([
            DYNAMIC_CONTROLS['general-photogrammetry'],
            #DYNAMIC_CONTROLS['2-photos'],
        ])

    if value == "PG" and n_clicks == 1:
        return html.Div([
            DYNAMIC_CONTROLS['general-photogrammetry'],
            DYNAMIC_CONTROLS['2-photos'],
        ])

    if value == "ML":
        return html.Div([
            html.H3('Next page: {}'.format(pathname))
        ])

    if value == "FU":
        return html.Div([
            html.H3('Next page: {}'.format(pathname))
        ])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')