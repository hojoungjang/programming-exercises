"""
백준
Puyo puyo
https://www.acmicpc.net/problem/11559
"""

import sys

ROWS = 12
COLS = 6

EMPTY = "."

MIN_EXPLOSION_SIZE = 4

def solution(grid):

    def dfs(r, c, color):
        visited.add((r,c))
        sub_visited.add((r,c))

        for r_offset, c_offset in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_r = r + r_offset
            new_c = c + c_offset

            if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS:
                continue

            if grid[new_r][new_c] != color:
                continue

            if (new_r, new_c) in sub_visited:
                continue

            dfs(new_r, new_c, color)

    def gravity():
        for c in range(COLS):
            fill_r = ROWS - 1
            for r in reversed(range(ROWS)):
                if grid[r][c] != EMPTY:
                    grid[fill_r][c] = grid[r][c]
                    fill_r -= 1
            
            for r in reversed(range(fill_r + 1)):
                grid[r][c] = EMPTY

    ############################################
    chain_cnt = 0

    while True:
        # find explosions
        visited = set()
        explosion = set()

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited or grid[r][c] == EMPTY:
                    continue

                sub_visited = set()
                dfs(r, c, color=grid[r][c])

                if len(sub_visited) >= MIN_EXPLOSION_SIZE:
                    explosion.update(sub_visited)

        # no explosion break
        if not explosion:
            break

        # explode
        for r, c in explosion:
            grid[r][c] = EMPTY

        # gravity
        gravity()

        chain_cnt += 1
    
    return chain_cnt

if __name__ == "__main__":
    grid = [[char for char in sys.stdin.readline().strip()] for _ in range(ROWS)]
    print(solution(grid))