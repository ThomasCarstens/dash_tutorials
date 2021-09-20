import dash
import dash_core_components as dcc
import dash_html_components as html
import os
print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# HELLO WORLD: PICTURE FROM LINK WITH RESERVED HTML.
image_directory =  os.getcwd() + '/3-opt-dashboard/'
print(image_directory)
#html.Img(id='image')
#https://github.com/plotly/dash/issues/71

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

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),

    # content will be rendered in this element
    html.Div(id='page-content')
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')],
              dash.dependencies.Input('top-dropdown', 'value'))
def display_page(pathname, value):
    if value == "PG":
        return html.Div([
            html.H3('You are on page {}'.format(pathname)),
        

        ### ADDING PICTURES FROM ASSET FOLDER.
            html.Div(html.Img(src=app.get_asset_url('detail-post.png'))) #helloWorld has no asset folder
        ])

    else:
        return html.Div([
            html.H3('Next page: {}'.format(pathname))
        ])


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')