#-*-coding: utf-8 -*-
import matplotlib.pyplot as plt

from skimage.feature import hog
import numpy as np 
from sklearn import svm
import cv2 as cv
import pandas as pd
import seaborn as sns; sns.set(font_scale=1.2)
from PIL import Image
import Image, ImageDraw
import pandas as pd 
from skimage.feature import hog
from sklearn import datasets
import sys

def main():
    digit = pd.read_csv('testglob.csv')
    feat = pd.read_csv('features.csv')
    digit.head()
    features = feat.as_matrix()
    type_label = digit['label'].tolist()
    model = svm.SVC(kernel='linear',decision_function_shape='ovr')
    model.fit(features,type_label)
    img = Image.open(sys.argv[1])
    img = img.resize((16,32), Image.ANTIALIAS)   
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)
    
    prediction = model.predict([fd])
    print "Your Data is :" + str(prediction)

if __name__ == "__main__": main()