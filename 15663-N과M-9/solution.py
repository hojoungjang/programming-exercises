"""
백준
N과 M (9)
https://www.acmicpc.net/problem/15663
"""

import sys

def solution(nums, max_len):

    def combine():
        if len(combo) == max_len:
            if (combo_tuple := tuple(combo)) not in combo_set:
                combo_set.add(combo_tuple)
                print(" ".join(str(val) for val in combo))
            return

        for i, num in enumerate(nums):
            if i not in used:
                used.add(i)
                combo.append(num)
                combine()
                combo.pop()
                used.remove(i)

    nums.sort()
    combo = []
    used = set()
    combo_set = set()
    combine()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    nums = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    solution(nums, m)
