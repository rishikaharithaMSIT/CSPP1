'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    li_keys = []
    for each_key in dictionary:
        li_keys.append(each_key)

    li_keys.sort()

    for each_key in li_keys:
        print(each_key, "-", ''.join('#' for e in range(dictionary[each_key])))

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
