"""
백준
1,2,3 더하기
https://www.acmicpc.net/problem/9095
"""

import sys

def solution(num):
    memo = [0 for _ in range(num+1)]
    for i in range(1, min(3, num) + 1):
        memo[i] = 1

    for i in range(1, num+1):
        if i - 1 > 0:
            memo[i] += memo[i-1] 
        if i - 2 > 0:
            memo[i] += memo[i-2]
        if i - 3 > 0:
            memo[i] += memo[i-3]

    return memo[num]

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        num = int(sys.stdin.readline().strip())
        print(solution(num))
