"""
백준
크게 만들기
https://www.acmicpc.net/problem/2812
"""

import sys

def solution(digits, k):
    new_digits = []
    rm_cnt = 0
    
    for i in range(len(digits)):
        while rm_cnt < k and new_digits and new_digits[-1] < digits[i]:
            new_digits.pop()
            rm_cnt += 1
        new_digits.append(digits[i])

    while rm_cnt < k:
        new_digits.pop()
        rm_cnt += 1
    return "".join(new_digits)


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    digits = [val for val in sys.stdin.readline().strip()]
    print(solution(digits, k))
