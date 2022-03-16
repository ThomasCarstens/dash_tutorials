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

increment = 2000 #20 for demo, 300 for dev
lighting_alignment = 8.3 
clock_ms = 300
time_alignment = 0.0845 # 84 < x < 85
gps_alignment = 8.2 # 8 < x < 8.5

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

#df_log= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/10_05_12_log_message_0.csv')
#df_log= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/10_06_37_log_message_0.csv')
df_log= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/03_12_58_log_message_0.csv')
df_adc= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/03_12_58_adc_report_0.csv')
df_gps= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/03_12_58_vehicle_local_position_0.csv')
df_acc0= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/03_12_58_sensor_accel_0.csv')
df_acc1= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/03_12_58_sensor_accel_1.csv')
df_acc = df_acc0 + df_acc1
df_z= pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/03_12_58_vehicle_local_position_0.csv')

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
# adc_flight01 = df_adc['raw_data[4]'][24531:-10000]
# milliseconds_adc = (df_adc['timestamp'][24531:])/1000
# x_adc = milliseconds_adc - (df_adc['timestamp'][24531])/1000
#print(df_adc['raw_data[4]'][24531:])

#### EQUIVALENT GPS VALUE.
#247949321 @24474#closest difference: 4000 nanoseconds.

# from [0,100] to [30,60] but also reverse it where 60 = 30 and 30 = 60
array_diff = 47561 - 47523 #+ 24500 - 24474      #24474
x_pos = df_gps['x'][24474:-5000]
y_pos = df_gps['y'][24474:-5000]
z_pos = df_gps['z'][24474:-5000]
t_pos = df_gps['timestamp'][24474:-5000]

#HUMIDITY DATA

#LIGHTING DATA
raw_data = df_adc['raw_data[4]'][24531:-5000-array_diff]
adc_flight01 = (100-raw_data)/100*30 + 30
milliseconds_adc = (df_adc['timestamp'])/1000
x_adc = milliseconds_adc/1000





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
df_dht11_2 = pd.read_csv('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/DHT11_2.CSV', decimal=".", sep=',', index_col=False)

#Data restart
#df_dht11_1 = df_dht11_1.drop([5362])
df_dht11_1 = df_dht11_1[:5362]

df_dht11 = df_dht11_2

arduino_time = df_dht11['Time (ms)'] - df_dht11['Time (ms)'][0]
arduino_time = list(map(float, arduino_time/1000))
arduino_temp = df_dht11['temperature (C*)']
arduino_temp = list(map(float, arduino_temp))
arduino_humid = list(map(float, df_dht11['humidity (%)']))

reversed_humid = []
for point in arduino_humid:
    new_ = point*0.2 + 10
    reversed_humid.append(new_)
arduino_humid = reversed_humid

#print(arduino_time[5360:5370])
fitted_temp = fita2blen(arduino_temp[:-2700], len(x_pos)) #[:-2700] aligns with lighting
fitted_humid = fita2blen(arduino_humid[:-2700], len(x_pos))

speed = []
for i in range(len(df_z)):
    speed.append(math.sqrt(df_z['vx'][i]**2 + df_z['vy'][i]**2 + df_z['vz'][i]**2))
acc = []
for i in range(len(df_z)):
    acc.append(math.sqrt(df_z['ax'][i]**2 + df_z['ay'][i]**2 + df_z['az'][i]**2))

shorten_vel = np.array(speed [::])
shorten_acc = np.array(acc [::5])
#print(shorten_acc)
print('acc len:', len(shorten_acc), 'vs', len(x_pos))
fitted_vel = fita2blen(shorten_vel, len(x_pos))
fitted_acc = fita2blen(shorten_acc, len(x_pos))
# fitted_vel_plane = fita2blen(shorten_vel_plane, len(x_pos))
df_surface = pd.DataFrame({
                            't': np.array(t_pos),
                            'x': np.array(x_pos),
                            'y': np.array(y_pos),
                            'z': np.array(z_pos),
                            'light': np.array(adc_flight01),
                            'temp': np.array(fitted_temp), 
                            'humid': np.array(fitted_humid), 
                            'acc': np.array(fitted_acc),
                            'vel': np.array(fitted_vel),
                            # 'vel_plane': np.array(fitted_vel_plane),
                            
                            })

print(df_surface['x'].shape, 'is y vs lighting is', df_surface['light'].shape)
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
external_1 = np.array(df_test_vib2['Y:LogMag g (0-peak).3'][::])
external_2 = np.array(df_test_vib2['Y:LogMag g (0-peak)'][::])
difference_out = drone_out / drive_out
# RuntimeWarning: invalid value encountered in true_divide
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
    title="Final Sensitivity Curve for UAV Vibration Probe",
    title_x=0.5,
    xaxis_title="Frequency (Hz)",
    yaxis_title="Sensitivity",
)

#Set Scale
# accT_graph.update_xaxes(range=(0.0, 7000.0))
accT_graph.update_yaxes(range=(-1.0, 5.0))

# accT_graph.add_trace(
#     go.Scattergl(
#         x =  time_test,
#         y =  external_1,
#         mode='markers',
#         name='Translational x interference',
#         marker_color = 'black',
#         marker_size = 1
#     ),
# )

# accT_graph.add_trace(
#     go.Scattergl(
#         x =  time_test,
#         y =  external_2,
#         mode='markers',
#         name='Translational y interference',
#         marker_color = 'black',
#         marker_size = 1
#     ),
# )


accT_graph.add_trace(
    go.Scattergl(
        x =  time_test,
        y =  difference_out,
        mode='markers',
        name='Difference between drone and reference vibrations',
        marker_color = 'blue',
        marker_size = 2
    ),
)

accT_graph.add_hline(y=1, line=dict(
    color="Red",
    width=1,
    dash="dot",
))


# accT_graph.add_trace(
#     go.Scattergl(
#         x =  time_test,
#         y =  drive_out,
#         mode='markers',
#         name='Drive value',
#         marker_color = '#119DFF',
#         marker_size = 2
#     ),
# )

# accT_graph.add_trace(
#     go.Scattergl(
#         x =  time_test,
#         y =  drone_out,
#         mode='lines',
#         name='Reference',
#         marker_color = 'blue'
#     ),
# )
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



# psd_graph.add_trace(
#     go.Scattergl(
#         x =  time_pieton,
#         y =  vib_pieton,
#         mode='markers',
#         name='Raw data',
#         marker_color = 'brown',
#         marker_size = 1
#     ),
# )

print("len of filtered is", len(vib_pieton_filtered))
psd_graph.add_trace(
    go.Scattergl(
        x =  time_pieton,
        y =  vib_pieton_filtered[153000:180000:],
        mode='markers',
        name='Footsteps',
        marker_color = 'orange'
    ),
)

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
# gain_graph.update_xaxes(range=(0.0, 10000.0))
# gain_graph.update_yaxes(range=(-0.3, 1.0))

# Add Data
# gain_graph.add_trace(
#     go.Scattergl(
#         x =  f[:],
#         y =  abs(Pxx_ratio)[:],
#         mode='lines',
#         name='Nacelle moins amortissante'
#     ),
# )
# gain_graph.add_trace(
#     go.Scattergl(
#         x =  f[:],
#         y =  abs(Pxx_avecmousse)[:],
#         mode='lines',
#         name='Nacelle plus amortissante'
#     ),
# )

# gain_graph.update_traces(marker=dict(size=2),
#                     selector=dict(mode='lines'))


from PIL import Image
field_img = Image.open('/home/txa/Documents/data/droneData_alliantech/DATA_zone_monitoring/test_site.png')


xy_graph = go.Figure()

xy_graph.add_layout_image(
        dict(
            source=field_img,
            xref="x",
            yref="y",
            x=-40,
            y=50,
            sizex=130,
            sizey=110,
            sizing="stretch",
            opacity=0.7,
            layer="below",
            )
)
# Set templates
xy_graph.update_layout(template="plotly_white")


#Annotations on Graph
xy_graph.update_layout(
    # title="Temperature over the field",
    # title_x=0.5,
    xaxis_title="x position (m)",
    yaxis_title="y position (m)",
)


#Position Legend
xy_graph.update_layout(legend=dict(
    yanchor="bottom",
    y=0.85,
    xanchor="right",
    x=0.99
))


# #Set Scale
xy_graph.update_xaxes(range=(-40.0, 90.0))
xy_graph.update_yaxes(range=(-60, 50.0))

import math

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

y_rotpos = []
x_rotpos = []
xy_pt = []
graph_center = [15.0, 0.0]
rotation_angle = 45 / 360 * 2* math.pi


for i in range(24474,24474+len(x_pos)):
    xy_pt = [x_pos[i], y_pos[i]]
    x_rot, y_rot = rotate(graph_center, xy_pt, rotation_angle)
    x_rotpos.append(x_rot)
    y_rotpos.append(y_rot)


# df_surface['temp']

# Add Data
cropped_investigation_start = 20000
cropped_investigation_end = 25000

print('displacement of temp', len(df_surface['temp']), 'equivalent is', len(x_rotpos))
xy_graph.add_trace(
    go.Scattergl(
        x =  x_rotpos[:-830],#[2000:],#[cropped_investigation_start:cropped_investigation_end],
        y =  y_rotpos[:-830],#[2000:],#[cropped_investigation_start:cropped_investigation_end],
        mode='markers',
        marker=dict(
                    color=df_surface['temp'][830:],#fitted_temp[2000:],#[cropped_investigation_start:cropped_investigation_end],#adc_flight01,
                    colorscale='sunset_r', #'Viridis' #for lighting
                    showscale=True, )
    ),
)

gain_graph.add_trace(
    go.Scattergl(
        x =  x_rotpos,#[:-830],#[2000:],#[cropped_investigation_start:cropped_investigation_end],
        y =  y_rotpos,#[:-830],#[2000:],#[cropped_investigation_start:cropped_investigation_end],
        mode='markers',
        marker=dict(
                    color=df_surface['temp'],#[830:],#fitted_temp[2000:],#[cropped_investigation_start:cropped_investigation_end],#adc_flight01,
                    colorscale='sunset_r', #'Viridis' #for lighting
                    showscale=True, )
    ),
)

xy_graph.update_traces(marker=dict(size=2),
                    selector=dict(mode='markers'))


_3d_lighting_graph = go.Figure()

# #Annotations on Graph
# _3d_lighting_graph.update_layout(
#     title="Lighting surface",
#     title_x=0.5,
#     xaxis_title="Frequency (Hz)",
#     yaxis_title="Gain",
# )


# #Position Legend
# _3d_lighting_graph.update_layout(legend=dict(
#     yanchor="bottom",
#     y=0.85,
#     xanchor="right",
#     x=0.99
# ))

#Set Scale
# _3d_lighting_graph.update_xaxes(range=(-20.0, 45.0))
# _3d_lighting_graph.update_yaxes(range=(-40, 30.0))

# Add Data

# _3d_lighting_graph.add_trace(

#     go.Surface(z=df_surface['light'][1::50], 
#     x=df_surface['x'][1::50], 
#     y=df_surface['y'][1::50], 
#     showscale=False, 
#     opacity=0.9, 

#     ),)

# _3d_lighting_graph.add_trace(
#     go.Scatter3d(
#         x =  x_pos,
#         y =  y_pos,
#         z = z_pos,
#         mode='markers',
#         name='Nacelle moins amortissante',
#         marker=dict(
#                     color=adc_flight01,
#                     colorscale='Viridis')
#     ),
# )



# _3d_lighting_graph.update_traces(marker=dict(size=2),
#                     selector=dict(mode='lines'))


#arduino_graph = go.Figure()
from plotly.subplots import make_subplots
arduino_graph = make_subplots(specs=[[{"secondary_y": True}]])
#Annotations on Graph
arduino_graph.update_layout(
    # title="Arduino Sensor",
    # title_x=0.5,
    xaxis_title="Time (s)",
    #yaxis_title="Gain",
)
# Set y-axes titles
arduino_graph.update_yaxes(title_text="Temperature (Celsius) and Humidity (arbitrary)", secondary_y=False)
arduino_graph.update_yaxes(title_text="Lighting (arbitrary)", secondary_y=True)

#Position Legend
# arduino_graph.update_layout(legend=dict(
#     yanchor="bottom",
#     y=0.7,Altitude
#     xanchor="right",
#     x=0.85
# ))

arduino_graph.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
arduino_duration = (1065652 - 347123) #347123 == 247945064
print('arduino: stop at:', (782170427-247945064)/1000 + 347123   )
#Set Scale
# arduino_graph.update_xaxes(range=(0.0, 10000.0))
# arduino_graph.update_yaxes(range=(-0.3, 1.0))
print ('full arduino', len(arduino_time), len(arduino_temp), 'vs', len(x_rotpos))
#print (arduino_time)
# Add Data
arduino_graph.add_trace(
    go.Scattergl(
        x =  arduino_time[:-2700],#df_surface['t']/1000000,#[:-2700],#[cropped_investigation_start:cropped_investigation_end], #align full at [:-2700]
        y =  arduino_temp[:-2700],#[cropped_investigation_start:cropped_investigation_end],
        mode='lines',
        name='Temperature',
        marker_color = 'red'
        
    ), secondary_y=False,
)


from scipy.signal import butter, lfilter, freqz
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Setting standard filter requirements.
order = 6
fs = 100.0       
cutoff = 0.5  

b, a = butter_lowpass(cutoff, fs, order)
acc_filtered = butter_lowpass_filter(df_surface['acc'], cutoff, fs, order)


# 4 POSE GRAPHS
# arduino_graph.add_trace(
#     go.Scatter(
#         x =  x_adc,
#         y =  df_surface['acc'],#[cropped_investigation_start:cropped_investigation_end],
#         mode='lines',
#         name='Acceleration',
        
#     ), secondary_y=True,
# )

# LIGHTING EVALUATION: HOW FAST IS THE FASTEST?
adc_m = []
adc_speeds = []
LDR_range = (150-20)+1
adc_range = 500#len(adc_flight01[:-1])
import time
t_i = time.time()

for i in range(24531, adc_range): #-1 for full
    #print(adc_flight01[i+1])
    for j in range(len(x_adc[i+99:-1])): 

        # find closest to 1 second
        if (x_adc[j]-x_adc[i]) >=1:
            if i%10 ==0:
                print(i,'/', adc_range, '|', (i-24531)/(adc_range-24531))
            if i%100 ==0:
                t_f = time.time()
                t_100 = t_f-t_i
                t_left = t_100 * (adc_range-i)/100
                print('time per 100:', t_f-t_i, 'in minutes:', t_left/60)
                t_i = t_f
            if i%10000 ==0:
                np.savetxt('timer-dash/sensor_performance/adc_speeds.csv', adc_speeds, delimiter=',')
                np.savetxt('timer-dash/sensor_performance/adc_m.csv', adc_m, delimiter=',')
                adc_m_clean = list(filter(lambda num: num != 0, adc_m))
                adc_speeds_clean = list(filter(lambda num: num != 0, adc_speeds))
                print(max(np.absolute(adc_m_clean)), 'is max light change/m' )
                print(min(np.absolute(adc_m_clean)), 'is min light change/m.')
                print(max(np.absolute(adc_speeds_clean)), 'is max light change/s.')
                print(min(np.absolute(adc_speeds_clean)), 'is min light change/s.')
                lux_max = math.exp(-1.4*math.log(max(np.absolute(adc_m_clean)))+7.098)
                lux_min = math.exp(-1.4*math.log(min(np.absolute(adc_m_clean)))+7.098)
                print('LUX RANGE is', lux_max, 'to', lux_min)
            break


    # Use this interval to determine the temp range per second
    diff = (adc_flight01[j]-adc_flight01[i])
    # increment version is:
    #diff = (adc_flight01[i+1]-adc_flight01[i])*100/LDR_range
    duration = x_adc[j]-x_adc[i]
    #duration = x_adc[i+1]-x_adc[i]
    adc_speeds.append(diff*100/LDR_range)
    #adc_speed s_r: D/s.. Velocity v: m/s -> s_r/v = D/m
    # average velocity
    sumv = 0
    count= 0
    for vi in range(1+len(df_surface['vel'][i:j])):
        sumv += df_surface['vel'][vi]
        count +=1
    av = sumv/count
    #print(av, 'is av')
    adc_m.append(((diff/duration)/av))
    
# print(x_adc[11]-x_adc[10], 'is time...')
# print(max(adc_m), 'is max light change/m.')
# # 6.5524
# print(min(adc_m), 'is min light change/m.')
# # 11207.3741 

# print(max(adc_speeds), 'is max light change/s.')
# # 6.5524
# print(min(adc_speeds), 'is min light change/s.')
#11207.3741 

arduino_graph.add_trace(
    go.Scattergl(
        x =  arduino_time,
        y =  adc_speeds,
        mode='lines',
        name='Light Sensor Speed',
        marker_color = 'orange'
        
    ), secondary_y=True,
)

arduino_graph.add_trace(
    go.Scattergl(
        x =  arduino_time,
        y =  adc_m,
        mode='lines',
        name='Lighting (Lux/m)',
        marker_color = 'orange' ##37b8ec
        
    ), secondary_y=True,
)


# TEMP EVALUATION: HOW FAST IS THE FASTEST?

temp_speeds = []
temp_m = []
DHT11_range = (90-20)+1
for i in range(len(arduino_time[:-1])):
    #First find the second interval corresponding to start.
    for j in range(len(arduino_time[i:-1])): 
        if (arduino_time[j]-arduino_time[i]) >=1:
            break

    # Use this interval to determine the temp range per second
    diff = (arduino_temp[j]-arduino_temp[i])
    duration = arduino_time[j]-arduino_time[i]
    # This gives the range per increment (not exactly)
    temp_speeds.append(diff*100/DHT11_range)
    sumv = 0
    count= 0
    for vi in range(1+len(df_surface['vel'][i:j])):
        sumv += df_surface['vel'][vi]
        count +=1
    av = sumv/count
    temp_m.append(((diff/duration)/av))

temp_speeds_clean = list(filter(lambda num: num != 0, temp_speeds))
temp_m_clean = list(filter(lambda num: num != 0, temp_m))

print(max(np.absolute(temp_m_clean)), 'is max temp change/m.')
# 6.5524
print(min(np.absolute(temp_m_clean)), 'is min temp change/m.')

print(max(np.absolute(temp_speeds_clean)), 'is max temp change/s.')
# 6.5524
print(min(np.absolute(temp_speeds_clean)), 'is min temp change/s.')


(72.74, 0.21167)
(86.44, 0.9256)
(92.44, 3.02006)

arduino_graph.add_trace(
    go.Scattergl(
        x =  arduino_time,
        y =  temp_speeds,
        mode='lines',
        name='DH11 (%/s)',
        marker_color = 'purple'
        
    ), secondary_y=False,
)

arduino_graph.add_trace(
    go.Scattergl(
        x =  arduino_time,
        y =  temp_m,
        mode='lines',
        name='DH11 (%/m)',
        marker_color = 'purple'
        
    ), secondary_y=False,
)

arduino_graph.add_trace(
    go.Scatter(
        x =  x_adc,
        y =  acc_filtered,#[cropped_investigation_start:cropped_investigation_end],
        mode='lines',
        name='Acc Trendline',
        #marker_size = 0.5
        
    ), secondary_y=False,
)

arduino_graph.add_trace(
    go.Scatter(
        x =  x_adc,
        y =  df_surface['vel'],#[cropped_investigation_start:cropped_investigation_end],
        mode='lines',
        name='Velocity',
        #marker_size = 0.5
        
    ), secondary_y=False,
)

arduino_graph.add_trace(
    go.Scatter(
        x =  x_adc,
        y =  -df_surface['z'],#[cropped_investigation_start:cropped_investigation_end],
        mode='lines',
        name='Altitude',
        #marker_size = 0.5
        
    ), secondary_y=False,
)

arduino_graph.add_trace(
    go.Scatter(
        x =  arduino_time,#[cropped_investigation_start:cropped_investigation_end],
        y =  arduino_humid[800:],#[cropped_investigation_start:cropped_investigation_end],
        mode='lines',
        name='Humidity',
        marker_color = 'blue'
        
    ), secondary_y=False,
)



arduino_graph.add_trace(
    go.Scattergl(
        x =  x_adc,
        # y =  adc_flight01,
        y = df_surface['light'],#[cropped_investigation_start:cropped_investigation_end],
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
        x =  df_surface['t']/1000000,
        y =  adc_flight01,
        mode='markers',
        name='Lighting',
        marker_color = 'goldenrod'
        
    ), secondary_y=False,
)

humidity_graph.add_trace(
    go.Scatter(
        x =  df_surface['t']/1000000,
        y =  arduino_humid,
        mode='markers',
        name='Humidity',
        
    ), secondary_y=True,
)
#247947456 START similar to  247945064
#  1065652
#  347134


humidity_graph.update_traces(marker=dict(size=1),
                    selector=dict(mode='markers'))


app.layout = html.Div([
                html.H6(children='', id='random-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

                dcc.Store(id='current_df_traj', data = [[0,0,0]]), #ensures rangeslider consistent 

                html.Div(className='row', children = [

                    dcc.Interval(
                            id='interval-component',
                            interval=1*clock_ms, # in milliseconds
                            n_intervals=0
                    ),
                    dcc.Store(id='intermediate-value', data = 0),

                    html.Div([
                        html.Div([
                            html.H2(children='Environment Data Collection over Zone', id='small-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

                            dcc.RangeSlider(
                                id='traj-edit-tool',
                                min=1,
                                max=100000,
                                step=1,
                                value=[1, 100000])
                            ]),
                        # ## FFT GRAPH
                        # ################

                        # html.Div(dcc.Graph(
                        #     id='accT',
                        #     figure=fusion_graph, 
                        #     style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        # ), className= 'five columns'),


                        # ## GAIN IN VIB
                        # ################

                        # html.Div(dcc.Graph(
                        #     id='trajectory',
                        #     figure=accT_graph,
                        #     style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        # ), className= 'five columns'),

                        # ## PHOTO/VIDEO 1
                        # ################

                        # html.Div([
                        #     html.H3(children='Flight Analysis', id='01-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
                        #     html.Iframe(
                        #     id = 'passingby_video',
                        #     src="https://drive.google.com/file/d/1EF272V1ftuAgAScBfpF5QSSfBIkoJyHK/preview",
                        #         style={"height": "300px", "width": "65%"}),
                        # ], className='five columns'),

                        # ## PHOTO/VIDEO 2
                        # ################

                        # html.Div([
                        #     html.H3(children='Flight Analysis', id='02-title', style = {'width': '100%', 'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
                        #     html.Iframe(
                        #     id = 'followdrone_video',
                        #     src="https://drive.google.com/file/d/1EF272V1ftuAgAScBfpF5QSSfBIkoJyHK/preview",
                        #         style={"height": "300px", "width": "65%"}),
                        # ], className='five columns'),

                        # ##
                        html.Div(dcc.Graph(
                            id='vibration_graph',
                            figure=psd_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                        # html.Div(dcc.Graph(
                        #     id='SPECTROGRAM',
                        #     figure=spectrogram_graph,
                        #     style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        # ), className= 'five columns'),

                        ## GAIN DIFFERENCE
                        ################

                        html.Div(dcc.Graph(
                            id='nacelle_graph',
                            figure=gain_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),



                        ## GIF
                        ################

                        html.Div(gif.GifPlayer(
                            gif='assets/drone_operators.gif',
                            
                            still=field_img,
                        ), className= 'five columns'),


                        ## DRONE FLIGHT OVER FIELD WITH LUMINOSITY
                        ################

                        html.Div(dcc.Graph(
                            id='xy_graph',
                            figure=xy_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),


                        ## ARDUINO SENSORS
                        ################

                        html.Div(dcc.Graph(
                            id='temperature_graph',
                            figure=arduino_graph,
                            style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        ), className= 'five columns'),

                        ## ARDUINO TEST GRAPH
                        ################

                        # html.Div(dcc.Graph(
                        #     id='humidity_graph',
                        #     figure=humidity_graph,
                        #     style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        # ), className= 'ten columns'),

                        ## OLD??
                        ################

                        # html.Div(dcc.Graph(
                        #     id='PSD',
                        #     figure=psd_graph,
                        #     style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        # ), className= 'five columns'),


                        ## TRYING TO GET A SURFACE GRAPH
                        ################

                        # html.Div(dcc.Graph(
                        #     id='3dgraph',
                        #     figure=_3d_lighting_graph,
                        #     style = {'width': '90%', 'height': '420px', 'display': 'flex', 'align-items': 'right', 'justify-content': 'right'}
                        # ), className= 'five columns'),


                    ]),
                ]),
        ])
#REALTIIIME
#temperature_graph
from dash.dependencies import Input, Output, State

# @app.callback(
#     #utput("temperature_graph", "figure"), 
#     Output('intermediate-value', 'data'), 
#     #Output('xy_graph', 'figure'),
#     Output('vibration_graph', 'figure'),
#     [Input('interval-component', 'n_intervals')],
#     State('intermediate-value', 'data'))
# def update_bar_chart(n, data):

#     visible_graph_max = data

#     saved_time = data+increment
#     timestep = saved_time
    
#     # arduino_temp = arduino_temp[:visible_graph_max]
#     # arduino_humid = arduino_humid[:visible_graph_max]
#     # adc_flight01 = adc_flight01[:visible_graph_max]

#     # # ARDUINO GRAPH
#     # ###############

#     # arduino_graph = make_subplots(specs=[[{"secondary_y": True}]])
#     # #Annotations on Graph
#     # arduino_graph.update_layout(
#     #     title="Environment Monitoring Sensors During Flight",
#     #     title_x=0.5,
#     #     xaxis_title="Time (s)",
#     #     #yaxis_title="Gain",
#     # )
#     # # Set y-axes titles
#     # arduino_graph.update_yaxes(title_text="<b>Temperature</b> (*C)", range=(18.0, 26.3), secondary_y=False)
#     # arduino_graph.update_yaxes(title_text="<b>Humidity(%) and Lighting</b> common axis", range=(30.0, 70.0), secondary_y=True)

#     # #Position Legend
#     # arduino_graph.update_layout(legend=dict(
#     #     orientation='h',
#     #     yanchor="bottom",
#     #     y=0.99,
#     #     xanchor="right",
#     #     x=0.85
#     # ))

#     # #Set Scale
#     # arduino_graph.update_xaxes(range=(0.0, 480.0))
#     # #arduino_graph.update_yaxes(range=(-0.3, 1.0))

#     # # Add Data
#     # arduino_graph.add_trace(
#     #     go.Scattergl(
#     #         x =  arduino_time,
#     #         y =  arduino_temp, #[:visible_graph_max],
#     #         mode='lines',
#     #         name='Temperature',
            
#     #     ), secondary_y=False,
#     # )

#     # arduino_graph.add_trace(
#     #     go.Scatter(
#     #         x =  arduino_time,
#     #         y =  arduino_humid, #[:visible_graph_max],
#     #         mode='lines',
#     #         name='Humidity',
            
#     #     ), secondary_y=True,
#     # )

#     # arduino_graph.add_trace(
#     #     go.Scattergl(
#     #         x =  x_adc,
#     #         y =  adc_flight01, #[:int(visible_graph_max*lighting_alignment)],
#     #         mode='lines',
#     #         name='Lighting',
#     #         marker_color = 'goldenrod'
            
#     #     ), secondary_y=True,
#     # )

#     # # arduino_graph.add_vline(x=visible_graph_max*time_alignment, line=dict(
#     # #     color="Red",
#     # #     width=1,
#     # #     dash="dot",
#     # # ))
#     # arduino_graph.update_traces(marker=dict(size=2),
#     #                     selector=dict(mode='lines'))


#     # # XY GRAPH
#     # ############
#     # xy_graph = go.Figure()

#     # xy_graph.add_layout_image(
#     #         dict(
#     #             source=field_img,
#     #             xref="x",
#     #             yref="y",
#     #             x=-40,
#     #             y=50,
#     #             sizex=130,
#     #             sizey=110,
#     #             sizing="stretch",
#     #             opacity=0.7,
#     #             layer="below",
#     #             )
#     # )
#     # # Set templates
#     # xy_graph.update_layout(template="plotly_white")


#     # #Annotations on Graph
#     # xy_graph.update_layout(
#     #     title="Lighting over the field",
#     #     title_x=0.5,
#     #     xaxis_title="x position (m)",
#     #     yaxis_title="y position (m)",
#     # )


#     # # #Set Scale
#     # xy_graph.update_xaxes(range=(-40.0, 90.0))
#     # xy_graph.update_yaxes(range=(-60, 50.0))

#     # # Add Data
#     # xy_graph.add_trace(
#     #     go.Scattergl(
#     #         x =  x_rotpos, #[:int(visible_graph_max*gps_alignment)],
#     #         y =  y_rotpos, #[:int(visible_graph_max*gps_alignment)],
#     #         mode='markers',
#     #         name='Nacelle moins amortissante',
#     #         marker=dict(
#     #                     color=adc_flight01,
#     #                     colorscale='Viridis')
#     #     ),
#     # )
#     # xy_graph.update_traces(marker=dict(size=2),
#     #                     selector=dict(mode='markers'))

#     psd_graph = go.Figure()

#     psd_graph.update_layout(
#         title="Vibrations measured by Drone Leg Accelerometer During Passage of Person",
#         title_x=0.5,
#         xaxis_title="Time (s)",
#         yaxis_title="Measured acceleration",
#     )
#     # #Annotations on Graph
#     # psd_graph.update_layout(
#     #     title="Gain Difference of 2 Payloads",
#     #     title_x=0.5,
#     #     xaxis_title="Frequency (Hz)",
#     #     yaxis_title="Gain",
#     # )

#     #Position Legend
#     psd_graph.update_layout(legend=dict(
#         yanchor="bottom",
#         y=0.0,
#         xanchor="right",
#         x=0.99
#     ))

#     #Set Scale
#     psd_graph.update_xaxes(range=(16.0, 21.0))
#     psd_graph.update_yaxes(range=(-0.05, 0.07))

#     # Add Data

#     print("len of filtered is", len(vib_pieton_filtered))
#     psd_graph.add_trace(
#         go.Scattergl(
#             x =  time_pieton,
#             y =  vib_pieton_filtered[145000:200000:][:visible_graph_max],
#             # 153000 start of walk #180000 end of
#             mode='markers',
#             name='Vibration pieton',
#             marker_color = 'goldenrod'
#         ),
#     )

#     psd_graph.add_trace(
#         go.Scattergl(
#             x =  time_pieton,
#             y =  vib_pieton[:visible_graph_max],
#             # 153000 start of walk #180000 end of
#             mode='markers',
#             name='Vibration pieton',
#             marker_color = 'red',
#             marker_size = 1
#         ),
#     )


#     psd_graph.update_traces(marker=dict(size=2),
#                         selector=dict(mode='markers'))
#     #return arduino_graph, saved_time, xy_graph, psd_graph
#     return saved_time, psd_graph

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
