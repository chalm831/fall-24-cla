import sys
from PIL import Image

if len(sys.argv) != 2: #for if the user forgets to specify an argument 
    exit("This command requires one arguemnt the name of an image file ")

img = Image.open (sys.argv[1])

print ("You typed the file name: " + sys.argv[1] )
print ("This is a " + img.format)
print (img.format_description) 
print ( "Size: + img.size ")

#this program does not error control for if they type an image that doesnt exist or a file that isnt an image