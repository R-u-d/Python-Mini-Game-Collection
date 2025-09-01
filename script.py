# Work off the platform in groups using the following code as a base



# NUMBER GUESSING GAME




# PAPER, ROCK, SCISSORS


# After coming out of the while loop, print thanks for playing


# TIC-TAC-TOE
# Function to print the board



# Function to check the winner



# Function to run fo the actual tic-tac-toe game where your other functions will be used

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
    
    # Ask if the user wants to play again
        print(" ")
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

if __name__ == "__main__":
    tic_tac_toe()
   

# MENU SYSTEM

    

    
# RUN THE MENU
