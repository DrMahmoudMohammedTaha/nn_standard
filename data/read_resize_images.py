
# pip install opencv-python

import glob
import cv2
import numpy as np
import os

target_size = (128, 128)

def read_resize_images(source_dir , categories):
    temp_list = []
    for category in categories:
        for filepath in glob.glob(os.path.join(source_dir, category, "*")):
            label = 0 if category == "cats" else 1
            img = cv2.imread(filepath)
            img = cv2.resize(img, target_size)
            temp_list.append((img, label))

    print("folder: " + os.path.join(source_dir))
    print(len(temp_list)) 
    print(temp_list[0])   
    return temp_list

# source file, catefories list
train_list = read_resize_images( "D:\\Artificial Intelligence\\Machine Learning\\_projects\\dogs_cats_classification\\data\\processed\\train", ["cat", "dog"])
test_list = read_resize_images( "D:\\Artificial Intelligence\\Machine Learning\\_projects\\dogs_cats_classification\\data\\processed\\test", ["cat", "dog"])
val_list = read_resize_images( "D:\\Artificial Intelligence\\Machine Learning\\_projects\\dogs_cats_classification\\data\\processed\\val", ["cat", "dog"])

