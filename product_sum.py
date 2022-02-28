def productSum(array, multiplyer=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplyer +1)
        else:
            sum += element
        return sum + multiplyer

array = [5,2,[7,-1],3,[6,[-13,8],4]]

print(array[0],array[1])
print(array[1])
print('array3a',array[3])
print('array3b',array[2],[1])
print('array4',array[4])

result = productSum(array)
print('result', result)
