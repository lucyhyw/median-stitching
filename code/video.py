import numpy as np
import cv2
from remove import median_filter

cap = cv2.VideoCapture('./green.mov')
allFrames = []
frames = np.arange(0, 10700, 15)
ret = True
WINDOW_SIZE = 40

while(cap.isOpened() and ret):
    ret, frame = cap.read()

    if ret:
        allFrames.append(np.array(frame))

allFrames = np.array(allFrames)
framesWeWant = np.array([allFrames[i] for i in frames])

height, width, layers = allFrames[0].shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('green_video.avi',fourcc,8,(width,height))
for i in range(len(framesWeWant)):
    if (i < WINDOW_SIZE):
        video.write(np.uint8(median_filter(framesWeWant[i: i + WINDOW_SIZE+1: 10,:,:,:])))
    elif (i >= len(framesWeWant) - WINDOW_SIZE):
        video.write(np.uint8(median_filter(framesWeWant[i-WINDOW_SIZE: i+1: 10,:,:,:])))
    else:
        video.write(np.uint8(median_filter(framesWeWant[i-WINDOW_SIZE: i+WINDOW_SIZE + 1: 10,:,:,:])))

cap.release()
video.release()
cv2.destroyAllWindows()
