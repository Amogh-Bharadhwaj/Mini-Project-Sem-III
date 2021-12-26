'''TIC TAC TOE'''

import numpy as np
  
def create_tic_tac_toe(): #Creates the board
    return(np.array([['_', '_', '_'],
                     ['_', '_', '_'],
                     ['_', '_', '_']]))
  
def player_choice(board, player): #We allow the player to choose his/her position
    select = tuple(map(int,input("Enter a position: ").split())) #(0,0) 
    flag = 2
    while flag == 2:
    	for i in select:
    		if i > 2 or board[select[0]][select[1]] in ['X','O']:
    			break
    		else:
    			flag -= 1
    	if flag == 0:
    		break
    	select = tuple(map(int,input("Enter a valid position: ").split()))
    board[select[0]][select[1]] = player
    return(board)

def winner_in_row(board, player): #Checking row-wise for winner
    for x in board:
        win = True  
        for y in x:
            if y != player:
                win = False
                continue
                  
        if win == True:
            return(win)
    return(win)
  
def winner_in_col(board, player): #Checking column-wise for winner
    for x in range(len(board)):
        win = True
          
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
                  
        if win == True:
            return(win)
    return(win)


def winner_in_diagonal(board, player): #Checking diagonals for winner
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win
  
def evaluate(board): #Checking all win conditions
    winner = 0
      
    for player in ['X', 'O']:
        if (winner_in_row(board, player) or winner_in_col(board,player) or winner_in_diagonal(board,player)):
        	winner = player
        if np.all(board != '_') and winner == 0: #Here, we check if all the spaces on the board are filled and if we already have a winner
        	winner = 'noone. The match is a Draw'
    return winner
  
def play_tic_tac_toe(): #This is game
    board, winner = create_tic_tac_toe(), 0
    print(board)
      
    while winner == 0:
        for player in ['X', 'O']:
            board = player_choice(board, player)
            print(board)
            winner = evaluate(board)
            if winner != 0:
                break
    return(winner)
def ticcer():
    print("The winner is " + play_tic_tac_toe())