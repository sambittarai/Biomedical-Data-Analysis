'''
Different ways of importing images in python
'''

#########################################################
# 1. pillow (PIL)

from PIL import Image
import numpy as np

img = Imageopen("images/img.jpg") # It is not a numpy array
print(type(img))

img.show()
print(img.format) #jpeg

img_arr = np.asarray(img)

#########################################################
# 2. Matplotlib

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread("images/img.jpg") # It is imported as a numpy array
print(type(img))
plt.imshow(img)
plt.colorbar()
plt.show()

##########################################################
# 3. Scikit-image

from skimage import io, img_as_float, img_as_ubyte

image = io.imread("images/img.jpg")
# image = io.imread("images/img.jpg").astype(np.float)
print(type(image)) #numpy array
# image_float = img_as_float(image)
#There is a difference between "astype" and "img_as_float", when converting the image to float.
plt.imshow(image)
plt.show()

############################################################
# 4. OpenCV

import cv2

grey_img = cv2.imread("images/img.jpg", 0) #grayscale image
color_img = cv2.imread("images/img.jpg", 1) #color image

# plt.imshow(img) # displaying images in this way, looks little bit different. Because cv2 handles the images in BGR format not RGB.
# plt.show()
# plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)) #converts the color space.

cv2.imshow("grey_Image", grey_img)
cv2.imshow("color_Image", color_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows() #kill all the windows

############################################################
# 5. glob 
# Reading multiple files at a folder at the same time

import cv2
import glob

image = []
path = "images/multiple_images/*"
for file in glob.glob(path):
	img = cv2.imread(file)
	image.append(img)

	cv2.imshow("Image", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

