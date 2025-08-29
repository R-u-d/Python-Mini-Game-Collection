# NUMBER GUESSING GAME




# PAPER, ROCK, SCISSORS



# After coming out of the while loop, print thanks for playing




# TIC-TAC-TOE
    
# Function to print the board



# Function to check the winner



# Function to run fo the actual tic-tac-toe game where your other functions will be used


# MENU SYSTEM
import subprocess as sp

scores = {
    "\n\n< < < [ Number Guessing Game ] > > >\n": {
        "Player 1": [1337,22],
        "Player 2": [999,3333]
    },
    "\n< < < [ Rock,Paper,Scissors ] > > >\n": {
        "Player 1": [4321,44],
        "Player 2": [541,55]
    },
    "\n< < < [ Tic-Tac-Toe ] > > >\n": {
        "Player 1": [543,66],
        "Player 2": [541,77]
    }
}

def high_scores():
    for k,v in scores.items():
        c(255, 100, 100)
        print(k)
        cr()
        for k2,v2 in v.items():
            print(f"{'':<9}{k2:<{len(k2)+2}}  {max(v2)}")
            

    input ("\nPress any key to continue...")

def c(R,G,B):
    print(f"\x1b[38;2;{R};{G};{B}m", end="")

def cr():
    print("\x1b[0m", end="")



def main_menu():
    try:
        # MAIN LOOP
        global user_exit
        user_exit = False
        while not user_exit:
            menu_options = """
...:::| WELCOME TO THE ARCADE MINI GAME COLLECTION! |:::...

Which game do you want to play?
1. Number Guessing
2. Rock,Paper,Scissors
3. Tic-Tac-Toe 
4. High Scores
5. EXIT
"""     
            print(menu_options)
            user_input = input("Please enter your number: ")
            if user_input.isdigit():
                print("\n")
                    #print("Input is digit")
                if int(user_input) in range(1, 6):
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
                        print("...:::| H I G H  S C O R E S |:::...\n")
                        high_scores()
                    if user_input == "5":
                        
                        exit() # Exit
                else:
                    print("Only numbers between 1-4 allowed!")
            else:
                print("Only numbers allowed!")
    except KeyboardInterrupt:
        ...


def exit():
    while True:
        exit_input = input("Are you sure, you want to exit? [Y]ES/[N]O: \n").strip().lower()
        if exit_input in ["n", "no"]:
            return
        if exit_input in ["y", "yes"]:
            sp.run(['cowsay', 'THANKS FOR PLAYING, GOODBYE!'])
            global user_exit
            user_exit = True
            return
        else:
            print("Incorrect input. Please answer with '[Y]ES' or '[N]O'.")

# RUN THE MENU
main_menu()    

