"""
백준
컵라면
https://www.acmicpc.net/problem/1781
"""
import sys
from heapq import heappush, heappop

def solution(n, noodles):
    noodles.sort(reverse=True)
    nidx = 0

    task_queue = []
    total_reward = 0

    for time in reversed(range(1, n+1)):
        
        while nidx < n and noodles[nidx][0] == time:
            heappush(task_queue, -noodles[nidx][1])
            nidx += 1

        if task_queue:
            reward = -heappop(task_queue)
            total_reward += reward

    return total_reward

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    noodles = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(n, noodles))
