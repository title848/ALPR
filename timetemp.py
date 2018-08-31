#-*-coding: utf-8 -*-
import timeit
import cv2 as cv
import numpy as np
from imutils import contours
import argparse
import imutils
import sys
from switchtest import *
		
start = timeit.default_timer()		
scores = []
img = cv.imread(sys.argv[1])
img3 = cv.resize(img,(100,100))

for i in range(1,47):
	img1 = cv.imread('char/%s.jpg'%i)
	result = cv.matchTemplate(img3,img1,cv.TM_CCOEFF)
	(_,score,_,_) = cv.minMaxLoc(result)
	scores.append(score)
	

Indexx = scores.index(max(scores))
img2 = cv.imread('char/%s.jpg'%(Indexx+1))
c = swcase(Indexx+1)
stop = timeit.default_timer()
print('Time: ', stop - start)
cv.imshow('img',img2)
cv.waitKey(0)




