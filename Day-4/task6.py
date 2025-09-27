import random
import time
import os

PIECES = {
    "I": [[1,1,1,1]],
    "O": [[1,1],[1,1]],
    "T": [[0,1,0],[1,1,1]],
    "L": [[1,0],[1,0],[1,1]],
    "J": [[0,1],[0,1],[1,1]],
    "S": [[0,1,1],[1,1,0]],
    "Z": [[1,1,0],[0,1,1]]
}

def create_board(rows=20, cols=10):
    return [[0]*cols for _ in range(rows)]

def can_place(board, piece, r, c):
    pr, pc = len(piece), len(piece[0])
    rows, cols = len(board), len(board[0])
    for i in range(pr):
        for j in range(pc):
            if piece[i][j]:
                rr, cc = r+i, c+j
                if rr < 0 or rr >= rows or cc < 0 or cc >= cols or board[rr][cc]:
                    return False
    return True

def place(board, piece, r, c):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j]:
                board[r+i][c+j] = 1

def print_board(board):
    os.system("cls" if os.name=="nt" else "clear")
    for row in board:
        print("".join("#" if x else "." for x in row))

def drop_piece(board, piece):
    cols = len(board[0])
    start_c = cols//2 - len(piece[0])//2
    r = 0
    # drop until collision
    while True:
        if not can_place(board, piece, r+1, start_c):
            place(board, piece, r, start_c)
            break
        r += 1

# minimal loop
board = create_board(20,10)
for _ in range(10):
    piece = random.choice(list(PIECES.values()))
    if not can_place(board, piece, 0, len(board[0])//2 - len(piece[0])//2):
        print("Game over")
        break
    drop_piece(board, piece)
    print_board(board)
    time.sleep(0.3)
