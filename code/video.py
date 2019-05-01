import numpy as np
import cv2
from remove import median_filter

cap = cv2.VideoCapture('./green.mov')
allFrames = []
frames = np.arange(0, 2250, 15)
ret = True

while(cap.isOpened() and ret):
    ret, frame = cap.read()

    if ret:
        allFrames.append(np.array(frame))

allFrames = np.array(allFrames)
framesWeWant = np.array([allFrames[i] for i in frames])

height, width, layers = allFrames[0].shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('green_video.avi',fourcc,2,(width,height))
for frame in framesWeWant:
    video.write(frame)

cap.release()
video.release()
cv2.destroyAllWindows()
