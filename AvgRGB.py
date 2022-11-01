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
