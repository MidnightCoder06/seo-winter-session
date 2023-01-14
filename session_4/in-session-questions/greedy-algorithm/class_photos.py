
def classPhotos(redShirtHeights, blueShirtHeights):

    # sort in height order
    # default sort method is 0(log n)
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    # determine which color is in the front and back -> tallest student must be in the back row
    shirtColorInFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"

    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColorInFirstRow == "RED":
            if redShirtHeight >= blueShirtHeight:
                return False 
        else:
            if blueShirtHeight >= redShirtHeight:
                return False

    return True





