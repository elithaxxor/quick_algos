array = [1,2,4,5,32,7,23,234,6,42,12345]

for i in range(len(array) - 2):
    left = i + 1
    right = len(array) - 1
    print(i,'-->', array[i])
    print('left', left)
    print('right', right)
