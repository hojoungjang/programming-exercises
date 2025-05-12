"""
백준
순회강연
https://www.acmicpc.net/problem/2109
"""

from heapq import heappop, heappush
import sys

def solution(rewards):
    if not rewards:
        return 0
    
    last_day = max(day for _, day in rewards)
    schedule = [[] for _ in range(last_day + 1)]
    for pay, day in rewards:
        schedule[day].append(pay)

    pq = []
    earnings = 0

    for day in reversed(range(1, last_day+1)):
        for pay in schedule[day]:
            heappush(pq, -pay)

        if pq:
            pay = heappop(pq) * -1
            earnings += pay
    
    return earnings


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    rewards = []
    for _ in range(n):
        reward = tuple(map(int, sys.stdin.readline().strip().split(" ")))
        rewards.append(reward)

    print(solution(rewards))
