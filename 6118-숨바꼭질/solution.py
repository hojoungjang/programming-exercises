import sys
from collections import deque

BARN_ID = 0
BARN_DIST = 1
BARN_DIST_COUNT = 2

def solution(graph):
    start = 1
    queue = deque([start, None])
    visited = set([start])
    dist = 0

    # [<헛간 번호>, <헛간 거리>, <같은 거리 헛간 개수>]
    hiding_barn = [-1, -1, 0]

    while queue:
        if queue[0] is None:
            queue.popleft()
            if queue:
                queue.append(None)
            dist += 1
            continue

        barn_id = queue.popleft()
        if dist == hiding_barn[BARN_DIST]:
            hiding_barn[BARN_DIST_COUNT] += 1
            hiding_barn[BARN_ID] = min(hiding_barn[BARN_ID], barn_id)
        else:
            hiding_barn = [barn_id, dist, 1]

        for next_barn_id in graph[barn_id]:
            if next_barn_id in visited:
                continue
            visited.add(next_barn_id)
            queue.append(next_barn_id)
    
    return hiding_barn
    

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        graph[u].append(v)
        graph[v].append(u)
    barn_id, barn_dist, barn_count = solution(graph)
    print(f"{barn_id} {barn_dist} {barn_count}")