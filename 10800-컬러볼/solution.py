"""
백준
컬러볼
https://www.acmicpc.net/problem/10800
"""

import sys
from collections import defaultdict

def solution(balls):
    sorted_balls = sorted([(i, color, size) for i, (color, size) in enumerate(balls)], key=lambda x: (x[2]))
    size_sums = [0 for _ in range(len(balls))]
    size_run_sum = 0
    color_sums = defaultdict(int)

    same_size_idx = 0

    for ball_id, color, size in sorted_balls:
        while sorted_balls[same_size_idx][2] < size:
            _, c, s = sorted_balls[same_size_idx]
            color_sums[c] += s
            size_run_sum += s
            same_size_idx += 1

        size_sums[ball_id] = size_run_sum - color_sums.get(color, 0)
    
    return size_sums

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    balls = []
    for _ in range(n):
        color, size = map(int, sys.stdin.readline().strip().split(" "))
        balls.append((color, size))

    for size_sum in solution(balls):
        print(size_sum)
