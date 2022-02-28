#determine if the array is monotonic (left to right are either non increaseing or non decreasing)
# NONINCREASING / NON DECREASING (back to back elements with same element value are still monotonic
# first determine the array is going up or down (check order of first two arrays)
## first determien the direction

def isMonotonic(array):
    i = 0
    j = i + 1
    len_array = len(array) - 1
    print(len_array)
    direction = True
    while i < len_array:
        direction = isReversed(i, j, array)
        i += 1
    return direction

def isReversed(i, j, array):
    if array[i] > array[j]:
        while array[i] > array[j + 1]:
            return True
    elif array[i] == array[j]:
        while array[i] < array[j + 1]:
            return True
    elif array[i] < array[j]:
        return False

array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
results = isMonotonic(array)
print(results)


## second try
def isMonotonic(array):
    isNonIncreasing = True
    isNonDecreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        elif array[i] > array[i - 1]:
            isNonIncreasing = False

    return isNonDecreasing or isNonIncreasing

