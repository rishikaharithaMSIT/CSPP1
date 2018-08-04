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

  

    for iterator_num in range(input_num+1):
    	
    	if iterator_num % 15 == 0:
    		print("FizzBuzz")
    	elif iterator_num % 3 == 0:
    		print("Fizz")
    	elif iterator_num % 5 == 0:
    		print("Buzz")
    	else:
       		print(iterator_num)


if __name__ == "__main__":
    main()
