## read and resized images
# pip install opencv-python

import glob
import cv2
import numpy as np
import os

target_size = (128, 128)

def read_resize_images(source_dir , categories):
    x_temp = []
    y_temp = []
    for category in categories:
        for filepath in glob.glob(os.path.join(source_dir, category, "*")):
            label = 0 if category == "cats" else 1
            img = cv2.imread(filepath)
            img = cv2.resize(img, target_size)
            img = np.array(img)
            y_temp.append(label)
            x_temp.append(img)

    print("folder: " + os.path.join(source_dir))
    print(len(x_temp)) 
    print(x_temp[0])   
    return x_temp , y_temp

# source file, catefories list
x_train , y_train = read_resize_images( "D:\\Artificial Intelligence\\Machine Learning\\_projects\\dogs_cats_classification\\data\\processed\\train", ["cat", "dog"])
x_test , y_test = read_resize_images( "D:\\Artificial Intelligence\\Machine Learning\\_projects\\dogs_cats_classification\\data\\processed\\test", ["cat", "dog"])
x_val , y_val = read_resize_images( "D:\\Artificial Intelligence\\Machine Learning\\_projects\\dogs_cats_classification\\data\\processed\\val", ["cat", "dog"])

