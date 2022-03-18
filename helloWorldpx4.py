# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from logging import log
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

#### VALUES INDOORS (NO GPS)
#log_adc = pd.read_csv("~/Documents/data/testData/log_3_2021-6-18-10-44-52_adc_report_0.csv")
#log_accel = pd.read_csv("11_09_32_adc_report_0.csv")
#log_gps =pd.read_csv("~/Documents/data/testData/log_3_2021-6-18-10-44-52_vehicle_local_position_0.csv")

#### VALUES OUTDOORS (WITH GPS)
log_adc = pd.read_csv("~//Documents/data/droneData_alliantech/square_alliantech/log_8_2021-6-18-12-37-18_adc_report_0.csv")
#log_accel = pd.read_csv("11_09_32_adc_report_0.csv")
log_gps =pd.read_csv("~//Documents/data/droneData_alliantech/square_alliantech/log_8_2021-6-18-12-37-18_vehicle_local_position_0.csv")

#label xaxis as (UTC(12-37-18) + timestamp// 10**9)
#then convert old timestamps to add to new dataframe.
local_time_timestamps = []
for timestamp in log_adc['timestamp']:
    local_time_timestamps.append(((timestamp+1624019838000000-2*3600*10**6)//(10**3)))
print(local_time_timestamps[0])
time_axis=local_time_timestamps[0::10]
df_square = pd.DataFrame({'adc_report': log_adc['raw_data[4]'],
                            'gps_lat': log_gps['x'],
                            'gps_lon': log_gps['y'],
                            'altitude': log_gps['z'],
                            })




print (df_square)
print(log_adc)
#SAVE FINAL DATABASE
#df_init.to_csv('~/Documents/DashBeginnerTutorials/df_init.csv', index=False)
print(list(log_adc))
print(list(log_gps))

# INITIALIZE: empty SCATTERPLOT trace
scat = go.Figure()
scat.update_layout(
    title="Lighting measurements over time",
    title_x=0.2,
    xaxis_title="Time (100 messages per second)",
    yaxis_title="ADC values",
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="#000000"
    )
)

# Add range slider
scat.update_layout(
    xaxis=dict(
        #rangeslider_range = [time_axis[1], time_axis[50]],
        rangeslider_thickness = 0.1,
        rangeslider=dict(
            visible=True,
            #autorange=False,
            #fixedrange= False,
            range=[time_axis[1], time_axis[50]]
        ),
        type="date"
    )
)
# Set custom x-axis labels
scat.update_xaxes(
    #ticktext=["End of Q1", "End of Q2", "End of Q3", "End of Q4"],
    #tickvals=["2016-04-01", "2016-07-01", "2016-10-01", "me"],
    type = 'date'
)
# Prefix y-axis tick labels with dollar sign
scat.update_yaxes(ticksuffix="m")

###USELESS SINCE WE USE px.scatter for colour.
# scat2= go.Figure()
# scat2.update_layout(
#     title="Lighting levels on full path",
#     title_x=0.2,
#     xaxis_title="GPS Latitude",
#     yaxis_title="GPS Longitude",
#     font=dict(
#         family="Courier New, monospace",
#         size=10,
#         color="#000000"
#     )
# )
# scat2.update_layout(yaxis_range=[-10,10])
# scat2.update_layout(xaxis_range=[-10,10])

# Add traces
# scat2.add_trace(go.Scatter(x=log_gps['x'], y=log_gps['y'],
#                     mode='lines+markers',
#                     name='x vs y'))
# scat2.add_trace(go.Scatter(x=log_gps['ref_lat'], y=log_gps['ref_lon'],
#                     mode='lines+markers',
#                     name='ref_lat vs ref_lon'))

#adc_report                        0    2  101  1   96 #101Hz
#vehicle_local_position            0   15  100  1  168 #100Hz
#100Hz = 0.01s/message ==> timestamps go from ... to ... .

scat2 = px.scatter_3d(df_square, x='gps_lat', y='gps_lon', z='altitude', color='adc_report', 
                    title="Lighting levels on full path",
                    color_continuous_scale=px.colors.sequential.Inferno[::-1],

                    )



scat2.update_xaxes(title_text="Latitude", title_font=dict(
        family="Courier New, monospace",
        size=10,
        color="#000000"))
scat2.update_yaxes(title_text="Longitude", title_font=dict(
        family="Courier New, monospace",
        size=10,
        color="#000000"))


scat2.update_traces(marker=dict(size=2),
                  selector=dict(mode='markers'))
# scat2.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_gps['ref_lat'],
#                     mode='lines+markers',
#                     name='ref_lat'))
# scat2.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_gps['ref_lon'],
#                     mode='lines+markers',
#                     name='ref_lat'))


# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[0]'],
#                     mode='lines+markers',
#                     name='channel0'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[1]'],
#                     mode='lines+markers',
#                     name='channel1'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[2]'],
#                     mode='lines+markers',
#                     name='channel2'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[3]'],
#                     mode='lines+markers',
#                     name='channel3'))
scat.add_trace(go.Scatter(x=time_axis, y=log_adc['raw_data[4]'],
                    mode='lines+markers',
                    name='channel4'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[5]'],
#                     mode='lines+markers',
#                     name='channel5'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[6]'],
#                     mode='lines+markers',
#                     name='channel6'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[7]'],
#                     mode='lines+markers',
#                     name='channel7'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[8]'],
#                     mode='lines+markers',
#                     name='channel8'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[9]'],
#                     mode='lines+markers',
#                     name='channel9'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[10]'],
#                     mode='lines+markers',
#                     name='channel10'))
# scat.add_trace(go.Scatter(x=log_adc['timestamp'], y=log_adc['raw_data[11]'],
#                     mode='lines+markers',
#                     name='channel11'))



app.layout = html.Div([
    html.Div(dcc.Graph(
        id='number2',
        figure=scat
    )),

    # dcc.RangeSlider(
    #     id="my-range-slider",
    #     min=0,
    #     max=100,
    #     step=1,
    #     # marks={
    #     #     0: '0 °F',
    #     #     3: '3 °F',
    #     #     5: '5 °F',
    #     #     7.65: '7.65 °F',
    #     #     10: '10 °F'
    #     # },
    #     value=[1, 100]
    # ),

    dcc.Slider(
        id='my-slider',
        min=1,
        max=100,
        step=1,
        value=10,
    ),
    
    html.Div(dcc.Graph(
        id='life-exp-vs-gdp',
        figure=scat2
    ))
])

## NEARLY DONE. returns array, needs to be the correct one+method to attach to graph.
@app.callback(
    dash.dependencies.Output('number2', 'figure'),
    dash.dependencies.Input('number2', 'relayoutData'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_figure(figdata, trim_step):
    print("hello")
    print(trim_step)
    print(figdata)
    time_axis = local_time_timestamps[::trim_step]
    adc_values = log_adc['raw_data[4]'][::trim_step]
    scat.data = []
    scat.add_trace(go.Scatter(x=time_axis, y=adc_values,
                        mode='lines+markers',
                        name='trim_step:%d'% trim_step)
    )
    # Add range slider
    scat.update_layout(
        xaxis=dict(
            type="date",
            #rangeslider_range = [time_axis[1], time_axis[50]],
            rangeslider_thickness = 0.1,
            rangeslider=dict(
                visible=True,
                #autorange=False,
                #fixedrange= False,
                
            ),
            range=[figdata['xaxis.range'][0], figdata['xaxis.range'][1]]
            

    ))
    #filtered_df = df[df.year == selected_year]

    # fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
    #                  size="pop", color="continent", hover_name="country",
    #                  log_x=True, size_max=55)
    # fig.update_layout(title_text="update_layout() Syntax Example",
    #                 title_font=dict(size=30))
    #scat.update_layout(range=[selected_year])

    return scat


if __name__ == '__main__':
    app.run_server(debug=True)