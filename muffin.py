import matplotlib.pyplot as plt

#from skimage.feature import hog
#from skimage import data, exposure
import numpy as np 
from sklearn import svm
import cv2 as cv
#import sys
import pandas as pd
import seaborn as sns; sns.set(font_scale=1.2)
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
    recipes = pd.read_csv('Baking.csv')
    sns.lmplot('Milk', 'Sugar', data=recipes, hue='Type',
                palette='Set1', fit_reg=False, scatter_kws={"s": 70});
    recipes.head()
    ingredients = recipes[['Milk','Sugar']].as_matrix()
    type_label = np.where(recipes['Type']=='Muffin',0,(np.where(recipes['Type']=='Cupcake',1,2)))
    print(ingredients)
    model = svm.SVC(kernel='linear',decision_function_shape='ovo')
    model.fit(ingredients,type_label)

    w = model.coef_[0]
    #print(w)
    a = -w[0] / w[1]
    xx = np.linspace(5,60)
    yy = a * xx - (model.intercept_[0]) / w[1]
    b= model.support_vectors_[0]
    yy_down = a*xx + (b[1]-a*b[0])
    b= model.support_vectors_[-1]
    yy_up = a*xx + (b[1]-a*b[0])
    muffin_or_cupcake(model,28,3)
    muffin_or_cupcake(model,17,9)
    muffin_or_cupcake(model,18,25)

    sns.lmplot('Milk', 'Sugar', data=recipes, hue='Type',
            palette='Set1', fit_reg=False, scatter_kws={"s": 70});
    plt.plot(xx,yy,linewidth=2,color='black')
    plt.plot(xx,yy_down,'k--')
    plt.plot(xx,yy_up,'k--')
    plt.scatter(model.support_vectors_[:,0],model.support_vectors_[:,1],s=80,facecolors='none')
    sns.lmplot('Milk', 'Sugar', data=recipes, hue='Type',
            palette='Set1', fit_reg=False, scatter_kws={"s": 70});
    plt.plot(xx,yy,linewidth=2,color='black')
    plt.show()

if __name__ == "__main__": main()