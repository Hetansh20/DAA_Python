# Define the board as a list of 9 spaces
board = [" "] * 9

# Function to print the Tic-Tac-Toe board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Check for winner
def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),   # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_full():
    return " " not in board

player = "X"

while True:
    print_board()
    move = int(input(f"Player {player}, choose position (1-9): ")) - 1
    
    if board[move] != " ":
        print("That spot is taken! Try again.")
        continue
    
    board[move] = player
    
    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break
    
    if is_full():
        print_board()
        print("It's a tie!")
        break
    
    player = "O" if player == "X" else "X"  # Switch player
