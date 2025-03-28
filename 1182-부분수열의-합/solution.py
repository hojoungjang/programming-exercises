"""
백준
부분수열의 합
https://www.acmicpc.net/problem/1182
"""

import sys

def solution(seq, target):
    count = 0

    def combine(idx, total):
        nonlocal count

        if idx >= len(seq):
            return

        total += seq[idx]
        if total == target:
            count += 1
        combine(idx + 1, total)
        total -= seq[idx]
        combine(idx + 1, total)

    combine(idx=0, total=0)
    return count

if __name__ == "__main__":
    n, s = map(int, sys.stdin.readline().strip().split(" "))
    seq = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    print(solution(seq, s))