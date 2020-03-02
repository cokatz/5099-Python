
"""
Created on Thu Feb 27 16:17:48 2020

@author: bshaw
"""


"""
Tic-tac-toe game skeleton using NumPy
"""


import numpy as np
import random



def print_header():
    print("-------------------------------")
    print("         TIC TAC TOE")
    print("-------------------------------\n")


def create_board():
    # 2.	Set up or initialize the board
    return 


def place(board, player, position):
    # is move available 
    available = possibilities(board)
    # make move
    return board
    


def possibilities(board):
    # what spaces are available
    return 


def random_place(board, player):
    empty = possibilities(board)
    return place(board, player, random.choice(empty))


def row_win(board, player):
    # determine if there is a row win
    return 


def col_win(board, player):
    #determine if there is a column win
    return 


def diag_win(board, player):
    #determine if there is a diag win
    return 


def evaluate(board, players):
    winner = 0
    for player in players:
        if row_win(board, player):
            winner = player
        elif col_win(board, player):
            winner = player
        elif diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def game_loop():

   #code for 1.	Ready to play? … Play Again?
    play_game()
            


def play_game():
    """
    Game proper.
    """
    board = create_board()
    print("Here is the board.")
    print(board)
    print()
   # print instructions
   
   # determine play order who is X and O

   # get moves by human or computer
   #set up to evaluate winner
      # if human get input("what position do you want to move?")
           #Place move 
           place(board, player, position) 
           print(board)
       
        # else computer move  get random available move
            #Place move 
            random_place(board, player) # smart move block or win
            print(board)
            
        winner = evaluate(board, players)
    
        #    if winner print who won and return winner 
        #   so that the game loop can ask to play again
                
    return winner

def main():
    """
    Main program for playing tictactoe.
    """
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
    