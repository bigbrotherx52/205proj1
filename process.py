from PIL import Image 

imgList = []
for i in range(9):
    imgList.append( Image.open("project1/" + str(i+1) + ".png"))
    
    
imgWidth, imgHieght = imgList[0].size
reds = []
greens = []
blues = []
    
    
imgNew = Image.new("RGB", (imgWidth,imgHieght))
    
for x in range(imgWidth):
    for y in range(imgHieght):
        for img in imgList:
            locRed, locGreen, locBlue =img.getpixel((x,y));
            
            reds.append(locRed)
            greens.append(locGreen)
            blues.append(locBlue)

            reds.sort()
            greens.sort()
            blues.sort()
            
            colorNew = (reds[len(reds)/2], greens[len(greens)/2], blues[len(blues)/2])
            
            imgNew.putpixel((x,y), colorNew)

        reds[:] = []
        greens[:] = []
        blues[:]= []
            

imgNew.save("newImg.png")