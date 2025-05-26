"""
백준
레이저 통신
https://www.acmicpc.net/problem/6087
"""

import sys
sys.setrecursionlimit(10001)

EMPTY = "."
WALL = "*"
TARGET = "C"

def solution(rows, cols, grid):
    def get_targets():
        coords = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == TARGET:
                    coords.append((r, c))
        return coords
    
    def dfs(r, c, direction, mirrors):
        visited[r][c] = (mirrors, direction[0], direction[1])

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_mirrors = mirrors
            if (dr, dc) != direction:
                new_mirrors += 1
                
            new_r = r + dr
            new_c = c + dc

            if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                continue

            if grid[new_r][new_c] == WALL:
                continue

            if visited[new_r][new_c][0] < new_mirrors:
                continue

            if visited[new_r][new_c][0] == new_mirrors and visited[new_r][new_c][1:] == (dr, dc):
                continue

            dfs(new_r, new_c, (dr, dc), new_mirrors)


    coords = get_targets()
    start_r, start_c = coords[0]
    end_r, end_c = coords[1]
    visited = [[(float("inf"), -1, -1) for _ in range(cols)] for _ in range(rows)]
    
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(start_r, start_c, d, 0)

    return visited[end_r][end_c][0]

if __name__ == "__main__":
    w, h = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[val for val in sys.stdin.readline().strip()] for _ in range(h)]
    print(solution(h, w, grid))