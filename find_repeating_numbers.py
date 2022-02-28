# o of n because hash table has only lsowercase *26)  vals

# brute force
def firstNonRepeatingCharacter(string):
    for idx in range(len(string)):
        foundDuplicate = False
        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate=True
    if not foundDuplicate:
        return idx
    return -1


def firstNonRepeatingCharacterII(string):
    charicterFrequenies={}
    for charicter in string:
        charicterFrequenies[charicter] =  charicterFrequenies.get(charicter, 0) + 1
        print('frequency', charicterFrequenies[charicter])

    for idx in range(len(string)):
        charicter = string[idx]
        if charicterFrequenies[charicter] == 1:
            print('check',charicter )
            return idx
    return -1



string="abcdcaf"
resultII=firstNonRepeatingCharacterII(string)
print(resultII)
result=firstNonRepeatingCharacter(string)
print(result)
