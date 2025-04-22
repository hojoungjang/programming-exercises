"""
백준
케빈-베이컨의-6단계-법칙
https://www.acmicpc.net/problem/1389
"""

import sys
from collections import deque

def solution(n, graph):

    def bfs(start_user):
        queue = deque([start_user, None])
        visited = set([start_user])
        level = 0
        score = 0

        while queue:
            if queue[0] is None:
                queue.popleft()
                if queue:
                    queue.append(None)
                level += 1
                continue

            user = queue.popleft()
            score += level

            for next_user in graph[user]:
                if next_user in visited:
                    continue
                queue.append(next_user)
                visited.add(next_user)
        
        return score

    #################################
    min_score = float("inf")
    min_score_user = 0
    for user in range(1,n+1):
        score = bfs(user)
        if score < min_score:
            min_score = score
            min_score_user = user
    return min_score_user

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        graph[u].append(v)
        graph[v].append(u)
    print(solution(n, graph))