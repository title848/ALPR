
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np 
from sklearn import svm
import cv2 as cv
#import sys
import pandas as pd
import seaborn as sns; sns.set(font_scale=1.2)
from sklearn.svm import SVC 

recipes = pd.read_csv('Baking.csv')

X = recipes[['Milk','Sugar','Flour','Butter','Egg','Baking Powder','Vanilla','Salt']].as_matrix()
y = np.where(recipes['Type']=='Muffin',0,(np.where(recipes['Type']=='Cupcake',1,2)))
# dividing X, y into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
svm_predictions = svm_model_linear.predict(X_test)
 
# model accuracy for X_test
accuracy = svm_model_linear.score(X_test, y_test)
 
# creating a confusion matrix
cm = confusion_matrix(y_test, svm_predictions)
print(svm_model_linear)