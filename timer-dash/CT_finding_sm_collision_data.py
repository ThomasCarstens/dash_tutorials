import pandas as pd

# bot2bot unsuccessful
# collision_time = "/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/stringbot2bot.csv"
# position_at_time = "/home/txa/Documents/data/droneData_alliantech/eval_tests/xr_chore/tf_v2_bot2bot.csv"

# hdi2?
# COLLISION SCRIPT: list of detected collisions from Unity. /cf2pattern from the rosbag associated.
just_collision_position = '/home/txa/Documents/data/droneData_alliantech/eval_tests/bot2bot/df_dronecollisions.csv'
#INPUTS #############
# STRINGS FROM MESSAGE.
collision_time = '/home/txa/Documents/data/droneData_alliantech/eval_tests/bot2bot/events_drone.csv'
# POSITION SCRIPT: /tf from the rosbag associated.
position_at_time = "/home/txa/Documents/data/droneData_alliantech/eval_tests/bot2bot/tf_drone.csv"

get_time = pd.read_csv(collision_time)

every_kill_time = []
for i in range(len(get_time['field.data'])):
    if get_time['field.data'][i] == 'kill':
        print ('test', get_time['%time'][i]//(10**9))
        if len(every_kill_time)>0 and get_time['%time'][i]//(10**9) == every_kill_time[-1]//(10**9): 
            every_kill_time.pop()
        every_kill_time.append(get_time['%time'][i])
        #print(get_time['field.data'].index(value))
        #print(get_time['%time'][0])
#every_kill_time = list(map(int, every_kill_time))
get_position = pd.read_csv(position_at_time)

coincide_array = []
for i in range(len(every_kill_time)):
    # print ("C:", every_kill_time[i])
    # print ("P:", get_position['%time'][i])
    # if len(coincide_array)>0 and every_kill_time[i]//(10**9) == coincide_array[-1]//(10**9): 
    #     coincide_array.pop()

    packet_array = []
    for j in range( len(get_position)):
        if int(get_position['%time'][j])//(10**9) == every_kill_time[i]//(10**9):
            packet_array.append(get_position['%time'][j])

    if len(packet_array)>0:
        coincide_array.append(packet_array)
    if len(packet_array)>1:
        print('it happens')

for each in coincide_array:
    print (each[0])

# 1630746044001918783
# 1630746045003619724
# 1630746046001889434
# 1630746059003908331
# 1630746064002505058
# 1630746065001859703
# 1630746066000923664
# 1630746074001172922
# 1630746075000559201
# 1630746076000808541
# 1630746078000292672
pos_array = []
for each in coincide_array:
    for j in range( len(get_position)):
        if int(get_position['%time'][j]) == each[0]:
            pos_array.append([get_position['%time'][j],
            get_position['field.transforms0.transform.translation.x'][j], 
            get_position['field.transforms0.transform.translation.y'][j], 
            get_position['field.transforms0.transform.translation.z'][j]])

for pos in pos_array:
    print(pos)

fn = open("/home/txa/Documents/data/droneData_alliantech/eval_tests/bot2bot/df_clean_collisions.txt", "w")
fn.write('time, x, y, z\n')
fn.close()
for i in range(len(pos_array)):
    f = open("/home/txa/Documents/data/droneData_alliantech/eval_tests/bot2bot/df_clean_collisions.txt", "a")
    f.write(str(pos_array[i][0])+','+str(pos_array[i][1])+','+str(pos_array[i][2])+','+str(pos_array[i][3])+'\n')
    f.close()