import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import hog
from skimage import data, exposure
import cv2 as cv
import sys
from thresh import *
from PIL import Image
import Image, ImageDraw

img = Image.open("1.JPEG")
img = img.resize((64,128), Image.ANTIALIAS)
#img = cv.imread('char/1.jpg')   

fd, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(2, 2), visualize=True, multichannel=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(img, cmap=plt.cm.gray)
ax1.set_title('Input image')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

image_array = np.asarray(hog_image_rescaled,dtype=float)
np.savetxt('test.txt',hog_image_rescaled,fmt="%s")
print(len(hog_image_rescaled))
ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()