def is_safe(board, row, col, n):
    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, n):
    if row == n:  # All queens are placed
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            if solve_nqueens(board, row + 1, n):  # Solve for next row
                return True
            board[row][col] = 0  # Backtrack

    return False

def n_queens_with_first_placed(n, first_row, first_col):
    board = [[0] * n for _ in range(n)]  # Initialize the board
    board[first_row][first_col] = 1  # Place the first queen

    if solve_nqueens(board, first_row + 1, n):  # Solve for remaining queens
        return board
    return None

# Main program
n = int(input("Enter the size of the chessboard (n): "))
first_row = int(input(f"Enter the row index for the first queen (0 to {n-1}): "))
first_col = int(input(f"Enter the column index for the first queen (0 to {n-1}): "))

if 0 <= first_row < n and 0 <= first_col < n:
    solution = n_queens_with_first_placed(n, first_row, first_col)
    if solution:
        print("\nSolution:")
        for row in solution:
            print(row)
    else:
        print("\nNo solution exists for the given configuration.")
else:
    print("\nInvalid initial position. Please ensure the indices are within the bounds.")
