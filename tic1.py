import tkinter as tk
from tkinter import messagebox

# Game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# Color settings
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

# Function to handle button clicks
def button_click(row, col):
    global curr_player

    if board[row][col] == 0:
        # Mark the board with the current player's symbol
        board[row][col] = curr_player
        buttons[row][col].config(text=curr_player, state="disabled", disabledforeground=color_light_gray)

        # Check if the current player wins
        if check_winner(curr_player):
            messagebox.showinfo("Game Over", f"Player {curr_player} wins!")
            reset_game()
        else:
            # Switch players
            curr_player = playerO if curr_player == playerX else playerX

# Function to check if the current player has won
def check_winner(player):
    # Check rows, columns, and diagonals for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to reset the game
def reset_game():
    global curr_player, board
    curr_player = playerX
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state="normal", bg=color_blue)

# Window setup
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

# Button grid setup
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text="", width=10, height=3, font=('normal', 20),
                           bg=color_yellow, command=lambda row=row, col=col: button_click(row, col))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Start the game window
window.mainloop()
