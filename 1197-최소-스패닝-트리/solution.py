"""
https://www.acmicpc.net/problem/1197
"""
import sys
from heapq import heappush, heappop

def solution(v, graph):
    edges = [(0, 1)]
    visited = set()
    total_weights = 0

    while len(visited) < v:
        while edges and edges[0][1] in visited:
            heappop(edges)

        weight, node = heappop(edges)    
        visited.add(node)
        total_weights += weight

        for edge in graph[node]:
            next_node, next_weight = edge
            if next_node in visited:
                continue
            heappush(edges, (next_weight, next_node))

    return total_weights


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().strip().split(" "))
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().strip().split(" "))
        graph[u].append((v, w))
        graph[v].append((u, w))
    print(solution(V, graph))
