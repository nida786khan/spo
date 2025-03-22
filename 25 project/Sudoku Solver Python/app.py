def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def is_valid(board, row, col, num):
    # Row check
    if num in board[row]:
        return False

    # Column check
    if num in [board[i][col] for i in range(9)]:
        return False

    # 3x3 Grid check
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
                
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty Cell
                for num in range(1, 10):  # Numbers 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):  # Recursively solve
                            return True
                        board[row][col] = 0  # Backtrack
                return False  # No valid number found
    return True

# 🧩 Example Sudoku Board (0 = Empty Cell)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("🔹 Unsolved Sudoku Board:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\n✅ Solved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("\n❌ No Solution Exists")
