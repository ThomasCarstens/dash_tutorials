import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd
img = plt.imread("assets/fond_tourne.png") 
img2 = plt.imread("assets/test_site.png") 

# This script is designed for plotting a smooth trajectory with a colour included.
#       AFTER DECIDING ON CONFIG: colour and data_offset.
#       FIGURE OUT: trim (speed of traj)

# Choose one: LIGHT, HUMIDITY, TEMPERATURE
sensor = "HUMIDITY"
trim = 1000 # batches of _ messages per point. Original frequency is: ...
version = "01"
time_steps = 500 # speed (maybe full execution?) on gif.

            # df_smlatency = pd.DataFrame({
            #                             'delays_time': (delays_time),
            #                             'delays': (delays),
            #                             'sim_time': (time_xr)[lower_bound:],
            #                             'x': (drone_xr_x)[lower_bound:], 
            #                             'y': (drone_xr_y)[lower_bound:],
            #                             'z': (drone_xr_z)[lower_bound:]
                                        
            #                             })
# Gathered data from WEB_arcade_dashboard_1.py (with data rotations)
df_smlatency = pd.read_csv('sensor_performance/smlatency.csv')
df_smvisual = pd.read_csv('sensor_performance/df_smvisual.csv')
delays_time = np.array(df_smlatency['delays_time'])
delays = np.array(df_smlatency['delays'])

t = np.array(df_smvisual['sim_time'])
x = np.array(df_smvisual['x'])
y = np.array(df_smvisual['y'])
z = np.array(df_smvisual['z'])

# init the figure, so the colorbar can be initially placed somewhere
marker_size = 7
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False , xlim=(delays_time[0], delays_time[-1]), ylim=(0, 60)) 

s = ax.scatter(delays_time[0], delays[0], s = marker_size, marker = ".", edgecolor = None)
ax.imshow(img, extent=[0-15, 40+15, -40, 30])
# cb = fig.colorbar(s)

# get the axis for the colobar
# cax = cb.ax

def animate(i):
    """ Perform animation step. """
    s = ax.scatter(delays_time[i], delays[i], s = marker_size, marker = ".", edgecolor = None)
    # fig.colorbar(s, cax=cax)


ani = animation.FuncAnimation(fig, animate, interval=50, frames=range(time_steps))

ani.save("latency_v"+version+".gif", writer='pillow')