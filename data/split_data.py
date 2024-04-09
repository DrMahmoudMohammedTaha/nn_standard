
# pip install split-folders

import splitfolders
import os

dirname = os.path.dirname(__file__)
# input: folder that contsins all classes sub folders , ratios
# ouput: folder that will have train, val, test sub folders with specified ratios
splitfolders.ratio(os.path.join(dirname, "raw"), output=os.path.join(dirname, "processed"), seed=42, ratio=(0.6, 0.2, 0.2))
