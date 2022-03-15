import cv2
vidcap = cv2.VideoCapture('/home/txa/Documents/DashBeginnerTutorials/cutup_frames/DJI_0199.MP4')
success,image = vidcap.read()
count = 0
while success:
  #   cv2.imwrite("/home/txa/Documents/DashBeginnerTutorials/cutup_frames/nature/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
    # print('Read a new frame: ', success)
  if count % 150 == 0:
    cv2.imwrite("/home/txa/Documents/DashBeginnerTutorials/cutup_frames/nature/19frame%d.jpg" % count, image)     # save frame as JPEG file
  # if count > 700 and count < 800:
  #   if count % 20 == 0:
  #     cv2.imwrite("/home/txa/Documents/DashBeginnerTutorials/cutup_frames/nature/me%d.jpg" % count, image)     # save frame as JPEG file

  if count > 440 and count < 460:
    if count % 5 == 0:
      cv2.imwrite("/home/txa/Documents/DashBeginnerTutorials/cutup_frames/nature/19me%d.jpg" % count, image)     # save frame as JPEG file



  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1
