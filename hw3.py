

def cheer(team_name):
    print('How do you spell winner?')
    print('I know, I know!')
    for char in team_name:
        print(char.upper(), end=' ')
    print("!\nAnd that's how you spell winner!")
    print("Go "+team_name+'!')

def vowelCount(text):
    a = str(text.count('a'))
    e = str(text.count('e'))
    i = str(text.count('i'))
    o = str(text.count('o'))
    u = str(text.count('u'))
    #is there a way to do this better/prettier?
    print("a, e, i, o, and u appear, respectively, "+a+', '+e+', '+i+', '+o+', '+u+' times.')


def crypto(txt_file_name):
    with open(txt_file_name) as txt_file:
        for line in txt_file:
            true_line= line.strip('\n')
            if "secret" in line:
                print(true_line.replace("secret","xxxxxx"))
            else:
                print(true_line)
        print('\n'.strip('\n'))


def links(html_file_name):
    with open(html_file_name) as html_file:
        html_file_contents = html_file.read()
        return html_file_contents.count('</a>')

def duplicate(txt_file_name):
    with open(txt_file_name) as txt_file:
        for line in txt_file:
            line_no_comma = line.replace(',', ' ')
            line_no_quest_comma = line_no_comma.replace('?', ' ')
            line_no_per_quest_comma = line_no_quest_comma.replace('.', ' ')
            clean_line_lower = line_no_per_quest_comma.lower()
            clean_line_list = clean_line_lower.split(' ')
            for element in clean_line_list:
                if clean_line_list.count(element) >1:
                    return True
            return False


if __name__ == '__main__':
    import doctest
    print(doctest.testfile('hw3TEST.py'))