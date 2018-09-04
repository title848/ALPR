import matplotlib.pyplot as plt

#from skimage.feature import hog
#from skimage import data, exposure
import numpy as np 
from sklearn import svm
import cv2 as cv
#import sys
import pandas as pd
import seaborn as sns; sns.set(font_scale=1.2)
from PIL import Image
import Image, ImageDraw
import pandas as pd 
from skimage.feature import hog
#import csv
def muffin_or_cupcake(model,Milk, Sugar):
    if(model.predict([[Milk, Sugar]]))==0:
        print('Ingredient : Milk = ' + str(Milk) + 'Sugar = '+ str(Sugar))
        print('You\'re looking at a muffin recipe!')
    elif(model.predict([[Milk, Sugar]]))==1:
        print('Ingredient : Milk = ' + str(Milk) + 'Sugar = '+ str(Sugar))
        print('You\'re looking at a cupcake recipe!')
    else:
        print('Ingredient : Milk = ' + str(Milk) + 'Sugar = '+ str(Sugar))
        print('You\'re looking at a cheesecake recipe!')
def main():
    digit = pd.read_csv('train.csv')
    #feat = pd.read_csv('feature.csv')
    #sns.lmplot('Milk', 'Sugar', data=digit, hue='Type',
    #            palette='Set1', fit_reg=False, scatter_kws={"s": 70});
    digit.head()

    #features = digit.iloc[:,1:253]
    #for i in digit.rows:
     #   features1 = digit[i].tolist()
     #   features.append(features1)
    features = digit[0:633].as_matrix()
    #ingredients = recipes[0:5].as_matrix()
    print(features)
    #print(features)
    #features = df[df.columns[2:4]] 
    type_label = digit['label'].tolist()
    #print(features)
    model = svm.SVC(kernel='linear',decision_function_shape='ovr')
    model.fit(features,type_label)
    img = Image.open('char/38.jpg')
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 8),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)
    print(len(fd))
    prediction = model.predict(fd)
    print(prediction)
    #w = model.coef_<10   yy = a * xx - (model.intercept_[0]) / w[1]
    #b= model.support_vectors_[0]
    #yy_down = a*xx + (b[1]-a*b[0])
    #b= model.support_vectors_[-1]
    #yy_up = a*xx + (b[1]-a*b[0])
    #muffin_or_cupcake(model,28,3)
    #muffin_or_cupcake(model,17,9)
    #muffin_or_cupcake(model,18,25)

    #sns.lmplot('Milk', 'Sugar', data=digit, hue='Type',
     #       palette='Set1', fit_reg=False, scatter_kws={"s": 70});
    #plt.plot(xx,yy,linewidth=2,color='black')
    #plt.plot(xx,yy_down,'k--')
    #plt.plot(xx,yy_up,'k--')
    #plt.scatter(model.support_vectors_[:,0],model.support_vectors_[:,1],s=80,facecolors='none')
    #sns.lmplot('Milk', 'Sugar', data=digit, hue='Type',
    #        palette='Set1', fit_reg=False, scatter_kws={"s": 70});
    #plt.plot(xx,yy,linewidth=2,color='black')
    #plt.show()

if __name__ == "__main__": main()