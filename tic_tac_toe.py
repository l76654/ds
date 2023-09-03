# Initialize the Tic Tac Toe board
board = [" " for _ in range(9)]

# Function to display the Tic Tac Toe board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to check if the game is over
def is_game_over(board):
    # Check rows, columns, and diagonals
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True

    # Check for a tie (board is full)
    if " " not in board:
        return True

    return False

# Function to get player input and update the board
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Main game loop
current_player = "X"
while True:
    display_board(board)
    player_move(current_player)
    
    if is_game_over(board):
        display_board(board)
        if " " not in board:
            print("It's a tie!")
        else:
            print(f"Player {current_player} wins!")
        break

    current_player = "O" if current_player == "X" else "X"
