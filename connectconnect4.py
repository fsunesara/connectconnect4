import numpy as np
import pygame

def create_board():
	board = np.zeros((6,6,7,7), int) #bigrow, bigcolumn, row, column
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

def winning_move(big, board, piece, row, col):
	if big:
		for a in range(len(board)-3):
			for b in range(len(board[a])):
				if board[b][a] ==  piece and board[b][a+1] == piece and board[b][a+2] == piece and board[b][a+3] == piece:
					return True

		for c in range(len(board)):
			for d in range(len(board[a])-3):
				if board[b][a] ==  piece and board[b+1][a] == piece and board[b+2][a] == piece and board[b+3][a] == piece:
					return True

		for e in range(len(board)-3):
			for f in range(len(board[a])-3):
				if board[b][a] ==  piece and board[b+1][a+1] == piece and board[b+2][a+2] == piece and board[b+3][a+3] == piece:
					return True

		for g in range(len(board)-3):
			for h in range(3, len(board[g])):
				if board[b][a] ==  piece and board[b-1][a+1] == piece and board[b-2][a+2] == piece and board[b-3][a+3] == piece:
					return True

	for i in range(len(board[col][row])-3):
		for j in range(len(board[col][row][i])):
			print("wewee")
	return False
	
board = create_board()
print_board(board)

