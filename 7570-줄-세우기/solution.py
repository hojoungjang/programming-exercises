"""
백준
줄 세우기
https://www.acmicpc.net/problem/7570
"""

import sys

# def solution(nums):
    
#     def _solution(nums, start, end):
#         if len(nums) == 1 or start > end:
#             return 0

#         cnt = 0
#         mid = (start + end) // 2
#         mid_idx = nums.index(mid)

#         left_rem = []
#         left_transfer = set()

#         for i in range(mid_idx):
#             if nums[i] < mid:
#                 left_rem.append(nums[i])
#             else:
#                 left_transfer.add(nums[i])
#                 cnt += 1

#         right_rem = []
#         right_transfer = set()

#         for i in range(mid_idx+1, len(nums)):
#             if nums[i] > mid:
#                 right_rem.append(nums[i])
#             else:
#                 right_transfer.add(nums[i])
#                 cnt += 1

#         # left
#         left_nums = []
#         for num in range(1, mid):
#             if num in right_transfer:
#                 left_nums.append(num)
#         left_nums.extend(left_rem)
#         cnt += _solution(left_nums, start, mid - 1)

#         # right
#         right_nums = right_rem
#         for num in range(mid+1, end+1):
#             if num in left_transfer:
#                 right_nums.append(num)
#         cnt += _solution(right_nums, mid+1, end)

#         return cnt

#     ##############################
#     return _solution(nums, 1, len(nums))


def solution(n, nums):
    idx_map = {num: idx for idx, num in enumerate(nums)}
    max_len = [1 for _ in range(n + 1)]  # max contiguous length

    for num in range(2, n + 1):
        if idx_map[num-1] < idx_map[num]:
            max_len[num] = max_len[num-1] + 1
    
    return n - max(max_len)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    print(solution(n, nums))