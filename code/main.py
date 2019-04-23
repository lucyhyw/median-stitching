import numpy as np
import os
import sys
from skimage import io, color
from remove import median_filter, mode_filter, subtract

def main(folder):
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

    # lecture_folder = os.path.join(data_dir, "lecture-capture")
    # lecture_images = []
    # for f in os.listdir(lecture_folder):
    #     img = io.imread(os.path.join(lecture_folder, f))
    #     if img is not None:
    #         lecture_images.append(img)
    # io.imsave('lecture.png', median_filter(lecture_images))

    green_folder = os.path.join(data_dir, "green")
    # green_images = []
    # num_images = len(os.listdir(green_folder))
    # if (num_images % 2 == 0): # if we have an even number of images
    #     last_img = os.listdir(green_folder)[num_images - 1] # pick last image
    #     file_last_img = os.path.join(green_folder, last_img)
    #     print(file_last_img)
    #     os.system("cp " + file_last_img + " " + os.path.join(green_folder, "duplicate.jpg"))
    # for f in os.listdir(green_folder):
    #     img = io.imread(os.path.join(green_folder, f))
    #     if img is not None:
    #         green_images.append(img)
    # io.imsave('green.png', median_filter(green_images))
    green_folder = os.path.join(data_dir, "green")
    green_saved = "green.png"
    img0 = io.imread(os.path.join(green_folder, "009.jpg"))
    img1 = io.imread(os.path.join(green_folder, "009.jpg"), as_gray=True)
    img2 = io.imread(green_saved, as_gray=True)
    io.imsave('hahaha.png', subtract(img0,img1,img2))
    # img_folder = os.path.join(data_dir, folder)
    # images = []
    # for f in os.listdir(img_folder):
    #     img = io.imread(os.path.join(img_folder, f))
    #     if img is not None:
    #         images.append(img)
    # io.imsave(folder + '.png', median_filter(images))
    # #io.imsave(folder + '-mode.png', mode_filter(images))

if __name__ == '__main__':
    folder = 'ams' if len(sys.argv) == 1 else sys.argv[1]
    main(folder)
