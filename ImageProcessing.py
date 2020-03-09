# https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
#https://pillow.readthedocs.io/en/stable/reference/Image.html

from PIL import Image

# im = Image.open("myfile.jpg", mode="r")
# show image
# im.show()

# rotate image and show
# im.rotate(45).show()

# getting width and height
# print(im.size)


# importing image class from PIL package


# creating image object
img1 = Image.open("myfile.jpg")

# creating image2 object having alpha
img2 = Image.open("myfile2.jpg")
# img2 = img2.resize(img1.size)

# using alpha_composite
im3 = Image.alpha_composite(img1, img2)
# im3.show()


# im_grey = im.convert('LA') # convert to grayscale
# width, height = im.size

# total = 0
# for i in range(0, width):
#     for j in range(0, height):
#         total += im_grey.getpixel((i,j))[0]

# print(total)
# mean = total / (width * height)
# print(mean)
