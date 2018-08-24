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
    if rows and cols:
        game = "Invalid"
    elif rows and diag:
        game = "Invalid"
    elif cols and diag:
        game = "Invalid"
    elif rows and cols and diag:
        game = "Invalid"
    elif rows or cols or diag:
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
    if invalid_input:
        print("invalid input")
    elif x_game == "Invalid" or o_game == "Invalid":
        print("invalid game")
    elif x_game and o_game:
        print("invalid game")
    elif x_game:
            print("x")
    elif o_game:
            print("o")
    elif x_game is False and o_game is False:
        print("draw")

if __name__ == "__main__":
    main()
