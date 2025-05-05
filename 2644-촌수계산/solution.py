"""
백준
촌수계산
https://www.acmicpc.net/problem/2644
"""

import sys
from collections import deque

def solution(graph, start, end):
    queue = deque([start, None])
    visited = set([start])
    level = 0

    while queue:
        if queue[0] is None:
            queue.popleft()
            if queue: queue.append(None)
            level += 1
            continue

        node = queue.popleft()
        if node == end:
            return level
        
        for next_node in graph[node]:
            if next_node in visited:
                continue

            visited.add(next_node)
            queue.append(next_node)

    return -1


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    start, end = map(int, sys.stdin.readline().strip().split(" "))
    m = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        graph[u].append(v)
        graph[v].append(u)

    print(solution(graph, start, end))
