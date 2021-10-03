import dash_gif_component as gif
import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    gif.GifPlayer(
        gif='assets/hack_time.gif',
        still='assets/hacking-time0.jpg',
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')