"""
프로그래머스
무인도 여행
https://school.programmers.co.kr/learn/courses/30/lessons/154540
"""
import sys
sys.setrecursionlimit(100 * 100 + 1)

def solution(maps):
    def dfs(r, c):
        visited.add((r,c))
        size = int(maps[r][c])
        
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_r = r + dr
            new_c = c + dc
            
            if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                continue
            if (new_r, new_c) in visited:
                continue
            if maps[new_r][new_c] == "X":
                continue
                
            size += dfs(new_r, new_c)
        
        return size
    
    visited = set()
    rows = len(maps)
    cols = len(maps[0])
    islands = []
    
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] != "X" and (r,c) not in visited:
                islands.append(dfs(r, c))
                
    islands.sort()
    return islands if islands else [-1]
    