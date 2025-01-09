"""
백준
벌집
https://www.acmicpc.net/problem/2292
"""

from math import sqrt, ceil
import sys

def solution(n: int) -> int:
    a = 3
    b = 3
    c = 1 - n
    return ceil((-b + sqrt(b**2 - 4 * a * c)) / (2 * a)) + 1

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solution(n))
