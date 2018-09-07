#test test test
import matplotlib.pyplot as plt
import numpy as np 
from sklearn import svm
import cv2 as cv
import sys
import pandas as pd
#import seaborn as sns; sns.set(font_scale=1.2)
from skimage.feature import hog
from skimage import data, exposure

im = cv.imread('1.JPEG')
im = np.float32(im) / 255.0

gx = cv.Sobel(im, cv.CV_32F, 1, 0, ksize=1)
gy = cv.Sobel(im, cv.CV_32F, 0, 1, ksize=1)

mag, angle = cv.cartToPolar(gx, gy, angleInDegrees=True)

print(angle)