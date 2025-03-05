"""
백준
이분 그래프
https://www.acmicpc.net/problem/1707

그래프를 BFS로 탐색하며 각 노드와 인접한 노드를 두개의 집합으로 나누어 넣는다.
이때 set 자료구조를 사용한다. 만약 인접 노드를 담기 전에 이미 현재 노드랑 같은
set 에 담겨 있다면 이분 그래프의 성질을 만족할 수 없는 경우인 것이다.

입력 로직을 제외한
시간 복잡도: O(E)
* E 간선의 개수

공간 복잡도: O(V)
* 정점의 개수
"""

import sys
from collections import deque

def solution(graph):
    visited = set()
    for node in range(1, len(graph)):
        if node in visited:
            continue

        sets = [set([node]), set()]
        queue = deque([(node, 0)])

        while queue:
            cur_node, set_idx = queue.popleft()
            visited.add(cur_node)

            next_set_idx = (set_idx + 1) % 2
            for next_node in graph[cur_node]:
                if next_node in sets[next_set_idx]:
                    continue
                if next_node in sets[set_idx]:
                    return False
                sets[next_set_idx].add(next_node)
                queue.append((next_node, next_set_idx))
    
    return True
                

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        v, e = map(int, sys.stdin.readline().strip().split(" "))
        graph = [[] for _ in range(v+1)]
        for _ in range(e):
            u, v = map(int, sys.stdin.readline().strip().split(" "))
            graph[u].append(v)
            graph[v].append(u)
        if solution(graph):
            print("YES")
        else:
            print("NO")
