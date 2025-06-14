"""
Leetcode
Ones and Zeroes
https://leetcode.com/problems/ones-and-zeroes/
"""

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for s in strs:
            new_zeros = s.count("0")
            new_ones = s.count("1")
            new_dp = [[dp[z][o] for o in range(n+1)] for z in range(m+1)]

            for z in range(m+1):
                for o in range(n+1):
                    if dp[z][o] == 0:
                        continue
                    
                    new_z = z + new_zeros
                    new_o = o + new_ones

                    if new_z > m or new_o > n:
                        continue
                    
                    new_dp[new_z][new_o] = max(new_dp[new_z][new_o], dp[z][o] + 1)
            
            if new_zeros <= m and new_ones <= n:
                new_dp[new_zeros][new_ones] = max(new_dp[new_zeros][new_ones], 1)
            
            dp = new_dp

        return max(max(row) for row in dp)
