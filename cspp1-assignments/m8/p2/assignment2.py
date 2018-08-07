'''
Author: Rishika Haritha - 20186041
Encoding: Utf-8
'''

def sum_of_digits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n == 0:
    	return 0
    return n % 10 + sum_of_digits(n // 10)


def main():
    '''main function'''
    a = input()
    print(sum_of_digits(int(a)))

if __name__ == "__main__":
    main()
