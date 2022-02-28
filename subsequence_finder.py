# write a function that determins an arrays subsequence


def main(): ## o(n) - time; o(1) space
    ''' Set Index, and max/min params and track index'''
    input_array = [1,2,3,4,5]
    subSequence = [3,2,5]
    len_input_array, len_subSequence = len(input_array), len(subSequence)
    follow_array, follow_subSequence = 0, 0

    def find_sequence(array, subArray):
        ''' logic to find subsequence'''

        nonlocal len_input_array, len_subSequence, follow_array, follow_subSequence
        array_start, array_end = array[0], array[-1] ## set array postions


        while len_input_array < follow_array and len_subSequence < follow_subSequence:
            if array[follow_array] == subSequence[follow_subSequence]:  # if the array index is equla to len of sequence, rbeal
                follow_subSequence += 1
            follow_array += 1
        if array[follow_array] == len_subSequence:
            print(array[follow_array])
            return True
    find_sequence(input_array,subSequence) ## call to function


if __name__ == '__main__':
    main()