#main segmentation and ocr program
import timeit
import numpy.core.multiarray
import Image, ImageDraw
import cv2 as cv
import sys
import math, random
from itertools import product
from ufarray import *
import numpy as np
from thresh import *
from collections import Counter
from tempmatch import *
from PIL import Image
characters = []
minx1 = []
miny1 = []
maxx1 = []
maxy1 = []
def Average(lst):
    return sum(lst)/len(lst)
def run(img):
    data = img.load()
   # data = data1.resize((1000,500), Image.ANTIALIAS)
    width, height = img.size
    uf = UFarray()
    labels = {}
 #   pixel = []
   # ret,data = cv.threshold(data1,127,255,cv.THRESH_BINARY_INV)
    for y, x in product(range(height), range(width)):
        if data[x, y] == 0:
            pass

        elif y > 0 and data[x, y-1] == 255:
            labels[x, y] = labels[(x, y-1)]

        elif x+1 < width and y > 0 and data[x+1, y-1] == 255:
            c = labels[(x+1, y-1)]
            labels[x, y] = c

            if x > 0 and data[x-1, y-1] == 255:
                a = labels[(x-1, y-1)]
                uf.union(c, a)

            elif x > 0 and data[x-1, y] == 255:
                d = labels[(x-1, y)]
                uf.union(c, d)


        elif x > 0 and y > 0 and data[x-1, y-1] == 255:
            labels[x, y] = labels[(x-1, y-1)]
	   # pixel[labels[x, y]]  +=1

        elif x > 0 and data[x-1, y] == 255:
            labels[x, y] = labels[(x-1, y)]
	   # pixel[labels[x, y]]  +=1

        else:
            labels[x, y] = uf.makeLabel()


    uf.flatten()
    colors = {}
    k = []
    w = []
#    characters = []
    output_img = Image.new("RGB", (width, height))
    output_seg = Image.new("RGB", (width, height))
    outdata1 = output_seg.load()
    outdata = output_img.load()
#    b = Counter(uf.P)
#    mostcom = b.most_common(20)
    count = [0]*10
    flag = [0]*10
    pixel = [0]*(width+2*height)
#    minx = [width]*10
#    maxx = [0]*10
#    miny = [height]*10
#    maxy = [0]*10

#    for i in range(len(mostcom)):
#	k.append(mostcom[i][0])

    for (x, y) in labels :
        	component = uf.find(labels[(x, y)])
        	pixel[component] += 1
		labels[(x, y)] = component
	        if component not in colors:
        	    colors[component] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
		outdata1[x,y] = colors[component]
    lbil = []

    pixeled = sorted(pixel,reverse = True)
    pixelled = []
    for i in range(1,9):
	pixelled.append(pixeled[i])
    for i in range(len(pixel)):
	 if pixel[i] != pixeled[0] and flag[0] == 0:
		count[0]  += 1
	 else : flag[0] = 1
	 if pixel[i] != pixeled[1] and flag[1] == 0:
                count[1]  += 1
         else : flag[1] = 1
	 if pixel[i] != pixeled[2] and flag[2] == 0:
                count[2]  += 1
         else : flag[2] = 1
	 if pixel[i] != pixeled[3] and flag[3] == 0:
                count[3]  += 1
         else : flag[3] = 1
	 if pixel[i] != pixeled[4] and flag[4] == 0:
                count[4]  += 1
         else : flag[4] = 1
	 if pixel[i] != pixeled[5] and flag[5] == 0:
                count[5]  += 1
         else : flag[5] = 1
	 if pixel[i] != pixeled[6] and flag[6] == 0:
                count[6]  += 1
         else : flag[6] = 1
	 if pixel[i] != pixeled[7] and flag[7] == 0:
                count[7]  += 1
         else : flag[7] = 1
	 if pixel[i] != pixeled[8] and flag[8] == 0:
                count[8]  += 1
         else : flag[8] = 1
	 if pixel[i] != pixeled[9] and flag[9] == 0:
                count[9]  += 1
         else : flag[9] = 1

    for (x,y) in labels:
        if labels[(x,y)] in count and labels[(x,y)] != 0:
          #     	 if labels[(x,y)] not in character:
           #            	 character.append(labels[(x,y)])
		component = uf.find(labels[(x, y)])
		if pixel[component] > Average(pixelled)-(Average(pixelled)*0.7	) and pixel[component] < Average(pixelled)+(Average(pixelled)*1.5) and pixel[component] > width :
               		outdata[x, y] = colors[labels[(x,y)]]
			if component not in characters:
				characters.append(component)
    minx = [width]*len(characters)
    maxx = [0]*len(characters)
    miny = [height]*len(characters)
    maxy = [0]*len(characters)

    for i in range(len(characters)):
	   for(x,y) in labels:
		  component = uf.find(labels[(x, y)])
		  if component == characters[i]:
		  	if maxx[i] < x:
				    maxx[i] = x
			if minx[i] > x:
                                minx[i] = x
			if maxy[i] < y:
                                maxy[i] = y
			if miny[i] > y:
                                miny[i] = y

    #print(Average(pixelled))
    print(count,pixelled)
    #print(characters)
    #print(minx,miny,maxx,maxy)
    listt = []
    for i in range(len(characters)):
        count1 = 100000
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for j in range(len(characters)):
            if count1 > minx[j] and characters[j] not in listt: 
                count1 = minx[j]
                count2 = characters[j]
                count3 = maxx[j]
                count4 = miny[j]
                count5 = maxy[j] 
        listt.append(count2)
        maxx1.append(count3)
        miny1.append(count4)
        maxy1.append(count5)
        minx1 = sorted(minx)
    print('\n')
    #print(minx1,maxx1,miny1,maxy1)            

    return (labels, output_img,output_seg,minx1,miny1,maxx1,maxy1)
#def ocr(
def main():
    start = timeit.default_timer()
    ccv = ocv()
    ccv.thresh1(sys.argv[1])
    img = Image.open("img.jpg")
   # img = img.resize((450,200), Image.ANTIALIAS)
    img = img.point(lambda p: p > 110 and 255)
    img = img.convert('1')
    (labels, output_img,output_seg,minx1,miny1,maxx1,maxy1) = run(img)
    output_img.show()
    output_seg.show()
    output_img.save('color.jpg')
    output_seg.save('seg1.jpg')
    optcr = opcr()
    crop1 = []
    cha = " "
    for i in range(len(miny1)):
    	try:
        	if abs(miny1[i] - miny1[i+1] ) < 25 or abs(maxy1[i] - maxy1[i+1]) < 25 or abs(miny1[i] - miny1[i-1] ) < 25 or abs(maxy1[i] - maxy1[i-1]) < 25:# and maxy1[i+1] is exist:  	
        		cropx = img.crop((minx1[i],miny1[i],maxx1[i],maxy1[i])) 
        		crop1.append(cropx)
        except IndexError:	
        	if abs(miny1[i] - miny1[i-1] ) < 25 or abs(maxy1[i] - maxy1[i-1]) < 25:		
        		cropx = img.crop((minx1[i]-10,miny1[i]-10,maxx1[i]+10,maxy1[i]+10)) 
        		crop1.append(cropx)

        	#crop1[i].save('crop' + str(i) +'.jpg')
        	#ch = optcr.opchr('crop' + str(i) +'.jpg')
        	#cha = cha + str(ch)
    for i in range(len(crop1)):
    		crop1[i].save('crop' + str(i) +'.jpg')
        	ch = optcr.opchr('crop' + str(i) +'.jpg')
        	cha = cha + str(ch)    	
    print(cha)
    print(len(characters))
    #crop1[1].save('crop2.jpg')
    #crop1[2].save('crop3.jpg')
    #crop1[3].save('crop4.jpg')
    #crop1[4].save('crop5.jpg')
    #crop1[5].save('crop6.jpg')
    #crop1[6].save('crop7.jpg')

  #  crop1[0].show()
    stop = timeit.default_timer()

    print('Time: ', stop - start)
if __name__ == "__main__": main()

