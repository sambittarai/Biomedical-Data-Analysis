##########################################################
# skimage

from skimage import io
import matplotlib.pyplot as plt
from skimage.transform import rescale, resize, downscale_local_mean

img = io.imread("images/img.jpg", as_gray=True)
rescaled_img = rescale(img, 1.0/4.0, anti_aliasing=True)
resized_img = resize(img, (200, 200), anti_aliasing=True)
downscale_img = downscale_local_mean(img, (4,3), anti_aliasing=True)

###########################################################
# Edge Detection

from skimage.filters import roberts, sobel, scharr, prewitt

edge_roberts = roberts(img)
edge_sobel = sobel(img)
edge_scharr = scharr(img)
edge_prewitt = prewitt(img)

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True, figsize=(8,8))
ax = axes.ravel()

ax[0].imshow(img, cmap="gray")
ax.[0].set_title('Original Image')

ax[1].imshow(edge_roberts, cmap="gray")
ax.[1].set_title('Roberts Edge Detection')

ax[2].imshow(edge_scharr, cmap="gray")
ax.[2].set_title('Scharr')

ax[3].imshow(edge_sobel, cmap="gray")
ax.[0].set_title('Sobel')

for a in ax:
	a.axis('off')

plt.tight_layout()
plt.show()

#############################################################
# Canny Edge Detector

from skimage.feature import canny

edge_canny = canny(img, sigma=1) #reduces the noise
plt.imshow(edge_canny, cmap="gray")
plt.show()

#############################################################
# Segmentation using texture of the image (not the pixel values), because sometimes in microscopic images we have images with same pixel values but different textures
# We will use entropy filter

from skimage import io, restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import try_all_threshold

img = io.imread("images/cell.jpg")
entropy_img = entropy(img, disk(3))
plt.imshow(entropy_img, cmap="gray")
plt.show()

fig, ax = try_all_threshold(entropy_img, figsize=(10,8), verbose=False)

#############################################################
# Otsu based segmentation

from skimage.filters import threshold_otsu

threshold = threshold_otsu(entropy_img)
binary = entropy_img <= threshold
plt.imshow(binary, cmap="gray")
plt.show()