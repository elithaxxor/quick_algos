# make a new array and track  the sum of both # arrays, looking for
# sort the arrays
# use infinity to compare numbers and find teh smallest
# use while loop and conditional for BOTH array
# best to use array rather than hash table - array is fixed lengh
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")  #
    current = float("inf")
    smallestPair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1

        elif secondNum < firstNum:
            current = firstNum - secondNum

            idxTwo += 1
        
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]

    =return smallestPair


