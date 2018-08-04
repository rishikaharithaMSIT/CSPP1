'''
Author: Rishika Haritha - 20186041
Encoding: Utf-8
'''

def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = input()

    digits_product = 1

    for input_iterator in int_input:
    	digits_product *= int(input_iterator)
    	
    print(digits_product)



if __name__ == "__main__":
    main()
