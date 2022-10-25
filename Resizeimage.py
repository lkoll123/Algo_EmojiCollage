def resize(image3, scale):
    resizeImage = Image.new("RGB", (int(scale*image3.width), int(scale*image3.height)))
    for i in range(0, resizeImage.width):
        for j in range(0, resizeImage.height):
            r, g, b = image3.getpixel((int(i/scale), int(j/scale)))
            resizeImage.putpixel((i, j), (r, g, b))
        return resizeImage
