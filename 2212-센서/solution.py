"""
백준
센서
https://www.acmicpc.net/problem/2212
"""

import sys

def solution(sensors, k):
    sensors.sort()
    connections = sorted([(sensors[i] - sensors[i-1], i-1, i) for i in range(1, len(sensors))])
    active_conn = set((i, j) for dist, i, j in connections[:(len(connections) - (k - 1))])

    total = 0
    start = sensors[0]
    end = sensors[0]
    for i in range(1, len(sensors)):
        if (i-1, i) not in active_conn:
            total += end - start
            start = sensors[i]
            end = sensors[i]
        else:
            end = sensors[i]

    if start != end:
        total += end - start
    
    return total


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    sensors = list(map(int, sys.stdin.readline().strip().split(" ")))
    print(solution(sensors, k))
