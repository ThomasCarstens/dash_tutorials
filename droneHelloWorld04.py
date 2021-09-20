import numpy as np

# DRAWING A CUSTOM CIRCLE (SPIRAL LATER)

numRobots = 2

r = 0.3
height = 0.3
w = 2 * np.pi / numRobots
T = 2 * 2 * np.pi / w #txa: decreased it assuming it gives more  points.
#T = 100
# # horizontal circles
# for i in range(0, numRobots):
# 	phase = 6 * np.pi / numRobots * i

# 	with open("timed_waypoints_circle{}.csv".format(i), "w") as f:
# 		f.write("t,x,y,z\n")

# 		for t in np.linspace(0, T, 10):
# 			f.write("{},{},{},{}\n".format(t, r * np.cos(w * t + phase), r * np.sin(w * t + phase), height))

# list1 = [2, 2, 2]
# list2 = [1, 1, 1]
# difference = []
# zip_object = zip(list1, list2)
# for list1_i, list2_i in zip_object:
#     difference.append(list1_i-list2_i)
# print(difference)

spiral_points = []
spiral_absolute = []
phase =0
for t in np.linspace(0, T, 100):
    absolute_pt = [r * np.cos(w * t + phase), r * np.sin(w * t + phase), height]
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