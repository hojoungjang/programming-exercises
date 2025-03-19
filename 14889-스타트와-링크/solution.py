"""
백준
스타트와 링크
https://www.acmicpc.net/problem/14889
"""

import sys
from itertools import combinations

def solution(n, points):
    min_diff = float("inf")

    for team_start in combinations(range(n), n // 2):
        
        score_start = 0
        for i in team_start:
            for j in team_start:
                score_start += points[i][j]
        
        team_link = [num for num in range(n) if num not in team_start]    # O(n^2)
        score_link = 0
        for i in team_link:
            for j in team_link:
                score_link += points[i][j]
        
        min_diff = min(min_diff, abs(score_start - score_link))
    
    return min_diff


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    points = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(n, points))
