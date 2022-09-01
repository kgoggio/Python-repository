#kyle Goggio
#reference:
#reference for squares function: https://djangocentral.com/python-program-to-check-if-a-number-is-perfect-square/

def vowelIndex(word):
    vowel_lst = ['a','e','i','o','u','A','E','I','O','U']
    for char in word:
        if char in vowel_lst:
            return word.index(char)
    return(-1)

def flipCase(word):
    flipped_word = ''
    for c in word:
        if c == c.lower():
            flipped_word += c.upper()
        else:
            flipped_word += c.lower()
    return flipped_word

def palindromes(sentence):
    sentence_no_period = sentence.strip('.')
    sentence_no_per_ques = sentence_no_period.strip('?')
    sentence_no_scol_per_ques = sentence_no_per_ques.replace(';', '')
    sentence_no_exc_scol_per_ques = sentence_no_scol_per_ques.strip('!')
    sentence_no_punctuation = sentence_no_exc_scol_per_ques.replace(',', '')
    sentence_lst = sentence_no_punctuation.split(' ')
    palindrome_lst = []
    for item in sentence_lst:
        if item[0:].upper() ==item[::-1].upper():
            palindrome_lst.append(item)
    return palindrome_lst

def squares(num_lst):
    running_lst = []
    for row in num_lst:
        for item in row:
            item_sqrt = item**0.5
            if item_sqrt%1 == 0:
                running_lst.append(item)
                #why  does this work?
    return len(running_lst)
        #prints the list, reprinting each time new item is added
                #print(item)
                #that returns the individual perfect squares
                #





def rps(p1,p2):
    if p1 == 'R':
        if p2 == 'S':
            return -1
        elif p2 == 'R':
            return 0
        return 1

    elif p1 == 'P':
        if p2 == 'R':
            return -1
        elif p2 == 'P':
            return 0
        return 1

    else:
        p1 == 'S'
        if p2 == 'P':
            return -1
        elif p2 == 'S':
            return 0
        return 1




if __name__ == '__main__':
    import doctest
    print(doctest.testfile('hw4TEST.py'))