###########################################################
# Image processing using pillow

from PIL import Image

img = Image.open("images/img.jpg")

cropped_img = img.crop((0, 0, 300, 300))
cropped_img.save("save_images/cropped_img.jpg")

print(img.format) #jpeg
print(img.mode) #rgb
print(img.size) #(639, 513)

small_img = img.resize((200, 300)) #aspect ratio is not preserved
small_img.save("save_images/small_img.jpg")

img.thumbnai((200, 300)) #aspect ratio is preserved
img.save("save_images/img.jpg")


# Crop the image
img1 = Image.open("images/blue_heaven.jpg") #(639, 513)
img2 = Image.open("images/monkey.jpg") #(150, 200)

img1_copy = img1.copy()
img1_copy.paste(img2, (50,50))
img1_copy.save(save_images/img1_copy.jpg)

# Image Rotation

img = Image.open("images/img.jpg")
img90 = img.rotate(90)
#img90 = img.rotate(90, expand=True) #preserves the edges

# Image Flip

img = Image.open("images/monkey.jpg")
img_flipLR = img.transpose(Image.FLIP_LEST_RIGHT)
img_flipTB = img.transpose(Image.FLIP_TOP_BOTTOM)

img_flipLR.save("save_images/img_flipLR.jpg")
img_flipTB.save("save_images/img_flipTB.jpg")

# convert the image to grayscale

img = Image.open("images/monkey.jpg")
grey_img = img.convert("L")
grey_img.save("save_images/grey_monkey.jpg")


