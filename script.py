# Work off the platform in groups using the following code as a base

import random

# NUMBER GUESSING GAME




# PAPER, ROCK, SCISSORS
import random
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
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = "Paper"
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = "Rock"
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = "Scissors"

    #Print the result
    if result == "Draw":
        print("<== It´s a tie! ==>")
    elif result == choice_name:
        print("<== Congratulation ==>")
    else:
        print("<== Computer wins! ==>")

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

   

# MENU SYSTEM

    

    
# RUN THE MENU
