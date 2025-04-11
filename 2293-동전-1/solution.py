"""
백준
동전
https://www.acmicpc.net/problem/2293
"""

import sys

def solution(coins, k):
    cnt = 0

    def _solution(coin_idx, coin_sum):
        nonlocal cnt

        if coin_sum > k or coin_idx >= len(coins):
            return
        
        if coin_sum == k:
            cnt += 1
            return
        
        _solution(coin_idx, coin_sum + coins[coin_idx])
        _solution(coin_idx + 1, coin_sum)

    _solution(0, 0)
    return cnt

def solution_dp(coins, k):
    dp = [0 for _ in range(k + 1)]
    dp[0] = 1

    for coin in coins:
        for num in range(1, k+1):
            if num - coin < 0:
                continue
            dp[num] += dp[num - coin]

    return dp[k]


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    coins = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution_dp(coins, k))
