## o(log(n) time o(log(n)) space --> recursive calls

def binarySearch():
    def recursive_search():
        nonlocal right, left, center
        if left > right:
            return 'nothing found'
        potential_match = array[middle]
        print(f'\n\n potential_match, {potenetial_match}')
        if target == potential_match:
            return middle

    input_array, target = [1, 4, 9, 1, 2], 4
    right = len(input_array)
    left = 0
    center = ((0 + right)/2)
    print('center ', center)
    return recursive_search()

def main():
    binarySearch()
if __name__ == '__main__':
    main()



