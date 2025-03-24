"""
백준
컴백홈
https://www.acmicpc.net/problem/1189
"""

import sys

def solution(grid, k):

    def dfs(r, c, dist):
        nonlocal cnt

        if dist > k:
            return
        
        if r == 0 and c == cols - 1 and dist == k:
            cnt += 1
            return

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_r, new_c = r + dr, c + dc

            if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                continue

            if grid[new_r][new_c] == "T":
                continue

            if (new_r, new_c) in visited:
                continue

            visited.add((new_r, new_c))
            dfs(new_r, new_c, dist + 1)
            visited.remove((new_r, new_c))
    
    #########################################
    rows, cols = len(grid), len(grid[0])
    cnt = 0
    visited = set([(rows-1, 0)])
    dfs(rows - 1, 0, 1)
    return cnt


if __name__ == "__main__":
    rows, cols, k = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[val for val in sys.stdin.readline().strip()] for _ in range(rows)]
    print(solution(grid, k))