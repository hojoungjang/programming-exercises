"""
백준
퇴사 2
https://www.acmicpc.net/problem/15486
"""

import sys

def solution(schedule):
    n = len(schedule)
    max_earnings = [0 for _ in range(n + 1)]

    for i in reversed(range(n)):
        max_earnings[i] = max_earnings[i+1]
        time, price = schedule[i]
        end_i = i + time
        if end_i <= n:
            max_earnings[i] = max(max_earnings[i], max_earnings[end_i] + price)
    
    return max(max_earnings)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    schedule = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(schedule))