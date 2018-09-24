#-*-coding: utf-8 -*-
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
from createcsv import *

characters = []
minx1 = []
miny1 = []
maxx1 = []
maxy1 = []
allminmax = [[]]


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
        if data[x, y] == 255:
            pass

        elif y > 0 and data[x, y-1] == 0:
            labels[x, y] = labels[(x, y-1)]

        elif x+1 < width and y > 0 and data[x+1, y-1] == 0:
            c = labels[(x+1, y-1)]
            labels[x, y] = c

            if x > 0 and data[x-1, y-1] == 0:
                a = labels[(x-1, y-1)]
                uf.union(c, a)

            elif x > 0 and data[x-1, y] == 0:
                d = labels[(x-1, y)]
                uf.union(c, d)


        elif x > 0 and y > 0 and data[x-1, y-1] == 0:
            labels[x, y] = labels[(x-1, y-1)]
	   # pixel[labels[x, y]]  +=1

        elif x > 0 and data[x-1, y] == 0:
            labels[x, y] = labels[(x-1, y)]
	   # pixel[labels[x, y]]  +=1

        else:
            labels[x, y] = uf.makeLabel()
    stop = timeit.default_timer()
    uf.flatten()
    colors = {}
#   characters = []
    output_img = Image.new("RGB", (width, height))
    output_seg = Image.new("RGB", (width, height))
    outdata1 = output_seg.load()
    outdata = output_img.load()

    pixel = [0]*(width+2*height)


    for (x, y) in labels :
        component = uf.find(labels[(x, y)])
        pixel[component] += 1
        labels[(x, y)] = component
        if component not in colors:
            colors[component] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
        outdata1[x,y] = colors[component]
    
    lbil = []
    count10 = []
    #pixeled = sorted(pixel,reverse = True)
    pixelled = []
    cppixel = []
    cppixel = pixel[:]
    
    

    for j in range(0,10): # อาจจะต้องเปลี่ยนตรงนี้เป็นฟังค์ชันสักอันนึงของ python เพราะคิดว่าน่าจะมีคนทำไว้แล้ว จะทำให้ไวขึ้นเยอะมาก เพราะไม่ต้องวนลูปเอง
        cppixel[0] = min(cppixel)
        Index = cppixel.index(max(cppixel))
        count10.append(Index)
        pixelled.append(cppixel[Index])
        cppixel[Index] = min(cppixel)
           
    

    minx = [width]*10
    maxx = [0]*10
    miny = [height]*10
    maxy = [0]*10   

    for (x,y) in labels: 
        if labels[(x,y)] in count10 and labels[(x,y)] != 0:
            component = uf.find(labels[(x, y)])
            #if pixel[component] > Average(pixelled)-(Average(pixelled)*0.8) and pixel[component] < Average(pixelled)+(Average(pixelled)*1.5) :
               	#หา component 
            outdata[x, y] = colors[labels[(x,y)]]
            if maxx[count10.index(component)] < x:
                maxx[count10.index(component)] = x
            if minx[count10.index(component)] > x:
                minx[count10.index(component)] = x
            if maxy[count10.index(component)] < y: 
                maxy[count10.index(component)] = y
            if miny[count10.index(component)] > y:
                miny[count10.index(component)] = y
            if component not in characters:
                characters.append(component)
    
    maxx = maxx[:len(maxx)-(10-len(characters))]
    minx = minx[:len(minx)-(10-len(characters))]
    maxy = maxy[:len(maxy)-(10-len(characters))]
    miny = miny[:len(miny)-(10-len(characters))]
    

    
    '''for (x,y) in labels: #คอมเม้นไว้ก่อน เป็นโค้ดเวอร์ชันเก่า
        if labels[(x,y)] in count10 and labels[(x,y)] != 0:
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
                    miny[i] = y'''
    #print count10
    #print(Average(pixelled))
    #print pixelled
    #print(minx,miny,maxx,maxy)

    minxx = minx[:]
    for ii in range(len(minxx)):
        Index2 = minxx.index(min(minxx))
        minx1.append(minx[Index2])
        maxy1.append(maxy[Index2])
        maxx1.append(maxx[Index2])
        miny1.append(miny[Index2])
        #count11.append(Index2)
        minxx[Index2] = 10000
    #print(minx1,maxx1,miny1,maxy1,minx,maxx,miny,maxy)    
    #print('\n')
    #print 'Min X : ' + str(minx1)            
    #print 'Max X : ' + str(maxx1)
    #print 'Min Y : ' + str(miny1)
    #print 'Max Y : ' + str(maxy1)

    
    return (labels, output_img,output_seg,minx1,miny1,maxx1,maxy1,stop)
#def ocr(
def main():
    start = timeit.default_timer()
    ccv = ocv()
    ccv.thresh1(sys.argv[1])
    img = Image.open("img.jpg")
    img = img.resize((200,150), Image.ANTIALIAS)
    img = img.point(lambda p: p > 110 and 255)
    img = img.convert('1')
    (_, output_img,output_seg,minx1,miny1,maxx1,maxy1,stop) = run(img)
    #output_img.show()
    output_seg.show()
    output_img.save('color.jpg')
    output_seg.save('seg1.jpg') 
    crop1 = []
    cha = " "
    cha2 = " "
    '''for i in range(len(miny1)):
    	try:
        	if abs(miny1[i] - miny1[i+1] ) < 25 or abs(maxy1[i] - maxy1[i+1]) < 25 or abs(miny1[i] - miny1[i-1] ) < 25 or abs(maxy1[i] - maxy1[i-1]) < 25:# and maxy1[i+1] is exist:  	
        		cropx = img.crop((minx1[i],miny1[i],maxx1[i],maxy1[i])) 
        		crop1.append(cropx)
        except IndexError:	
        	if abs(miny1[i] - miny1[i-1] ) < 25 or abs(maxy1[i] - maxy1[i-1]) < 25:		
        		cropx = img.crop((minx1[i],miny1[i],maxx1[i],maxy1[i])) 
        		crop1.append(cropx)'''
                
    for i in range(len(miny1)):         
        if maxx1[i] - minx1[i] > 5 and maxx1[i] - minx1[i] < 33  and maxy1[i]-miny1[i] >22 and maxy1[i]-miny1[i] < 80 and maxy1[i] < 100: #and miny1[i] < 60 and maxy1[i] < 90   	
            cropx = img.crop((minx1[i],miny1[i],maxx1[i],maxy1[i])) 
            crop1.append(cropx)

    
    for i in range(len(crop1)):
        iimg = 'crop' + str(i) +'.jpg'
        crop1[i].save(iimg)
        fd = hog1(iimg)
        ch,ch2 , prob = svmpredict(fd)
        if prob == 0:
            cha = cha + str(ch)
            cha2 = cha2 + str(ch)

        elif prob == 1:
            if ch == 'ก':
                cha = cha + str(ch)
                cha2 = cha2 + str(ch)
            else:
                cha = cha + str(ch)
                cha2 = cha2 + str(ch2)
    print 'ป้ายทะเบียน หมายเลข : ' + cha
    print 'หรือ ป้ายทะเบียน หมายเลข : ' + cha2

    print('Time: ', stop - start)
if __name__ == "__main__": main()
