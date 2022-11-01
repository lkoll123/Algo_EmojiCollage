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

    os.remove(path + "//" + filename)
    resizeImage.save(path + "//" + filename, 'PNG')
    return resizeImage
