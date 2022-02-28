def sorted_array(input_array, target):
    input_array.sort()
    len_input_array = len(input_array)
    array_start = 0
    array_end = len_input_array - 1

    print(input_array)

    while input_array[array_start] < input_array[array_end]:
        calculated_val = input_array[array_start] + input_array[array_end]
        if calculated_val == target:
            return calculated_val, input_array[array_start], input_array[array_end]
        elif calculated_val < target:
            input_array[array_start] = input_array[array_start+1]
        elif calculated_val > target:
            input_array[array_end] = input_array[array_start-1]
        elif input_array[array_start] == len_input_array:
            break
        print(calculated_val)



def main():
    input_array = [3, 5,-4, 8, 11, 1, -1, 6]
    target = 10
    returned_array, element_one, element_two = sorted_array(input_array, target)
    print( element_one, element_two)

main()
