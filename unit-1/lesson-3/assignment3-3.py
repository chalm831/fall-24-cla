import sys
from PIL import Image

if len(sys.argv) != 3:
    exit("This command requires one argument: the name of 2 image files")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )

blended_img = Image.blend(img1,img2,.7) #images have to be the same size otherise it errors

blended_img.save("blended3.jpg")

# i tried being crazy and blending 3 images all together at once like:
# if len(sys.argv) != 4:
#     exit("This command requires three arguments: the name of 3 image files")

# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )
# img3 = Image.open( sys.argv[3] )

# blended_img = Image.blend(img1,img2,img3,.5) #images have to be the same size otherise it errors

# blended_img.save("blended2.jpg")
#that did not work out lol, my research said it would have to be like first two and then bledn again to the third?? how accurate that is im not sure