import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H2('Thank Mbkupfer for this modal'),
    html.Button("Open modal", id="open"),

    html.Div([  # modal div
        html.Div([  # content div
            html.Div([
                'This is the content of the modal',

            ]),

            html.Hr(),
            html.Button('Close', id='modal-close-button')
        ],
            style={'textAlign': 'center', },
            className='modal-content',
        ),
    ],
        id='modal',
        className='modal',
        style={"display": "none"},
    )
])


@app.callback(Output('modal', 'style'),
              Input('modal-close-button', 'n_clicks'),
              Input('open', 'n_clicks'))
def close_modal(close, open):

    if (close is None) and (open is None):
        return {"display": "none"}

    if (close is None) and (open is not None):
        return {"display": "block"}

    if (open == close + 1) and (open is not None) and (close is not None):
        return {"display": "block"}

    if (open == close) and (close is not None):
        return {"display": "none"}

    print("Modal window bug")




if __name__ == '__main__':
    app.run_server(debug=True)