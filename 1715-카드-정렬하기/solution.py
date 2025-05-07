"""
백준
카드 정렬하기
https://www.acmicpc.net/problem/1715
"""

import sys
from heapq import heapify, heappop, heappush

def solution(card_set_sizes):
    heapify(card_set_sizes)
    total_cmps = 0

    while len(card_set_sizes) > 1:
        size1 = heappop(card_set_sizes)
        size2 = heappop(card_set_sizes)
        new_size = size1 + size2
        heappush(card_set_sizes, new_size)
        total_cmps += new_size
    
    return total_cmps

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    card_set_sizes = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(card_set_sizes))
