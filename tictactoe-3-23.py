
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

    start = input("Do you want to play a game? (y/n) ")
    print(start)
    if start.lower() in ["y", "yes"]:
        repeat = True
        while repeat == True:
            play_game()
            loop = input("Do you want to play again? (y/n) ")
            if loop.lower() in ["y", "yes"]:
                repeat = True
            else:
                repeat = False
                print("Goodbye!")
    else:
        print("I'm sorry, I didn't understand.")
        game_loop()


def play_game():
    """
    Game proper.
    """
    board = create_board()
    print("Here is the board.")
    print(board)
    print()
    print("To place your position, indicate the row number and the column number.")
    print("For example, to place your position in the middle, type in 2,2 (without spaces).")
    print("If you want to place in the top left corner, type in 1,1 (without spaces")
    order = int(input("Do you want to go first or second? (1/2) "))

    if order == 1:
        human = 1
        computer = 2
        players = [human, computer]
    else:
        human = 2
        computer = 1
        players = [computer, human]
    print("You are player {}:".format(order))
    winner = 0
    while winner == 0:
        for player in players:
            if player == order:
                moved = 0
                while (moved ==0):
                    position = input("What position do you want to place? ")
                    print("You want to place at {} position.".format(position))
                    position = int(position[0])-1, int(position[2])-1
                    if position in possibilities(board):
                        place(board, player, position)
                        moved = 1
                    else:
                         print("Cannot place in that position.")
                print(board)
            else:
                print("My move:")
                random_place(board, player) # smart move block or win
                print(board)
            winner = evaluate(board, players)
            if winner > 0:
                if winner == order:
                    print("You win!!!")
                else:
                    print("I win!!!")
                break
            elif winner == -1:
                print("It's a draw!")
                break
            print()
    return winner

def main():
    """
    Main program for playing tictactoe.
    """
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
    