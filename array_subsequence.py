
def validate_array(array, subArray):
    sub_index = 0
    len_array = len(array)
    len_subArray = len(subArray)
    new_array = []
   # for x in range(0, len_array):
    for x in array:
        print(x)
        if x == len_subArray:
            return False
        elif x == subArray[sub_index]:
            new_array.append(subArray[sub_index])
            sub_index+=1
    return sub_index == len_subArray



def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx]==value:
            seqIdx += 1
    return seqIdx == len(sequence)





array = [5, 1, 22, 25, 6, -1, 8, 10]
subArray = [1, 6, -1, 10]
results = validate_array(array, subArray)
results00 = isValidSubsequence(array, subArray)
print(results)
print('x'*50)
print(results00)


