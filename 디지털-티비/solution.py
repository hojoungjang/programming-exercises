"""
백준
디지털 티비
https://www.acmicpc.net/problem/2816
"""

import sys

def solution(channels: list[str]) -> str:
    ans = []

    # find KBS1
    for kbs1_idx in range(len(channels)):
        if channels[kbs1_idx] == "KBS1":
            break
    
    ans.extend(["1" for _ in range(kbs1_idx)])
    ans.extend(["4" for _ in range(kbs1_idx)])

    channels = ["KBS1"] + channels[:kbs1_idx] + channels[kbs1_idx+1:]

    # find KBS2
    for kbs2_idx in range(len(channels)):
        if channels[kbs2_idx] == "KBS2":
            break

    ans.extend(["1" for _ in range(kbs2_idx)])
    ans.extend(["4" for _ in range(kbs2_idx - 1)])
    return "".join(ans)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    channels = [sys.stdin.readline().strip() for _ in range(n)]
    print(solution(channels))
