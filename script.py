from blessed import Terminal
import time
from subprocess import run
#==================================================================================
############################   CONTEXT MANAGER   ##################################
#==================================================================================
from contextlib import contextmanager
import builtins


@contextmanager
def sub_screen_io(custom_print,custom_input):
    org_print = builtins.__dict__['print']
    org_input = builtins.__dict__['input']
    builtins.print = custom_print
    builtins.input = custom_input
    try: yield
    finally:
        builtins.print = org_print
        builtins.input = org_input

#==================================================================================
###############################   CUSTOM I/O   ####################################
#==================================================================================
def clear_screen(end=''):
    original_print(term.home+term.clear,end=end)

import random


sf_buffer = []
pos = {
    'buffer':{'x':40,'y':11,'limit':16},
    'input':{'x':35,'y':28},
}

actual_color = "\x1b[31m"
history_color = "\x1b[31m"
reset_color = "\x1b[0m"

def slice_limit(b:list,limit=0):
    return max(0,len(b)-limit)

def region(buffer):
    start = slice_limit(buffer,limit=pos["buffer"]['limit'])
    return sf_buffer[start:]

def sf_print_buffer(x,y):
    sliced_region = region(sf_buffer)
    for i,line in enumerate(sliced_region):
        final_line = term.move_xy(x,y + i)
        if i == len(sliced_region)-1:
            final_line += actual_color
        final_line += line + reset_color
        original_print(final_line)

def refresh_subframe():
    clear_screen()
    original_print(get_subframe_CLR())
    original_print(term.move_xy(45,4) + get_subframe_title(arcade_menu))

#======================================================================== SF PRINT
def subframe_print(*values, sep=' ', end="\n"):
    refresh_subframe()
    #-------------------------------------------------------- fill buffer
    single_string = sep.join(map(str,values)) + end
    for line in single_string.splitlines():
        sf_buffer.append(line)
    #-------------------------------------------------------- print buffer
    sf_print_buffer(pos["buffer"]['x'],pos["buffer"]['y'])
#======================================================================== SF INPUT
def subframe_input(prompt=None):
    refresh_subframe()
    #-------------------------------------------
    #last_i = 0
    last_i = len(sf_buffer) - slice_limit(sf_buffer,limit=pos["buffer"]["limit"]) - 1
    for i,line in enumerate(sf_buffer[slice_limit(sf_buffer,limit=pos["buffer"]["limit"]):]):
        #last_i = i
        sf_print_buffer(pos["buffer"]['x'],pos["buffer"]['y'])
        #original_print(term.move_xy(pos["buffer"]['x'], 
        #                            pos["buffer"]['y'] + i) + line)
    if prompt == None: #________________________________________/|| HANDLE USER INPUT (NO PROMPT)
        original_print(term.move_xy(pos["input"]['x'], #----------/ move to 
                                    pos["input"]['y']), end="")#--\ input pos
        user_input = original_input() # -------------| catch it
        sf_buffer.append(user_input)  # -------------| store in buffer
        return user_input #--------------------------| return it
    else:#__________________________________________________________/|| HANDLE USER INPUT (PROMPT)
        original_print(term.move_xy(pos["buffer"]['x'], #------------| prompt in buffer
                                    pos["buffer"]['y'] + last_i + 1) + actual_color + prompt + reset_color)
        #---------------------------------------------------------------/ catch user input
        user_input = original_input(term.move_xy(pos["input"]['x'],  #- | and move to
                                                 pos["input"]['y'])) #--\ input pos
        sf_buffer.append(prompt + user_input) #--------------------| store in buffer
        return user_input #----------------------------------------| return it

#==================================================================================
###############################   GAMES  ##########################################
#==================================================================================

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
def print_board(v = (' ',)*9):
    print_board_block(v)

"""
  Ѻ ┃ χ ┃ Ѻ 
━━━━╋━━━╋━━━
  χ ┃ χ ┃ χ
━━━━╋━━━╋━━━
  Ѻ ┃ Ѻ ┃ Ѻ     
"""
def print_board_compact(v = (' ',)*9):
    cX,cO,cr = '\x1b[31m','\x1b[36m','\x1b[0m'
    for i in range(len(v)):
        if v[i].lower() == "x":
            v[i] = cX + "χ" + cr
        if v[i].lower() == "o":
            v[i] = cO + "Ѻ" + cr
    ttt = f"""
              {v[0]} ┃ {v[1]} ┃ {v[2]} 
            ━━━━╋━━━╋━━━
              {v[3]} ┃ {v[4]} ┃ {v[5]}
            ━━━━╋━━━╋━━━
              {v[6]} ┃ {v[7]} ┃ {v[8]}       
    """
    print(ttt)

def print_board_block(v = (' ',)*9):
    for i in range(len(v)):
        if v[i].lower() == "x":
            v[i] = "χ"
        if v[i].lower() == "o":
            v[i] = "Ѻ"
    cX,cO,cr = '\x1b[31m','\x1b[36m','\x1b[0m'
    vc = [cr]*9
    for i in range(len(v)):
        if v[i] == 'χ':
            vc[i] = cX
        if v[i] == 'Ѻ':
            vc[i] = cO
    ttt = f"""

                 ┃     ┃     
              {vc[0]}{v[0]}{cr}  ┃  {vc[1]}{v[1]}{cr}  ┃  {vc[2]}{v[2]}{cr}     
            _____┃_____┃_____
                 ┃     ┃     
              {vc[3]}{v[3]}{cr}  ┃  {vc[4]}{v[4]}{cr}  ┃  {vc[5]}{v[5]}{cr}
            _____┃_____┃_____
                 ┃     ┃     
              {vc[6]}{v[6]}{cr}  ┃  {vc[7]}{v[7]}{cr}  ┃  {vc[8]}{v[8]}{cr} 
                 ┃     ┃     
    
    
    """
    print(ttt)
    for i in range(len(v)):
        if v[i] == 'χ':
            v[i] = "X"
        if v[i] == 'Ѻ':
            v[i] = "O"

"⬜️ 🟥 🟧 🟨 🟩 🟦 🟪 🟫"
def print_board_emoji(v = (' ',)*9):
    for i in range(len(v)):
        if v[i] == " ":
            v[i] = "🟨"
        if v[i].lower() == "x":
            v[i] = "❌"
        if v[i].lower() == "o":
            v[i] = "⭕"
        
    ttt = f"""
            ⬜️⬜️⬜️🟦⬜️⬜️⬜️🟦⬜️⬜️⬜️
            ⬜️{v[0]}⬜️🟦⬜️{v[1]}⬜️🟦⬜️{v[2]}⬜️
            ⬜️⬜️⬜️🟦⬜️⬜️⬜️🟦⬜️⬜️⬜️
            🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
            ⬜️⬜️⬜️🟦⬜️⬜️⬜️🟦⬜️⬜️⬜️
            ⬜️{v[3]}⬜️🟦⬜️{v[4]}⬜️🟦⬜️{v[5]}⬜️
            ⬜️⬜️⬜️🟦⬜️⬜️⬜️🟦⬜️⬜️⬜️
            🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
            ⬜️⬜️⬜️🟦⬜️⬜️⬜️🟦⬜️⬜️⬜️
            ⬜️{v[6]}⬜️🟦⬜️{v[7]}⬜️🟦⬜️{v[8]}⬜️
            ⬜️⬜️⬜️🟦⬜️⬜️⬜️🟦⬜️⬜️⬜️
    """
    print(ttt)

def print_board_plain(v = (' ',)*9):
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
            print_board(board)
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

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [" "] * 9  # Represents the 9 positions on the board
    current_player = "X"
    game_over = False
    moves_count = 0
    
    while not game_over:
        #print_board(board)
        
        position = get_player_move(board, current_player)
        board[position] = current_player
        moves_count += 1
        if check_win(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            print_board(board)
            game_over = True
        elif moves_count == 9:
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"
    # Ask if the user wants to play again
    
    while True:
        print("Are you ready to play again...! (Y/N)")
        ans = input().lower()
        if ans == "y":
            tic_tac_toe()
            break
        elif ans == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input! Please enter Y or N")

# HIGH SCORES

scores = {
    "Number Guessing Game": {
        "Player 1": [1337,22],
        "Player 2": [999,3333]
    },
    "Rock,Paper,Scissors": {
        "Player 1": [4321,44],
        "Player 2": [541,55]
    },
    "Tic-Tac-Toe": {
        "Player 1": [543,66],
        "Player 2": [541,77]
    }
}

def high_scores():
    bl,br = "< < < [ "," ] > > >"
    print()# new line
    for k,v in scores.items():
        print('\n'+bl+k+br+'\n')
        for k2,v2 in sorted(v.items(), key=lambda i:max(i[1]), reverse=True):
            print(f"{'':<9}{k2:<{len(k2)+2}}  {max(v2)}")

    print("\nPress any key to continue...")
    with term.cbreak():
        while True:
            if term.inkey() or term.kbhit():
                original_print(" ")
                return



def exit():
    while True:
        exit_input = input("Are you sure, you want to exit? [Y]ES/[N]O: \n").strip().lower()
        if exit_input in ["n", "no"]:
            return
        if exit_input in ["y", "yes"]:
            #run(['cowsay', 'THANKS FOR PLAYING, GOODBYE!'])
            for i in range(50):
                sf_buffer.clear()
                print(get_cowsay(i%2))
                time.sleep(1/2)
            global user_exit
            user_exit = True
            return
        else:
            print("Incorrect input. Please answer with '[Y]ES' or '[N]O'.")


key_title = "Menu Title"
key_opts = "Menu Options"
key_opt1 = "Number Guessing Game"
key_opt2 = "Rock, Paper, Scissors"
key_opt3 = "Tic-Tac-Toe"
key_opt4 = "High Scores"
key_opt5 = "EXIT"
key_active = "Active Option key"
key_name = "Option Name"
key_func = "Option Function"
key_clr = "Default Color"
key_clr_reset = "Reset Color"
key_clr_inv = "Invert Color"
key_select = "Option Selection"
key_input = "Option Input"

   


arcade_menu = {
    key_title: "MINI GAME COLLECTION",
    key_clr_reset: "\x1b[0m",
    key_clr_inv: "\x1b[7m",
    key_select: 0,
    key_active: "",
    key_opts: {
        key_opt1: {
            key_name: "1. Number Guessing Game",
            key_func: number_guessing_game,
            key_clr: "\x1b[34m",
            key_input: ["1"]
        },
        key_opt2: {
            key_name: "2. Rock, Paper, Scissors",
            key_func: rock_paper_scissors,
            key_clr: "\x1b[36m",
            key_input: ["2"]
        },
        key_opt3: {
            key_name: "3. Tic-Tac-Toe",
            key_func: tic_tac_toe,
            key_clr: "\x1b[32m",
            key_input: ["3"]
        },
        key_opt4: {
            key_name: "4. High Scores",
            key_func: high_scores,
            key_clr: "\x1b[38;5;214m",
            key_input: ["4"]

        },
        key_opt5: {
            key_name: "5. EXIT",
            key_func: exit,
            key_clr: "\x1b[91m",
            key_input: ["5"]
        }
    }
}

#for v in arcade_menu[key_opts].values():
#        x = v[key_input]
#        print(x)
        
def get_frame_CLR(menu:dict):
    selection_index = get_selection(menu) 
    m_title = menu[key_title]
    m_opt_1 = menu[key_opts][key_opt1][key_name]
    m_opt_2 = menu[key_opts][key_opt2][key_name]
    m_opt_3 = menu[key_opts][key_opt3][key_name]
    m_opt_4 = menu[key_opts][key_opt4][key_name]
    m_opt_5 = menu[key_opts][key_opt5][key_name]
    m_c1 = menu[key_opts][key_opt1][key_clr]
    m_c2 = menu[key_opts][key_opt2][key_clr]
    m_c3 = menu[key_opts][key_opt3][key_clr]
    m_c4 = menu[key_opts][key_opt4][key_clr]
    m_c5 = menu[key_opts][key_opt5][key_clr]
    m_c_r = menu[key_clr_reset]
    m_c_i = menu[key_clr_inv]
    m_select = menu[key_select]
    m_c1 = m_c_i if selection_index == 0 else m_c1
    m_c2 = m_c_i if selection_index == 1 else m_c2
    m_c3 = m_c_i if selection_index == 2 else m_c3
    m_c4 = m_c_i if selection_index == 3 else m_c4
    m_c5 = m_c_i if selection_index == 4 else m_c5
    dots_v = [9478,9479,9482,9483]
    dots_v = [9588,9589,9590,9591,9592,9593,9594,9595,9596,9597]
    o = random.randint(0,5)
    oc = random.randint(-2,2)
    l= ('\x1b[38;5;161m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9577) if random.randint(0,100)   < 60 else chr(random.randint(9581,9584)) )+ f"\x1b[0m"
    a= ('\x1b[38;5;161m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9575) if random.randint(0,100)   < 60 else chr(random.randint(9581,9584)) )+ f"\x1b[0m"
    b= ('\x1b[38;5;161m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9517) if random.randint(0,100)   < 85 else chr(random.randint(9516,9531)+o) )+ f"\x1b[0m"
    c= ('\x1b[38;5;161m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9594) if random.randint(0,100)   < 85 else chr(random.randint(9588,9597)+o) )+ f"\x1b[0m"
    d= ('\x1b[38;5;118m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9529) if random.randint(0,100)   < 65 else chr(random.randint(9548,9549)+o) )+ f"\x1b[0m"
    e= ('\x1b[38;5;118m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9552) if random.randint(0,100)   < 85 else chr(random.randint(1024,1279)+o) )+ f"\x1b[0m"
    f= ('\x1b[38;5;81m'  if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9552) if random.randint(0,100)   < 85 else chr(random.randint(9476,9477)) )+ f"\x1b[0m"
    g= ('\x1b[38;5;81m'  if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9574) if random.randint(0,100)   < 85 else chr(random.randint(9472,9473)) )+ f"\x1b[0m"
    h= ('\x1b[38;5;81m'  if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9475) if random.randint(0,100)   < 85 else chr(random.randint(9478,9479)+o)  )+ f"\x1b[0m"
    i= ('\x1b[38;5;161m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(128584) if random.randint(0,100) < 50 else chr(random.randint(128584,128586)) )+ f"\x1b[0m"
    j=chr(random.randint(128336,128359))
    k=chr(random.randint(127761,127768))
    frame = f"""                                                                                                                                                                                                       
                                               ................................
                                            {c}{d}{e}{a}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{a}{b}.
                                         {c}{b}{a}{b}{c}{d}{g}                               .{e}{f}
                                      .{h}{a}{d}{f}   {d}{g}      {m_title}      {e}{f}
                                    {c}{a}{a}{h}      {d}{g}                                {e}{f}     
                                 {c}{b}{a}{b}.        {d}{b}{f}{f}{i}{f}{f}{f}{f}{f}{f}{f}{f}{f}{i}{f}{f}{f}{f}{f}{f}{f}{f}{f}{i}{f}{f}{f}{f}{f}{f}{e}{f}
                              .{g}{a}{d}{f}        {c}{b}{a}{b}{h}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{h}{d}{e}{a}{g}.
                             {h}{a}{g}        .{b}{a}{d}{c}                              {c}{g}{a}{a}{h}
                            {c}{a}{f}        {b}{a}{c} {g}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}{l}.{b}{a}{c}
                            {h}{a}         {c}{e}{f}{c}{a}{c}                           {b}{d}{c}{a}{g}
                            {h}{a}          {b}{d}.{d}{b}  {m_c1}{m_opt_1}{m_c_r}   {c}{a}{g}{h}{a}{c}                  {k}
                            {h}{a}         {f}{a}{c}{h}{a}.                            {c}{a}{h}{h}{a}{c}
                            {h}{a}          {c}{a}{f}{g}{a}{c}  {m_c2}{m_opt_2}{m_c_r}  {h}{a}{c}{b}{d}
                            {h}{a}          {f}{a}{c}{h}{a}.                            {c}{a}{h}{h}{a}{c}       #################################
                            {h}{a}           {d}{d}.{a}{h}   {m_c3}{m_opt_3}{m_c_r}            {d}{b}{c}{a}{g}       #    Use 1-5 or the Arrow Keys  #  
                            {h}{a}           {f}{a}{c}{h}{a}.                            {c}{a}{h}{h}{a}{c}      #       for navigation          #
                            {h}{a}           {d}{d}.{a}{h}   {m_c4}{m_opt_4}{m_c_r}            {d}{b}{c}{a}{g}       #################################                  
                            {h}{a}           {f}{a}{c}{h}{a}.                            {c}{a}{h}{h}{a}{c}
                            {h}{a}            {d}{b}.{d}{g}    {m_c5}{m_opt_5}{m_c_r}                 {g}{a}.{d}{a}{d}{g}
                            {h}{a}            {c}{a}{c}{g}{a}{c}                          {e}{g}{a}{f} {g}{a}
                            {h}{a}            .{d}{d}.{c}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{b}{g}{g}{h}{c}.{a}{d}{g}{a}{d}
                            {h}{a}              {h}{a}{a}{b}{h}{f}.  {c}{a}{d}{b}{a}{g}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{b}{d}{a}{c}{h}{d}{a}{f}{f}{b}{d}{a}{d}{b}{h}{c}
                            {h}{a}                  {c}{g}{d}{a}{a}{d}{g}{g}{d}{g}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{h}{b}{h}..{f}{f}......{c}{g}{a}{e}{e}{a}{b}{f}.
                            {h}{a}                        .{d}{a}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{b}{e}.
                            {h}{a}                         {b}{d}.                                {f}{e}.
                            {h}{a}                     .{c}{f}{b}{a}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{a}.
                            .{d}{d}.                  {h}{e}{b}{f}                              {h}{a}{a}{b}{f}.
                              {h}{a}{h}                 {h}{a}                                {h}{a}
                               .{d}{d}.               {h}{e}        {h}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{g}{c}     {h}{a}
                                .{d}{b}               {h}{a}       .{e}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{d}{b}     {h}{a}
                                .{d}{b}               {h}{a}       .{e}{f}            .{d}{b}     {h}{a}
                                .{d}{b}               {h}{e}       .{e}{f}     {j}     .{d}{b}     {h}{a}
                                .{d}{b}               {h}{a}       .{e}{f}            .{d}{b}     {h}{a}
                                .{d}{b}               {h}{a}        {d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{h}     {h}{a}
                                .{d}{b}               {h}{e}                              {h}{a}
                                .{d}{b}               {h}{a}                              {h}{a}
                                .{d}{b}               {h}{a}                              {h}{a}
                          {h}{d}{d}{d}{d}{d}{d}{a}{a}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{e}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{a}{d}{d}{d}{d}{d}{d}{d}{d}{f}
                          ...................................................................
     """
                           #{m_select} {selection_index}
    return frame

def get_subframe_CLR():
    a=f"\x1b[38;5;{random.randint(80,124)}m"+chr(random.randint(124,126))+f"\x1b[0m"
    b=f"\x1b[38;5;{random.randint(80,124)}m"+chr(random.randint(124,126))+f"\x1b[0m"
    c=f"\x1b[38;5;{random.randint(80,124)}m"+chr(126)+f"\x1b[0m"
    d=f"\x1b[38;5;{random.randint(80,124)}m"+chr(random.randint(124,126))+f"\x1b[0m"
    e=f"\x1b[38;5;{random.randint(80,124)}m"+chr(random.randint(124,126))+f"\x1b[0m"
    f=f"\x1b[38;5;{random.randint(80,124)}m"+chr(126)+f"\x1b[0m"
    g=f"\x1b[38;5;{random.randint(80,124)}m"+chr(124)+f"\x1b[0m"
    h=f"\x1b[38;5;{random.randint(80,124)}m"+chr(124)+f"\x1b[0m"
    i=f"\x1b[38;5;{random.randint(80,124)}m"+chr(124)+f"\x1b[0m"
    j=f"\x1b[38;5;{random.randint(80,124)}m"+chr(124)+f"\x1b[0m"
    o = random.randint(0,5)
    oc = random.randint(-2,2)
    a= ('\x1b[38;5;161m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9575) if random.randint(0,100)   < 60 else chr(random.randint(9581,9584)) )+ f"\x1b[0m"
    b= ('\x1b[38;5;161m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9517) if random.randint(0,100)   < 85 else chr(random.randint(9516,9531)+o) )+ f"\x1b[0m"
    c= ('\x1b[38;5;161m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9594) if random.randint(0,100)   < 85 else chr(random.randint(9588,9597)+o) )+ f"\x1b[0m"
    d= ('\x1b[38;5;118m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9529) if random.randint(0,100)   < 65 else chr(random.randint(9548,9549)+o) )+ f"\x1b[0m"
    e= ('\x1b[38;5;118m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9552) if random.randint(0,100)   < 75 else chr(random.randint(1024,1279)+o) )+ f"\x1b[0m"
    f= ('\x1b[38;5;81m'  if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9552) if random.randint(0,100)   < 85 else chr(random.randint(9476,9477)) )+ f"\x1b[0m"
    g= ('\x1b[38;5;81m'  if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9574) if random.randint(0,100)   < 75 else chr(random.randint(9472,9473)) )+ f"\x1b[0m"
    h= ('\x1b[38;5;81m'  if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9475) if random.randint(0,100)   < 85 else chr(random.randint(9478,9479)+o)  )+ f"\x1b[0m"
    i= ('\x1b[38;5;81m'  if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9574) if random.randint(0,100)   < 85 else chr(random.randint(9472,9473)) )+ f"\x1b[0m"
    j= ('\x1b[38;5;161m' if random.randint(0,100) < 89 else f'\x1b[38;5;{random.randint(197,230)+oc}m') + (chr(9577) if random.randint(0,100)   < 60 else chr(random.randint(9581,9584)) )+ f"\x1b[0m"
 
    

    z_frame_WTF_CLR = f"""
                        {h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}{h}
                     {e}{b}{a}{d}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{b}{d}{g}{h}
                  {e}{j}{d}{j}{e}{b}{i}                                                                                   {h}{a}{c}
               {h}{f}{d}{b}{c}   {b}{i}                                                                                    {a}{c}
             {e}{d}{d}{f}      {b}{i}                                                                                    {a}{c}     
          {e}{j}{d}{j}{h}        {b}{j}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{a}{c}
       {h}{i}{d}{b}{c}        {e}{j}{d}{j}{f}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{f}{b}{a}{d}{i}{h}
      {f}{d}{i}        {h}{j}{d}{b}{e}                                                                                {h}{i}{d}{d}{f}
     {e}{d}{c}        {j}{d}{e} {i}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{b}{h}{j}{d}{e}
     {f}{d}         {e}{a}{c}{e}{d}{e}                                                                               {j}{b}{e}{d}{i}
     {f}{d}         {e}{a}{c}{e}{d}{e}                                                                                {j}{b}{e}{d}{i}
     {f}{d}         {e}{a}{c}{e}{d}{e}                                                                                {j}{b}{e}{d}{i}
     {f}{d}          {j}{b}{h}{b}{j}                                                                                {e}{d}{i}{f}{d}{e}
     {f}{d}          {j}{b}{h}{b}{j}                                                                                {e}{d}{i}{f}{d}{e}
     {f}{d}          {j}{b}{h}{b}{j}                                                                                {e}{d}{i}{f}{d}{e}
     {f}{d}         {c}{d}{e}{f}{d}{h}                                                                                 {d}{f}{f}{d}{e}
     {f}{d}         {c}{d}{e}{f}{d}{h}                                                                                 {e}{d}{f}{f}{d}{e}
     {f}{d}         {c}{d}{e}{f}{d}{h}                                                                                 {e}{d}{f}{f}{d}{e}
     {f}{d}          {e}{d}{c}{i}{d}{e}                                                                                 {f}{d}{e}{j}{b}
     {f}{d}          {e}{d}{c}{i}{d}{e}                                                                                  {f}{d}{e}{j}{b}
     {f}{d}          {e}{d}{c}{i}{d}{e}                                                                                  {f}{d}{e}{j}{b}
     {f}{d}          {c}{d}{e}{f}{d}{h}                                                                                   {d}{f}{f}{d}{e}      
     {f}{d}           {b}{b}{h}{d}{f}                                                                                   {b}{j}{e}{d}{i}       
     {f}{d}           {c}{d}{e}{f}{d}{h}                                                                                  {e}{d}{f}{f}{d}{e}      
     {f}{d}           {b}{b}{h}{d}{f}                                                                                    {b}{j}{e}{d}{i} 
     {f}{d}           {c}{d}{e}{f}{d}{h}                                                                                  {e}{d}{f}{f}{d}{e}
     {f}{d}           {c}{d}{e}{f}{d}{h}                                                                                 {e}{d}{f}{f}{d}{e}
     {f}{d}            {b}{j}{h}{b}{i}    Input:                                                                       {i}{d}{h}{b}{d}{b}{i}
     {f}{d}            {e}{d}{e}{i}{d}{e}                                                                               {a}{i}{d}{c} {i}{d}
     {f}{d}            {h}{b}{b}{h}{e}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{j}{i}{i}{f}{e}{h}{d}{b}{i}{d}{b}
     {f}{d}              {f}{d}{d}{j}{f}{c}{h}  {e}{d}{b}{j}{d}{i}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{j}{b}{d}{e}{f}{b}{d}{c}{c}{j}{b}{d}{b}{j}{f}{e}
     {f}{d}                  {e}{i}{b}{d}{d}{b}{i}{i}{b}{i}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{e}{f}{j}{f}{h}{h}{c}{c}{h}{h}{h}{h}{h}{h}{e}{i}{d}{a}{a}{d}{j}{c}{h}
     {f}{d}                        {h}{b}{d}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{i}{j}{a}{h}
     {f}{d}                         {j}{b}{h}                                                                                    {c}{a}{h}
     {f}{d}                     {h}{e}{c}{j}{d}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{d}{h}


    """
    return z_frame_WTF_CLR

def get_subframe_title(menu):
    opt = get_active_option(menu)
    bl = "...:::| "
    br = " |:::..."
    if opt != None:
        return f"{opt[key_clr]}{bl}{opt[key_name][3:]:^20}{br}{menu[key_clr_reset]}"
    else: return ""

def get_cowsay(version=0):
    cow = rf"""
 ______________________________
| THANKS FOR PLAYING, GOODBYE! |
 ==============================
                            \ 
                             \
                               ^__^
                               (oo)\_______
                               (__)\       )\/\
                                   ||----w |
                                   ||     ||
"""
    cow2 = rf"""
 ______________________________
| THANKS FOR PLAYING, GOODBYE! |
 ==============================
                            \
                             \
                               ^__^
                               (-o)\_______ /\/
                              (__) \       )
                                   ||----w |
                                   ||     ||
"""
    return cow2 if version==1 else cow  

def init():
    global term, user_exit,original_print,original_input
    original_print = print
    original_input = input
    term = Terminal()  
    user_exit = False

def refresh_frame():
    #print("\x1b[H\x1b[J",end="") # H = Home / J = Clear Screen
    print(term.home + term.clear, end="") # H = Home / J = Clear Screen
    print(get_frame_CLR(arcade_menu),flush=True)
    

def read_input():
    global key_pressed
    with term.cbreak(), term.hidden_cursor():
       key_pressed = term.inkey(timeout=0)

def handle_input():
    global key_pressed
    key_str = repr(key_pressed)
    if key_str == "KEY_UP":
        arcade_menu[key_select] -=1
    if key_str == "KEY_DOWN":
        arcade_menu[key_select] +=1
    if key_str == "KEY_ENTER":
        game_launcher(arcade_menu)
    #if key_pressed == "1":
    #    arcade_menu[key_select] = 0
    #if key_pressed == "2":
    #    arcade_menu[key_select] = 1
    #if key_pressed == "3":
    #    arcade_menu[key_select] = 2
    #if key_pressed == "4":
    #    arcade_menu[key_select] = 3
    #if key_pressed == "5":
    #    arcade_menu[key_select] = 4
    for opts in arcade_menu[key_opts].values():
        if key_pressed in opts[key_input]:
            arcade_menu[key_select] = int(key_pressed) -1

def get_selection(menu):
    l = len(menu[key_opts])
    s = menu[key_select]
    return s % l

def get_active_option(menu):
    if menu[key_active] != "":
        return menu[key_opts][menu[key_active]]
    else: return None

def get_active_game_title(menu):
    if menu[key_active] != "":
        return menu[key_opts][menu[key_active]][key_name][2:]
    else:
        return None


def game_launcher(menu):
    global sf_buffer
    clear_screen()
    s = get_selection(menu)
    sf_buffer.clear()
    with sub_screen_io(subframe_print,subframe_input):
        if s == 0:
            menu[key_active] = key_opt1
            menu[key_opts][key_opt1][key_func]()
        if s == 1:
            menu[key_active] = key_opt2
            menu[key_opts][key_opt2][key_func]()
        if s == 2:
            menu[key_active] = key_opt3
            menu[key_opts][key_opt3][key_func]()
        if s == 3:
            menu[key_active] = key_opt4
            menu[key_opts][key_opt4][key_func]()
        if s == 4:
            menu[key_active] = key_opt5
            menu[key_opts][key_opt5][key_func]()
    time.sleep(0.5)

def arcade_run():
    try:
        init()
        while not user_exit:
            with term.hidden_cursor():
                refresh_frame()
                read_input()
                handle_input()
                time.sleep(1/10)
    except KeyboardInterrupt:
        ...
arcade_run()


#==================================================================================
###############################   TESTING GROUND   ################################
#==================================================================================

def get_frame(menu:dict):
    selection_index = get_selection(menu) 
    m_title = menu[key_title]
    m_opt_1 = menu[key_opts][key_opt1][key_name]
    m_opt_2 = menu[key_opts][key_opt2][key_name]
    m_opt_3 = menu[key_opts][key_opt3][key_name]
    m_opt_4 = menu[key_opts][key_opt4][key_name]
    m_opt_5 = menu[key_opts][key_opt5][key_name]
    m_c1 = menu[key_opts][key_opt1][key_clr]
    m_c2 = menu[key_opts][key_opt2][key_clr]
    m_c3 = menu[key_opts][key_opt3][key_clr]
    m_c4 = menu[key_opts][key_opt4][key_clr]
    m_c5 = menu[key_opts][key_opt5][key_clr]
    m_c_r = menu[key_clr_reset]
    m_c_i = menu[key_clr_inv]
    m_select = menu[key_select]
    m_c1 = m_c_i if selection_index == 0 else m_c1
    m_c2 = m_c_i if selection_index == 1 else m_c2
    m_c3 = m_c_i if selection_index == 2 else m_c3
    m_c4 = m_c_i if selection_index == 3 else m_c4
    m_c5 = m_c_i if selection_index == 4 else m_c5
    frame = f"""                                                                                                                                                                                                       
                                               ................................
                                            :#@%###############################%*.
                                         :*%*:#+                               .@-
                                      .=%#-   #+      {m_title}      @-
                                    :%%=      #+                                @-     
                                 :*%*.        #*--------------------------------@-
                              .+%#-        :*%*=----------------------------=#@%+.
                             =%+        .*%#:                            .+%%=
                            :%-        *%: +%%%%%%%%%%%%%%%%%%%%%%%%%%%#.*%:
                            =%         :@-:%:                           *#:%+
                            =%          *#.#*  {m_c1}{m_opt_1}{m_c_r}   :%+=%:
                            =%         -%:=%.                            :%==%:
                            =%          :%-+%:  {m_c2}{m_opt_2}{m_c_r}  =%:*#
                            =%          -%:=%.                            :%==%:      :::::::::::::::::::::::::::::::::                 
                            =%           ##.%=   {m_c3}{m_opt_3}{m_c_r}            #*:%+       #    Use 1-5 or the Arrow Keys     #                 
                            =%           -%:=%.                            :%==%:  #  for navigation  #                                 
                            =%           ##.%=   {m_c4}{m_opt_4}{m_c_r}            #*:%+      :::::::::::::::::::::::::::::::::             
                            =%           -%:=%.                            :%==%:
                            =%            #*.#+    {m_c5}{m_opt_5}{m_c_r}                 +%.#%#+
                            =%            :%:+%:                          @+%- +%
                            =%            .##.:+++++++++++++++++++++++*++=:.%#+%#
                            =%              =%%*=-.  :%#*%+%%%%%%%%%%%*#%:=#%--*#%#*=:
                            =%                  :+#%%#++#+::::::::::::=*=..--......:+%@@%*-.
                            =%                        .#%+++++++++++++++++++++++++++++++++*@.
                            =%                         *#.                                -@.
                            =%                     .:-*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.
                            .##.                  =@*-                              =%%*-.
                              =%=                 =%                                =%
                               .##.               =@        =+++++++++++++++:     =%
                                .#*               =%       .@=:::::::::::::#*     =%
                                .#*               =%       .@-            .#*     =%
                                .#*               =@       .@-            .#*     =%
                                .#*               =%       .@-            .#*     =%
                                .#*               =%        ################=     =%
                                .#*               =@                              =%
                                .#*               =%                              =%
                                .#*               =%                              =%
                          =######%%################@###############################%########-
                          ...................................................................
                           {m_select} {selection_index}
     """
    return frame

def get_subframe():
    z_frame = f"""
                        ....................................................................................
                     :#@%###################################################################################%*.
                  :*%*:#+                                                                                   .@-
               .=%#-   #+                                                                                    @-
             :%%=      #+                                                                                    @-     
          :*%*.        #*------------------------------------------------------------------------------------@-
       .+%#-        :*%*=--------------------------------------------------------------------------------=#@%+.
      =%+        .*%#:                                                                                .+%%=
     :%-        *%: +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.*%:
     =%         :@-:%:                                                                               *#:%+
     =%         :@-:%:                                                                                *#:%+
     =%         :@-:%:                                                                                *#:%+
     =%          *#.#*                                                                                :%+=%:
     =%          *#.#*                                                                                :%+=%:
     =%          *#.#*                                                                                :%+=%:
     =%         -%:=%.                                                                                 %==%:
     =%         -%:=%.                                                                                 :%==%:
     =%         -%:=%.                                                                                 :%==%:
     =%          :%-+%:                                                                                 =%:*#
     =%          :%-+%:                                                                                  =%:*#
     =%          :%-+%:                                                                                  =%:*#
     =%          -%:=%.                                                                                   %==%:      
     =%           ##.%=                                                                                   #*:%+       
     =%           -%:=%.                                                                                  :%==%:      
     =%           ##.%=                                                                                    #*:%+ 
     =%           -%:=%.                                                                                  :%==%:
     =%           -%:=%.                                                                                 :%==%:
     =%            #*.#+                                                                                 +%.#%#+
     =%            :%:+%:                                                                               @+%- +%
     =%            .##.:+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*++=:.%#+%#
     =%              =%%*=-.  :%#*%+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*#%:=#%--*#%#*=:
     =%                  :+#%%#++#+::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::=*=..--......:+%@@%*-.
     =%                        .#%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*@.
     =%                         *#.                                                                                    -@.
     =%                     .:-*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.

"""
    return z_frame
