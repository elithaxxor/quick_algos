def classPhotos(redShirtHeights, blueShirtHeights):

    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    len_redShirtHeights = len(redShirtHeights)
    len_blueShirtHeights = len(blueShirtHeights)

    print(redShirtHeights)
    print(blueShirtHeights)

    blue_shirt_pos = 0
    red_shirt_pos = 0

    for student in redShirtHeights:
        if redShirtHeights[red_shirt_pos] > redShirtHeights[red_shirt_pos+1]:
            redShirtHeights[red_shirt_pos] = redShirtHeights[red_shirt_pos+1]
    for student in blueShirtHeights:
        if blueShirtHeights[blue_shirt_pos] > blueShirtHeights[blue_shirt_pos+1]:
            blueShirtHeights[blue_shirt_pos] = blueShirtHeights[blue_shirt_pos + 1]

        array=[]
        largest_pos = ""
        if blueShirtHeights[0] > redShirtHeights[0]:
            largest_pos = 'BLUE'
            print(blueShirtHeights[0])
            array.append(blueShirtHeights[0])
            redShirtHeights.append(blueShirtHeights)
        else:
            largest_pos = 'RED'
            array.append(redShirtHeights[0])
            blueShirtHeights.append(redShirtHeights)

        if largest_pos =='RED':
            if redShirtHeights[red_shirt_pos] >= blueShirtHeights[blue_shirt_pos]:
                return False

        print(largest_pos)
        print(redShirtHeights)
        print(blueShirtHeights)

    return True

redShirtHeights = [6, 9, 2, 4, 5]
blueShirtHeights=[5, 8, 1, 3, 4]
result = classPhotos(redShirtHeights, blueShirtHeights)
print(result)


#### another version

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reversed=True)
    blueShirtHeights.sort(reversed=True)

    first_row = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
    for idx in range(0, len(redShirtHeights)):
        redShirtHeight = redShirtHeights(idx)
        blueShirtHeight = blueShirtHeights(idx)
        print(redShirtHeight, blueShirtHeight)
        if first_row == 'RED':
            if redShirtHeight >= blueShirtHeigh:
                return False
            elif blueShirtHeight >= blueShirtHeight:
                return False
        return True


