import sys

EMPTY = "."
BOMB = "O"

def solution(board, n):
    explosion_time = [[0 for _ in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == BOMB:
                explosion_time[i][j] = 3

    sec = 1
    while sec < n:
        sec += 1

        if sec % 2 == 0:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == EMPTY:
                        board[i][j] = BOMB
                        explosion_time[i][j] = sec + 3

        elif sec % 2 == 1:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if explosion_time[i][j] == sec:
                        board[i][j] = EMPTY
                        explosion_time[i][j] = 0
                        if i-1 >= 0:
                            board[i-1][j] = EMPTY
                        if i+1 < len(board):
                            board[i+1][j] = EMPTY
                        if j-1 >= 0:
                            board[i][j-1] = EMPTY
                        if j+1 < len(board[0]):
                            board[i][j+1] = EMPTY

    return board


if __name__ == "__main__":
    r, c, n = map(int, sys.stdin.readline().strip().split(" "))
    board = [[c for c in sys.stdin.readline().strip()] for _ in range(r)]
    board = solution(board, n)
    for r in board:
        print("".join(r))
