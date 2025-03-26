"""
백준
경사로
https://www.acmicpc.net/problem/14890
"""

import sys

def check_path(nums, l):
    n = len(nums)
    
    i = 0
    prev_height = nums[0]
    used = [0 for _ in range(n)]

    while i < n:
        cur_height = nums[i]

        if abs(cur_height - prev_height) > 1:
            return False

        if cur_height == prev_height:
            prev_height = cur_height
            i += 1
            continue

        if cur_height < prev_height:
            temp_i = i
            length = 0
            while temp_i < n and nums[temp_i] == cur_height and not used[temp_i] and length < l:
                used[temp_i] = 1
                temp_i += 1
                length += 1
        else:
            temp_i = i - 1
            length = 0
            while temp_i >= 0 and nums[temp_i] == prev_height and not used[temp_i] and length < l:
                used[temp_i] = 1
                temp_i -= 1
                length += 1

        if length < l:
            return False

        prev_height = cur_height
        if temp_i > i:
            i = temp_i
        else:
            i += 1
        
    return True
    
def solution(grid, l):
    n = len(grid)
    path_cnt = 0

    for r in range(n):
        if check_path(grid[r], l):
            path_cnt += 1
    
    for c in range(n):
        if check_path([grid[r][c] for r in range(n)], l):
            path_cnt += 1

    return path_cnt

if __name__ == "__main__":
    n, l = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(grid, l))
