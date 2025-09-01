# NUMBER GUESSING GAME

def number_guessing_game():
    #print,input = my_print, my_input
    random_number = random.randint(1, 100)
    attempts = 0 
    guessed_correctly = False
    while not guessed_correctly:
        guess = input("Guess the number: ")
        if guess.isdigit():
            guess = int(guess)
            attempts += 1
            if guess < random_number:
                print("Unlucky! Try again with a higher number.")       
            elif guess > random_number:            
                print("Unlucky! Try again with a lower number.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.") 
                guessed_correctly = True 
            while True:
                print('Do you want to play again? (y/n)')
                try_again = input().lower()
                if try_again == "y":
                    number_guessing_game()
                    return
                elif try_again == "n":
                    print('Thanks for playing, good luck next time!')
                    return
                else:
                    print('Incorrect input, please input y/n')
        else:
            print('Not a number, please input a number')
    #print,input = original_print,original_input


# PAPER, ROCK, SCISSORS

import random
def rock_paper_scissors():
    #print, input = my_print, my_input
    print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
        + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissors -> Rock wins \n"
        + "Paper vs Scissors -> Scissors wins \n")
    
    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

        # Take the input from user
        choice = input("Enter your choice Number: ") #<--------------------- simply collect the input first and work with it after
        if choice.isdigit(): #<--------------------------------------------- check if input is digit before you cast to int()
            choice = int(choice) #<----------------------------------------- it is now safe to cast int() cus we checked .isdigit()
        #choice = int(input("Enter your choice Number: ")) # <-------------- corrected this to 3 lines above
            
            if choice > 3 or  choice < 1:
                print('Invalid Number, Enter a number between 1-3!')
                continue #<------------------------------------------------- this is enough to not continue the logic below and just ask again above 

            #Looping until user enter valid input
            """ <----------------------------------------------------------- no need, the above if combined with continue is enough
            while choice > 3 or choice < 1:
                choice = int(input('Enter a valid Number please: ')) 
                if int(choice) == 1 or int(choice) == 2 or int(choice) == 3:
                    break
                else:
                    print('Invalid Number, please try again!')
            """

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
            print("Now it's Computer's Turn... ")

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
            result = "" #<-------------------------------- Safer to set result to "", there is a risk your if conditions below never set result to anything
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
        else:
            print("Input incorrect. Not a number!") #<------- this is if your .isdigit() check at the top fails
            continue #<-------------------------------------- so you dont ask the player to play again if the input was not a number. Just ask again
            
        #Ask if the user wants to play again
        while True: #<------------------------------------------------- you keep asking until the user responds with y or n
            print(" ")
            print("Are you ready to play again...! (Y/N)")
            ans = input().lower()
            if ans == "y":
                break #<------------------------------ break out of asking the player if they wanna play again, the logic will continue in the main while loop
            elif ans == "n": #<----------------------- print the exit message explicitly when the user choses to exit
                print()
                print("(<== Thanks for playing ==>)")
                print("See you Again!")
                print("<------------THE END-------------->")
                
                return
            else:
                print("Invalid Input: enter y or n")
    """ <------------------------------------------------------------ the old way of asking allowed any key to play again not just y
            #Ask if the user wants to play again
            print(" ")
            print("Are you ready to play again...! (Y/N)")
            ans = input().lower()
            if ans == "y":
                continue
            if ans == "n":
                break

        # After coming out of the while loop, print thanks for playing
            print()
            print("(<== Thanks for playing ==>)")
            print("See you Again!")
            print("<------------THE END-------------->")
    """
    #print,input = original_print, original_input



# TIC-TAC-TOE
    
# Function to print the board

def print_board(v = (' ',)*9):

    ttt = f"""
         |     |     
      {v[0]}  |  {v[1]}  |  {v[2]}     
    _____|_____|_____
         |     |     
      {v[3]}  |  {v[4]}  |  {v[5]}     
    _____|_____|_____
         |     |     
      {v[6]}  |  {v[7]}  |  {v[8]}     
         |     |     

    """
    print(ttt)

print_board()


# Function to check the winner
   
def check_win(board, player):
    """Checks if the current player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


# Function to run fo the actual tic-tac-toe game where your other functions will be used
    
def get_player_move(board, player):
    """Gets valid player input and returns the position."""
    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): "))
            if 1 <= move <= 9:
                if board[move - 1] == " ":
                    return move - 1
                else:
                    print("Position already taken. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def play_game():
    """Main function to run the Tic-Tac-Toe game."""
    board = [" "] * 9  # Represents the 9 positions on the board
    current_player = "X"
    game_over = False
    moves_count = 0
    
    while not game_over:
        print_board(board)
        position = get_player_move(board, current_player)
        board[position] = current_player
        moves_count += 1
        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            game_over = True
        elif moves_count == 9:
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"
    # Ask if the user wants to play again
    print(" ")
    while True:
        print("Are you ready to play again...! (Y/N)")
        ans = input().lower()
        if ans == "y":
            play_game()
            break
        elif ans == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input! Please enter Y or N")
play_game()


    
# MENU SYSTEM




# RUN THE MENU

