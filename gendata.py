#-*-coding: utf-8 -*-
import sys
import numpy as np
import cv2
import os

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30


def main():
	intClassifications = [] 
	intValidChars = [ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9'),
					 ord('ก'), ord('ข'), ord('ค'), ord('ง'), ord('จ'), ord('ฉ'), ord('ช'), ord('ฌ'), ord('ญ'), ord('ฎ'),
					 ord('ฐ'), ord('ฒ'), ord('ณ'), ord('ด'), ord('ต'), ord('ถ'), ord('ท'), ord('ธ'), ord('น'), ord('บ'),
					 ord('ป'), ord('ผ'), ord('พ'), ord('ภ'), ord('ม'), ord('ย'), ord('ร'), ord('ล'), ord('ว'), ord('ศ'),
					 ord('ษ'), ord('ส'), ord('ห'), ord('ฬ'), ord('อ'), ord('ฮ')]

	intChar = cv2.waitKey(0)
	if intChar == 27:                   
			sys.exit()                  
	elif intChar in intValidChars:
		intClassifications.append(intChar)
		npaFlattenedImage = imgROIResized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))
		npaFlattenedImages = np.append(npaFlattenedImages, npaFlattenedImage, 0) 

	fltClassifications = np.array(intClassifications, np.float32)

