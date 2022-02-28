def selectionSort(array):  # divide into two sublists- sorted and  unsorted.
    currentIdx = 0

    while currentIdx < len(array) - 1:  # current(0) to final index in urray
        smallestIdx = currentIdx  # to the left array index with the right arrays index
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i  # finds the smaller #
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
