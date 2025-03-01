"""
백준
로또
https://www.acmicpc.net/problem/6603
"""

import sys

def solution(k, nums):

    def _helper(i, selections):
        if len(selections) == 6:
            print(" ".join(str(num) for num in selections))
            return

        if i >= len(nums):
            return
        
        selections.append(nums[i])
        _helper(i+1, selections)
        selections.pop()
        _helper(i+1, selections)

    _helper(0, [])
    print()

if __name__ == "__main__":
    while True:
        nums = [int(num) for num in sys.stdin.readline().strip().split(" ")]
        k = nums[0]
        if k == 0:
            break
        nums = nums[1:]
        solution(k, nums)