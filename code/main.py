import numpy as np
import os
from skimage import io, color
from remove import median_filter

def main():
    data_dir = os.path.dirname(__file__) + '../data/'
    amsterdam_folder = os.path.join(data_dir, "ams")
    amsterdam_images = []
    for f in os.listdir(amsterdam_folder):
        img = io.imread(os.path.join(amsterdam_folder, f))
        if img is not None:
            amsterdam_images.append(img)
    io.imsave('test.png', median_filter(amsterdam_images))

if __name__ == '__main__':
    main()
