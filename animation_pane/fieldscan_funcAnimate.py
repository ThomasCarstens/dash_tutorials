import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd
img = plt.imread("assets/fond_tourne.png") 
img2 = plt.imread("assets/test_site.png") 

# This script is designed for plotting a smooth trajectory with a colour included.
#       AFTER DECIDING ON CONFIG: colour and data_offset: https://matplotlib.org/stable/tutorials/colors/colormaps.html
#       FIGURE OUT: trim (speed of traj)

# Choose one: LIGHT, HUMIDITY, TEMPERATURE
sensor = "HUMIDITY"
trim = 60 # batches of _ messages per point. Original frequency is: ...
version = "01"
time_steps = 500 # speed (maybe full execution?) on gif.


# Gathered data from AT_realtime_bar.py (with data rotations)
atmos_traj = pd.read_csv('sensor_performance/atmos_traj.csv')
x = np.array(atmos_traj['x'])
y = np.array(atmos_traj['y'])
L = np.array(atmos_traj['light'])
H = np.array(atmos_traj['humid'])
T = np.array(atmos_traj['temp'])


# for sensor: "LIGHT", x: x[:-830], y: y[:-830], colour: L[830:], colour:YlOrRd, 
humidity_offset = 830
temperature_offset = 0 
config = {"LIGHT": {"x": x, "y": y, "data": L, "colour":"YlOrRd", "path": "lightscan_v"+version+".gif" },
            "HUMIDITY": {"x": x[:-humidity_offset], "y": y[:-humidity_offset], "data": H[humidity_offset:], "colour":"YlOrRd", "path": "humidscan_v"+version+".gif"},
            "TEMPERATURE": {"x": x[:-temperature_offset], "y": y[:-temperature_offset], "data": T[temperature_offset:], "colour":"YlOrRd", "path": "tempscan_v"+version+".gif"},

}

# init the figure, so the colorbar can be initially placed somewhere
marker_size = 10
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(0-15, 40+15), ylim=(-40, 30))
s = ax.scatter(config[sensor]["x"][0], config[sensor]["y"][0], s = marker_size, c = config[sensor]["data"][0], cmap = config[sensor]["colour"], vmin = int(min(config[sensor]["data"])), vmax = int(max(config[sensor]["data"])), marker = ".", edgecolor = None)
ax.imshow(img, extent=[0-15, 40+15, -40, 30])
cb = fig.colorbar(s)

# get the axis for the colobar
cax = cb.ax



def animate(i):
    """ Perform animation step. """
    s = ax.scatter(config[sensor]["x"][i*trim], config[sensor]["y"][i*trim], s = marker_size, c = config[sensor]["data"][i*trim], cmap = config[sensor]["colour"], vmin = min(config[sensor]["data"]), vmax = max(config[sensor]["data"]), marker = ".", edgecolor = None)
    fig.colorbar(s, cax=cax)


ani = animation.FuncAnimation(fig, animate, interval=50, frames=range(time_steps))

ani.save(config[sensor]["path"], writer='pillow')