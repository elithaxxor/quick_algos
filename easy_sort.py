## o(n) time o(1) space

def main():
    def find_threeLargest(array, val):
        ''' HELPER FUNCTION:  TRAVERSE ARRAY, AND PRINT ARRAY / ELEMENT'''

        index = array.index(val)
        print(array, val, index)

        if array[2] is None or val > array[2]:
            updateArray_pos(array, val, index) #TODO
        elif array[1] is None or val > array[1]:
            updateArray_pos(array, val, index) #TODO
        elif array[3] is None or val > array[3]:
            updateArray_pos(array, val, index)  # TODO

    def updateArray_pos(array, val, position):
        ''' helper function-- after '''
        for i in range (position+1):
            if i == position:
                array[i] = val
            else:
                array[i] = array[i+1]

    ''' init '''
    input_array = [1,5,2,5,3,5]
    largest_inputs = [None, None, None]
    for val in input_array:  ##
        find_threeLargest(input_array, val)


if __name__ == '__main__':
    main()