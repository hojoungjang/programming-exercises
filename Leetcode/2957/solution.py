"""
Leetcode
2957. Remove Adjacent Almost-Equal Characters
https://leetcode.com/problems/remove-adjacent-almost-equal-characters
"""
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        cnt = 0
        i = 0
        while i < len(word)-1:
            if word[i] == word[i+1] or abs(ord(word[i]) - ord(word[i+1])) == 1:
                cnt += 1
                i += 2
            else:
                i += 1
        return cnt
