'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''tokenize'''
    token_dict = {}
    for each_line in string:
        line_words = each_line.split()
        for each_word in line_words:
            each_word = ''.join(e for e in each_word if e.isalnum())
            if each_word in token_dict:
                token_dict[each_word] += 1
            else:
                token_dict[each_word] = 1
        each_line += 1 #for pylint
    return token_dict

def main():
    '''main'''
    no_lines = int(input())
    in_str = []
    for each_line in range(no_lines):
        in_line = input()
        in_str.append(in_line)
    print(tokenize(in_str))

if __name__ == '__main__':
    main()
