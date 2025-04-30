"""
백준
걷기
https://www.acmicpc.net/problem/1459

포기포기 ㅠㅠ
"""

import sys

def solution(rows, cols, cost, diag_cost):
    offset_total = rows + cols
    max_dim_val = max(rows, cols)

    straight_only = offset_total * cost
    
    if offset_total % 2 == 1:
        maximize_diag = (max_dim_val - 1) * diag_cost + cost
    else:
        maximize_diag = max_dim_val * diag_cost
    
    mix = diag_cost * min(rows, cols) + cost * abs(rows - cols)

    return min(straight_only, maximize_diag, mix)


if __name__ == "__main__":
    rows, cols, cost, diag_cost = map(int, sys.stdin.readline().strip().split(" "))
    print(solution(rows, cols, cost, diag_cost))