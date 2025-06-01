"""
백준
저울
https://www.acmicpc.net/problem/10159
"""
import sys

def solution(graph):

    def _solution(node):
        visited.add(node)

        for next_node in graph[node]:
            counts[node].add(next_node)
            
            if next_node not in visited:
                _solution(next_node)
            
            for val in counts[next_node]:
                counts[node].add(val)
            
    visited = set()
    counts = [set() for _ in range(len(graph))]
    for i in range(1, len(graph)):
        if i in visited:
            continue
        _solution(i)
    return counts


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())

    graph = [[] for _ in range(n+1)]
    inv_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        graph[u].append(v)
        inv_graph[v].append(u)

    lts = solution(graph)
    gts = solution(inv_graph)

    for i in range(1, n+1):
        print(n - 1 - len(lts[i].union(gts[i])))
