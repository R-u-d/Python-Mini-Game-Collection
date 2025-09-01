# Work off the platform in groups using the following code as a base

import random

# NUMBER GUESSING GAME




# PAPER, ROCK, SCISSORS
import random

def rockpaperscissors():    
    print("...:::| ROCK, PAPER, SCISSORS |:::...\n")        
    print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")
    
    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

        # Take the input from user
        choice = int(input("Enter your choice Number: "))

        #Looping until user enter valid input
        while choice > 3 or choice < 1:
            choice = int(input('Enter a valid Number please: '))
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                print('Invalid Number, please try again!')

        #Initialize value of choice_name   
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'

        #Print user choice
        print('Your choice is:', choice_name)
        print()
        print("Now it´s Computer´s Turn... ")

        #Computer choose randomly any Number
        comp_choice = random.randint(1, 3)

        #Initialize value of comp_choice_name
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'

        print("Computer choice is: ", comp_choice_name)
        print()
        print(choice_name, "vs", comp_choice_name)

        #Determine the winner
        if (choice == 1 and comp_choice == 1) or (choice == 2 and comp_choice == 2) or (choice == 3 and comp_choice == 3):
            result = "DRAW"
        elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
            result = "Paper"
        elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
            result = "Rock"
        elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
            result = "Scissors"

        #Print the result
        if result == "DRAW":
            print("<== It´s a tie! ==>")
        elif result == choice_name:
            print("<== You won! ==>")
        else:
            print("<== You lose! ==>")

        #Ask if the user wants to play again
        print(" ")
        print("Are you ready to play again...! (Y/N)")
        ans = input().lower()
        if ans == "y":
            continue
        if ans == "n":
            break
        
        while ans != "y" and ans != "n":
            print("Invalid input! Please enter Y or N")
            ans = input().lower()
            if ans == "y":
                continue
            elif ans == "n":
                break
        if ans == "n":
            break

# After coming out of the while loop, print thanks for playing
    print()
    print("(<== Thanks for playing ==>)")
    print("See you Again!")
    print("<------------THE END-------------->")
rockpaperscissors()

# TIC-TAC-TOE
# Function to print the board



# Function to check the winner



# Function to run fo the actual tic-tac-toe game where your other functions will be used
def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertikale Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'
    turns = 0

    print(" Welcome to Tic Tac Toe Game!")
    
    while True:
        print_board(board)
        
        # Player Input
        try:
            move = int(input(f"Player '{current_player}', choose a position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if board[move] != ' ':
                print("Position already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # execute a move
        board[move] = current_player
        turns += 1
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
   

# MENU SYSTEM

    

    
# RUN THE MENU
