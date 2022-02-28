# #o(n^2) -time, o(n)- space
# def isPalindrome(string):
# 	reversedString=""
# 	for i in reversed(range(len(string))):
# 		reversedString += string[i]
# 	return string == reversedString
#
#

# o(n), (o)n
def isPalindrome(string):
    reversedChar=[]
    for i in reversed(range(string)):
        reversedChar.append(string(i))
    return string == "".join(reversedChar)



## recursive - base case i, j
def isPalindrome(string, i=0): ## set i to zero if
    j = len(string)- 1 - i # compare start to final index. base case
    # return true if reaches base case
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)

