"""
백준
감시 피하기
https://www.acmicpc.net/problem/18428
"""

import sys
from itertools import combinations

EMPTY = "X"
STUDENT = "S"
TEACHER = "T"
OBSTACLE = "O"

def get_target_coords(grid, target):
    coords = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == target:
                coords.append((r,c))
    return coords

def safe(grid, r, c):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_r = r
        new_c = c
        while 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
            if grid[new_r][new_c] == OBSTACLE:
                break
            if grid[new_r][new_c] == TEACHER:
                return False
            new_r += dr
            new_c += dc
    return True

def solution(grid):
    stu_coords = get_target_coords(grid, target=STUDENT)
    empty_coords = get_target_coords(grid, target=EMPTY)

    for obs_coords in combinations(empty_coords, 3):
        
        for r, c in obs_coords:
            grid[r][c] = OBSTACLE

        for r, c in stu_coords:
            if not safe(grid, r, c):
                break
        else:
            return True
        
        for r, c in obs_coords:
            grid[r][c] = EMPTY
    
    return False


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    grid = [[val for val in sys.stdin.readline().strip()] for _ in range(n)]
    print("YES" if solution(grid) else "NO")
