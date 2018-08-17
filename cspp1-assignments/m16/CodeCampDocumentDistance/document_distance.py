'''
    Document Distance - A detailed description is given in the PDF
'''
def frequency_count(in_str):
    words_list = in_str.split()
    for each_word in words_list:
        each_word = each_word.strip("!@#$%^&*()_?., ")
        print(each_word)
    print(words_list)

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    frequency_count(input1)
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
