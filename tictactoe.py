# Function to initialize the board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


# Function to print the current board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


# Function to check if the board is full (i.e., a draw)
def check_draw(board):
    return all([cell != " " for row in board for cell in row])


# Function to take player input
def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")


# Main function to control the game flow
def main():
    board = initialize_board()
    current_player = "X"

    while True:
        print_board(board)

        # Take input for the current player's move
        player_input(board, current_player)

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
