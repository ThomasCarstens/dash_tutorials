import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('redcap.csv')

app = dash.Dash()

year_options = []
for year in df['year'].unique():
    year_options.append({'label': str(year), 'value': year})

app.layout = html.Div([
    dcc.Graph(id='nursing titles'),
    dcc.Dropdown(id='year_picker', options=year_options,
                 value=df['year'].min())
])

@app.callback(Output('nursing titles', 'figure'),
              [Input('year_picker', 'value')])
def nursing_titles(year):
    dff = df[df['year'] == year]
    count = dff['title'].value_counts()
    data = go.Bar(x=count.index,
                  y=count.values)
    layout = go.Layout(title='Titles 2020')
    fig = go.Figure(data=data, layout=layout)
    return fig