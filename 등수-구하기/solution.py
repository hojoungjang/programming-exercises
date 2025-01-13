"""
백준
등수 구하기
https://www.acmicpc.net/problem/1205
"""
import sys
from bisect import bisect_right

def solution(scores: list[int], new_score: int, p: int) -> int:
    idx = bisect_right(scores, -new_score, key=lambda x: -x)
    if idx >= p:
        return -1
    scores.insert(idx, new_score)
    rank = 1
    same = 1
    for i in range(1, idx + 1):
        if scores[i-1] > scores[i]:
            rank += same
            same = 1
        elif scores[i-1] == scores[i]:
            same += 1
    return rank

if __name__ == "__main__":
    n, new_score, p = map(int, sys.stdin.readline().strip().split())
    if n != 0:
        scores = list(map(int, sys.stdin.readline().strip().split()))
    else:
        scores = []
    print(solution(scores, new_score, p))
