# linear time by sorting; n(log)n --> sorting algos run in n(log)n time
# create a swap function to move the smallest int from the left to right
# if int == int, pass
# set thhe smalest swap to the most recent right position (set multiple pointers)

def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
    j = len(array) - 1
    while i < j:  # the first while loop maintains array coverage
        while i < j and array[j] == toMove:  ## this controls the right array, travesing downline, swapping if value is smaler
            j -= 1  ## need to restate previouse while condition, otherwise results will not be valid
        if array[i] == toMove:
            swap(i, j, array)
        i += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

result = moveElementToEnd(array, toMove)
print(result)
