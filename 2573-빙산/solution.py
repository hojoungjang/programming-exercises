"""
백준
빙산
https://www.acmicpc.net/problem/2573
"""

import sys
from collections import deque

SEA = 0

def solution(grid):
    def count_groups():
        visited = set()
        count = 0

        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if grid[r][c] == SEA or (r, c) in visited:
                    continue

                queue = deque([(r, c)])
                visited.add((r, c))
                count += 1

                while queue:
                    cur_r, cur_c = queue.popleft()

                    for r_offset, c_offset in [(0,1), (0,-1), (1,0), (-1,0)]:
                        new_r = cur_r + r_offset
                        new_c = cur_c + c_offset

                        if grid[new_r][new_c] == SEA or (new_r, new_c) in visited:
                            continue

                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
        
        return count


    rows, cols = len(grid), len(grid[0])
    year = 0

    while 0 < (groups := count_groups()) < 2:
        # melting
        melt_mask = []
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if grid[r][c] == SEA:
                    continue

                melt_mag = 0
                for r_offset, c_offset in [(0,1), (0,-1), (1,0), (-1,0)]:
                    new_r = r + r_offset
                    new_c = c + c_offset

                    if grid[new_r][new_c] == SEA:
                        melt_mag += 1

                if melt_mag:
                    melt_mask.append((r, c, melt_mag))

        for r, c, mag in melt_mask:
            grid[r][c] = max(0, grid[r][c] - mag)

        year += 1
    
    return year if groups >= 2 else 0


if __name__ == "__main__":
    rows, cols = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(rows)]
    print(solution(grid))

