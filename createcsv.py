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
def muffin_or_cupcake(Milk, Sugar,Flour,Butter,Egg,BakingPowder,Vanilla,Salt):
    if(model.predict([[Milk, Sugar,Flour,Butter,Egg,BakingPowder,Vanilla,Salt]]))==0:
        print('You\'re looking at a muffin recipe!')
    elif(model.predict([[Milk, Sugar,Flour,Butter,Egg,BakingPowder,Vanilla,Salt]]))==1:
        print('You\'re looking at a cupcake recipe!')
    else:
        print('You\'re looking at a cheesecake recipe!')
   
recipes = pd.read_csv('Baking.csv')
sns.lmplot('Milk', 'Sugar', data=recipes, hue='Type',
            palette='Set1', fit_reg=False, scatter_kws={"s": 70});
recipes.head()
ingredients = recipes[['Milk','Sugar','Flour','Butter','Egg','Baking Powder','Vanilla','Salt']].as_matrix()
type_label = np.where(recipes['Type']=='Muffin',0,(np.where(recipes['Type']=='Cupcake',1,2)))
print(type_label)
model = svm.SVC(kernel='linear',decision_function_shape='ovo')
model.fit(ingredients,type_label)
dec = model.decision_function([[1]])
dec.shape[1]
w = model.coef_[0]
print(w)
a = -w[0] / w[1]
xx = np.linspace(5,60)
yy = a * xx - (model.intercept_[0]) / w[1]
b= model.support_vectors_[0]
yy_down = a*xx + (b[1]-a*b[0])
b= model.support_vectors_[-1]
yy_up = a*xx + (b[1]-a*b[0])
print(muffin_or_cupcake(28,3,55,7,5,2,0,0))
print(muffin_or_cupcake(17,9,54,10,8,1,0,1))
print(muffin_or_cupcake(18,25,42,9,5,1,0,0))

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



#if __name__ == "__main__": main()