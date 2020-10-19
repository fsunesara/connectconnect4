import numpy as np

def create_board():
    board = np.zeros((6,6,7,7), int)
    return board

def print_board(board):
    for a in range (len(board)): 
        for b in range (len(board[a])):
            for c in range (len(board[a][b])):
                for d in range (len(board[a][b][c])):
                    print(board[a][b][c][d], end=" ")
                print("\t", end="")
            print()
        print()

board = create_board()
print_board(board)
