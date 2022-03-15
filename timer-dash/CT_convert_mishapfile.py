# Toolset: Thesis
# Convert poorly formatted Unity File from the recording (0.1 version, 29 Sept 2021) 
# to csv format (for use as dataframe)

import pandas as pd
#INPUT: .txt 
#OUTPUT: .txt (manually change to .csv) readable as a df.
#NEXT STEPS: timer-dash/CT_finding_sm_collision_data.py

#bot2bot_botpath = '/home/txa/Documents/data/eval_tests/bot2bot/pos_bot_bot2bot.txt'
bot2bot_dronepath = '/home/txa/Documents/data/droneData_alliantech/xr_processing/1630745389NinjaskSphere(UnityEngine.Transform)gameobject.txt'
bot2bot_botpath = '/home/txa/Documents/data/droneData_alliantech/xr_processing/1630745389DragonSphere(UnityEngine.Transform)gameobject.txt'
output_drone_path = "/home/txa/Documents/data/droneData_alliantech/xr_processing/df_drone_pos.txt"
output_bot_path = "/home/txa/Documents/data/droneData_alliantech/xr_processing/df_bot_pos.txt"

# INPUT file
#df_xr_version = pd.read_csv('/home/txa/Documents/data/eval_tests/xr_chore/1630749025Dragon.txt', decimal=',')
with open(bot2bot_botpath, "r") as f:
    notes = f.readlines()

# OUTPUT file in FOLDER (previously created)
fn = open(output_bot_path, "w")
fn.write('time, x, y, z\n')
fn.close()
#print (notes)
df_xr_version = pd.DataFrame({})
for position in notes:
    #print (notes.index(position))
    if position.count(',') != 7: #safe divide at: (0) 1 (2) 3 (4) 5 (6) 7
        print (position)
        continue
    position_array = position.split(',')
    time = position_array[0]+'.'+position_array[1]
    x = position_array[2]+'.'+position_array[3]
    y = position_array[4]+'.'+position_array[5]
    z = position_array[6]+'.'+position_array[7][:-2]
    f = open(output_bot_path, "a")
    f.write(str(time)+','+str(x)+','+str(y)+','+str(z)+'\n')
    f.close()

print (f)
#     df_line = pd.DataFrame(
#         {
#             "time": [time],
#             "x": [x],
#             "y": [y],
#             "z": [z],
#         },
#         index= [0+notes.index(position), 1+notes.index(position), 
#         2+notes.index(position), 3+notes.index(position)]         #[notes.index(position)],
#     )
#     frames = [df_xr_version, df_line]
#     result = pd.concat(frames)
# print (result)
    #df_xr_version[{''}]
    # for digits in position:
    # if digits.index % 2 == 0 : # if even
    #     position.replace(',', new='.', 1)

# print (notes)
