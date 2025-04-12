"""
백준
포도주 시식
https://www.acmicpc.net/problem/2156
"""

import sys

def solution(wines):
    """
    3 consecutive not allowed

        6, 10, 13, 9, 8, 1
    1   6  10  19  25 31 29
    2   0  16  23  28 33 32
    """

    def _solution(idx, total, streak):
        nonlocal max_wine
        max_wine = max(max_wine, total)

        if idx >= len(wines):
            return
        
        if streak < 2:
            _solution(idx + 1, total + wines[idx], streak + 1)
        _solution(idx + 1, total, 0)

    max_wine = 0
    _solution(0, 0, 0)
    return max_wine


from collections import deque

MAX_STREAK = 3 

def solution_dp(wines):
    """
    case 1: wine at current index not included
    case 2: wine at current index included while index-1 not included
    case 3: wine at current index included while index-1 also included
    """
    if not wines:
        return 0

    dp = deque([0 for _ in range(MAX_STREAK)])
    dp[-1] = wines[0]

    for i in range(1, len(wines)):
        case1 = dp[2]
        case2 = dp[1] + wines[i]
        case3 = dp[0] + wines[i] + wines[i-1]

        dp.popleft()
        dp.append(max(case1, case2, case3))

    return dp[-1]


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    wines = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution_dp(wines))
