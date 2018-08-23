from operator import add
def mult_matrix(matrix1_D, matrix1, matrix2_D,matrix2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if matrix1_D[0] != matrix2_D[1] or matrix1_D[1] != matrix2_D[0]:
        return None
    multi_matrix =[]
    for i in range(matrix1_D[0]):
        row = []
        k = 0
        for j in range(matrix1_D[1]):
            k += matrix1[i][j]*matrix2[j][i]
            row.append(k)
        print(row)
def add_matrix(matrix1_D, matrix1, matrix2_D,matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if matrix1_D != matrix2_D:
        return None
    sum_matrix = []
    for i in range(matrix1_D[0]):
        row = list( map(add, matrix1[i], matrix2[i]))        
        sum_matrix.append(row)
    return sum_matrix
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
        in_1 = list(map(int, in_1))
        matrix1.append(in_1)

    matrix2_D = input().split(",")
    matrix2_D = list(map(int, matrix2_D))
    matrix2 = []
    for i in range(int(matrix2_D[0])):
        in_2 = input().split()
        in_2 = list(map(int, in_2))
        matrix2.append(in_2)


    
    

    print(add_matrix(matrix1_D, matrix1, matrix2_D,matrix2))
    print(mult_matrix(matrix1_D, matrix1, matrix2_D,matrix2))
if __name__ == '__main__':
    main()
