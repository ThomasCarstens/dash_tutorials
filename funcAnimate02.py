import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd
img = plt.imread("assets/fond_tourne.png") 
img2 = plt.imread("assets/test_site.png") 
lighting_traj_2= pd.read_csv('sensor_performance/lighting_traj.csv')
x = lighting_traj_2['x']
y = lighting_traj_2['y']
L = lighting_traj_2['light']
time_steps = 500
N_nodes = time_steps*2

positions = []
solutions = []
for i in range(time_steps):
    positions.append(np.random.rand(2, N_nodes))
    solutions.append(np.random.random(N_nodes))

solutions = np.array(solutions)
# c = solutions[0],
print('colorbar range: [', min(L), ',', max(L), ']')
print('shapes of c:', solutions.shape, ' and x, ', x.shape)
# init the figure, so the colorbar can be initially placed somewhere
marker_size = 7
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(0-15, 40+15), ylim=(-40, 30))
s = ax.scatter(x[0], y[0], s = marker_size, c = L[0], cmap = "viridis", vmin = int(min(L)), vmax = int(max(L)), marker = ".", edgecolor = None)
ax.imshow(img, extent=[0-15, 40+15, -40, 30])
cb = fig.colorbar(s)

# get the axis for the colobar
cax = cb.ax

trim = 60

def animate(i):
    """ Perform animation step. """
    # clear both plotting axis and colorbar axis
    #ax.clear()
    #cax.cla()
    #the new axes must be re-formatted
    #ax.set_xlim(0,1)
    #ax.set_ylim(0,1)
    #ax.grid(b=None)
    #ax.set_xlabel('x [m]')
    #ax.set_ylabel('y [m]')
    # and the elements for this frame are added
    #ax.text(0.02, 0.95, 'Time step = %d' % i, transform=ax.transAxes)

    s = ax.scatter(x[i*trim], y[i*trim], s = marker_size, c = L[i*trim], cmap = "YlOrRd", vmin = min(L), vmax = max(L), marker = ".", edgecolor = None)
    fig.colorbar(s, cax=cax)
    # plt.clim(0, 20) 

ani = animation.FuncAnimation(fig, animate, interval=50, frames=range(time_steps))

ani.save('animation2.gif', writer='pillow')