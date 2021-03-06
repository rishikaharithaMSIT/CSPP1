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
    flag = 0

    for input_iterator in int_input:
         if input_iterator == '-':
             flag = 1
         else:
             digits_product *= int(input_iterator)

    if flag == 1:
        print("-"+str(digits_product))
    else:
        print(digits_product)

if __name__ == "__main__":
    main()
