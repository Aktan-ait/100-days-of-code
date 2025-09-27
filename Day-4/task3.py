def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def valid(board, row, col, val):
    # row
    if any(board[row][c] == val for c in range(9)):
        return False
    # col
    if any(board[r][col] == val for r in range(9)):
        return False
    # 3x3 block
    br, bc = 3*(row//3), 3*(col//3)
    for r in range(br, br+3):
        for c in range(bc, bc+3):
            if board[r][c] == val:
                return False
    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty
    for val in range(1,10):
        if valid(board, r, c, val):
            board[r][c] = val
            if solve_sudoku(board):
                return True
            board[r][c] = 0
    return False

# Example puzzle (0 = empty)
puzzle = [
 [5,3,0,0,7,0,0,0,0],
 [6,0,0,1,9,5,0,0,0],
 [0,9,8,0,0,0,0,6,0],
 [8,0,0,0,6,0,0,0,3],
 [4,0,0,8,0,3,0,0,1],
 [7,0,0,0,2,0,0,0,6],
 [0,6,0,0,0,0,2,8,0],
 [0,0,0,4,1,9,0,0,5],
 [0,0,0,0,8,0,0,7,9]
]

if solve_sudoku(puzzle):
    for row in puzzle:
        print(row)
else:
    print("No solution")
