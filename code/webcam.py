import cv2
import time
import numpy as np
from skimage import io, transform
from remove import median_filter

SECONDS = 10

vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

i = 0
curr_time = time.time()
imgs = []

while rval and i < 10000:
    rval, frame = vc.read()
    if (time.time() - curr_time >= SECONDS):
        imgs.append(frame) # add the current image to img array
        if (len(imgs) % 2 != 0):
            med = np.array(median_filter(imgs), dtype=np.uint8)
            height, width, _ = np.array(frame).shape
            resized = transform.resize(med,(height//2, width//2))
            cv2.imshow('webcam', resized)
        curr_time = time.time()
    i += 1
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
