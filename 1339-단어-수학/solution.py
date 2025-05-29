"""
백준
단어 수학
https://www.acmicpc.net/problem/1339
"""

import sys

MAX_DIGIT_LEN = 8

def solution(num_strs):
    priority = {}
    for ns in num_strs:
        for i, digit in enumerate(ns[::-1]):
            if digit not in priority:
                priority[digit] = 0
            priority[digit] += 10 ** i

    mapping = {}
    value = 9
    for letter, _ in sorted(priority.items(), key=lambda x: (-x[1])):
        if letter not in mapping:
            mapping[letter] = value
            value -= 1

    total = 0
    for ns in num_strs:
        for i, letter in enumerate(ns[::-1]):
            total += mapping.get(letter, 0) * (10 ** i)
    return total

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    num_strs = [sys.stdin.readline().strip() for _ in range(n)]
    print(solution(num_strs))
