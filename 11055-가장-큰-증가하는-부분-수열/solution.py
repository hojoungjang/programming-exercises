"""
백준
가장 큰 증가하는 부분 수열
https://www.acmicpc.net/problem/11055
"""

import sys

def solution(nums):
    seq_sum = [num for num in nums]

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                seq_sum[i] = max(seq_sum[i], seq_sum[j] + nums[i])

    return max(seq_sum)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    print(solution(nums))
