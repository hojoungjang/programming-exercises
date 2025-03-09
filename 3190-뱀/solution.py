"""
백준
뱀
https://www.acmicpc.net/problem/3190

구현 문제 어렵네
속도감 있고 정확하게 푸는 연습을 해봐야겠다.
사실 이거 보다 난이도 높은것도 많고 더 나아가서
최적화까지 해야되는 경우도 있을것같은데 아직은 차근차근
적당한 난이도에서 빠르고 정확하게 푸는법과 디버깅 잘하고 반례를
잘 찾을 수 있도록 연습해야 겠다.
"""

import sys
from collections import deque

RIGHT = (0, 1)
LEFT = (0, -1)
DOWN = (1, 0)
UP = (-1, 0)

EMPTY = 0
SNAKE = 1

TIME = 0
DIR = 1

def change_direction(cur_dir, change_dir):
    new_dir = cur_dir
    if cur_dir == LEFT:
        if change_dir == "L":
            new_dir = DOWN
        elif change_dir == "D":
            new_dir = UP
    elif cur_dir == RIGHT:
        if change_dir == "L":
            new_dir = UP
        elif change_dir == "D":
            new_dir = DOWN
    elif cur_dir == UP:
        if change_dir == "L":
            new_dir = LEFT
        elif change_dir == "D":
            new_dir = RIGHT
    elif cur_dir == DOWN:
        if change_dir == "L":
            new_dir = RIGHT
        elif change_dir == "D":
            new_dir = LEFT
    return new_dir

def solution(n, apples, moves):
    apples_set = set(apples)
    moves_idx = 0
    board = [[0 for _ in range(n)] for _ in range(n)]

    snake = deque()
    head_r = head_c = 0
    direction = RIGHT
    time = 0

    while True:
        if head_r < 0 or head_r >= n or head_c < 0 or head_c >= n:
            break

        if board[head_r][head_c] == SNAKE:
            break

        board[head_r][head_c] = SNAKE
        snake.appendleft((head_r, head_c))

        if (head_r, head_c) in apples_set:
            apples_set.remove((head_r, head_c))
        elif len(snake) > 1:
            tail_r, tail_c = snake.pop()
            board[tail_r][tail_c] = EMPTY

        head_r += direction[0]
        head_c += direction[1]

        time += 1
        if moves_idx < len(moves) and time == moves[moves_idx][TIME]:
            direction = change_direction(direction, moves[moves_idx][DIR])
            moves_idx += 1

    return time

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    n_apples = int(sys.stdin.readline().strip())
    apples = [tuple(int(val) - 1 for val in sys.stdin.readline().strip().split(" ")) for _ in range(n_apples)]

    n_moves = int(sys.stdin.readline().strip())
    moves = []
    for _ in range(n_moves):
        t, d = sys.stdin.readline().strip().split(" ")
        moves.append((int(t), d))

    print(solution(n, apples, moves))
