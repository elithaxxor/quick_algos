## ceasers cyper- take a shift value, take in text to shift
# lowercase starts at 65 , upper at 97

def caeser_cypher(shift_val, text):
    cypher = []
    text_len = len(text)
    ascii_lower, ascii_upper = 97, 122 #unicode a-z
    new_str = ''

    count = 0
    for letter in text:
        if count == text_len:
            break
       # print(letter); print(ord(letter))
        ascii_val = ord(letter)
        new_text = ascii_val + shift_val
        cypher.append(new_text)
        new_str.join(letter)
    convert_cypher(cypher)
    print(cypher)
    print(new_str)


def convert_cypher(cypher):
    converted_cypher = ''
    for i in (cypher):
        if i == len(cypher):
            break
        print(chr(i))
        if i <= 122:
            print(i)
            converted_char_upper = chr(i)
        converted_char = chr(96 + i % 122)
        converted_cypher.join(converted_char)


        print('upper bound', converted_char_upper)
        print('lower bound', converted_char)

    print(converted_char_upper + converted_char)
    print('converted cypher', converted_cypher)


shift_val = 2
text = 'xyz'
caeser_cypher(shift_val, text)


def caesarCipherEncryptor(string, key):
    cypher = []
    text_len = len(text)
    ascii_lower, ascii_upper = 97, 122  # unicode a-z
    new_str = ''
    shift_val = key


count = 0
for letter in text:
    if count == text_len:
        break
    # print(letter); print(ord(letter))
    ascii_val = ord(letter)
    new_text = ascii_val + shift_val
    cypher.append(new_text)
    new_str.join(letter)
    print(new_text)
convert_cypher(cypher)
print(cypher)
print(new_str)
return cypher


def convert_cypher(cypher):
    converted_cypher = ''
    for i in (cypher):
        if i == len(cypher):
            break
        print(chr(i))
        if i <= 122:
            print(i)
            converted_char_upper = chr(i)
        converted_char = chr(96 + i % 122)
        converted_cypher.join(converted_char)
        return converted_cypher


def translate_cypher(result):
    print('x' * 50)
    print(type(result))
    converted_cyher = []
    for x in result:
        if x <= 122:
            print('x is less than 122')
    print(x)
    converted_char_upper = chr(x)
    converted_cyher.append(converted_char_upper)


converted_char = chr(96 + x % 122)
converted_cyher.append(converted_char)

# print(chr(x))
# print(converted_char)
# print('upper bound', converted_char_upper)
# print('lower bound', converted_char)
print(converted_cyher)
return (converted_cyher)

# print(converted_char_upper + converted_char)
# print('converted cypher', converted_cypher)


text = 'xyz'
key = 2
result = caesarCipherEncryptor(text, key)
print(result)

tru_res00 = convert_cypher(result)
print('true_res__1', tru_res00)

true_res = translate_cypher(result)
print('true res')
print(true_res)


def caesarCipherEncryptor(string, key):
    # Write your code here.
    newLetters = []
    newKey = key % 26
    print(newKey)
    alphabet = list('abdcdefghijklmnopqrstuvwxyz')
    for letter in string:
        new_letters = newLetters.append(getNewLetter(letter, newKey, alphabet))
    decrypt = "".join(newLetters)
    return decrypt


def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    print(newLetterCode)
    # 	if alphabet[newLetterCode] is None:
    # 		return

    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]


string = 'xyz'
key = 2

cypher = caesarCipherEncryptor(string, key)
print(cypher)



''' WORKING '''

def caesarCipherEncryptor(string, key):
    newLetters=[]
    newKey = key %26
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey))
	return "".join(newLetters)

def getNewLetter(letter,key):
	newLetterCode = ord(letter)+key
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


