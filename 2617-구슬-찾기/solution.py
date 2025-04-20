"""
백준
구슬 찾기
https://www.acmicpc.net/problem/2617


단방향 그래프에서 각 노드마다 방문 가능한 다른 노드의 개수를 구하는것이다.
각 노드마다 DFS/BFS 를 해주는 것은 비효율적일 것이다라는 생각을 하게 되었고
방문하는 노드 마다 방문 가능한 노드의 개수를 저장해서 추후 같은 노드를 방문하게
될 경우, 저장된 값을 사용하면 되겠다고 생각했다.

하지만 이 방법은 중복을 처리하지 못한다. 예를 들어 3에서 방문 가능한 노드가 1, 2 이고
2 에서 방문 가능한 노드가 1 일때 아래와 같은 그래프를 만들수 있다.

3 -> 2
|    |
v    |
1 <---

여기서 3에서 방문 가능한 노드를 찾기 위해 1 과 2 로 가는 간선을 처리할때 단순히 저장된
개수를 이용하게 되면, 노드 1이 두번 세어질 수 있다.

따라서 이문제는 단순히 방문 가능한 노드의 개수를 세는 것이 아니라, 방문 가능한 유니크한 노드의
개수를 알맞게 세어주어야 한다.
"""

import sys

def solution(n, greater_graph, smaller_graph):
    def dfs(graph, num, visited):
        visited.add(num)
        count = 0
        for next_num in graph[num]:
            if next_num in visited:
                continue
            count += dfs(graph, next_num, visited) + 1
        return count

    # greater_counts = [0 for _ in range(n+1)]
    # smaller_counts = [0 for _ in range(n+1)]

    half = (n+1) // 2
    invalid_mid_count = 0

    for num in range(1, n+1):
        greater_count = dfs(greater_graph, num, set())
        smaller_count = dfs(smaller_graph, num, set())
        if greater_count >= half or smaller_count >= half:
            invalid_mid_count += 1
    return invalid_mid_count
    

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    greater_graph = [[] for _ in range(n+1)]
    smaller_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        g, s = map(int, sys.stdin.readline().strip().split(" "))
        greater_graph[s].append(g)
        smaller_graph[g].append(s)
    print(solution(n, greater_graph, smaller_graph))