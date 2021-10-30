# ALLIANTECH
# Setting up the graphs for articles.

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_gif_component as gif

import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
import os
print(os. getcwd())
import numpy as np
import math
import plotly.express as px
from scipy.fft import fft, fftfreq
from scipy import signal

from scipy.signal import butter, sosfilt, sosfreqz

def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog=False, btype='bandpass', output='sos')
        return sos

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
        sos = butter_bandpass(lowcut, highcut, fs, order=order)
        y = sosfilt(sos, data)
        return y

def fita2blen(f_val, x_desired):
    MAX_X = len(f_val)
    FINALLEN_X = x_desired
    CURRENTLEN_X = len(f_val)
    #x on 10 points, then 100 points
    x_current = list(np.linspace(1,MAX_X,CURRENTLEN_X))
    x_final = list(np.linspace(1,MAX_X,FINALLEN_X))
    # interpolate on 100 values.
    interp = np.interp(x_final, x_current, f_val )
    interp = list(interp)
    return interp

#df_log= pd.read_csv('/home/txa/Documents/data/DATA_ zone_monitoring/10_05_12_log_message_0.csv')
#df_log= pd.read_csv('/home/txa/Documents/data/DATA_ zone_monitoring/10_06_37_log_message_0.csv')
df_log= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/03_12_58_log_message_0.csv')
df_adc= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/03_12_58_adc_report_0.csv')


#log_5_2021-8-10-05-26-30.ulg
word=''
print(df_log['text[1]'])
print(range(len(df_log.values)-1))
print(range(len(df_log)))
print("CALC:", 127-82)
print("CALC:", 127-82)
log_list = []
for j in range(len(df_log)):
    log_list.append(word)
    word = str(df_log['timestamp'][j])
    for i in range(0,127):
            #print((df_log['text['+str(i)+']'][4]))
            #try:
            log_value = (df_log['text['+str(i)+']'][j])

            if log_value < 0:
                break
                #log_value = 256-abs(log_value)
                #1 2 4 8 16 32 62 128 -> -85 = 85+128
            letter = chr(log_value)
            #print(log_value, letter)
            word=word+letter
            # except:
            #     #pass
            #     print("issue:", log_value, "at line", j, "text:", i)

#print(log_list)
for each in log_list:
    if 'slice' in each:
        print (each)
#if 'vehicle_magnetometer' in 
#247945064
#### EQUIVALENT ADC VALUE.
#247949441 #closest difference: 4000 nanoseconds.
adc_flight01 = df_adc['raw_data[4]'][24531:-10000]
milliseconds_adc = (df_adc['timestamp'][24531:])/1000
x_adc = milliseconds_adc - (df_adc['timestamp'][24531])/1000
#print(df_adc['raw_data[4]'][24531:])

## FIT IT??
#fita2blen(each['x'], len(df_mag_i))[min_selected:max_selected]


#[247945060:247945067]
######################
# SLICE ACCELERATION #
######################

df_sansmousse = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/F1F2F3voupe/Flight1_coupe_UNFILTERED.csv', decimal=",", sep=';', skiprows = 22)
df_avecmousse = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/F1F2F3voupe/Flight3MOUSSE_coupe_UNFILTERED.csv', decimal=",", sep=';', skiprows = 22)
df_test_vibration = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/PiedDrone/test-drone_1.csv', sep=';')
df_pieton = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/Pieton4_coupe_UNFILTERED.csv', decimal=",", sep=';', skiprows = 22)
df_test_vib2 = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/PiedDrone/spectrum_test_pied_mycsv.csv', decimal=".", sep=',', skiprows = 28)
df_find_start_msg = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/10_06_37_log_message_0.csv')
df_dht11_1 = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/DHT11.CSV', decimal=".", sep=',', index_col=False)
#Data restart
#df_dht11_1 = df_dht11_1.drop([5362])
df_dht11_1 = df_dht11_1[:5362]

arduino_time = df_dht11_1['Time (ms)']
arduino_time = list(map(int, arduino_time))
arduino_temp = df_dht11_1['temperature (C*)']
arduino_temp = list(map(float, arduino_temp))
arduino_humid = list(map(float, df_dht11_1['humidity (%)']))
print(arduino_time[5360:5370])

#print(log_decoder(df_find_start_msg))

# MORE POINTS
sansmousse_ref = np.array(df_sansmousse['Chan 0:Dytran'][::])
sansmousse_nacelle = np.array(df_sansmousse['Chan 1:Dytran2'][::])

avecmousse_ref = np.array(df_avecmousse['Chan 0:Dytran'][::])
avecmousse_nacelle = np.array(df_avecmousse['Chan 1:Dytran2'][::])
print(df_pieton)
print(df_test_vib2)
# ch1_out = np.array(df_test_vibration['Channel  1(g)'][::])
# ch2_out = np.array(df_test_vibration['Channel  2(g)'][::])
# time_test = np.array(df_test_vibration['Time(s)'][::])

drone_out = np.array(df_test_vib2['Y:LogMag g (0-peak).1'][::])
drive_out = np.array(df_test_vib2['Y:LogMag g (0-peak).2'][::])
difference_out = drone_out / drive_out
time_test = np.array(df_test_vib2['X:Frequency (Hz)'][::])

#print(df_test_vib2)
vib_pieton = np.array(df_pieton['Chan 0:Dytran'][::])
time_pieton = np.array(df_pieton['Time'][::])
vib_pieton_filtered = butter_bandpass_filter(vib_pieton, 0.5, 100, 10000, order=8)


############ SANS MOUSSE: LA REFERENCE
# Number of sample points
sample_f = 25000.0
nperseg_filter = 64.0

N = len(sansmousse_ref)
# sample spacing
T = 1.0 / sample_f

temp = butter_bandpass_filter(sansmousse_ref, 7, 12, sample_f, order=5)*0.8

yf = fft(sansmousse_ref)
#print("THIS IS", yf)
xf = fftfreq(N, T)[:N//2]
#print(sansmousse_ref)

f, Pxx_den = signal.welch(sansmousse_ref, sample_f, nperseg=nperseg_filter)

#f_spect, t_spect, Sxx = signal.spectrogram(sansmousse_ref, sample_f, nperseg=4096, noverlap =1024)

############ SANS MOUSSE: LA NACELLE
# Number of sample points
Nn = len(sansmousse_nacelle)
# sample spacing
Tn = 1.0 / 25000.0

tempn = butter_bandpass_filter(sansmousse_nacelle, 7, 12, sample_f, order=5)*0.8

yfn = fft(sansmousse_nacelle)
print(yfn)
xfn = fftfreq(Nn, Tn)[:Nn//2]
print(sansmousse_nacelle)

fn, Pxx_denn = signal.welch(sansmousse_nacelle, sample_f, nperseg=nperseg_filter)

#f_spectn, t_spectn, Sxxn = signal.spectrogram(sansmousse_nacelle, sample_f, nperseg=4096, noverlap =1024)

Pxx_ratio = Pxx_denn / Pxx_den
print ("here is the len:", len(Pxx_ratio))


############ AVEC MOUSSE: LA REFERENCE
# Number of sample points
sample_f = 25000.0

N_2ref = len(avecmousse_ref)
# sample spacing
T_2ref = 1.0 / sample_f

temp_2ref = butter_bandpass_filter(avecmousse_ref, 7, 12, sample_f, order=5)*0.8

yf_2ref = fft(avecmousse_ref)
#print("THIS IS", yf_2ref)
xf_2ref = fftfreq(N_2ref, T_2ref)[:N_2ref//2]

f_2ref, Pxx_den_2ref = signal.welch(avecmousse_ref, sample_f, nperseg=nperseg_filter)

#f_spect, t_spect, Sxx = signal.spectrogram(sansmousse_ref, sample_f, nperseg=4096, noverlap =1024)

############ AVEC MOUSSE: LA NACELLE
# Number of sample points
N_2nac = len(avecmousse_nacelle)
# sample spacing
T_2nac = 1.0 / 25000.0

temp_2nac = butter_bandpass_filter(avecmousse_nacelle, 7, 12, sample_f, order=5)*0.8

yf_2nac = fft(avecmousse_nacelle)
print(yfn)
xf_2nac = fftfreq(N_2nac, T_2nac)[:N_2nac//2]
print(avecmousse_nacelle)

fn_2nac, Pxx_den_2nac = signal.welch(avecmousse_nacelle, sample_f, nperseg=nperseg_filter)

#f_spectn, t_spectn, Sxxn = signal.spectrogram(sansmousse_nacelle, sample_f, nperseg=4096, noverlap =1024)

Pxx_avecmousse = Pxx_den_2nac / Pxx_den_2ref
print ("here is the len:", len(Pxx_avecmousse))


# ######################
# # ALL MY PLOTS       #
# ######################

accT_graph = go.Figure()
# accT_graph.add_trace(
#     go.Scattergl(
#         x =  time_test,
#         y =  drone_out,
#         mode='markers',
#         name='Drone'
#     ),
# )

# accT_graph.add_trace(
#     go.Scattergl(
#         x =  time_test,
#         y =  drive_out,
#         mode='markers',
#         name='Reference'
#     ),
# )

accT_graph.update_layout(
    title="Gain of Drone Leg Accelerometer on Vibrating Pot Frequencies",
    title_x=0.5,
    xaxis_title="Frequency (Hz)",
    yaxis_title="Gain",
)

#Set Scale
# accT_graph.update_xaxes(range=(0.0, 7000.0))
accT_graph.update_yaxes(range=(-1.0, 5.0))

accT_graph.add_trace(
    go.Scattergl(
        x =  time_test,
        y =  difference_out,
        mode='lines',
        name='Reference',
        marker_color = 'green'
    ),
)

# line_1 = np.array()
# for i in range(1, len(time_test)):
#     line_1 = (line_1.append([1])) 
# print (len(line_1), line_1)

# accT_graph.add_trace(
#     go.Scattergl(
#         x =  time_test,
#         y =  line_1,
#         mode='lines',
#         name='Gain of 1',
#         marker_color = 'black'
#     ),
# )

accT_graph.update_traces(marker=dict(size=1),
                    selector=dict(mode='lines'))

fusion_graph = go.Figure()

fusion_graph.add_trace(
    go.Scattergl(
        x =  xf[:]*60,
        y =  abs(yf)[:],
        mode='markers',
        name='Reference'
    ),
)

fusion_graph.add_trace(
    go.Scattergl(
        x =  xfn[:]*60,
        y =  abs(yfn)[:],
        mode='markers',
        name='Nacelle'
    ),
)




fusion_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='markers'))

psd_graph = go.Figure()

psd_graph.update_layout(
    title="Vibrations measured by Drone Leg Accelerometer During Passage of Person",
    title_x=0.5,
    xaxis_title="Time (s)",
    yaxis_title="Measured acceleration",
)
# #Annotations on Graph
# psd_graph.update_layout(
#     title="Gain Difference of 2 Payloads",
#     title_x=0.5,
#     xaxis_title="Frequency (Hz)",
#     yaxis_title="Gain",
# )

#Position Legend
psd_graph.update_layout(legend=dict(
    yanchor="bottom",
    y=0.0,
    xanchor="right",
    x=0.99
))

#Set Scale
# psd_graph.update_xaxes(range=(0.0, 7000.0))
# psd_graph.update_yaxes(range=(0.0, 1.0))

# Add Data

print("len of filtered is", len(vib_pieton_filtered))
psd_graph.add_trace(
    go.Scattergl(
        x =  time_pieton,
        y =  vib_pieton_filtered[153000:180000:],
        mode='markers',
        name='Vibration pieton',
        marker_color = 'goldenrod'
    ),
)


# psd_graph.add_trace(
#     go.Scattergl(
#         x =  time_pieton,
#         y =  vib_pieton,
#         mode='markers',
#         name='Not filtered'
#     ),
# )

# psd_graph.add_trace(
#     go.Scattergl(
#         x =  f*60,
#         y =  Pxx_den,
#         mode='markers',
#         name='PSD'
#     ),
# )

# psd_graph.add_trace(
#     go.Scattergl(
#         x =  fn*60,
#         y =  Pxx_denn,
#         mode='markers',
#         name='PSD'
#     ),
# )



psd_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='markers'))

                    
gain_graph = go.Figure()

#Annotations on Graph
gain_graph.update_layout(
    title="Gain Difference of 2 Payloads",
    title_x=0.5,
    xaxis_title="Frequency (Hz)",
    yaxis_title="Gain",
)


#Position Legend
gain_graph.update_layout(legend=dict(
    yanchor="bottom",
    y=0.85,
    xanchor="right",
    x=0.99
))

#Set Scale
gain_graph.update_xaxes(range=(0.0, 10000.0))
gain_graph.update_yaxes(range=(-0.3, 1.0))

# Add Data
gain_graph.add_trace(
    go.Scattergl(
        x =  f[:],
        y =  abs(Pxx_ratio)[:],
        mode='lines',
        name='Nacelle moins amortissante'
    ),
)
gain_graph.add_trace(
    go.Scattergl(
        x =  f[:],
        y =  abs(Pxx_avecmousse)[:],
        mode='lines',
        name='Nacelle plus amortissante'
    ),
)

gain_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='lines'))


#arduino_graph = go.Figure()
from plotly.subplots import make_subplots
arduino_graph = make_subplots(specs=[[{"secondary_y": True}]])
#Annotations on Graph
arduino_graph.update_layout(
    title="Arduino Sensor",
    title_x=0.5,
    xaxis_title="Frequency (Hz)",
    #yaxis_title="Gain",
)
# Set y-axes titles
arduino_graph.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
arduino_graph.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

#Position Legend
arduino_graph.update_layout(legend=dict(
    yanchor="bottom",
    y=0.7,
    xanchor="right",
    x=0.85
))

#Set Scale
# arduino_graph.update_xaxes(range=(0.0, 10000.0))
# arduino_graph.update_yaxes(range=(-0.3, 1.0))

# Add Data
arduino_graph.add_trace(
    go.Scattergl(
        x =  arduino_time,
        y =  arduino_temp,
        mode='lines',
        name='Temperature',
        
    ), secondary_y=False,
)

arduino_graph.add_trace(
    go.Scatter(
        x =  arduino_time,
        y =  arduino_humid,
        mode='lines',
        name='Humidity',
        
    ), secondary_y=True,
)

arduino_graph.add_trace(
    go.Scattergl(
        x =  x_adc,
        y =  adc_flight01,
        mode='lines',
        name='Lighting',
        marker_color = 'goldenrod'
        
    ), secondary_y=True,
)


arduino_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='lines'))


# SAME WITH LIGHTING.
#humidity_graph = go.Figure()
humidity_graph = make_subplots(specs=[[{"secondary_y": True}]])
#Annotations on Graph
humidity_graph.update_layout(
    title="Arduino Sensor",
    title_x=0.5,
    xaxis_title="Frequency (Hz)",
    #yaxis_title="Gain",
)
# Set y-axes titles
humidity_graph.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
humidity_graph.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

#Position Legend
humidity_graph.update_layout(legend=dict(
    yanchor="bottom",
    y=0.7,
    xanchor="right",
    x=0.85
))

#Set Scale
# arduino_graph.update_xaxes(range=(0.0, 10000.0))
# arduino_graph.update_yaxes(range=(-0.3, 1.0))

# Add Data
humidity_graph.add_trace(
    go.Scattergl(
        x =  x_adc,
        y =  adc_flight01,
        mode='markers',
        name='Lighting',
        marker_color = 'goldenrod'
        
    ), secondary_y=False,
)

humidity_graph.add_trace(
    go.Scatter(
        x =  arduino_time,
        y =  arduino_humid,
        mode='markers',
        name='Humidity',
        
    ), secondary_y=True,
)


humidity_graph.update_traces(marker=dict(size=1),
                    selector=dict(mode='markers'))

app.layout = html.Div([

                dcc.Store(id='current_df_traj', data = [[0,0,0]]), #ensures rangeslider consistent 

                html.Div(className='row', children = [
                    html.Div([
                        html.Div([
                            html.H6(children='DRONE PORTEUR: GPS+MAGNETO @pts', id='small-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),

                            dcc.RangeSlider(
                                id='traj-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000])
                            ]),

                        html.Div(dcc.Graph(
                            id='accT',
                            figure=fusion_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),


                        html.Div(dcc.Graph(
                            id='trajectory',
                            figure=accT_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                        html.Div(dcc.Graph(
                            id='PSD',
                            figure=psd_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                        # html.Div(dcc.Graph(
                        #     id='SPECTROGRAM',
                        #     figure=spectrogram_graph,
                        #     style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        # ), className= 'five columns'),

                        html.Div(dcc.Graph(
                            id='nacelle_graph',
                            figure=gain_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                        html.Div(dcc.Graph(
                            id='temperature_graph',
                            figure=arduino_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                        html.Div(dcc.Graph(
                            id='humidity_graph',
                            figure=humidity_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                    ]),
                ]),
        ])
#REALTIIIME
#temperature_graph


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
