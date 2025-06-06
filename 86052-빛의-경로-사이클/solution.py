"""
프로그래머스
빛의 경로 사이클
https://school.programmers.co.kr/learn/courses/30/lessons/86052
"""

import sys
sys.setrecursionlimit(1000000)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def solution(grid):
    
    def dfs(r, c, d, length):
        visited.add((r, c, d))
        length += 1
        
        if grid[r][c] == "L":
            if d == UP:
                d = LEFT
            elif d == DOWN:
                d = RIGHT
            elif d == LEFT:
                d = DOWN
            elif d == RIGHT:
                d = UP
        elif grid[r][c] == "R":
            if d == UP:
                d = RIGHT
            elif d == DOWN:
                d = LEFT
            elif d == LEFT:
                d = UP
            elif d == RIGHT:
                d = DOWN
                
        dr, dc = d
        new_r = (r + dr) % rows
        new_c = (c + dc) % cols
        if (new_r, new_c, d) == start:
            return length
        if (new_r, new_c, d) in visited:
            return 0
        return dfs(new_r, new_c, d, length)
            
    rows = len(grid)
    cols = len(grid[0])
    
    lengths = []
    visited = set()
    
    for r in range(rows):
        for c in range(cols):
            for start_dir in [UP, DOWN, LEFT, RIGHT]:
                start = (r, c, start_dir)
                cycle_len = dfs(r, c, start_dir, 0)
                if cycle_len:
                    lengths.append(cycle_len)
                
    return sorted(lengths)
