import logging
import time
import numpy as np

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

#Step-by-Step: Motion Commander
#https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/user-guides/sbs_motion_commander/

URI = 'radio://0/27/2M/E7E7E7E7E7'
DEFAULT_HEIGHT = 0.3
DEFAULT_TRANSLATION = 0.3
# spiral_points = [[0, DEFAULT_TRANSLATION, 0],
#                 [DEFAULT_TRANSLATION, 0, 0], 
#                 [0, -DEFAULT_TRANSLATION, 0],
#                 [-DEFAULT_TRANSLATION, 0, 0]
#                 ]
is_deck_attached = True

numRobots = 1
r = 0.8
height = 0.3
final_height = 1.0
w = 2 * np.pi / numRobots
T = 2* 2 * np.pi / w #txa: decreased it assuming it gives more  points.
spiral_increment_x = []
spiral_increment_y = []
spiral_points = []
spiral_absolute = []
phase =0
nb_points = 100
height_increment = height
for t in np.linspace(0, T, nb_points):
    height_increment += (final_height - height) / nb_points 
    absolute_pt = [r * np.cos(w * t + phase), r * np.sin(w * t + phase), height_increment]
    spiral_absolute.append (absolute_pt)
    if t != 0:
        t0=t-1
        relative_pt = []
        zip_object = zip(spiral_absolute[-1], spiral_absolute[-2])
        for now_i, before_i in zip_object:
            relative_pt.append(now_i-before_i)
        #relative_pt = spiral_absolute[-1] - spiral_absolute[-2]
        spiral_points.append (relative_pt)

print (len(spiral_points))


logging.basicConfig(level=logging.ERROR)

def simple_log(scf, logconf):
    with SyncLogger(scf, lg_stab) as logger:

        for log_entry in logger:

            timestamp = log_entry[0]
            data = log_entry[1]
            logconf_name = log_entry[2]

            print('[%d][%s]: %s' % (timestamp, logconf_name, data))

            #break

def move_linear_simple(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        time.sleep(1)
        mc.forward(DEFAULT_TRANSLATION)
        time.sleep(1)
        mc.back(DEFAULT_TRANSLATION)
        time.sleep(1)

def take_off_simple(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        time.sleep(3)
        mc.stop()

#mc.circle_right(0.5, velocity=0.5, angle_degrees=180)
def move_circle_simple(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        mc.circle_right(0.3, velocity=0.3)
        time.sleep(3)
        mc.stop()
#move_distance(self, distance_x_m, distance_y_m, distance_z_m,
#                      velocity=VELOCITY)
def move_translation(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        mc.move_distance(distance_x_m=DEFAULT_TRANSLATION, distance_y_m=DEFAULT_TRANSLATION, distance_z_m=DEFAULT_TRANSLATION,
                      velocity=0.3)
        time.sleep(1)
        mc.stop()

def move_square(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        for vector3 in spiral_points:
            mc.move_distance(distance_x_m=vector3[0], distance_y_m=vector3[1], distance_z_m=vector3[2],
                        velocity=0.5)
            #time.sleep(1)
        mc.stop()

def param_deck_flow(name, value_str):
    value = int(value_str)
    print(value)
    global is_deck_attached
    if value:
        is_deck_attached = True
        print('Deck is attached!')
    else:
        is_deck_attached = False
        print('Deck is NOT attached!')

def log_pos_callback(timestamp, data, logconf):
    spiral_increment_x.append(data['stateEstimate.x'])
    spiral_increment_y.append(data['stateEstimate.y'])
    print( spiral_increment_x, spiral_increment_y )

if __name__ == '__main__':

    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                        cb=param_deck_flow)
        time.sleep(1)

        logconf = LogConfig(name='Position', period_in_ms=10)
        logconf.add_variable('stateEstimate.x', 'float')
        logconf.add_variable('stateEstimate.y', 'float')
        scf.cf.log.add_config(logconf)
        logconf.data_received_cb.add_callback(log_pos_callback)

        if is_deck_attached:
            logconf.start()
            move_square(scf)
            logconf.stop()