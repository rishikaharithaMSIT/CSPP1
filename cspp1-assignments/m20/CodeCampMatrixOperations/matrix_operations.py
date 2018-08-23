def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    pass

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and mqtrix 2

    # multiply matrix 1 and matrix 2
    matrix1_D = input().split(",")
    matrix1_D = list(map(int, matrix1_D))
    matrix1 = []
    for i in range(int(matrix1_D[0])):
        in_1 = input().split()
        print(in_1)

    matrix2_D = input().split(",")
    matrix2 = []
    for i in range(int(matrix2_D[0])):
        matrix2.append(input().split())
        matrix2 = list(map(int, matrix2[i]))

    if matrix1_D is not matrix2_D:
    	print("can't add")    
if __name__ == '__main__':
    main()
