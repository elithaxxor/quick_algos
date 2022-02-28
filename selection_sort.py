import sys
def selectionSort():
    array = [5,9,9,2,1,4]
    array_index = 0
    end_pos = len(array) - 1
    next_pos = len(array) + 1

    def swap(next_pos, i, array):
        array[i], array[next_pos] = array[next_pos], array[i]
        print(array[next_pos], array[i])

    while array_index < end_pos:
        small_index = array_index
        for i in range(next_pos, end_pos):
            if array[small_index] > array[i]:
                smallest_val = i
        swap(next_pos, small_index, array)
        next_pos +=1
    return array

def main():
    sorted_array = selectionSort()
    print(sorted_array)


if __name__ == '__main__':
    main()
else:
    sys.exit(1)

