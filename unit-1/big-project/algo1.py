import sys
from PIL import Image
import random
import os #my research led me to the os module which is helpful for managing directories this is how i imported that library of funtions, it also allows me to create file  "paths" which is how i tell the python program where it can find files and where it can place them 

#The first big problem was how do I get the program to select random images from the folder 
#I knew I wanted the folder name to be input from the command line to run the program, similar to the way tarot reading operate in which you pick a card
#a big hole was how did i get the program to interact with the folder itself because I wanted the user to not have to type in specific image names but rather have the program randomize the selection 

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
#this is saying store in this variable: card pick path is where you will find the images which we have set as a user argument you will join that file path with the randomized image choices so that it is all in the correct place 
image1 = Image.open(random_image1_path)
image2 = Image.open(random_image2_path)


width, height = image1.size
pixel_count = 50000 #how many pixels it is selcting for manipulation at first i did a 100 thats why my clusters were so small

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
#these numbers above are responsible for defining the center both in the x and c thats why in the failure image with the mother you see it so far up to the left, i had divided both by 4 so x more to the left y more to the top by having them be two they are right in the center 
#i messed around with these numbers a lot, if you look at my "failures" folder at first the burst wasn't visible enough 
std_dev_x = width // 8
std_dev_y = height // 8
#these ones control how dispersed the spread will be using standard diviation, i had put in 4 orgininally if you look at the failure picture with the blue eye makeup it is more centered however its reallys pread apart you still cant tell what it is 
for n in range(pixel_count):
   x = int(random.gauss(center_x, std_dev_x))
   y = int(random.gauss(center_y, std_dev_y))
#this was to randomize these coordinates using the center and spread we fed it in another version of this lagorithm i could randomize this most likely by implementing randomization when creating the variables for center and deviation 
   x = max(0, min(x, width - 1)) 
   y = max(0, min(y, height - 1))
#here I am making sure that the coordinates dont go of fthe image so they arent less then 0 which is the highest point of the image as we learned before. 
   image1_pixels = image1.getpixel((x,y))
   image2.putpixel((x,y), image1_pixels)
#now i get pixels from first randome image base don teh conditions given and put those pixels wit the put function onto my new image
output_path = os.path.join(cardpick_path, "blended_image.png") 
image2.save(output_path)
#again using the os function I am able to make a file  path through which my images are coming from and the new one wil be saved to, making it easy to call the path for the file in my save command
#i think it could be cool if i could tell the user this image and this mage are being blended and maybe add more error control i only really have one piece