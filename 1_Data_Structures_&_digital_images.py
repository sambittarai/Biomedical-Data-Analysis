'''
dtypes...
uint8 - 0 to 255
uint16 - 0 to 65535
uint32 - 0 to ((2**32) - 1)
float - -1 to 1 or 0 to 1
int8 - -128 to 127
int16 - -32768 to 32767
int32 - -2**31 to 2**31 - 1

Functions that convert images to desired dtype and properly rescale their values
img_as_float - Convert to 64-bit floating point
img_as_ubyte - Convert to 8-bit uint
img_as_uint - Convert to 16-bit uint
img_as_int - Convert to 16-bit int

We need to be careful when changing the data types, because you may loose some information when unknowingly if you downsample the image by converting it to 8-bit instead of 16-bit
'''

from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float #converts the image's pixel values to floating point values 

my_image = io.imread("Images/test_image.jpg")
# my_image[10:100, 10:100, :] = [255, 0, 0]
float_image = img_as_float(my_image)
random_image = np.random.random([500, 500])
plt.imshow(random_image)
plt.show()
