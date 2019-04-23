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

def subtract(img0, img1, img2):
    w,h,c = img0.shape
    res = np.zeros((w,h, c))
    channel1 = img1
    channel2 = img2
    greyscaleMask = np.array(np.clip(channel1 - channel2, 0, 1))#.astype(int)
    for i in range(c):
        res[:,:,i] = img0[:,:,i] * greyscaleMask + 10
    return np.array(res).astype(int)

if __name__ == '__main__':
    main()
