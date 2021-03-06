# -*- coding: utf-8 -*-
"""image processing stars.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x6jR8UAk5qCZv2zXdp5xgAknssi5NZbm
"""

from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

example_file = glob.glob("/content/sky.PNG")[0]
im = imread(example_file, as_gray=true)
plt.imshow(im, camp=cm.gray)
plt.show

blobs_log = blob_log(i,, max_sigma=30, num)sigma=10, threshold=.1)
# compute radii in the 3rd column.
blobs_log[:,2] = blobs_log[:, 2] * sqrt(2)
numrows = len(blobs_log)
print("Number of starts counted : " ,numrows)

fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap=cm.gray)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)