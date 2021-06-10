import random as rn
# ----- Global Variables ----- 

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Who turn is it?
current = ["X", "O"]
current_player = rn.choice(current)

# Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print(board[6] + " | " + board[7] + " | " + board[8])  

# Play game Tic Tac Toe
def play_game():

    # Display initial board
    display_board()
    
    # While game is still in progress
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        # Check if the game has ended
        check_if_game_over()
        # Flip to the other player
        flip_player()
    
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# Handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1 - 9: ")
    Valid = False
    while not Valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1 - 9: ")
        position = int(position) - 1
        if board[position] == "-":
                Valid = True
        else:
            print("You can't go there. Go again.")
    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    # Set up global variables
    global winner 
    # check rows
    row_winner  = check_rows()
    # check columns 
    colum_winner = check_columns()
    # check diagonals
    diagonals_winner = check_diagonals()
    if row_winner:
        #there was a winner
        winner = row_winner
    elif colum_winner:
        #there was a winner
        winner - colum_winner
    elif diagonals_winner:
        #there was a winner
        winner = diagonals_winner
    else:
        #there was no winner
        winner = None
    return 

def check_rows():
    # Set up global variables
    global game_still_going
    # Check if any of the rows have all the same values ( and it is not empty )
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner *(X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return 


def check_columns():
    # Set up global variables
    global game_still_going
    # Check if any of the colum have all the same values ( and it is not empty )
    colum_1 = board[0] == board[3] == board[6] != "-"
    colum_2 = board[1] == board[4] == board[7] != "-"
    colum_3 = board[2] == board[5] == board[8] != "-"
    # If any colum does have a match, flag that there is a win
    if colum_1 or colum_2 or colum_3:
        game_still_going = False
    # Return the winner *(X or O)
    if colum_1:
        return board[0]
    elif colum_2:
        return board[1]
    elif colum_3:
        return board[2]
    return 


def check_diagonals():
    # Set up global variables
    global game_still_going
    # Check if any of the diagonals have all the same values ( and it is not empty )
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    # If any diagonals does have a match, flag that there is a win
    if diagonals_1 or diagonals_2 :
        game_still_going = False
    # Return the winner *(X or O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


def check_if_tie():
    # Set up global variables
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return 


def flip_player():
    # Global variables we need 
    global current_player
    # if the current player was "X", then change it to "O"
    if current_player == "X":
        current_player = "O"
    # if the current player was "O", then change it to "X"
    elif current_player == "O":
        current_player = "X"
    return 

play_game()


# board 
# display board information
# play game 
# handle turn
# check win condition
  # check rows 
  # # check columns
  # check diagonals
# check tie condition
# flip player