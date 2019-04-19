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
    print("res")
    print(res)
    return np.array(res).astype(int)

if __name__ == '__main__':
    main()
