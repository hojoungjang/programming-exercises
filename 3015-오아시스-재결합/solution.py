"""
백준
오아시스 재결합
https://www.acmicpc.net/problem/3015
"""

import sys

def solution(heights):
    pair_cnt = 0
    stack = []
    for height in heights:
        while stack and height > stack[-1][0]:
            _, cnt = stack.pop()
            pair_cnt += cnt
        
        if stack and height == stack[-1][0]:
            _, top_cnt = stack.pop()
            pair_cnt += top_cnt
            stack.append((height, top_cnt + 1))
        else:
            stack.append((height, 1))

    stack = []
    for height in heights[::-1]:
        while stack and height > stack[-1][0]:
            _, cnt = stack.pop()
            pair_cnt += cnt
        
        if stack and height == stack[-1][0]:
            _, top_cnt = stack.pop()
            stack.append((height, top_cnt + 1))
        else:
            stack.append((height, 1))

    return pair_cnt

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    heights = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(heights))