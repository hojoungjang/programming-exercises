"""
Leetcode
2750. Ways to Split Array Into Good Subarrays
https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/description/
"""

class Solution:
    def numberOfGoodSubarraySplits(self, nums: list[int]) -> int:
        """
        [1, 0, 0, 1, 0, 1]
         1  2  3  3  

        ans(nums[:1]) + ans(nums[1:])
        ans(nums[:2]) + ans(nums[2:])
        

        [0, 1, 0, 0, 1]
         0, 1         3

        [0, 1, 0]
         0  1. 1 
         4 - 1
        """
        if nums.count(1) == 0:
            return 0
        
        start = nums.index(1)
        cnt = 1

        for end in range(start+1, len(nums)):
            if nums[end] == 1:
                cnt *= (end - start)
                start = end
        return cnt % (10**9 + 7)
