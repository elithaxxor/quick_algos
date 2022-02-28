def bubbleSort(array):
    print('array', array)
    start_pos = 0
    start_val = array[0]
    end_pos = len(array)-1
    end_val = array[-1]
    isSorted=False
    print('start_ps',start_pos, 'start_val' ,start_val, 'end_pos' , end_pos, 'end_val' , end_val)

    counter = 0
    while not isSorted:
        for i in range(end_pos, start_pos, -1):
            print(i,'-> ',(array[i]))
            for j in range(start_pos, end_pos):
                print('-> ', (array[j]))
                print(j, '+1', array[start_pos + 1])
                if array[j] > array[start_pos+1]:
                    print('found dupe', array[end_pos-1])
                    swap(j, j+1, array)
                    isSorted=True

            print('count', counter)
        counter +=1
    return array
def swap(i, j, array):
    array[i], array[j]=array[j], array[i]
    print('X' * 50)
    print(array)

array = [45,234, 335,124,20,23, 23]
result= bubbleSort(array)
print('final result', result)

## ANOTHER ONE


def bubbleSort(array):
	isSorted = False
	counter = 0
	while not isSorted:
		isSorted=True
		for i in range(len(array) - 1):
			 if array[i] > array[i+1]:
				swap(i, i+1, array)
				isSorted=False
		counter += 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]


