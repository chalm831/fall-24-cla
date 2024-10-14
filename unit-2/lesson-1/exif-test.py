from os import listdir, path
from PIL import Image, ExifTags 
#when i was doing research for my unit 1 project i actually came across this and i did'nt use it but it did kind of leave me wondering

image_directory = "images"

files = listdir (image_directory)
#at first i tried like changing what the value for files was but that got real omplicate sand it kept gaving me all kinds of erros 
#i feel like because i was using a lot of my unit 1 roject to guide me a little bit through using os as it did before tp sort through directories i lost a little bit of how to actually code this individual program separately.
for file in files:
  img = Image.open(path.join(image_directory, file))
  exifData = img.getexif()
  print(exifData)

  for key in img.getexif().keys():
    print(key, ExifTags.TAGS[key])
#once I put this inside a for loop it was much easier because it stopped telling me that irt was having errros with opening the file or not finding it 
# print(exifData)

#my first sucessful run was only one image so i added more
#i also experimented by adding image sthat were nt taken in an iphone, some that were developed film transfarred into digital mode, some with a professional camera, computer screenshots, saved from pinterest etc. 
# At first it just did the same one as before. so clealry i had to edit how it was acessing the directory 
#i took: files = listdir ("images") and expanded it so that i could be more specific abt it acessing the whole directory. first tell it where the image directory is and then get the list of files in it. Two seprste steps alloed me to actually get all of them instead of the same. Supposedly. 
#next i tried another iphone image in the folder to see if that worked and while i did that i realized oh pause i renamed that image 0.jpg on purpose before and when i changed the name it gave me an error. huh. 
#i needed to change what images i was asking the program to open because i was saying "images" path and 0.jpg which is ofc just that one image i purposefully named that bc of how it was in the original example. 
#even then i stillkept getting errors. Bceause omce again i put something oustide the loop that should have been inside it. Very common error for me actually. print inside not outside. 
#then it kind of worked like it gave me the tags for two but it kept gicing me an error for line 11 and i need help.