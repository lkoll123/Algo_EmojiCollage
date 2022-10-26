def cropMultiple(im, multiple):
    newWidth = im.width - (im.width % multiple)
    newHeight = im.height - (im.height % multiple)
    
    resizeImage = Image.new("RGB", (newWidth,newHeight))
    
    for i in range(newWidth):
        for j in range(newHeight):
            r,g,b = im.getpixel((i, j))
            resizeImage.putpixel((i,j), (r,g,b))

    return resizeImage
