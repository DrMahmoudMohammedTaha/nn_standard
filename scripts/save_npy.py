

import os
import numpy as np
from PIL import Image

def save_npy(images_folder):

    # List to store image data
    image_data = []

    # Iterate over the images in the directory
    for filename in os.listdir(images_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Add more extensions if needed
            # Load image and convert to grayscale if necessary
            image = Image.open(os.path.join(images_folder, filename))
            # Convert image to numpy array and append to the list
            image_data.append(np.array(image))

    # Convert the list of numpy arrays to a single numpy array
    image_data = np.array(image_data)

    # Save the numpy array to .npy file
    np.save( images_folder + ".npy", image_data)

save_npy("D:\\Artificial Intelligence\\Machine Learning\\_projects\\nn_mnist\\data\\train\\0")

# image_data = np.load("D:\\Artificial Intelligence\\Machine Learning\\_projects\\nn_mnist\\data\\train\\0.npy")
# print(image_data.shape)
