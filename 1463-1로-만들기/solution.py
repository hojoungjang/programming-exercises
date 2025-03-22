"""
백준
1로 만들기
https://www.acmicpc.net/problem/1463
"""

import sys

def solution(num):
    memo = [i for i in range(num + 1)]
    memo[1] = 0

    for i in range(1, num+1):
        num1 = i * 3
        num2 = i * 2
        num3 = i + 1

        if num1 <= num:
            memo[num1] = min(memo[num1], memo[i] + 1)
        if num2 <= num:
            memo[num2] = min(memo[num2], memo[i] + 1)
        if num3 <= num:
            memo[num3] = min(memo[num3], memo[i] + 1)

    return memo[num]

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    print(solution(num))
