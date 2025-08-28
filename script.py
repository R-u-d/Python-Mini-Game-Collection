# NUMBER GUESSING GAME




# PAPER, ROCK, SCISSORS



# After coming out of the while loop, print thanks for playing




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
