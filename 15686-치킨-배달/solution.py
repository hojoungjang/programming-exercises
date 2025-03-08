"""
백준
치킨 배달
https://www.acmicpc.net/problem/15686
"""
import sys
from collections import deque
from itertools import combinations

EMPTY = 0
HOUSE = 1
CHICKEN = 2

def solution(grid, m):

    def find_target(target):
        coords = []
        for r in range(n):
            for c in range(n):
                if grid[r][c] == target:
                    coords.append((r,c))
        return coords

    n = len(grid)
    min_total_dist = float("inf")
    house_coords = find_target(HOUSE)
    chicken_coords = find_target(CHICKEN)

    for coords in combinations(chicken_coords, m):
        total_dist = 0
        for h_r, h_c in house_coords:
            dist = 2 * n
            for c_r, c_c in coords:
                dist = min(dist, abs(h_r - c_r) + abs(h_c - c_c))
            total_dist += dist
        min_total_dist = min(min_total_dist, total_dist)
    return min_total_dist


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[int(num) for num in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(grid, m))
