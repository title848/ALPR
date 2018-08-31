#Image_preprocessing 
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys

img = cv.imread(sys.argv[1])

blur = cv.GaussianBlur(img,(5,5),0)
dst = cv.fastNlMeansDenoisingColored(blur,None,10,10,7,21)
gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
ret,thresh1 = cv.threshold(gray,127,255,cv.THRESH_BINARY)

cv.imshow('img1',thresh1)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
