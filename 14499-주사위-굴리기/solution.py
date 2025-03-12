"""
백준
주사위 굴리기
https://www.acmicpc.net/problem/14499
"""

import sys

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

MOVES_OFFSET = {
    RIGHT: (0, 1),
    LEFT: (0, -1),
    UP: (-1, 0),
    DOWN: (1, 0),
}

NUM_OF_FACES = 6

OPPOSITE_SIDE = [5, 3, 4, 1, 2, 0]

def update_face(move, face, up_idx, down_idx, left_idx, right_idx):
    if move == UP:
        new_face = up_idx
        up_idx = OPPOSITE_SIDE[face]
        down_idx = face
    elif move == DOWN:
        new_face = down_idx
        down_idx = OPPOSITE_SIDE[face]
        up_idx = face
    elif move == LEFT:
        new_face = left_idx
        left_idx = OPPOSITE_SIDE[face]
        right_idx = face
    elif move == RIGHT:
        new_face = right_idx
        right_idx = OPPOSITE_SIDE[face]
        left_idx = face
    return new_face, up_idx, down_idx, left_idx, right_idx
        

def solution(board, start_pos, moves):
    tops = []
    faces = [0 for _ in range(NUM_OF_FACES)]
    r, c = start_pos
    
    face = 0
    up = 1
    down = 3
    left = 4
    right = 2

    # iterate `moves` and follow the rules
    for move in moves:
        r_offset, c_offset = MOVES_OFFSET[move]

        r += r_offset
        c += c_offset

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            r -= r_offset
            c -= c_offset
            continue

        face, up, down, left, right = update_face(move, face, up, down, left, right)

        # 1. if board[r][c] == 0: copy faces[bottom] to board[r][c]
        if board[r][c] == 0:
            board[r][c] = faces[face]
        else:
            # 2. otherwise copy board[r][c] to faces[bottom]
            faces[face] = board[r][c]
            board[r][c] = 0

        # 3. print top
        tops.append(faces[OPPOSITE_SIDE[face]])

    return tops


if __name__ == "__main__":
    n, m, r, c, k = map(int, sys.stdin.readline().strip().split(" "))
    board = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    moves = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    tops = solution(board, (r,c), moves)
    for num in tops:
        print(num)
