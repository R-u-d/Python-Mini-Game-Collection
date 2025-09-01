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

