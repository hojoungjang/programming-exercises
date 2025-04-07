"""
백준
RGB거리
https://www.acmicpc.net/problem/1149
"""

import sys

R = 0
G = 1
B = 2

def solution(paint_costs):
    costs = [0, 0, 0]

    for i in range(len(paint_costs)):
        new_costs = [val for val in paint_costs[i]]
        new_costs[R] += min(costs[G], costs[B])
        new_costs[G] += min(costs[R], costs[B])
        new_costs[B] += min(costs[R], costs[G])
        costs = new_costs
    
    return min(costs)
        

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    paint_costs = [
        [int(val) for val in sys.stdin.readline().strip().split(" ")]
        for _ in range(n)
    ]
    print(solution(paint_costs))