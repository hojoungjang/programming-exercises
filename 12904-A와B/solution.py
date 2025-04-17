"""
백준
A와 B
https://www.acmicpc.net/problem/12904
"""

import sys

def solution(s, t):
    while t and t != s:
        if t[-1] == "A":
            t = t[:-1]
        elif t[-1] == "B":
            t = t[:-1][::-1]
    return 1 if t == s else 0

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    print(solution(s, t))
