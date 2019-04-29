import numpy as np
import os
from skimage import io
from scipy import signal

def median_filter(images):
    img_arr = np.array(images)
    n,w,h,c = img_arr.shape
    res = np.zeros((w,h,c))
    for i in range(c): # three rgb channels:
        channel = img_arr[:,:,:,i]
        print(channel)
        res[:,:,i] = signal.medfilt(channel, kernel_size=(n,1,1))[n//2]
    # print("res")
    # print(res)
    return np.array(res).astype(int)

def subtract(img1, img2):
    w,h,c = img1.shape
    res = np.zeros((w,h,c))
    for i in range(c):
        channel1 = np.round(img1[:,:,i]).astype(int)
        channel2 = np.round(img2[:,:,i]).astype(int)
        res[:,:,i] = (channel1 - channel2) * 2
        # print(chan100:200,100:200,i])
    # print(res)
    return np.array(np.clip(res, 0, 255)).astype(int)

def mode_filter(images):
    img_arr = np.array(images)
    n,w,h,c = img_arr.shape
    res = np.zeros((w,h,c))
    for i in range(c): # three rgb channels:
        channel = img_arr[:,:,:,i]
        res[:,:,i], _ = stats.mode(channel, axis=0)
    return np.array(res).astype(int)

if __name__ == '__main__':
    main()
