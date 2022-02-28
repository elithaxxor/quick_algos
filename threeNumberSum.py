# first sort the array, that way the left element is garuneteed to be smaller than right
# move one pointer at a time to ensure summation is correct
# if left and right sub sequence do not add to target, then shift right and left and check condition,b


def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        print(i, '-->', array[i])
        print('left', left)
        print('right', right)

        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1  ## to continue traversing the array
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets


