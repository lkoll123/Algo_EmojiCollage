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
    
    
