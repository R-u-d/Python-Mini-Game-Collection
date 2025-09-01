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





