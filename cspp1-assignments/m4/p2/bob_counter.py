'''
Author: Rishika Haritha - 20186041
Date: 1-August-2018
Encoding: Utf-8
'''

'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''

def main():
    '''This is main function'''
    input_string = input()
    # the input string is in s
    # remove pass and start your code here
    count_bob = 0 
    for i in range(len(input_string)-2):
        if input_string[i:i+3] == 'bob':
            count_bob += 1
    print(count_bob)

if __name__ == "__main__":
    main()
