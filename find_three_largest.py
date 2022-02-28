def findThreeLargestNumbers(array):
    three_largest = [None, None, None]
    print(array)
    start = array[0]
    end = len(array) - 1
    end_val = array[-1]
    middle = end // 2
    middle_val = array[middle]
    print('start_val', start, 'end_val', end_val, 'middle_val', middle_val)
    print('\nend', end)
    print('middle', middle)
    for num in array:
        print('large array',num)
        updateLargest(num, three_largest)
    return three_largest


def updateLargest(num, three_largest):
    print(num, three_largest)
    if(three_largest[2] is None or num > three_largest[2]):
        shiftAndUpdate(three_largest, num, 2)
    elif (three_largest[1] is None or num > three_largest[1]):
        shiftAndUpdate(three_largest, num, 1)
    elif (three_largest[0] is None or num > three_largest[0]):
        shiftAndUpdate(three_largest, num, 0)

def shiftAndUpdate(array, num, index):
    print('array', array)
    print('shifting.. val', num, '\nindex', index)
    for i in range(index+1):
        if i == index:
            array[i] = num
            print('updated array', array)
        else:
            array[i]=array[i+1]
            print('shift array i+1', array)

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
result = findThreeLargestNumbers(array)
print('result', result)
