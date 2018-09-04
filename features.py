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

digit = pd.read_csv('train.csv')
digit.head()
data =[]
data = digit['label'].tolist()
print(data)