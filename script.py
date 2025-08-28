# NUMBER GUESSING GAME
import random

def number_guessing_game():
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


# PAPER, ROCK, SCISSORS
import random


def rockpaperscissors():
    print("<-------ROCK------PAPER------SCISSORS------GAME------>")
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
        ans


# After coming out of the while loop, print thanks for playing
    print()
    print("(<== Thanks for playing ==>)")
    print("See you Again!")
    print("<------------THE END-------------->")



# TIC-TAC-TOE
    
# Function to print the board



# Function to check the winner



# Function to run fo the actual tic-tac-toe game where your other functions will be used
def tic_tac_toe():
    print("CURRENTLY UNDER DEVELOPMENT...")
   

# MENU SYSTEM
def main_menu():
    try:
        # MAIN LOOP
        global user_exit
        user_exit = False
        while not user_exit:
            user_input = input("\n...:::| WELCOME TO THE ARCADE MINI GAME COLLECTION! |:::...\n\nWhich game do you want to play? \n1. Number Guessing \n2. Rock,Paper,Scissors \n3. Tic-Tac-Toe \n4. EXIT\n \nEnter your number: ")
            if user_input.isdigit():
                print("")
                print("")
                    #print("Input is digit")
                if int(user_input) in range(1, 5):
                    #print("Input in range")
                    if user_input == "1":
                        print("...:::| NUMBER GUESSING GAME |:::...\n")
                        number_guessing_game() # Play Number Guessing 
                    if user_input == "2":
                        print("...:::| ROCK, PAPER, SCISSORS |:::...\n")
                        rockpaperscissors() # Play Rock, Paper, Scissors 
                    if user_input == "3":
                        print("...:::| TIC-TAC-TOE |:::...\n")
                        tic_tac_toe()# Play Tic-Tac-Toe (UNDER DEVELOPMENT)
                    if user_input == "4":
                        exit() # Exit
                else:
                    print("Only numbers between 1-4 allowed!")
            else:
                print("Only numbers allowed!")
    except KeyboardInterrupt:
        ...

def exit():
    while True:
        exit_input = input("\nAre you sure, you want to exit? [Y]ES/[N]O: ").strip().lower()
        if exit_input in ["n", "no"]:
            return
        if exit_input in ["y", "yes"]:
            print("\n...:::| THANKS FOR PLAYING, GOODBYE! |:::...\n")
            global user_exit
            user_exit = True
            return
        else:
            print("Incorrect input. Please answer with '[Y]ES' or '[N]O'.")

# RUN THE MENU
main_menu()    
