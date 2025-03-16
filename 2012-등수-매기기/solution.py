"""
백준
등수 매기기
https://www.acmicpc.net/problem/2012
"""

import sys

def solution(preferences):
    preferences.sort()
    return sum(abs((i+1) - val) for i, val in enumerate(preferences))
    

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    preferences = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(preferences))
