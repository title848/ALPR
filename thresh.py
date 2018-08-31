import cv2 as cv
import numpy as np

class ocv:
   def thresh1(self,data1):
	img = cv.imread(data1)
	blur = cv.GaussianBlur(img,(5,5),0)
	#median = cv.medianBlur(blur,5)
	dst = cv.fastNlMeansDenoisingColored(blur,None,10,10,7,21)
	gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
	retval1,thresh1 = cv.threshold(gray,105,255,cv.THRESH_BINARY_INV)
	cv.imwrite('img.jpg',thresh1)

