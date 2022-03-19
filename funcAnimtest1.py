import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# creating a blank window
# for the animation
fig = plt.figure()
axis = plt.axes(xlim =(-50, 50),
                ylim =(-50, 50))
 
# line, = axis.plot([], [], lw = 2)
scat = axis.scatter([], [], s=60)
colors_set = plt.get_cmap('viridis')
# what will our line dataset
# contain?
def init():
    # line.set_data([], [])
    # return line,
    scat.set_offsets([])
    return scat,
 
# initializing empty values
# for x and y co-ordinates
xdata, ydata = [], []
lighting_traj_2= pd.read_csv('sensor_performance/lighting_traj.csv')
# animation function
def animate(i):
    # t is a parameter which varies
    # with the frame number
    t = 0.1 * i
     
    # x, y values to be plotted
    x = lighting_traj_2['x']
    y = lighting_traj_2['y']
    # x = t * np.sin(t)
    # y = t * np.cos(t)
    # vel = x
    # appending values to the previously
    # empty x and y data holders
    xdata.append(x)
    ydata.append(y)
    # plt.scatter(x, y, c=lighting_traj_2['light'][i], cmap="viridis")

    # data = np.hstack()
    data = np.hstack((x[:i,np.newaxis], y[:i, np.newaxis]))
    scat.set_offsets(data)
    return scat,

    # line.set_data(xdata, ydata, c=colors_set)
    # anim.event_source.interval = vel
     
    return line,
 
# calling the animation function    
anim = animation.FuncAnimation(fig, animate,
                            init_func = init,
                            frames = len( lighting_traj_2['x'])+1,
                            interval = 1,
                            blit = True)
 
# saves the animation in our desktop
anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)