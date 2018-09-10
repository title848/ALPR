#-*-coding: utf-8 -*-
import matplotlib.pyplot as plt
import timeit
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
import pickle

def swcase(x):
        return {
            10: 'ก',
            20: 'ข',
            30: 'ค',
            40: 'ง',
            50: 'จ',
            60: 'ฉ',
            70: 'ช',
            80: 'ฌ',
            90: 'ญ',
            100: 'ฎ',
            110: 'ฐ',
            120: 'ฒ',
            130: 'ณ',
            140: 'ด',
            150: 'ต',
            160: 'ถ',
            170: 'ท',
            180: 'ธ',
            190: 'น',
            200: 'บ',
            210: 'ป',
            220: 'ผ',
            230: 'พ',
            240: 'ภ',
            250: 'ม',
            260: 'ย',
            270: 'ร',
            280: 'ล',
            290: 'ว',
            300: 'ศ',
            310: 'ษ',
            320: 'ส',
            330: 'ห',
            340: 'ฬ',
            350: 'อ',
            360: 'ฮ',
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
        }[x]
def hog1(imag):
    img = Image.open(imag)
    img = img.resize((16,32), Image.ANTIALIAS)
    fd, _x_ = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)
    return fd
def svmpredict(model,feature1):
    prediction = model.predict([feature1])
    print "Your Data is :" + str(swcase(prediction[0]))

def main():
    start = timeit.default_timer()
    
    #digit = pd.read_csv('testglob.csv')
    #digit.head()
    #type_label = digit['label'].tolist()
    #features = digit.loc[:, digit.columns != 'label'].as_matrix()
#    model = svm.SVC(kernel='linear',decision_function_shape='ovr')
#    model.fit(features,type_label)   
    filename = 'finalized_model.sav'
    #pickle.dump(model, open(filename, 'wb'))
    fd  = hog1(sys.argv[1])
    model = pickle.load(open(filename, 'rb'))
    svmpredict(model,fd)

    fd  = hog1(sys.argv[2])
    svmpredict(model,fd)
    stop = timeit.default_timer()
    print('Time: ', stop - start)
if __name__ == "__main__": main()