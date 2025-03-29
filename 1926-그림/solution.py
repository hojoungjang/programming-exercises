"""
백준
그림
https://www.acmicpc.net/problem/1926
"""

import sys
from collections import deque

def solution(canvas):
    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        size = 0

        while queue:
            r, c = queue.popleft()
            size += 1
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_r = r + dr
                new_c = c + dc

                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if (new_r, new_c) in visited:
                    continue
                if canvas[new_r][new_c] == 0:
                    continue
                
                queue.append((new_r, new_c))
                visited.add((new_r, new_c))
        
        return size

    ######################################
    rows = len(canvas)
    cols = len(canvas[0])
    visited = set()
    max_size = 0
    qty = 0

    for r in range(rows):
        for c in range(cols):
            if canvas[r][c] == 0 or (r, c) in visited:
                continue
            visited.add((r,c))
            max_size = max(max_size, bfs(r, c))
            qty += 1

    return qty, max_size

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    canvas = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    qty, max_size = solution(canvas)
    print(qty)
    print(max_size)