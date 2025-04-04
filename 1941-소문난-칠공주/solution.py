"""
백준
소문난 칠공주
https://www.acmicpc.net/problem/1941
"""

import sys
from collections import deque

ROWS = 5
COLS = 5

NUM_OF_MEMBERS = 7

def solution(classroom):
    def get_combination(r, c, combo):
        if len(combo) == 7:
            if [classroom[r][c] for r, c in combo].count("S") >= 4:
                combination.append(combo[:])
            return
        
        if r >= ROWS or c >= COLS:
            return

        offset_r, new_c = divmod(c + 1, COLS)
        new_r = r + offset_r

        combo.append((r, c))
        get_combination(new_r, new_c, combo)
        combo.pop()
        get_combination(new_r, new_c, combo)

    #######################################
    ans = 0
    combination = []
    get_combination(0, 0, [])
    for combo in combination:
        queue = deque([combo[0]])
        combo_set = set(combo[1:])

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_r = r + dr
                new_c = c + dc

                if (new_r, new_c) in combo_set:
                    queue.append((new_r, new_c))
                    combo_set.remove((new_r, new_c))
        
        if not combo_set:
            ans += 1
    
    return ans

if __name__ == "__main__":
    classroom = [sys.stdin.readline().strip() for _ in range(ROWS)]
    print(solution(classroom))