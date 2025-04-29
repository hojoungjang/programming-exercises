"""
백준
로봇 조종하기
https://www.acmicpc.net/problem/2169
"""

import sys

def solution(grid):
    dp = [val for val in grid[0]]
    for i in range(1, len(grid[0])):
        dp[i] += dp[i-1]

    for r in range(1, len(grid)):

        for c in range(len(grid[0])):
            dp[c] += grid[r][c]

        left_to_right = [val for val in dp]
        for c in range(1, len(grid[0])):
            left_to_right[c] = max(left_to_right[c], grid[r][c] + left_to_right[c-1])

        right_to_left = [val for val in dp]
        for c in reversed(range(len(grid[0]) - 1)):
            right_to_left[c] = max(right_to_left[c], grid[r][c] + right_to_left[c+1])

        for c in range(len(grid[0])):
            dp[c] = max(left_to_right[c], right_to_left[c])

    return dp[-1]


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(grid))