"""
백준
토마토
https://www.acmicpc.net/problem/7569
"""

import sys
from collections import deque

RIPE = 1
UNRIPE = 0
EMPTY = -1

def solution(boxes, rows, cols, height):
    visited = set()
    queue = deque()

    for h in range(height):
        for r in range(rows):
            for c in range(cols):
                if boxes[h][r][c] == RIPE:
                    visited.add((h, r, c))
                    queue.append((h, r, c))

    queue.append(None)
    days = 0
    while queue:
        if queue[0] is None:
            queue.popleft()
            if queue: queue.append(None)
            days += 1
            continue

        h, r, c = queue.popleft()
        boxes[h][r][c] = RIPE

        for dh, dr, dc in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            new_h = h + dh
            new_r = r + dr
            new_c = c + dc

            if new_h < 0 or new_h >= height:
                continue
            if new_r < 0 or new_r >= rows:
                continue
            if new_c < 0 or new_c >= cols:
                continue
            
            if (new_h, new_r, new_c) in visited or boxes[new_h][new_r][new_c] == EMPTY:
                continue

            visited.add((new_h, new_r, new_c))
            queue.append((new_h, new_r, new_c))
    
    for h in range(height):
        for r in range(rows):
            for c in range(cols):
                if boxes[h][r][c] == UNRIPE:
                    return -1
                
    return days - 1

if __name__ == "__main__":
    cols, rows, height = map(int, sys.stdin.readline().strip().split(" "))
    boxes = []
    for _ in range(height):
        box = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(rows)]
        boxes.append(box)
    print(solution(boxes, rows, cols, height))
