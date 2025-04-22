"""
백준
말이-되고픈-원숭이
https://www.acmicpc.net/problem/1600
"""

import sys
from collections import deque

EMPTY = 0
BLOCKED = 1

NORMAL_MOVES = [(-1,0), (1,0), (0,-1), (0,1)]
HORSE_MOVES = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2)]

def solution(board, max_horse_move_count):
    rows, cols = len(board), len(board[0])
    start = (0, 0, max_horse_move_count)
    end = (rows-1, cols-1)

    queue = deque([start, None])
    visited = set([start])
    moves = 0

    while queue:
        if queue[0] is None:
            queue.popleft()
            if queue:
                queue.append(None)
            moves += 1
            continue
        
        r, c, horse_move_count = queue.popleft()
        if (r, c) == end:
            return moves
        
        if horse_move_count > 0:
            for dr, dc in HORSE_MOVES:
                new_r = r + dr
                new_c = c + dc
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue

                new_state = (new_r, new_c, horse_move_count - 1)

                if new_state in visited:
                    continue

                if board[new_r][new_c] == BLOCKED:
                    continue

                visited.add(new_state)
                queue.append(new_state)

        for dr, dc in NORMAL_MOVES:
            new_r = r + dr
            new_c = c + dc
            if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                continue

            new_state = (new_r, new_c, horse_move_count)

            if new_state in visited:
                continue

            if board[new_r][new_c] == BLOCKED:
                continue

            visited.add(new_state)
            queue.append(new_state)

    return -1


if __name__ == "__main__":
    horse_move_count = int(sys.stdin.readline().strip())
    cols, rows = map(int, sys.stdin.readline().strip().split(" "))
    board = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(rows)]
    print(solution(board, horse_move_count))
