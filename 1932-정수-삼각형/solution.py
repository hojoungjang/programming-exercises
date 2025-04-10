"""
백준
정수 삼각형
https://www.acmicpc.net/problem/1932
"""

import sys

def solution(n, triangle):
    if not triangle:
        return 0
    
    level_maximums = [val for val in triangle[-1]]
    for i in reversed(range(n - 1)):
        for j in range(len(triangle[i])):
            level_maximums[j] = max(level_maximums[j], level_maximums[j+1]) + triangle[i][j]
    return level_maximums[0]

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    triangle = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(n, triangle))