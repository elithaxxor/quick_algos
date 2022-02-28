def binarySearch(array, target):
    right = len(array) - 1
    left = 0
    print('right', right)
    print('target', target)
    return binarySearchHelper(array, target, left, right)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = array[middle]
    # array.sort()
    # print(potential_match)
    if target == potential_match:
        print('found match with target+array: {middle, target}', middle, target)
        return middle
    if target < potential_match:
        return binarySearchHelper(array, target, left, middle - 1)
    elif target > potential_match:
        return binarySearchHelper(array, target, middle + 1, right)
    # else:
    #     return binarySearchHelper(array, target, left, middle)


test_array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
find = 71
result = binarySearch(test_array, find)
print(result)
