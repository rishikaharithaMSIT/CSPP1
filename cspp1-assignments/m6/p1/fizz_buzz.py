'''
Author: Rishika Haritha - 20186041
Encoding: Utf-8
'''

'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    input_num = int(input())
    start_index = 1
    while start_index <= input_num:
            if start_index % 15 == 0:
                print("FizzBuzz")
            elif start_index % 3 == 0:
                print("Fizz")
            elif start_index % 5 == 0:
                print("Buzz")
            else:
                print(start_index)
            start_index += 1


if __name__ == "__main__":
    main()
