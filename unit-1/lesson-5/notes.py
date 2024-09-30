# from PIL import Image
# import random

# # let's make a 100x100 black image

# width = 100
# height = 100

# img = Image.new("HSV", (width,height), (0,0,0) )

# for y in range(height):
#     for x in range(width):    
#         # randomColorValue = random.randrange(255)
    
#         r = random.random()

#         if r > .5:
#             img.putpixel( (x,y), (240,255,255) )

# img = img.convert("RGB")

# img.save("so-random.png")

from PIL import Image
import random

# let's make a 100x100 white image

width = 100
height = 100

img = Image.new("RGB", (width,height), (255,255,255) )

# loop 500 times, and each time, pick a random x and a random y
# and draw a pixel there
for n in range(500):

    x = int( random.gauss(50,10) )
    y = int( random.gauss(50,10) )

    img.putpixel( (x,y), (0,0,0) )

img.save("rando.png")