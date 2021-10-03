

# UNVERIFIED
# Attempt to automate csv>bag from google drive.
# Now possible with link file.

import os
import pandas as pd
def convert2df(url):
    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    print(path)
    os.system("rostopic echo -b " + path + " -p /tf >> ~/Downloads/tf_human_drone.csv")
    df = pd.read_csv("~/Downloads/tf_human_drone.csv")
    if df.empty:
        print('empty')
    return df

bag_path = "https://drive.google.com/file/d/1flPma71EcR_LP-wdNKMo5MSKyBH-Oh_H/view?usp=sharing"
#get bag on system.

# with open(bag_path, "r") as f:
#     notes = f.readlines()

notes = convert2df(bag_path)
print (notes)

# bag_system = 
# #then get bag to csv.
# os.system("rostopic echo -b", bag_system, " -p /tf >> ~/Downloads/tf_human_drone.csv")