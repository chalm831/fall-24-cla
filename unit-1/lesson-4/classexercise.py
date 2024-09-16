# import sys
# from PIL import Image 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 10x10 image
# img = Image.new("RGB", (10,10) )

# data = []
# for i in range(100):
#     pixel = (i, 0, 0)
#     data.append( pixel )

# img.putdata(data)

# img.save(sys.argv[1])

# import sys
# from PIL import Image 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# data = []
# for i in range(160000):
#     pixel = (i, 0, 255-i)
#     data.append( pixel )

# img.putdata(data)

# img.save(sys.argv[1])

# import sys
# from PIL import Image 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         b = 0
#         if x % 50 == 0:
#             b = 255
            
#         if y % 20 == 0:
#             r = 255

#         if y % 30 == 0:
#             r = 255
#             b = 255

#         pixel = (r, 0, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])

import sys
from PIL import Image 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         g = 0
#         b = 0
#         if x % 50 > 25:
#             r = 255

#         if y % 50 > 25:
#             b = 255

#         if x % 100 > 50 and y % 100 > 50:
#             g = 255

#         pixel = (r, g, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])

# if len(sys.argv) != 3:
#     exit("This program requires two arguments: the name of two image files to combine.")


# # open both images
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )

# # resize both images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )

# # make a new image 600x600, with a white background
# new_image = Image.new( "RGB", (400,400), "white" )

# # paste in the first image to the upper-left corner (0,0)
# new_image.paste(img1, (0,0) )

# # paste in the second image, to (200,200)
# new_image.paste(img2, (20, 20) )

# # save the resulting image
# new_image.save("overlay-two-images.jpg")

# import sys
# from PIL import Image 

# if len(sys.argv) != 3:
#     exit("This program requires two arguments: the name of two image files to combine.")


# # open both images
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )

# # resize both images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )

# # make a new image 600x600, with a white background
# # Note that this image now has an "alpha" component
# new_image = Image.new( "RGBA", (600,600), "white" )

# # paste in the first image to the upper-left corner (0,0)
# new_image.paste(img1, (0,0) )

# # add some transparency (alpha) to the second image
# img2.putalpha(128)

# # paste in the second image, preserving its new transparency
# new_image.alpha_composite(img2, (200,200) )

# # save the resulting image
# # Note that we must convert it to RGB with no alpha to save it as a JPEG
# new_image.convert("RGB").save("new.jpg")

# # Alternatively, we could have avoided converting by saving it to a
# # PNG like this (since PNGs allow alpha):
# # new_image.save("new.png")