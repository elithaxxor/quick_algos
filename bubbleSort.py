
def bubbleSort():
    ''' Set up data structure. last index is hihgest value.  '''
    input_array = ['4', '2', '3', '4']
    input_array_len = len(input_array)
    isSorted=False

    def bubble_elements(i, array):
        j = int(i) + 1
        array[i], array[j] = array[i], array[j]
        ''' helper function, to sort the array. array will not be copied, just iterated many times'''

    count = 0
    while not isSorted:
        for i in range(0, (input_array_len - count)):
            if input_array[i] > input_array[i+1]:
                sorted_array = bubble_elements(input_array, i)
                isSorted=Falses
            return sorted_array


def main():
    bubbleSort()
if __name__ == '__main__':
    sorted_array = main()
    print(sorted_array)
