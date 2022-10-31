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
  
#Squarecropfunction
def cropSquare(filename,size):
    fullpath = 'C:\\Users\\lukad\\Algo 2022\\EmojiList\\' + filename
    im = Image.open(fullpath)
    if (im.width < im.height):
        scale = size/im.width
    else:
        scale = size/im.height

    count = 0
    resizeImage = Image.new("RGB", (int(scale*im.width), int(scale*im.height)))
    for i in range(0, resizeImage.width):
        for j in range(0, resizeImage.height):
            count = count + 1
            try:
                RGB = im.getpixel((int(i/scale), int(j/scale)))
                resizeImage.putpixel((i, j), (RGB[0], RGB[1], RGB[2]))
            except:
                resizeImage.putpixel((i, j), (255, 255, 255))

    return resizeImage

#Function that uses cropSquare ad emojiread functions to crop, and then append averageRGB values for all emoji to a list

#this list will be a list of lists, holding the averageRGB values of all emojis in a folder
averageRGB = []

def emojiRGB(inputarr):
  #accessing all files in folderEmojiList, which holds all of the emojis
  counter = 0
  for filename in os.listdir("C:\\Users\\lukad\\Algo 2022\\EmojiList"):
    counter = counter + 1
    #using cropSquare function to crop emoji to 50x50 Pixels size, and assigning the resized image to variable resizedimage
    resizedimage = cropSquare(filename, 50)
    emojiread(resizedimage, inputarr)
    print(counter)
      
    
  print(inputarr)
  
  
emojiRGB(averageRGB)

    
        
  
