"""
백준
스타트와 링크
https://www.acmicpc.net/problem/11000
"""

import sys
from heapq import heappush, heappop

def solution(intervals):
    if not intervals:
        return 0
    
    intervals.sort()
    max_rooms = 1
    min_heap = []

    for start, end in intervals:
        while min_heap and min_heap[0] <= start:
            heappop(min_heap)
        heappush(min_heap, end)
        max_rooms = max(max_rooms, len(min_heap))
        
    return max_rooms


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    intervals = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(intervals))