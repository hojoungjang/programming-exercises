"""
백준
동전 문제
https://www.acmicpc.net/problem/1398
"""

import sys

def solution(num: str):
    dp = [0 for _ in range(101)]
    coins = [1, 10, 25]
    
    for i in range(1, 101):
        dp[i] = float("inf")

        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
            
    cnts = 0
    amount = int(num)
    while amount > 0:
        val = amount % 100
        cnts += dp[val]
        amount //= 100
    return cnts
        
if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        num = sys.stdin.readline().strip()
        print(solution(num))
