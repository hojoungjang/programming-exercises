"""
백준
흙길 보수하기
https://www.acmicpc.net/problem/1911
"""

import sys
from math import ceil

def solution(pools, l):
    pools.sort(key=lambda x: (x[0], x[1]))
    last_idx = 0
    total = 0

    for start, end in pools:
        start = max(start, last_idx)
        required_len = end - start
        board_cnt = ceil(required_len / l)
        total += board_cnt
        last_idx = start + l * board_cnt

    return total


if __name__ == "__main__":
    n, l = map(int, sys.stdin.readline().strip().split(" "))
    pools = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(pools, l))
