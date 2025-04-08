"""
백준
피보나치 함수
https://www.acmicpc.net/problem/1003
"""

import sys

MAX_NUM = 40
memo = [None for _ in range(MAX_NUM + 1)]

def fib(n):
    if n == 0:
        return (1, 0)
    if n == 1:
        return (0, 1)
    
    if not memo[n-1]:
        memo[n-1] = fib(n-1)
    if not memo[n-2]:
        memo[n-2] = fib(n-2)

    return (memo[n-1][0] + memo[n-2][0], memo[n-1][1] + memo[n-2][1])


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        zeros, ones = fib(n)
        print(f"{zeros} {ones}")