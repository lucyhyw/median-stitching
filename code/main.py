import numpy as np
import os
import sys
from skimage import io, color
from remove import median_filter, mode_filter, subtract

def main(folder):
    data_dir = os.path.dirname(__file__) + '../data/'

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
