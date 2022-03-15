import dash_gif_component as gif
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go


app = dash.Dash(__name__)


template_graph = go.Figure()



app.layout = html.Div([

    html.Div(dcc.Graph(
        id='algo03',
        figure=template_graph
    )),
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')