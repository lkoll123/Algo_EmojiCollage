#Squarecropfunction
def cropSquare(filename,size):
    resizeImage = Image.new("RGB", (size,size))
    fullpath = 'C:\\Users\\lukad\\Algo 2022\\EmojiList\\' + filename
    im = Image.open(fullpath)
    if (im.width < im.height):
        scale = size/im.width
    else:
        scale = size/im.height
    
    for i in range(size):
        for j in range(size):
            r,g,b = im.getpixel((i/scale, j/scale))
            resizeImage.putpixel((i,j), (r,g,b))

    return resizeImage
