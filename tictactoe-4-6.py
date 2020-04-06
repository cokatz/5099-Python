
"""
Created on Thu Feb 27 16:17:48 2020

@author: bshaw
"""


"""
Tic-tac-toe game using NumPy
"""


import numpy as np
import random


def print_header():
    print("-------------------------------")
    print("         TIC TAC TOE")
    print("-------------------------------\n")


def create_board():
    return np.zeros((3,3), dtype=np.int32)


def place(board, player, position):
    if board[position[0], position[1]] == 0:
        board[position[0], position[1]] = player
    else:
        print("Cannot place in that position.")
    return board


def possibilities(board):
    empty = np.where(board == 0)
    first = empty[0].tolist()
    second = empty[1].tolist()
    return [x for x in zip(first, second)]


def random_place(board, player):
    empty = possibilities(board)
    return place(board, player, random.choice(empty))


def row_win(board, player):
    return np.any((np.all(board == player, axis=1)))


def col_win(board, player):
    return np.any((np.all(board==player, axis=0)))


def diag_win(board, player):
    diag1 = np.diag(board)
    diag2 = np.diag(np.fliplr(board))
    return np.all(diag1 == player) or np.all(diag2 == player)

def find_winner(board, player, players):
    no_move =[-1,-1]
    moves = possibilities(board)
    for move in moves:
        test_board=board.copy()
        test_board[move[0],move[1]] = player
        # now set winning_move to evaluate(test_board,players)
        winning_move = evaluate(test_board,players)
        # if winner return move
        if winning_move > 0:
            return move
    return no_move

def find_block(board, player, players):
    if player == 1:
        player = 2
    else:
        player = 1
    return find_winner(board, player,players)

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


def game_loop(index,arr):

#    start = input("Do you want to play a game? (y/n) ")
#    print(start)
#    if start.lower() in ["y", "yes"]:
#        repeat = True
#        while repeat == True:
#            play_game()
#            loop = input("Do you want to play again? (y/n) ")
#            if loop.lower() in ["y", "yes"]:
#                repeat = True
#            else:
#                repeat = False
#                print("Goodbye!")
#    else:
#        print("I'm sorry, I didn't understand.")
#        game_loop()
    if index ==1:
        repeat = 1
        while repeat < 5: # need to change to 101
            play_game(index,arr)
            repeat += 1
    elif index == 2:
        repeat = 1
        while repeat < 5: # need to change to 101
            play_game(index,arr)
            repeat += 1
    else:
        repeat = 1
        while repeat < 5: # need to change to 101
            play_game(index,arr)
            repeat += 1

def play_game(group,arr):
    """
    Game proper.
    """
    board = create_board()
#    print("Here is the board.")
#   print(board)
#    print()
#    print("To place your position, indicate the row number and the column number.")
#    print("For example, to place your position in the middle, type in 2,2 (without spaces).")
#    print("If you want to place in the top left corner, type in 1,1 (without spaces")
#    order = int(input("Do you want to go first or second? (1/2) "))

#    if order == 1:
#        human = 1
#        computer = 2
#        players = [human, computer]
#    else:
#        human = 2
#        computer = 1
#        players = [computer, human]  
    
#    print("You are player {}:".format(order))
    
    
    players = [1,2]
    winner = 0
    while winner == 0:
        for player in players:
            if group == 1:
                random_place(board, player)
            elif group == 2:   # had if group == 2:
                if player == 1:
                    random_place(board, player)
                else:
                    move = find_winner(board, player, players)
                    if move ==[-1,-1]:
                        block = find_block(board, player, players)
                        if block ==[-1,-1]:
                            random_place(board, player)
                        else:
                            place(board, player, block)
                    else:
                        place(board, player, move)
            else:
                move = find_winner(board, player, players)
                if move ==[-1,-1]:
                    block = find_block(board, player, players)
                    if block ==[-1,-1]:
                        random_place(board, player)
                    else:
                        place(board, player, block)
                else:
                    place(board, player, move) 
           
            winner = evaluate(board, players)
            if winner > 0:
                if player == 1:
                    arr[0] += 1
#                    print("You win!!!")
                else:
                    arr[1] += 1
#                    print("I win!!!")
                break
            elif winner == -1:
                arr[2] += 1
#                print("It's a draw!")
                break
            
    return winner

def main():
    """
    Main program for playing tictactoe.
    """
    print_header()
    both_rand=[0,0,0]
    one_rand = [0,0,0]
    both_smart=[0,0,0]
    game_loop(1,both_rand)
    game_loop(2,one_rand)
    game_loop(3,both_smart)
    print("Both Random", both_rand)
    print("One Random", one_rand)
    print("Both Smart", both_smart)


if __name__ == '__main__':
    main()
    