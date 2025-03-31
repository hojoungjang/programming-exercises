"""
백준
⚾
https://www.acmicpc.net/problem/17281

베이스를 배열로 구현하면 시간초과 남
베이스를 각각 변수로 만들면 통과 ㅋㅋㄹㅃㅃ
"""

import sys
from itertools import permutations

FOURTH_PLAYER = 3
NUMBER_OF_BASES = 4
NUMBER_OF_PLAYERS = 9
EMPTY = 0
LOAD = 1
HOME = 3

def play(order, records):
    def update_bases(offset):
        nonlocal score
        
        for idx in reversed(range(NUMBER_OF_BASES - 1)):
            if bases[idx] == EMPTY:
                continue

            new_idx = idx + offset
            if new_idx >= HOME:
                score += 1
            else:
                bases[new_idx] = LOAD
            bases[idx] = EMPTY

        if offset > HOME:
            score += 1
        else:
            bases[offset - 1] = LOAD

    ###################################
    score = 0
    order_idx = 0
    
    for record in records:

        out_cnt = 0
        bases = [0 for _ in range(NUMBER_OF_BASES - 1)]

        while out_cnt < 3:
            player = order[order_idx]
            result = record[player]
            if result:
                update_bases(result)
            else:
                out_cnt += 1
            
            order_idx = (order_idx + 1) % NUMBER_OF_PLAYERS
    
    return score


def solution(records):
    max_score = 0
    for order in permutations(range(NUMBER_OF_PLAYERS)):
        if order[FOURTH_PLAYER] != 0:
            continue
        # print(order)
        max_score = max(max_score, play(order, records))
    return max_score

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())   # number of innings
    records = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(records))