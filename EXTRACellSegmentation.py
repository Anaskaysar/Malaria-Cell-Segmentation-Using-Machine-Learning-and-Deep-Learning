"""
Manual and auto thresholding
"""

import cv2
import matplotlib.pyplot as plt
from skimage import io,filters
img = io.imread("/Users/ali-11/Downloads/Week 6/malaria-cell (1).png")
plt.imshow(img)

#########################MANUAL##################
#Separate blue channels as they contain nuclei pixels (DAPI). 
blue_channel = img[:,:,0]
plt.imshow(blue_channel, cmap='gray')

plt.hist(blue_channel.flat, bins=100, range=(0,150))

ret2, thresh2 = cv2.threshold(blue_channel,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Now, let us segment the image, meaning assign values of 0, 1, 2, ... to pixels
import numpy as np 
regions1=np.digitize(blue_channel, bins=np.array([ret2]))
plt.imshow(regions1)


