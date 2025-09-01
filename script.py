# NUMBER GUESSING GAME


# PAPER, ROCK, SCISSORS



# After coming out of the while loop, print thanks for playing


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


    #####
    

# Function to check the winner


    
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

        #####
        
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

