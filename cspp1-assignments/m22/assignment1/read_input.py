'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''Read input'''
    no_lines = int(input())
    for each_line in range(no_lines):
        in_line = input()
        print(in_line)
        each_line += 1 #for pylint

if __name__ == '__main__':
    main()
