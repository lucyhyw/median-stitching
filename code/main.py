import numpy as np
import os
from skimage import io, color
from remove import median_filter

def main():
    data_dir = os.path.dirname(__file__) + '../data/'
    # amsterdam_folder = os.path.join(data_dir, "ams")
    # amsterdam_images = []
    # for f in os.listdir(amsterdam_folder):
    #     img = io.imread(os.path.join(amsterdam_folder, f))
    #     if img is not None:
    #         amsterdam_images.append(img)
    # io.imsave('amsterdam.png', median_filter(amsterdam_images))

    # pond_folder = os.path.join(data_dir, "pond")
    # pond_images = []
    # for f in os.listdir(pond_folder):
    #     img = io.imread(os.path.join(pond_folder, f))
    #     if img is not None:
    #         pond_images.append(img)
    # io.imsave('pond.png', median_filter(pond_images))

    lecture_folder = os.path.join(data_dir, "lecture-capture")
    lecture_images = []
    for f in os.listdir(lecture_folder):
        img = io.imread(os.path.join(lecture_folder, f))
        if img is not None:
            lecture_images.append(img)
    io.imsave('lecture.png', median_filter(lecture_images))

if __name__ == '__main__':
    main()
