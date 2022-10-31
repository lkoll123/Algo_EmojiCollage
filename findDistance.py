#takes in an rgb value in the form of a list, and a list of such rgb values
#returns the index of the closest rgb value to the set value
def findDistance(rgb, listOfRGBs):
    
    minDistance = (listOfRGBs[0][0] - rgb[0])**2 + (listOfRGBs[0][1] - rgb[1])**2 + (listOfRGBs[0][2] - rgb[2])**2
    for i in range(len(listOfRGBs)):
        currentDistance = 0
        for j in range(3):
            currentDistance += (listOfRGBs[i][j] - rgb[j])**2
        if (currentDistance < minDistance):
            minDistance = currentDistance
            minIndex = i
    return minIndex
