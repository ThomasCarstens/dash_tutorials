import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output #not actual component: for callbacks.

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div(["Input: ",
              dcc.Input(id='my-input', value='initial value', type='text')]),
    html.Br(),
    html.Div(id='my-output'), #children would get overwritten anyway.

])


@app.callback(
    Output(component_id='my-output', component_property='children'), #Output is child comp of my-output
    Input(component_id='my-input', component_property='value')
) #don't even put a blank line...
def update_output_div(input_value): #callback function declaration: called upon change
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)