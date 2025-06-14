"""
백준
가장 긴 증가하는 부분 수열 4
https://www.acmicpc.net/problem/14002
"""
import sys
from bisect import bisect_left

def solution(nums):
    seq = []

    for num in nums:
        idx = bisect_left(seq, num)
        if idx >= len(seq):
            seq.append(num)
        else:
            seq[idx] = num

    return seq

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    seq = solution(nums)
    print(len(seq))
    print(" ".join(str(val) for val in seq))
