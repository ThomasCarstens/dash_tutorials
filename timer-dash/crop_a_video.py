
import cv2

# top, right, bottom, left = 10, 450+10, 360+10, 10  # Sample values.

# BOT_CROP
top_drift = 0
left_drift = 820
top= top_drift
right = 450+left_drift
bottom = 360+top_drift
left = left_drift  # Sample values.

# top_drift = 5
# left_drift = 450
# top= top_drift
# right = 450+left_drift
# bottom = 360+top_drift
# left = left_drift  # Sample values.

input_video = cv2.VideoCapture('/home/txa/Documents/data/eval_tests/videos/trimmed/dragon_trim.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('/home/txa/Documents/data/eval_tests/videos/dragon.avi', fourcc, 30, (450, 360))

while True:
    ret, frame = input_video.read()

    if not ret:
        break

    # Following crop assumes the video is colored, 
    # in case it's Grayscale, you may use: crop_img = frame[top:bottom, left:right]  
    crop_img = frame[top:bottom, left:right, :]

    output_movie.write(crop_img)


# Closes the video writer.
output_movie.release()


# import numpy as np
# import cv2

# # Open the video
# cap = cv2.VideoCapture('/home/txa/Documents/data/eval_tests/videos/trimmed/human_bot_drone.mp4')

# # Initialize frame counter
# cnt = 0

# # Some characteristics from the original video
# w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

# # Here you can define your croping values
# x,y,h,w = 0,400,400,400

# # output
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('/home/txa/Documents/data/eval_tests/videos/result.avi', fourcc, fps, (w, h))
# # fourcc = cv2.FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
# # videoOut = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

# # Now we start
# while(cap.isOpened()):
#     ret, frame = cap.read()

#     cnt += 1 # Counting frames

#     # Avoid problems when video finish
#     if ret==True:
#         # Croping the frame
#         crop_frame = frame[y:y+h, x:x+w]

#         # Percentage
#         xx = cnt *100/frames
#         print(int(xx),'%')

#         # Saving from the desired frames
#         #if 15 <= cnt <= 90:
#         #    out.write(crop_frame)

#         # I see the answer now. Here you save all the video
#         out.write(crop_frame)

#         # Just to see the video in real time          
#         cv2.imshow('frame',frame)
#         cv2.imshow('croped',crop_frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break


# cap.release()
# out.release()
# cv2.destroyAllWindows()