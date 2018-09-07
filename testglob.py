#this is the real create csv file from NECTEC Dataset
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import hog
from skimage import data, exposure
import cv2 as cv
import sys
from thresh import *
from PIL import Image
import Image, ImageDraw
import pandas as pd 
import glob
data = []
filenamee = []
for filename in glob.glob('Dataset2/Char/*/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)
    data.append(fd)
    filenamee.append(filename)

df = pd.DataFrame(data)
ff = pd.DataFrame(filenamee)
ff.to_csv('filename2.csv')
df.to_csv('testglob2.csv')


    