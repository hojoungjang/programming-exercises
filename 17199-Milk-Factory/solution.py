"""
백준
Milk Factory
https://www.acmicpc.net/problem/17199
"""
import sys

def solution(graph):
    def dfs(node):
        visited[node] = 1

        for next_node in graph[node]:
            if next_node not in visited:
                dfs(next_node)
            visited[node] += visited[next_node]

    visited = {}
    for start in range(1, len(graph)):
        if start in visited:
            continue
        dfs(start)
        if visited[start] == len(graph)-1:
            return start
    return -1

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        graph[v].append(u) # reversed edge graph
    print(solution(graph))
