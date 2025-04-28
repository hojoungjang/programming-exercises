"""
백준
불커기
https://www.acmicpc.net/problem/11967
"""

import sys
from collections import deque

def solution(n, switch_map):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    grid[0][0] = 1
    
    start = (0, 0)
    queue = deque([start])
    visited = set([start])
    frontier = set()
    light_cnt = 1
    
    while queue:    
        r, c = queue.popleft()

        for switch_r, switch_c in switch_map.get((r, c), []):
            if grid[switch_r][switch_c] == 0:
                grid[switch_r][switch_c] = 1
                light_cnt += 1
                if (switch_pos := (switch_r, switch_c)) in frontier:
                    queue.append(switch_pos)
                    visited.add(switch_pos)
                    frontier.remove(switch_pos)

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_r, new_c = r+dr, c+dc
            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
                continue

            if (new_r, new_c) in visited:
                continue

            if grid[new_r][new_c] == 0:
                frontier.add((new_r, new_c))
                continue

            queue.append((new_r, new_c))
            visited.add((new_r, new_c))
    
    return light_cnt


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    switch_map = {}
    for _ in range(m):
        from_r, from_c, to_r, to_c = map(int, sys.stdin.readline().strip().split(" "))
        if (from_r-1, from_c-1) not in switch_map:
            switch_map[(from_r-1, from_c-1)] = []
        switch_map[(from_r-1, from_c-1)].append((to_r-1, to_c-1))
    print(solution(n, switch_map))
