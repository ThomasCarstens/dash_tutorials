import cv2
import numpy as np
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_movie_from_frames
from moviepy.config import get_setting
from moviepy.tools import subprocess_call
# start_time = (5*60)+40
# end_time = (6*60)+10
# ffmpeg_extract_subclip("/home/txa/Documents/data/eval_tests/videos/BotDrone.mkv", start_time, end_time, targetname="/home/txa/Documents/data/eval_tests/videos/BotDrone_trim.mp4")

# fps = 60
# folder = "/home/txa/Documents/data/eval_tests/videos/avoid_pics"
# filename = "/home/txa/Documents/avoid.gif"
# def gif_maker(filename, folder, fps, digits=300, bitrate= 4096):
#     s = "frame" + "%02d" % (digits+300) + ".jpg"
#     cmd = [get_setting("FFMPEG_BINARY"), "-y", "-f","image2",
#              "-r", "%d"%fps,
#              "-i", os.path.join(folder,folder) + '/' + s,
#              "-b:v", "%dk"%bitrate,
#              "-r", "%d"%fps,
#              filename]
    
#     subprocess_call(cmd)
# gif_maker(filename, folder, fps, digits=6, bitrate= 4096)
# filenames = []
# for i in range (300, 601):
#     filenames.append("/home/txa/Documents/data/eval_tests/videos/avoid_pics/frame"+str(i)+".jpg")


# import imageio
# with imageio.get_writer('/home/txa/Documents/avoid.gif', mode='I') as writer:
#     for filename in filenames:
#         image = imageio.imread(filename)
#         writer.append_data(image)
# # ffmpeg_merge_video_audio(video,audio,output, vcodec='copy',
# #                              acodec='copy', ffmpeg_output=False,
# #                              logger = 'bar')

########## TIMESTAMPS
######################

# CHORE_TRIM: /home/txa/Documents/data/eval_tests/videos/XR_chore.mkv
# start_time = (4*60)
# end_time = (4*60)+57

# HDI_TRIM: /home/txa/Documents/data/eval_tests/videos/IntroHDI.mkv
# start_time = (8*60)
# end_time = (8*60)+18

# # DRAGON_TRIM
# start_time = (7*60)+35
# end_time = (7*60)+45

# BOT AND DRONE
# start_time = (5*60)+40
# end_time = (6*60)+10

print(os. getcwd())
cap = cv2.VideoCapture("/home/txa/Downloads/Drone demo for the DVIC website.mp4")
#out = cv2.VideoWriter('first_search.mp4', -1, 20.0, (640,480))

count = 0
while(True):
    ret, frame = cap.read()
    if ret:

        # hsv is better to recognize color, convert the BGR frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # in hsv red color located in two region. Create the mask for red color
        # mask the red color and get an grayscale output where red is white
        # everything else are black

        #mask = cv2.inRange(hsv, (0,50,30), (180,255,255)) #hue, saturation, value

        #mask2 = cv2.inRange(hsv, (175,50,20), (180,255,255)) 
        #mask = cv2.bitwise_or(mask1, mask2)

        #(0,50,30) to (180,255,255)
        #HUE:
        #SAT:
        #VAL:

        # get the index of the white areas and make them orange in the main frame
        # for i in zip(*np.where(mask == 255)):
        #         frame[i[0], i[1], 0] = 255
        #         frame[i[0], i[1], 1] = 255
        #         frame[i[0], i[1], 2] = 255
        #out.write(frame)
        
        every_x_frames = 1
        if count%every_x_frames == 0:
            cv2.imwrite("/home/txa/Downloads/chore_pics/frame%d.jpg" % count, frame)     # save frame as JPEG file
        count += 1
        # play the new video
        # cv2.imshow("res",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:

        break

# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()