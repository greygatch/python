"""

Simple Battleship game via Codecademy

"""
from random import randint

board = []

# create 5 rows of 5 O's
for i in range(5):
    board.append(["O"] * 5)

# print board without brackets
def print_board(board):
    for each in board:
        print " ".join(each)
    print "\n"

# create random x and y value
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board) - 1)

# assign ship position to random values    
ship_row = random_row(board)
ship_col = random_row(board)

# begin game
print "Let's play Battleship!\n"
print_board(board)
print "\n"

# four turns
for turn in range(4):
    
    print "Turn: ", turn + 1
    
    # get values from user
    guess_row = int(raw_input("Guess the row: "))
    guess_col = int(raw_input("Guess the column: "))
    
    # ftw
    if guess_row == ship_row and guess_col == ship_col:
        print "Direct hit! Battleship sunk!\n"
        board[guess_row][guess_col] = "!"
        print_board(board)
        break
        
    # determine how user missed
    else:
        if guess_row not in range(5) and guess_col not in range(5):
            print "Not even close!\n"
        elif board[guess_row][guess_col] == "X":
            print "You've fired at this area before.\n"
        else:
            print "Miss!\n"
            board[guess_row][guess_col] = "X"
        print_board(board)
        
    # if out of turns, reveal location of ship
    if turn == 3:
        print "Game over!\n"
        print "The ship was at location", ship_row, ",", ship_col
        board[ship_row][ship_col] = "#"
        print_board(board)
        break
