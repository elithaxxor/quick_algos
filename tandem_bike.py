def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    len_redShirtSpeeds = len(redShirtSpeeds)
    len_blueShirtSpeeds = len(blueShirtSpeeds)

    total_red = ''
    total_blue = ''
    if fastest is True:
        for index, val in enumerate(redShirtSpeeds):
            print(index, val)
            print(blueShirtSpeeds[index])
            if index < len_redShirtSpeeds:
                total_red = redShirtSpeeds[index] + redShirtSpeeds[len_redShirtSpeeds - 1]
                total_blue = blueShirtSpeeds[index] + blueShirtSpeeds[len_blueShirtSpeeds - 1]
                print('red', total_red)
                print('blue', total_blue)
                print('total ', total_red + total_blue)
            return (total_red + total_blue)

    elif fastest is False:
        reversed_red = reverse_array(redShirtSpeeds)
        print('reversed_red', reversed_red)
    for index, val in enumerate(blueShirtSpeeds):
        if index < len_blueShirtSpeeds:
            total_red = redShirtSpeeds[index] + redShirtSpeeds[index - 1]
            total_blue = blueShirtSpeeds[index] + blueShirtSpeeds[index - 1]

            print('red', total_red)
            print('blue', total_blue)
            print('total ', total_red + total_blue)
            return (total_blue - total_red)


def reverse_array(array):
    start = 0
    len_array = len(array)

    end =  len_array - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    print(array)
    return array

redShirtSpeeds=[5,5,3,9,2]
blueShirtsSpeeds=[3,6,7,2,1]
fastest=True
results = tandemBicycle(redShirtSpeeds,blueShirtsSpeeds,fastest)
print('final_results', results)




### second try ##

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if not fastest:
        reverse_array(redShirtSpeeds)
    totalSpeed = 0

    for idx in range(len(redShirtsSpeeds)):
        rider1 = redShirtsSpeeds[idx]
        rider2 = blueShirtsSpeeds[len(blueShirtsSpeeds) - idx - 1]
        total_speed += max(rider1, rider2)
    return total_speed


def reverse_array(array):
    start = 0
    len_array = len(array)

    end =  len_array - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    print(array)
    return array
