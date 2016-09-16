board = []
for i in range(0,10):
    board.append(["O"] * 10)
"""
wL can also be used
while len(board) < 10:
    board.append(["0"] * 10)
"""
#this function print the list without "" and []
def print_board(board):
    for row in board:
        print " ".join(row)
print_board(board)

#this functions generate random row and column number
from random import randint

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board) - 1)

#this stores ship coordinates in the variables
ship_row = random_row(board) + 1
ship_col = random_col(board) + 1
board_len = len(board) + 1

#fucntion is defined that let's user guess and make sure that he enteres a number
guess_row = 0
guess_col = 0
def guess():
    global guess_row
    global guess_col
    try:
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
    except SyntaxError:
        print "You didn't enter anything!"
        guess()
    except NameError:
        print "Please enter a number!"
        guess()

#fL is created to let the user guess multiple times
for turn in range(100):
    print "Turn", turn + 1
    #this let's user guess
    guess()
    #this code block checks if the user guessed rigth or wrong and reacts to it
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        break
    else:
        if guess_row not in range(board_len) or guess_col not in range(board_len):
            print "Oops, that's not even in the ocean!"
        elif board[guess_row - 1][guess_col - 1] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row - 1][guess_col - 1] = "X"
            print_board(board)
            if guess_row == ship_row:
                print "Close! You guessed the row but not the column."
                print "Try again!"
            elif guess_col == ship_col:
                print "Close! You guessed the column but not the row."
                print "Try again!"
            else:
                pass
        if turn == 9 :
            print "Game Over!"
            print "My ship coordinates was: "
            print "Row -", ship_row
            print "Column -", ship_col
            break
