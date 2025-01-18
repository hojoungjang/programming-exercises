"""
백준
진우의 달 여행
https://www.acmicpc.net/problem/17484
"""

import sys

def solution(grid) -> int:
    moves = [(1, -1), (1, 0), (1, 1)]

    def travel(r, c, choices, cost):
        nonlocal min_cost
        if r == len(grid) - 1:
            min_cost = min(min_cost, cost + grid[r][c])
            return
        
        cost += grid[r][c]
        for choice in choices:
            r_offset, c_offset = moves[choice]
            new_r, new_c = r + r_offset, c + c_offset

            if new_c < 0 or new_c >= len(grid[0]):
                continue

            new_choices = set(i for i in range(len(moves)) if i != choice)
            travel(new_r, new_c, new_choices, cost)


    min_cost = float("inf")
    choices = set(i for i in range(len(moves)))
    for c in range(len(grid[0])):
        travel(0, c, choices, 0)
    return min_cost


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[int(num) for num in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(grid))