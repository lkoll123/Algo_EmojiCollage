import os
from PIL import Image
#function that takes in image(emoji), and list(inputarr) and appends a list containing the average of all R values, all B values, and all G values onto that list
def emojiread(emoji, inputarr):
  #Getting width and height of image)
  width, height = emoji.size
  #counting number of pixels in image and assigning it to numpixels
  numpixels = width * height
  #list cumulativeRGB will hold the added total of all R, G, and B values of all pixels in the emoji
  cumulativeRGB = [0, 0, 0]
  #list avgRGB will hold the average of all R, G, and B values of all pixels in the emoji
  avgRGB = [0, 0, 0]
  #nested for loop to access every pixel(every x and y position)
  for x in range(0, width):
    for y in range(0, height):
      #Accessing the r, g, b values at the current pixel, and adding them to list cumulativeRGB
      originalrgb = emoji.getpixel((x, y))
      for i in range(0, 3):
        cumulativeRGB[i] = cumulativeRGB[i] + originalrgb[i]
  #adding the int truncated average of all R, G, B values into list avgRGB by dividing cumulativeRGB values by numpixels(which holds number of pixels)
  for j in range(0, 3):
    avgRGB[j] = avgRGB[j] + int(cumulativeRGB[j]/numpixels)
  #appending averageRGB to inputarr
  inputarr.append(avgRGB)
  
#takes in a file name, side length(size), and location of file (path)
#returns the image cropped into a square and then scaled to the requested size for each side length
def cropSquare(filename,size,path):
    #stores the path to the specific image in variable fullpath
    fullpath = path + '\\' + filename
    im = Image.open(fullpath)
    #Generates a scale based off of whether the height or length is longer
    if (im.width < im.height):
        scale = size/im.width
    else:
        scale = size/im.height
    
    resizeImage = Image.new("RGB", (int(scale*im.width), int(scale*im.height)))
    for i in range(0, resizeImage.width):
        for j in range(0, resizeImage.height):
            try:
                RGB = im.getpixel((int(i/scale), int(j/scale)))
                resizeImage.putpixel((i, j), (RGB[0], RGB[1], RGB[2]))
            except:
                resizeImage.putpixel((i, j), (255, 255, 255))
    os.remove(path + "//" + filename)
    resizeImage.save(path + "//" + filename, 'PNG')
    return resizeImage

#Function that uses cropSquare ad emojiread functions to crop, and then append averageRGB values for all emoji to a list

#this list will be a list of lists, holding the averageRGB values of all emojis in a folder
averageRGB = []

#takes in an empty list (inputarr) and the path where the emojis are stored (pathToPics).
#calls both cropSquare and emojiread for all emojis in folder, taking in a list inputarr and appending all averageRGB values, generated by the emojiread function, to inputarr
def emojiRGB(inputarr, pathToPics):
  #accessing all files in folderEmojiList, which holds all of the emojis
  counter = 0
  for filename in os.listdir(pathToPics):
    #using cropSquare function to crop emoji to 50x50 Pixels size, and assigning the resized image to variable resizedimage
    resizedimage = cropSquare(filename, 50, pathToPics)
    emojiread(resizedimage, inputarr)
    try:
        
        os.rename(pathToPics + '//' + filename,pathToPics + '//' + str(counter) + '.png')
    except FileExistsError as e:
        pass
    counter += 1
      
  #printing inputarr with all average RGBS for all emojis
  return inputarr

#takes in a file name and the multiple by which the height and width should be divisible, and returns the image cropped to fit those parameters
def cropMultiple(filename, multiple, path):
    fullpath = path + '\\' + filename
    im = Image.open(fullpath)
    newWidth = im.width - (im.width % multiple)
    newHeight = im.height - (im.height % multiple)
    resizeImage = Image.new("RGB", (newWidth,newHeight))
    
    for i in range(newWidth):
        for j in range(newHeight):
            r,g,b = im.getpixel((i, j))
            resizeImage.putpixel((i,j), (r,g,b))

    os.remove(path + "\\" + filename)
    resizeImage.save(path + "\\" + filename, 'PNG')
    print(resizeImage.width, resizeImage.height)
    return resizeImage
  
   
  
#takes in a file name, top left corner coordinates of a part of an image, the width of the section, and the height.
#returns the average RGB value in that area.
def avgRGB(filename, startX, startY, width, height, path):    
    r = 0
    g = 0
    b = 0
    fullpath = path + '\\' + filename
    im = Image.open(fullpath)
    
    for i in range(startX, startX + width):
        for j in range(startY, startY + height):
            r += im.getpixel((i,j))[0]
            g += im.getpixel((i,j))[1]
            b += im.getpixel((i,j))[2]
    area = width*height
    avgR = int(r/area)
    avgG = int(g/area)
    avgB = int(b/area)
    avgRGB = avgR, avgG, avgB

    return avgRGB
  
#takes in an rgb value in the form of a list, and a list of such rgb values
#returns the index of the closest rgb value to the set value
def findClosest(rgb, listOfRGBs):
    
    minDistance = (listOfRGBs[0][0] - rgb[0])**2 + (listOfRGBs[0][1] - rgb[1])**2 + (listOfRGBs[0][2] - rgb[2])**2
    for i in range(len(listOfRGBs)):
        currentDistance = 0
        minIndex = 0
        for j in range(3):
            currentDistance += (listOfRGBs[i][j] - rgb[j])**2
        if (currentDistance < minDistance):
            minDistance = currentDistance
            minIndex = i
    return minIndex
  
def Placeimage(img, xStart, yStart, fileNumber, pathEmoji, pathImage, new):
    fullpathEmoji = pathEmoji + '\\' + str(fileNumber) + '.png'
    fullpathImage = pathImage + '\\' + img
    emoji = Image.open(fullpathEmoji)
    image = Image.open(fullpathImage)
    
    for x in range(0, emoji.width):
        for y in range(0, emoji.height):
            origrgb = emoji.getpixel((x, y))
            new.putpixel((xStart + x, yStart + y), (origrgb[0], origrgb[1], origrgb[2]))
                		
    return newimg

pathTwo = 'C:\\Users\\vgonz\\OneDrive\\Documents'  
path = 'C:\\Users\\vgonz\\OneDrive\\Documents\\Algorithm Design\\EmojiPics'  
fileName = '900x520_piano-min.jpg'


#Calling emojiRGB
emojiRGB(averageRGB, path)
#Using cropMultiple function to crop image to a square that is a multiple of the emoji width and height(50)
cropMultiple(fileName, 50, pathTwo)
mainImage = Image.open(pathTwo + '\\' + fileName)
newimg = Image.new("RGB", (mainImage.width, mainImage.height))
newimg.save(pathTwo + '\\' + 'newimg.jpg')
for x in range(0, int(mainImage.width/50)):
    for y in range(0, int(mainImage.height/50)):
        newimage = Image.open(pathTwo + '\\' + 'newimg.jpg')
        #Getting the average rgb value of a 50*50 square in image fileName
        avgval = avgRGB(fileName, 50 * x, 50 * y, 50, 50, pathTwo)
        #Getting the closest RGB value in array averageRGB(holds all of the average RGBS of the emojis), to the avgval found in the given 50*50 square of pixels in image fileName
        closeRGB = findClosest(avgval, averageRGB)
        
        Placeimage((str(closeRGB) + '.png'), 50 * x, 50 * y, closeRGB, path , path, newimage)

newimage.show()
