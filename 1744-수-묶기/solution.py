"""
백준
수 묶기
https://www.acmicpc.net/problem/1744
"""

import sys

def solution(nums):
    zeros = nums.count(0)
    negatives = sorted([num for num in nums if num < 0])
    positives = sorted([num for num in nums if num > 0], reverse=True)

    total = 0
    for i in range(0, len(positives)-1, 2):
        total += max(positives[i] * positives[i+1], positives[i] + positives[i+1])
    if len(positives) % 2 == 1:
        total += positives[-1]
    
    for i in range(0, len(negatives)-1, 2):
        total += max(negatives[i] * negatives[i+1], negatives[i] + negatives[i+1])
    if len(negatives) % 2 == 1 and not zeros:
        total += negatives[-1]
    
    return total


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(nums))
