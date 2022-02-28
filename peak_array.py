# PEAK --> array with int values increasing to tip, then decreasing.
## identify largest value
# the peak will have lower value on the left, higher value on the right
# set array position, left, middle right. iterate through array,
# create function to to A-B test LMR values.
# identify the lenght of back array


def longestPeak(array):
    for idx in range(start, end): ## to check accuracy

        print(array)
        start = 0
        start_plus = start + 1
        end = len(array) - 1

        beginning = array[start]
        middle = array[start_plus]
        forward = middle + 1
        print(beginning, middle, forward)
        print(start, end)

        print(array[start])
        peak_val = middle > beginning < forward
        print('peak_val', peak_val)
        if not peak_val:
            continue

        while middle > beginning and forward < middle:
            print('found middle at', middle)
            peak_array = len(array[middle] + 1)
            return peak_array
            # return peak_array
        start += 1


array = [34, 36, 67, 99, 88, 77, 66, 55]
results = longestPeak(array)
print('results', results)

# for idx in range(start, array[-1]): ## to check accuracy
#     print(idx, array[idx])
#

# for idx in range(start, array[-1]): ## to check accuracy
