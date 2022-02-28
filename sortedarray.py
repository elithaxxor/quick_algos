

def sorted_array(input_array):
    len_input_array = len(input_array)
    array = [0 for _ in input_array] ## to create an empty array that scales to inputsize
    print(array)
    for i in range(len_input_array):
        squared_val = input_array[i]
        array[i] = squared_val * squared_val
    array.sort()
    return array

def main():
    input_array = [1,2,9,5,7,3,4,5]
    returned_array = sorted_array(input_array)
    print(returned_array)
main()
