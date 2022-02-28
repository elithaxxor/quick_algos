def generateDocument(characters, document):
    charicterCounts = {}

    for charicter in characters:
        if charicter not in charicterCounts:
            charicterCounts = 0

        charicterCounts[charicter] += 1

    for charicter in document:
        if charicter not in charicterCounts or charicterCounts[charicter] == 0:
            return False

        charicterCounts[charicter] -= 1

    return True


charciters = "Bste!hetsi ogEAxp	elrt x "
document = "AlgoExpert is the Best!"

generateDocument(charciters, document)

