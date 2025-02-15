"""
백준
숫자 카드 2
https://www.acmicpc.net/problem/10816
"""

from collections import Counter
import sys

def solution1(cards, queries):
    """
    추가 자료구조를 사용한 풀이법
    """
    counts = Counter(cards)
    ans = [0 for _ in range(len(queries))]
    for i, query in enumerate(queries):
        ans[i] = counts.get(query, 0)
    return ans

def solution2(cards, queries):
    """
    이분탐색을 이용한 풀이법
    """
    from bisect import bisect_left, bisect_right
    cards.sort()
    ans = []
    for query in queries:
        lo = bisect_left(cards, query)
        hi = bisect_right(cards, query)
        ans.append(hi - lo)
    return ans

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    cards = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    m = int(sys.stdin.readline().strip())
    queries = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    counts = solution2(cards, queries)
    print(" ".join(str(c) for c in counts))