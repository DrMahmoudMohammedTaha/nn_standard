
import os
import shutil


def extract_classes(source, classes):

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


extract_classes("raw" , ["cat" , "dog"])