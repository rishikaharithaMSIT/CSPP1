def checkGame(board, player):
    game = False
    def checkRows(board, player):
        rows = False
        for i in range(len(board)):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                rows = True
        return rows
    def checkCols(board, player):
        cols = False
        for i in range(len(board)):
            if board[0][i] == player and board[1][i] == player and board[2][i]== player:
                cols = True
        return cols
    def checkdiags(board, player):
        diags = False
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            diags = True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            diags = True 
        return diags

    rows = checkRows(board, player)
    cols = checkCols(board, player)
    diag = checkdiags(board, player)
    if rows == True and cols == True:
        game = "Invalid"
    elif rows == True and diag == True:
        game = "Invalid"
    elif cols == True and diag == True:
        game = "Invalid"
    elif rows == True and cols == True and diag == True:
        game = "Invalid"
    elif rows == True or cols == True or diag == True:
        game = True
    return game

def main():
    board = []
    invalid_input = False
    for i in range(3):
        in_row = input().split()
        board.append(in_row)
        for j in in_row:
            if j != 'x' and j != 'o' and j != '.':
                invalid_input = True

    x_game = checkGame(board, 'x')
    o_game = checkGame(board, 'o')
    if invalid_input == True:
        print("invalid input")
    elif x_game == "Invalid" or o_game == "Invalid":
        print("invalid game")
    elif x_game == True and o_game == True:
        print("invalid game")
    elif x_game == True:
            print("x")
    elif o_game == True:
            print("o")
    elif x_game == False and o_game == False:
        print("draw")

if __name__ == "__main__":
    main()
