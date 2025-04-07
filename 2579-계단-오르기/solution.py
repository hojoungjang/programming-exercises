"""
백준
계단 오르기
https://www.acmicpc.net/problem/2579
"""

import sys

MAX_STEP_OFFSET = 2
ONE_AWAY = 1
TWO_AWAY = 0

def solution(nums):
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return nums[0]

    scores = [[0, 0] for _ in range(MAX_STEP_OFFSET)]
    scores[TWO_AWAY] = (nums[0], 0)
    scores[ONE_AWAY] = (max(scores[0]) + nums[1], nums[1])

    for i in range(2, len(nums)):
        new_two_away = scores[ONE_AWAY]
        scores[ONE_AWAY] = (scores[ONE_AWAY][1] + nums[i], max(scores[TWO_AWAY]) + nums[i])
        scores[TWO_AWAY] = new_two_away

    return max(scores[-1])

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(nums))