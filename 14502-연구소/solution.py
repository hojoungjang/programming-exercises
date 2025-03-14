"""
백준
연구소
https://www.acmicpc.net/problem/14502
"""

import sys
from collections import deque

EMPTY = 0
WALL = 1
VIRUS = 2

MAX_WALLS = 3

def solution(board):
    rows = len(board)
    cols = len(board[0])

    def get_safe_cell_count():
        # spread virus and count empty cells
        board_copy = [[val for val in row] for row in board]
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if board_copy[r][c] == VIRUS and (r, c) not in visited:
                    queue = deque([(r, c)])
                    visited.add((r, c))

                    while queue:
                        cur_r, cur_c = queue.popleft()
                        board_copy[cur_r][cur_c] = VIRUS

                        for r_offset, c_offset in [(0,1), (0,-1), (1,0), (-1,0)]:
                            new_r = cur_r + r_offset
                            new_c = cur_c + c_offset

                            if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                                continue

                            if board_copy[new_r][new_c] == WALL:
                                continue

                            if (new_r, new_c) in visited:
                                continue
                            
                            visited.add((new_r, new_c))
                            queue.append((new_r, new_c))

        return sum(row.count(EMPTY) for row in board_copy)

    def build_wall(r, c, new_walls):
        nonlocal max_count
        if new_walls == MAX_WALLS:
            max_count = max(max_count, get_safe_cell_count())
            return
        
        if r >= rows:
            return
        
        extra_r, new_c = divmod(c + 1, cols)
        new_r = r + extra_r

        if board[r][c] == EMPTY:
            orig, board[r][c] = board[r][c], WALL
            build_wall(new_r, new_c, new_walls + 1)
            board[r][c] = orig
        
        build_wall(new_r, new_c, new_walls)

    ##################################################
    max_count = 0
    build_wall(0, 0, 0)
    return max_count


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    board = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(board))