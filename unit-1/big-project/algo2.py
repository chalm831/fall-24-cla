import sys
from PIL import Image, ImageFilter #At first i did not import ImageFilter because i missunderstood it to be within the same module as image, while they are from the same library after resarching the error I got: NameError: name 'ImageFilter' is not defined. I was able to understand I need to import both for them to do their seprate functions
import random
import os 

#I copy pasted the parts of my algorithm that asked for a folder (card) choice as system input 
if len(sys.argv) < 2:
    print ("pick a card(folder) to see your future!")
    sys.exit(1)

cardpick_path = sys.argv[1]

images = [f for f in os.listdir (cardpick_path) if f.lower().endswith (('.png', '.jpg', '.jpeg'))]
#once again making sure that the files selected are all images in formats that allow them to be composited 

random_image1_name = random.choice(images)
random_image2_name = random.choice([img for img in images if img != random_image1_name])

random_image1_path = os.path.join(cardpick_path, random_image1_name)
random_image2_path = os.path.join(cardpick_path, random_image2_name)

image1 = Image.open(random_image1_path)
image2 = Image.open(random_image2_path)

image1 = image1.convert ("RGBA")
image2 = image2.convert ("RGBA")
#I forgot that I needed the images to be in RGBA mode to be used by the alpha composite this is because the A in RGBA allows for it to consider opacity which is what I’m trying to manipulate with this  program and the alpa.composite command. When I ran it without i got ValueError: image has wrong mode 
# ValueError: image has wrong mode (i put the RGBA conversion after the filter I had to move it up)

image1_edgefilter = image1.filter(ImageFilter.FIND_EDGES)
image2_edgefilter = image2.filter(ImageFilter.FIND_EDGES)
#here i wanted to add a layer of interest that made the final image a little bit more interesting using the filter function from the image library I am choosing the find edges to detect them for me to be used later in my composition

# image1_alphavalue = 255
# image2_alphavalue = 128

# image1.putalpha(image1_alphavalue) 
# image2.putalpha(image2_alphavalue)
#this version of my code has it so that only the edges showed and the middle was transparent. Full transparency (no pun intended) i was suuuuper stuck and running out of time at this point so i asked my friend Ai to help me understand why this was happening.
# "The issue you're facing where only the edges are visible and the rest of the image is transparent is because of how the FIND_EDGES filter works. The filter highlights the edges in white and turns the rest of the image black or transparent, but when you composite two edge-filtered images, the areas without edges (which are transparent or black) are not showing any content." 
#to solve this I did the following:

image1_blended = Image.blend (image1, image1_edgefilter, 0.5) #opacity is from 0 to 1 so this is medium
image2_blended = Image.blend(image2, image2_edgefilter, 0.5)
#tthis blens the original image to the edge filter version using opacity so that they are overlayed in a way you can see both, and its doing this two both individual images


combined_image = Image.alpha_composite(image1_blended, image2_blended)
#this takes teh two filteres images and blends them meaning random filtered image 1 and random filteres image 2 

# combined_image.save = os.path.join(cardpick_path, "blended_image.png") 
#I tried this command first emmulating the one from my last program, while i was happy the program was running and not breaking it wasn't producing an output

output_path = os.path.join(cardpick_path, "combined_image.png") 
combined_image.save(output_path)
