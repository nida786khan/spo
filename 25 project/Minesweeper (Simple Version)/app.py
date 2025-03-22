import random

def create_board(size, mines):
    board = [[" "]*size for _ in range(size)]
    for _ in range(mines):
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        board[x][y] = "💣"
    return board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (4 * len(board) - 1))

size, mines = 5, 5
board = create_board(size, mines)
print_board(board)
