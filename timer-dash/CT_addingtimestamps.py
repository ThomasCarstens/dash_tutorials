import sys
import os
import csv
import rosbag
import rospy

##################
# DESCRIPTION:
# Creates CSV file from a string: two colums: time(nanosecond unix timestamp) 
#                                              and signal(string from our protocol)
# 
# USAGE EXAMPLE:
# BEFORE ARG EDIT:
# rosrun your_package get_jstate_csvs.py /root/catkin_ws/bagfiles your_bagfile.bag
# NOW: add script below.
# ##################

filename = 'hand_test1.bag' #sys.argv[2]
directory = '/home/txa/Documents/data/droneData_alliantech/eval_tests/ht1/'#sys.argv[1]
print("Reading the rosbag file")
if not directory.endswith("/"):
  directory += "/"
extension = ""
if not filename.endswith(".bag"):
  extension = ".bag"
bag = rosbag.Bag(directory + filename + extension)

# Create directory with name filename (without extension)
results_dir = directory + filename[:-4] + "_results"
if not os.path.exists(results_dir):
  os.makedirs(results_dir)

print("Writing robot joint state data to CSV")

with open('timestamped_gestures.csv', mode='w') as data_file:
  data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  data_writer.writerow(['time', 'hand_signal'])
  # Get all message on the /joint states topic
  for topic, msg, t in bag.read_messages(topics=['/hand_signal']):
    signal = msg.data
    data_writer.writerow([t, signal])

print("Finished creating csv file!")
bag.close()