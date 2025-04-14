"""
백준
암호코드
https://www.acmicpc.net/problem/2011

brute force 솔루션 -> solution()
dynamic programming 솔루션 -> solution_dp()

추가로 주어진 암호가 올바른지 확인할 필요가 있다.
"""

import sys

def solution(nums):
    """
    A: 1
    ...
    Z: 26

    25114
    
    2    5    1    1    4

    1   1+1   2
    """
    
    def _solution(idx):
        if idx == len(nums):
            return 1

        cnt = 0
        if 1 <= nums[idx] <= 9:
            cnt += _solution(idx + 1)
        
        if idx + 1 < len(nums):
            two_digit_num = nums[idx] * 10 + nums[idx+1]
            if 10 <= two_digit_num <= 26:
                cnt += _solution(idx + 2)
        
        return cnt

    ########################################
    cnt = _solution(0)
    return cnt % 1_000_000


def solution_dp(nums):
    if not nums:
        return 0

    one_away = 1
    two_away = 1

    for i in range(len(nums)):
        new_one_away = 0
        if 1 <= nums[i] <= 9:
            new_one_away += one_away
        if i-1 >= 0:
            two_digit_num = nums[i-1] * 10 + nums[i]
            if 10 <= two_digit_num <= 26:
                new_one_away += two_away
        if new_one_away == 0:
            return 0
        one_away, two_away = (new_one_away % 1_000_000), (one_away % 1_000_000)

    return one_away

if __name__ == "__main__":
    nums = [int(val) for val in sys.stdin.readline().strip()]
    print(solution_dp(nums))
