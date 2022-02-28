def runLengthEncoding(string, document):
    str_len = len(string)
    end_pos = str_len -1
    start_pos = 0
    end_val = string[-1]
    start_val = string[0]

    ### document vals ###
    doc_len = len(document)
    doc_end = len(document)-1
    doc_start = document[0]
    doc_end_val = document[-1]
    print('str_len',str_len, 'end_pos',end_pos, 'start_pos',start_pos)
    print('end_val',end_val)
    print('X'*50)
    print('doc_len',doc_len, 'doc_end_pos',doc_end, 'doc_start_pos',doc_start)
    print('end_val',doc_end_val)
    alphabet = 'abscedfhighjklmpqrstuvwxyz'

    found_alphabet = ""
    count = 0
    alphabet_dict = {found_alphabet: count}
    for index in range(start_pos, end_pos):
        if string[index] in alphabet:
            print('X'* 50 )
            print('indexing.. ', index, string[index], count)
            alphabet_dict=
            count += 1
            print( count )

        count+=1

    # return string

def find_dupe():
    #TODO
    count = 0
    found_alphabet = {}
    while document <= end_pos[-1]:
        if string[index] in alphabet:
            print('alphabet found', alphabet)
            found_alphabet.add(alphabet)
            count += 1
        if count == doc_len or count == str_len:
            return found_alphabet
    print('found alphabets', found_alphabets)


string = 'AAAAAAAAABBCCCCDD'
document = "Bste!hetsi ogEAxpelrt x"

result = runLengthEncoding(string, document)
print('result', result)




