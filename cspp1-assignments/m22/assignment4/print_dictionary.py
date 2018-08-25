'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''print dictionary'''
    li_keys = []
    for each_key in dictionary:
        li_keys.append(each_key)

    li_keys.sort()

    for each_key in li_keys:
        print(each_key, "-", dictionary[each_key])

def main():
    '''in main()'''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
