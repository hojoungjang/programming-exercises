"""
https://leetcode.com/problems/queries-on-a-permutation-with-key/
"""
from collections import deque

class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        queue = deque([i for i in range(1, m+1)])
        ans = []

        for query in queries:
            stack = []

            idx = 0
            while queue:
                num = queue.popleft()
                if num == query:
                    ans.append(idx)
                    break
                stack.append(num)
                idx += 1
            
            while stack:
                queue.appendleft(stack.pop())
            queue.appendleft(query)
    
        return ans
