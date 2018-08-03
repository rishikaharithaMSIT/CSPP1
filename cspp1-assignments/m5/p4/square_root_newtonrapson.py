'''
Author: Rishika Haritha - 20186041
Encoding: Utf-8
'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''main function'''
    square_num = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    # your code starts here
    guess_num = square_num/2.0

    while abs(guess_num**2 - square_num) >= epsilon:
        guess_num = guess_num - ((guess_num**2) - square_num)/(2*guess_num)

    print(guess_num)

if __name__ == "__main__":
    main()
