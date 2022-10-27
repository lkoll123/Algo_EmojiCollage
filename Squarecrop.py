#takes in a file name and a side length(size)
#returns the image cropped into a square and then scaled to the requested size for each side length
def cropSquare(filename,size):
    fullpath = 'C:\\Users\\lukad\\Algo 2022\\EmojiList\\' + filename
    im = Image.open(fullpath)
    if (im.width < im.height):
        scale = size/im.width
    else:
        scale = size/im.height
    
    resizeImage = Image.new("RGB", (int(scale*im.width), int(scale*im.height)))
    for i in range(0, resizeImage.width):
        for j in range(0, resizeImage.height):
            RGB = im.getpixel((int(i/scale), int(j/scale)))
            resizeImage.putpixel((i, j), (RGB[0], RGB[1], RGB[2]))

    return resizeImage
