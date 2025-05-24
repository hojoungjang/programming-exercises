"""
백준
퇴사
https://www.acmicpc.net/problem/14501
"""

import sys

def solution(tasks):
    max_days = len(tasks)
    pay = [0 for _ in range(max_days + 2)]

    for d in reversed(range(1, max_days + 1)):
        days, rewards = tasks[d - 1]
        
        if (d + days) > (max_days + 1):
            continue

        for i in range(d + days, max_days + 2):
            pay[d] = max(pay[d], pay[i] + rewards)
        for i in range(d+1, d + days):
            pay[d] = max(pay[d], pay[i])
        
    return max(pay)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    tasks = [tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]
    print(solution(tasks))
