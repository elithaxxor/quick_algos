def spirarlTraveral(array):
    result = []
    startRow = 0
    endRow =len(array)-1 # height
    startCol= 0
    endCol = len(array[0])-1 # length
    print(startRow, endRow) # -->> PERMITER
    print(startCol, endCol) # -->> ELEMENTS

    while startRow <= endRow and startCol <= endCol:
        for idx in range(startCol, endCol+1): # top row
            result.append(array[startRow][idx])
            print(result)
        #
        for idx2 in range(startRow+1, endRow+1): # right side
            result.append(array[idx2][endCol])   # swap the idx position and val from previous for loop, to ensure proper appending [val] plus array[val]

        for idx3 in reversed(range(startCol, endCol)): # bottom traversal
            result.append(array[endRow][idx3])

        for idx4 in reversed(range(startRow+1, endRow)): #left traversal
            result.append(array[startRow+1])


array = (
    [1,2,3,45,5],
    [1,23,3,4,53],
    [31,233,32,41,533]
)

spirarlTraveral(array)
