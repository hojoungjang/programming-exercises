"""
Leetcode
1144. Decrease Elements To Make Array Zigzag
https://leetcode.com/problems/decrease-elements-to-make-array-zigzag
"""

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        def _movesToMakeZigzag(nums, sign):
            cnt = 0
            for i in range(len(nums)-1):
                # nums[i] > nums[i+1]
                if sign and nums[i+1] >= nums[i]:
                    cnt += nums[i+1] - nums[i] + 1
                    nums[i+1] = nums[i] - 1
                # nums[i] < nums[i+1]
                elif not sign and nums[i] >= nums[i+1]:
                    cnt += nums[i] - nums[i+1] + 1
                    nums[i] = nums[i+1] - 1
                sign = not sign
            return cnt

        return min(_movesToMakeZigzag(nums[:], True), _movesToMakeZigzag(nums[:], False))
