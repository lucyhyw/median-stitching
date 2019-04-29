import numpy as np
import os
import sys
from skimage import io, color
from remove import median_filter, mode_filter, subtract

def main(folder):
    data_dir = os.path.dirname(__file__) + '../data/'
    # img0 = io.imread(os.path.join(green_folder, "009.jpg"))
    # print(img0)
    # img1 = io.imread(os.path.join(green_folder, "009.jpg"), as_gray=True)
    # img2 = io.imread(green_saved, as_gray=True)
    # io.imsave('hahaha.png', subtract(img0,img1,img2))

    img_folder = os.path.join(data_dir, folder)
    images = []
    for f in os.listdir(img_folder):
        img = io.imread(os.path.join(img_folder, f))
        if img is not None:
            images.append(img)
    if (len(images) % 2 == 0):
        images = images[0:-1] # remove last image if odd number
    io.imsave(folder + '.png', median_filter(images))
    #io.imsave(folder + '-mode.png', mode_filter(images))

if __name__ == '__main__':
    folder = 'ams' if len(sys.argv) == 1 else sys.argv[1]
    main(folder)
