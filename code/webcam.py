import cv2
import time
import numpy as np
from skimage import io, transform
from remove import median_filter

MAX_SIZE = 1000
HIGH_FREQ = 100
LOW_FREQ = 10

imgs = []

def update_imgs(vc):
    rval, frame = vc.read()
    height, width, _ = np.array(frame).shape
    resized = transform.resize(frame, (height//2, width//2), preserve_range=True)

    if (len(imgs) >= MAX_SIZE):
        imgs.pop(0)
    imgs.append(resized) # add the current image to img array
    return rval

def apply_median_filter(temp):
    if (len(temp) % 2 == 0):
        temp.pop(0)
    return np.array(median_filter(temp), dtype=np.uint8)

def low_frequency(index):
    temp = imgs[index % LOW_FREQ :: LOW_FREQ]
    cv2.imshow('webcam', apply_median_filter(temp))
    key = cv2.waitKey(1)
    return key != 27

def high_frequency(index):
    if (len(imgs) < MAX_SIZE):
        temp = imgs[index % FREQUENCY :: FREQUENCY]
    else:
        temp = imgs[0 :: FREQUENCY]

    cv2.imshow('webcam', apply_median_filter(temp))
    key = cv2.waitKey(1)
    return key != 27

def main():
    vc = cv2.VideoCapture(0)
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
    i = 0
    while rval and i < 10000:
        rval = update_imgs(vc)
        if (i <= 2 * HIGH_FREQ):
            rval = low_frequency(i)
        else:
            rval = high_frequency(i)
        i += 1
    cv2.destroyWindow("preview")

if __name__ == '__main__':
    main()
