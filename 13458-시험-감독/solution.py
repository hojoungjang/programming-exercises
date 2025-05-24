"""
백준
시험 감독
https://www.acmicpc.net/problem/13458
"""

from math import ceil
import sys

def solution(rooms, sup, sub_sup):
    cnt = 0

    for examinees in rooms:
        examinees = max(examinees - sup, 0)
        cnt += 1
        cnt += ceil(examinees / sub_sup)
    
    return cnt

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    rooms = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    sup, sub_sup = map(int, sys.stdin.readline().strip().split(" "))
    print(solution(rooms, sup, sub_sup))
