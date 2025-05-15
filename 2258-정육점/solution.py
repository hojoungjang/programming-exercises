"""
백준
정육점
https://www.acmicpc.net/problem/2258
"""

import sys

def solution(meats, target_weight):
    meats.sort(key=lambda x: (x[1], -x[0]))
    base_weight = 0
    total_weight = 0
    total_price = 0
    cur_price = -1
    min_price = float("inf")

    for weight, price in meats:
        if price != cur_price:
            cur_price = price
            base_weight += total_weight
            total_price = 0
            total_weight = 0
        
        total_price += price
        total_weight += weight

        if base_weight + total_weight >= target_weight:
            min_price = min(min_price, total_price)
    
    return min_price if min_price != float("inf") else -1


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    meats = [tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]
    print(solution(meats, target_weight=m))
