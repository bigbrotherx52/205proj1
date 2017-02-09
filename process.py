
#title: Project1
#Name: Harlan Cheer
#date: 2-9-17

from PIL import Image 

#image array
imgList = []
#import images
for i in range(9):
    imgList.append( Image.open("Project1Images/" + str(i+1) + ".png"))
    
#set size
imgWidth, imgHieght = imgList[0].size

#create color lists
reds = []
greens = []
blues = []
    
#create a new image with same dimensions of originals
imgNew = Image.new("RGB", (imgWidth,imgHieght))
    

for x in range(imgWidth):
    for y in range(imgHieght):
        for img in imgList:
            #get the color values of the pixels
            locRed, locGreen, locBlue =img.getpixel((x,y));
            
            #add to lists
            reds.append(locRed)
            greens.append(locGreen)
            blues.append(locBlue)

            #sort each list, to get the median
            reds.sort()
            greens.sort()
            blues.sort()
            
            #create a tuple of the colors
            colorNew = (reds[len(reds)/2], greens[len(greens)/2], blues[len(blues)/2])
            
            #set the pixel of x,y to new color
            imgNew.putpixel((x,y), colorNew)

        #clear the color lists for the next pixel
        reds[:] = []
        greens[:] = []
        blues[:]= []
            
#save the image
imgNew.save("newImg.png")