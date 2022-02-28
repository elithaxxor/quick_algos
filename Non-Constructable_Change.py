## The minimum value of change is defined as the maximum input_array element - 1
## ie [1,4,9] the minimum anount of chang ethat cannot be created is 8 ]

def main(): ## load input
    input_array = [1, 4, 9, 14]
    input_array.sort()
    input_array_len = len(input_array)
    array_end_val = input_array[-1]
    array_start_val = input_array[0]


    def find_min_change(coin_bag, bag_min, bag_max): ## logic to calculate min_max change
        print(coin_bag)
        for index,  coin in enumerate(coin_bag):
            min_val = coin_bag[index+1]
            if coin > min_val:
                return min_val
            coin_bag += coin_bag[coin+1]
        return coin_bag

    the_change = find_min_change(input_array, array_start_val, array_end_val) ## call to logic
    print(the_change)

if __name__ == '__main__':
    main()

