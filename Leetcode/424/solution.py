"""
Leetcode
Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/description
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z",
        ]
        max_len = 0
        for c in characters:
            start = 0
            replace_cnt = 0
            for end in range(len(s)):
                if s[end] != c:
                    if k == 0:
                        start = end + 1
                        continue
                    while replace_cnt >= k and start < end:
                        if s[start] != c:
                            replace_cnt -= 1
                        start += 1
                    replace_cnt += 1

                max_len = max(max_len, end - start + 1)

        return max_len
