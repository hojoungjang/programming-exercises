"""
백준
IF문 좀 대신 써줘
https://www.acmicpc.net/problem/19637

처음에 전투력 칭호 범위를 리니어 서치를 하였다가 
시간초과가 되었다.

바이너리 서치로 바꾸어서 통과했다.
"""

import sys
from bisect import bisect_left

def solution(labels, powers):
    power_labels = []
    for power in powers:
        idx = bisect_left(labels, power, key=lambda x: x[1])
        power_labels.append(labels[idx][0])
    return power_labels

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    labels = list(map(lambda x: (x[0], int(x[1])), [sys.stdin.readline().strip().split(" ") for _ in range(n)]))
    powers = [int(sys.stdin.readline().strip()) for _ in range(m)]

    power_labels = solution(labels, powers)
    for l in power_labels:
        print(l)
