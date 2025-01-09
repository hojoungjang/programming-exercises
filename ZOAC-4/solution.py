"""
백준
ZOAC 4
https://www.acmicpc.net/problem/23971
"""

import sys
from math import ceil

def solution(h, w, n, m):
    new_h = ceil(h / (n + 1))
    new_w = ceil(w / (m + 1))
    return new_h * new_w


if __name__ == "__main__":
    h, w, n, m = map(int, sys.stdin.readline().split(" "))
    print(solution(h, w, n, m))
