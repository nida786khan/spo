import math

# Tic-Tac-Toe Board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Players
HUMAN = "X"
AI = "O"

# ✅ Function to Print Board
def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

# ✅ Function to Check for Winner
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# ✅ Function to Check if Board is Full
def is_full():
    return all(cell != " " for row in board for cell in row)

# ✅ Minimax Algorithm for AI
def minimax(is_maximizing):
    winner = check_winner()
    if winner == HUMAN:
        return -1
    elif winner == AI:
        return 1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = AI
                    score = minimax(False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = HUMAN
                    score = minimax(True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# ✅ AI Move
def best_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = AI
                score = minimax(False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = AI

# ✅ Main Game Loop
while True:
    print_board()
    
    if check_winner() or is_full():
        break

    # Human Move
    row, col = map(int, input("Enter row and col (0-2): ").split())
    if board[row][col] == " ":
        board[row][col] = HUMAN
    else:
        print("Invalid move, try again!")
        continue
    
    # AI Move
    if not check_winner() and not is_full():
        best_move()

print_board()
winner = check_winner()
if winner:
    print(f"{winner} wins! 🏆")
else:
    print("It's a tie! 🤝")
