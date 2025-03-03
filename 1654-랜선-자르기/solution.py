"""
백준
랜선 자르기
https://www.acmicpc.net/problem/1654

간단하게 이분탐색으로 풀린다! 길이를 이분탐색의 범위로 인지하는게
관건일것같다.
"""

import sys

def solution(wires: list[int], n: int) -> int:
    lo = 1
    hi = max(wires)

    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = sum(wire_len // mid for wire_len in wires)
        if cnt < n:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return hi


if __name__ == "__main__":
    k, n = map(int, sys.stdin.readline().strip().split(" "))
    wires = [int(sys.stdin.readline().strip()) for _ in range(k)]
    print(solution(wires, n))