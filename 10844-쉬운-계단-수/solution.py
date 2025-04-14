"""
백준
쉬운 계단 수
https://www.acmicpc.net/problem/10844

brute force 솔루션 -> solution()
dynamic programming 솔루션 -> solution_dp()
"""

import sys

DIGITS = 10
MOD = 1_000_000_000

def is_step(num):
    num, digit = divmod(num, 10)
    while num:
        num, new_digit = divmod(num, 10)
        if abs(digit - new_digit) != 1:
            return False
        digit = new_digit
    return True

def solution(n):
    ans = 0
    for num in range(10**(n-1), 10**n):
        if is_step(num):
            ans = (ans + 1) % 1_000_000_000
    return ans


def solution_dp(n):
    dp = [1 for _ in range(DIGITS)]
    dp[0] = 0

    for _ in range(1, n):
        new_dp = [0 for _ in range(DIGITS)]
        for i in range(DIGITS):
            if i-1 >= 0:
                new_dp[i] += dp[i-1] 
            if i+1 < DIGITS:
                new_dp[i] += dp[i+1]
        dp = new_dp

    return sum(dp) % MOD


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(solution_dp(n))