'''
    Document Distance - A detailed description is given in the PDF
'''
import copy
import math

def frequency_count(in_str):
    words_list = in_str.split()
    freq_dict = {}
    for each_word in words_list:
        each_word = each_word.strip("!-@#$%^&*()_?.,\n ")
        each_word = each_word.lower()
        if each_word in freq_dict:
            freq_dict[each_word] += 1
        else:
            freq_dict[each_word] = 1
    return freq_dict

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def remove_stop_words(in_freq):
    in_freq_copy = copy.deepcopy(in_freq)
    stop_words = load_stopwords("stopwords.txt")
    for each_key in in_freq:
        if each_key in stop_words:
            del in_freq_copy[each_key]
    return in_freq_copy
def compute_similarity(freq_dict1,freq_dict2):
    common_dict  = {}
    for each_key in freq_dict1:
        if each_key not in freq_dict2:
            freq_dict2[each_key] = 0
    for each_key in freq_dict2:
        if each_key not in freq_dict1:
            freq_dict1[each_key] = 0

    for each_word in freq_dict1:
        if each_word in common_dict:
            common_dict[each_word].append(freq_dict1[each_word])
        else:
            common_dict[each_word] = [freq_dict1[each_word]]
    for each_word in freq_dict2:
        if each_word in common_dict:
            common_dict[each_word].append(freq_dict2[each_word])
        else:
            common_dict[each_word] = [freq_dict2[each_word]]
    num_val = 0.0
    den_val = 1.0
    den_sum1 = 0.0
    den_sum2 = 0.0
    for each_key in common_dict:
        #print(common_dict[each_key][0])
        num_val = num_val + (common_dict[each_key][0] * common_dict[each_key][1])
        den_sum1 = den_sum1 + (common_dict[each_key][0] ** 2)
        den_sum2 = den_sum2 + (common_dict[each_key][1] ** 2) 
    den_val = math.sqrt(den_sum1) * math.sqrt(den_sum2)
    #print(num_val/den_val)
    return num_val/den_val

def similarity(input1, input2):
    '''
        Compute the document distance as given in the PDF
    '''
    in1_freq = frequency_count(input1)
    in2_freq = frequency_count(input2)
    freq_dict1 = remove_stop_words(in1_freq)
    freq_dict2 = remove_stop_words(in2_freq)
    similarity_val = compute_similarity(freq_dict1,freq_dict2)
    return round(similarity_val, 8)
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
