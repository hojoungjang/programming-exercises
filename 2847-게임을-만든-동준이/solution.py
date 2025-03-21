"""
백준
게임을 만든 동준이
https://www.acmicpc.net/problem/2847
"""
import sys

def solution(scores):
    reduction = 0
    highest = float("inf")
    for i in reversed(range(len(scores))):
        if scores[i] >= highest:
            highest -= 1
            reduction += scores[i] - highest
        else:
            highest = scores[i]
    return reduction

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    scores = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(scores))
