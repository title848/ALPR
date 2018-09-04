#this is the real create csv file from NECTEC Dataset
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import hog
from skimage import data, exposure
import cv2 as cv
import sys
from thresh import *
from PIL import Image
import Image, ImageDraw
import pandas as pd 
import glob
data = []

for filename in glob.glob('Dataset2/000/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    data1 = [0]
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)
    data1.append(fd)
    data.append(fd)
for filename in glob.glob('Dataset2/111/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)

    data.append(fd)
for filename in glob.glob('Dataset2/222/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)
    data.append(fd)
for filename in glob.glob('Dataset2/333/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)

    data.append(fd)
for filename in glob.glob('Dataset2/444/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)
    data.append(fd)
for filename in glob.glob('Dataset2/555/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)

    data.append(fd)
for filename in glob.glob('Dataset2/666/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)
    data.append(fd)
for filename in glob.glob('Dataset2/777/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)
    data.append(fd)

for filename in glob.glob('Dataset2/888/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False)                        
    data.append(fd)

for filename in glob.glob('Dataset2/999/*.bmp'):
    img = Image.open(filename)
    img = img.resize((16,32), Image.ANTIALIAS)   
    
    fd, hog_image = hog(img, orientations=9, pixels_per_cell=(4, 4),
                        cells_per_block=(2, 2),block_norm="L1", transform_sqrt=True, visualize=True, multichannel=False) 

    data.append(fd)
#df = pd.DataFrame()
df = pd.DataFrame(data)
#print(data)
#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)    
df.to_csv('train1.csv')
#ax1.axis('off')
#ax1.imshow(img, cmap=plt.cm.gray)
#ax1.set_title('Input image')

# Rescale histogram for better display
#hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

#image_array = np.asarray(hog_image_rescaled,dtype=float)
#np.savetxt('test.txt',fd.reshape(1,-1),fmt="%s")
#np.savetxt("train.csv", fd.reshape(1,-1), delimiter=",")
print(fd.reshape(1,-1))
#ax2.axis('off')
#ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
#ax2.set_title('Histogram of Oriented Gradients')
#lt.show()