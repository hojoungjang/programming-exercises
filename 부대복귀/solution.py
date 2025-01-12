"""
프로그래머스
부대복귀
https://school.programmers.co.kr/learn/courses/30/lessons/132266

처음에는 각 source 노드에서 destination 노드까지 BFS 를 하였는데, 이럴 경우
시간초과가 된다.

문제가 자연스럽게 이런 구현을 유도하는 느낌이 없지 않아 있다. 하지만 잘 생각해보면
이럴경우 겹치는 순회를 반복적으로 하게 되는걸 알아 차릴 수 있다.

그래서 뒤집어서 생각해보면 destionation 노드에서 각 노드를 방문하면 전체 그래프를
한번만 순회해서 모든 source 노드와 destination 노드의 거리를 알 수 있다.
"""
from collections import deque

def solution(n, roads, sources, destination):
    # make the graph
    graph = {i: [] for i in range(n + 1)}
    for start, end in roads:
        graph[start].append(end)
        graph[end].append(start)
        
    # start from destination and record distance to other nodes
    distances = [-1 for _ in range(n+1)]
    dist = 0
    visited = set([destination])
    queue = deque([destination, -1])
    while queue:
        cur_node = queue.popleft()
        if cur_node == -1:
            dist += 1
            if queue: queue.append(-1)
            continue

        distances[cur_node] = dist

        for next_node in graph[cur_node]:
            if next_node in visited:
                continue
            visited.add(next_node)
            queue.append(next_node)
    
    return [distances[source] for source in sources]