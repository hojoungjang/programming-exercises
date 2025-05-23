"""
프로그래머스
귤 고르기
https://school.programmers.co.kr/learn/courses/30/lessons/138476
"""
from collections import Counter

def solution(k, tangerine):
    tang_sorted = sorted(Counter(tangerine).items(), key=lambda x: (-x[1]))
    ans = 0
    for size, count in tang_sorted:
        if k <= 0:
            break
        ans += 1
        k -= count
    return ans
