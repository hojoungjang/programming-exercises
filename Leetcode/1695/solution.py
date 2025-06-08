"""
Leetcode
Maximum Erasure Value
https://leetcode.com/problems/maximum-erasure-value/description/
"""

class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        counts = set()
        start = 0
        max_score = 0
        score = 0

        for end in range(len(nums)):

            while nums[end] in counts:
                counts.remove(nums[start])
                score -= nums[start]
                start += 1
            
            counts.add(nums[end])
            score += nums[end]
            max_score = max(max_score, score)
        
        return max_score
