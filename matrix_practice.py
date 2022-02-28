import numpy
from numpy import *

def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1  # the first and last portion of top array
    startCol, endCol = 0, len(array[0] - 1)
    print('matrix bounds')
    print(startRow, endRow)
    print(startCol, endCol)

    while startRow <= endRow and startCol <= endCol: #conditional to maintain matrix bound
        for col in range(startRow, endRow):
            pass

array1 = array([
    [1,2,3,4],
    [1,2,3,4],
])eeeeee333weeeee3wwfdddjh
print('X' * 50)


spiralTraverse(array1)

print('X' * 50)



print(array1)
print(array1.dtype)
print(array1.ndim)
print(array1.shape)
print(array1.size) # dimension s
print(array1.itemsize) #byte size

print('X' * 50)
## convert to 1 dimension
array2 = array1.flatten()
print(array2)
print('X' * 50)
array3 = array2.reshape(2,4)
print(array3)
print('X' * 50)

## create matrix object
print('start of matrix ')
m = matrix('1234;9244;2444')
m2 = matrix(array1)
m3 = m * m2
print(diagonal(m))
print(type(m))
print(m)
print(m3)