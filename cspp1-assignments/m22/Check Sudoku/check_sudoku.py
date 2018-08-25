'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def make_cols(sudoku):
    '''make cols'''
    col_s = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(9):
            col_s[i].append(sudoku[j][i])
    return col_s
def make_squares(sudoku):
    sq_s = [[], [], [], [], [], [], [], [], []]
    sq_s = [[sudoku[0][0:3]+sudoku[1][0:3]+sudoku[2][0:3]], \
    [sudoku[3][0:3]+sudoku[4][0:3]+sudoku[5][0:3]],\
    [sudoku[6][0:3]+sudoku[7][0:3]+sudoku[8][0:3]],\
    [sudoku[0][3:6]+sudoku[1][3:6]+sudoku[2][3:6]],\
    [sudoku[3][3:6]+sudoku[4][3:6]+sudoku[5][3:6]],\
    [sudoku[6][3:6]+sudoku[7][3:6]+sudoku[8][3:6]],\
    [sudoku[0][6:9]+sudoku[1][6:9]+sudoku[2][6:9]],\
    [sudoku[3][6:9]+sudoku[4][6:9]+sudoku[5][6:9]],\
    [sudoku[6][6:9]+sudoku[7][6:9]+sudoku[8][6:9]],\
    ]
    print(sq_s)

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    #make_rows()

    col_s = make_cols(sudoku)
    make_squares(sudoku)
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()