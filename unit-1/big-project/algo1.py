import sys
from PIL import Image
import random
import os #my research led me to the os module which is helpful for managing directories this is how i imported that library of funtions

#The first big problem was how do I get the program to select random images from the folder 
#I knew I wanted the folder name to be input from the command line to run the program, similar to the way tarot reading operate in which you pick a card
#a big hole was how did i get the program to interact with the folder itself because I wanted the user to not have to type in specific cimage names but rather have the program randomize the selection 

if len(sys.argv) < 2:
    print ("pick a card(folder) to see your future!")
    sys.exit(1)

cardpick_path = sys.argv[1]

#at this point is when I understood that using the os function would allow me to get all the images from the folder 
images = [f for f in os.listdir (cardpick_path) if f.lower().endswith (('.png', '.jpg', '.jpeg'))]
#this allows me to create the list based on the folder the user gives the algorithm that will be used for randomization within a variable, it also allows me to error control by only selecting valid formats for image. thsi was helpeful because when i was originally downloading from are.na they downloaded .web

# random_image1 = random.choice(images)
# random_image2 = random.choice(images) #i was misisng an extra step that assured that i wasnt going to combine the same image with the same 

# #here im having the program randomize image choices for the variables
random_image1_name = random.choice(images)
random_image2_name = random.choice([img for img in images if img != random_image1_name])

random_image1_path = os.path.join(cardpick_path, random_image1_name)
random_image2_path = os.path.join(cardpick_path, random_image2_name)

image1 = Image.open(random_image1_path)
image2 = Image.open(random_image2_path)


width, height = image1.size
pixel_count = 50000 

#######################################################
#this code worked well for changing one random pixel for another random pixel but that doesnt look that cool tbh so i was like ok...let me eat dinner and lets try the gaussian distrbution 
# for n in range (pixel_count):
#      x = random.randint(0, width - 1)
#      y = random.randint(0, height - 1)

# image1_pixels = random_image1.getpixel((x,y))
# random_image2.putpixel((x,y), image1_pixels)

# output_path = os.path.join(cardpick_path, "blendedagain_image.png")
# random_image2.save(output_path)

####################################################
#for this iteration i used the one pixel version as sort of template and the notes from lesson 5 to try and figure it out 

center_x = width // 2
center_y = height // 2
#i messed around with these numbers a lot, if you look at my "failures" folder at first the burst wasn't visible enough 
std_dev_x = width // 8
std_dev_y = height // 8

for n in range(pixel_count):
   x = int(random.gauss(center_x, std_dev_x))
   y = int(random.gauss(center_y, std_dev_y))

   x = max(0, min(x, width - 1))
   y = max(0, min(y, height - 1))

   image1_pixels = image1.getpixel((x,y))
   image2.putpixel((x,y), image1_pixels)

output_path = os.path.join(cardpick_path, "blended_image.png") 
image2.save(output_path)

#i think it could be cool if i could tell the user this image and this mage are being blended and maybe add more error control i only really have one piece