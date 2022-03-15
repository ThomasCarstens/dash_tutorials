# Alliantech.
# FOCUS on graphing Vibration Data.

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

from scipy.signal import butter, sosfilt, sosfreqz, sos2tf

def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog=False, btype='bandstop', output='sos')
        return sos

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
        sos = butter_bandpass(lowcut, highcut, fs, order=order)
        print ("sos is", sos, "done")
        print ("tf is", sos2tf(sos), "done")
        y = sosfilt(sos, data)
        return y


#np.where(a < 5, a, 10*a)

path1 = '~/Documents/data/droneData_alliantech/in-vivo/11_40_32_'
path2 = '~/Documents/data/droneData_alliantech/in-vivo/11_56_06_'
path3 = '~/Documents/data/droneData_alliantech/in-vivo/12_10_04_'
path4 = '~/Documents/data/droneData_alliantech/in-vivo/12_22_20_'

df_traj1= pd.read_csv('~/Documents/data/droneData_alliantech/in-vivo/11_40_32_vehicle_local_position_0.csv')
df_traj2= pd.read_csv('~/Documents/data/droneData_alliantech/in-vivo/11_56_06_vehicle_local_position_0.csv')
df_traj3= pd.read_csv('~/Documents/data/droneData_alliantech/in-vivo/12_10_04_vehicle_local_position_0.csv')
df_traj4= pd.read_csv('~/Documents/data/droneData_alliantech/in-vivo/12_22_20_vehicle_local_position_0.csv')

####################
# PX4 ACCELERATION #
####################
df_acc2a = pd.read_csv(path2 + 'sensor_accel_0.csv')
df_acc2b = pd.read_csv(path2 + 'sensor_accel_1.csv')
df_acc2 = pd.concat([df_acc2a, df_acc2b])
# Get absolute values
df_acc2_abs = []
df_acc2_xy_abs = []
for i in range(len(df_acc2['x'])):#range(len(log_acc['timestamp']))
    # print(df_acc2['x'])
    # print("Here is", (df_acc2['x'].values[i])**2)
    # print("done")
    x = df_acc2['x'].values[i]
    y = df_acc2['y'].values[i]
    z = df_acc2['z'].values[i]
    acc_abs = math.sqrt(x**2 + y**2 + z**2)
    acc_abs_xy = math.sqrt(x**2 + y**2)
    df_acc2_abs.append(acc_abs)
    df_acc2_xy_abs.append(acc_abs_xy)

######################
# SLICE ACCELERATION #
######################
df_slice1 = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/in-vivo/Test_Flight2_altitude_UNFILTERED.csv', decimal=",", sep=';', skiprows = 22)
df_slice = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/in-vivo/Test_Flight1_UNFILTERED.csv', decimal=",", sep=';', skiprows = 22)
df_mini1 = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/in-vivo/Drone.csv', skiprows = 21)
# ATTEMPT TO PUT EXACT TIMES.
import datetime
start_1 = datetime.datetime(2021, 8, 6, 14, 1, 50)
start_2 = datetime.datetime(2021, 8, 6, 14, 6, 8)

# Slice ==> ABSOLUTE TIME: df_slice1_timestamps

#NEW
start_slice = start_2 #SLICE TAKEOFF
#162824906539355
df_mini1_timestamps = []
for timestamp in df_mini1['Time']:
    #print(timestamp)
    #dt = datetime.timedelta(seconds = timestamp/100000) 
    #print("HEY", timestamp, timestamp//1000000000)
    dt = datetime.datetime.fromtimestamp(timestamp/1000000000)
    #print(dt)
    datetime_value = dt 
    #print(datetime_value)
    df_mini1_timestamps.append(datetime_value)
print("len of slice", len(df_mini1_timestamps) )

df_slice1_timestamps = []
for timestamp in df_slice1['Time']:
    #print(timestamp)
    dt = datetime.timedelta(microseconds = timestamp*1000000) 
    datetime_value = start_slice + dt 
    #print(datetime_value)
    df_slice1_timestamps.append(datetime_value)
print("len of slice", len(df_slice1_timestamps) )

# PX4 ==> ABSOLUTE TIME: df_acc2_timestamps
start_drone = datetime.datetime(2021, 8, 6, 13, 56, 6) #DRONE TAKEOFF.

df_acc2_timestamps = []
for timestamp in df_traj2['timestamp']:
    since_start = datetime.timedelta(microseconds = timestamp)
    point_x = since_start + start_drone
    df_acc2_timestamps.append(point_x)
print("len of acc2", len(df_acc2_timestamps) )

## TEST
difference = df_slice1_timestamps [0] - df_acc2_timestamps[0]
print("fist is", df_slice1_timestamps [0])
print("starting at", difference )
print("equivalent to", difference.microseconds )
difference = df_slice1_timestamps [498903] - df_acc2_timestamps[38000]   #START POINT
print("=>", difference )
print("last is", df_slice1_timestamps [-1])
print("=>", df_slice1_timestamps [517903] - df_acc2_timestamps[38200] )


#SLICE[0:1947904] ==> PX4[33100:52280]
import numpy as np

# fusion_graph.add_trace(
#     go.Scattergl(
#         x =  df_slice1_timestamps[498903:517903:],
#         y =  df_slice1['Chan 0:3225A'][498903:517903:],
#         mode='markers',
#         name='SLICE DATA'
#     ),
# )

# LARGE DATA 20 seconds
# slice_array = np.array(df_slice1['Chan 0:3225A'][308903:487903][::])
# df_slice1_window = np.array(df_slice1_timestamps[308903:487903][::])
# LAND: 0.8 seconds
# slice_array = np.array(df_slice1['Chan 0:3225A'][508903:517903:][::])
# df_slice1_window = np.array(df_slice1_timestamps[508903:517903:][::])
# MORE POINTS
slice_array = np.array(df_slice1['Chan 0:3225A'][::50])
df_slice1_window = np.array(df_slice1_timestamps[::50])
#GOING WITH MINI.
mini1_array = np.array(df_mini1['28736:ch1'][::])
df_mini1_window = np.array(df_mini1_timestamps[::])


############ SLICE
# Number of sample points
N = len(slice_array)
# sample spacing
T = 1.0 / 10000.0

temp = butter_bandpass_filter(slice_array, 7, 12, 10000, order=5)*0.8

yf = fft(slice_array)
print(yf)
xf = fftfreq(N, T)[:N//2]
print(slice_array)

f, Pxx_den = signal.welch(slice_array, 10000, nperseg=1024)

f_spect, t_spect, Sxx = signal.spectrogram(slice_array, 10000, nperseg=4096, noverlap =1024)

############ MINI
# Number of sample points
Nm = len(mini1_array)
# sample spacing
Tm = 1.0 / 1024.0

tempm = butter_bandpass_filter(mini1_array, 7, 12, 1024, order=5)*0.8

yfm = fft(mini1_array)
print(yfm)
xfm = fftfreq(N, T)[:N//2]
print(mini1_array)

fm, Pxx_denm = signal.welch(mini1_array, 1024, nperseg=1024)

f_spectm, t_spectm, Sxxm = signal.spectrogram(mini1_array, 1024, nperseg=256, noverlap =0)

# plt.pcolormesh(t, f, Sxx, shading='gouraud')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()
# plt.semilogy(f, Pxx_den)
# plt.ylim([0.5e-3, 1])
# plt.xlabel('frequency [Hz]')
# plt.ylabel('PSD [V**2/Hz]')
# plt.show()

######################
# ALL MY PLOTS       #
######################
# df_slice1_timestamps[448903:487903]

accT_graph = go.Figure()

accT_graph.add_trace(
    go.Scattergl(
        x =  df_slice1_window,
        y =  slice_array,
        mode='markers',
        name='OVER TIME'
    ),
)

accT_graph.add_trace(
    go.Scattergl(
        x =  df_slice1_window,
        y =  temp,
        mode='markers',
        name='Filtered.'
    ),
)

accT_graph.add_trace(
    go.Scattergl(
        x =  df_mini1_window,
        y =  mini1_array,
        mode='markers',
        name='MINI.'
    ),
)

accT_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='markers'))

fusion_graph = go.Figure()

fusion_graph.add_trace(
    go.Scattergl(
        x =  xf[420:]*60,
        y =  abs(yf)[1:],
        mode='markers',
        name='FFT_slice'
    ),
)

fusion_graph.add_trace(
    go.Scattergl(
        x =  xfm[420:]*60,
        y =  abs(yfm)[1:],
        mode='markers',
        name='FFT_mini'
    ),
)

fusion_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='markers'))

psd_graph = go.Figure()

psd_graph.add_trace(
    go.Scattergl(
        x =  f*60,
        y =  Pxx_den,
        mode='markers',
        name='PSD'
    ),
)

psd_graph.add_trace(
    go.Scattergl(
        x =  fm*60,
        y =  Pxx_denm,
        mode='markers',
        name='PSD_mini'
    ),
)

psd_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='markers'))

                    
spectrogram_graph = go.Figure()

spectrogram_graph.add_trace(
    go.Heatmap(
        x= t_spect,
        y= f_spect*60,
        z= np.log10(Sxx),
        colorscale='Jet',
    ),
)

spectrogram_graph_mini = go.Figure()

spectrogram_graph_mini.add_trace(
    go.Heatmap(
        x= t_spectm,
        y= f_spectm*60,
        z= np.log(Sxxm),
        colorscale='Jet',
    ),
)

spectrogram_graph_mini.update_layout(
    title="Spectrogram of FIMI over Flight",
    title_x=0.5,
    #title_y=0.95,
    xaxis_title="Time (s)",
    yaxis_title="Frequency (rpm)",

    )

# fusion_graph.add_trace(
#     go.Scattergl(
#         x =  df_slice1_timestamps[498903:517903:],
#         y =  df_slice1['Chan 0:3225A'][498903:517903:],
#         mode='markers',
#         name='SLICE DATA'
#     ),
# )

# fusion_graph.add_trace(
#     go.Scattergl(
#         x =  df_acc2_timestamps[38000:38200],
#         y =  df_acc2['x'][38000:38200],
#         mode='markers',
#         name='PIXHAWK DATA'
#     ),
# )


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
                            id='SPECTROGRAM_MINI',
                            figure=spectrogram_graph_mini,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                    ]),
                ]),
        ])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
