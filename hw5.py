def doubleVowel(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i + 1] in vowels:
            return True
    return False

def numPairs(targ_num, num_lst):
    total = 0
    for i in range(len(num_lst)):
        for j in range(i + 1, len(num_lst)):
            if num_lst[i] + num_lst[j] == targ_num:
                total += 1
    return total



def hideShow(input_str, msking_str):
    final_str = ''
    for i in range(len(msking_str)):
        if msking_str[i] == '0':
            final_str += input_str[i].replace(input_str[i], '#')
        else:
            if msking_str[i] == '1':
                final_str += input_str[i]
    return final_str
    # this works


def clean(string):
    x = 0
    y = -1
    white_space = [' ', '\n', '\t']
    while string[x] in white_space:
        x += 1
    string = string[x:]

    while string[y] in white_space:
        y -= 1
    string = string[:y + 1]
    return string


# find a way to do this without replace

def sequence(num):
    print(num)
    while num > 1:
        if num % 2 == 1:
            num += 1
            print(num)
        else:
            num = num // 2
            print(num)
    # this works


if __name__ == '__main__':
    import doctest

    print(doctest.testfile('hw5TEST.py'))
