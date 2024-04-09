
import os
import shutil


def split_data(source, classes):

    dirname = os.path.dirname(__file__)
    source_directory = os.path.join(dirname, source)
    print("source: " + source_directory)
  
    for c in classes:
        temp = os.path.join(dirname, c)
        print( c + ": " + temp)
        os.makedirs(temp, exist_ok=True)

    for filename in os.listdir(source_directory):
        for c in classes:
            if c in filename:
                shutil.move(os.path.join(source_directory, filename), os.path.join(dirname,c, filename))


split_data("raw" , ["cat" , "dog"])