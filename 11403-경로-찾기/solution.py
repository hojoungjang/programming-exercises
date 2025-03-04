"""
백준
경로 찾기
https://www.acmicpc.net/problem/11403

DFS 로 간단하게 풀수 있다. 이떄 방향 그래프 (directed graph) 이기 때문에
아마 유니온 파인드는 적용할 수 없을 것 같다. 각 노드를 시작점으로 잡는 경우에 
대해서 DFS 를 이용하여 탐색하며 방문하는 노드를 마킹을 해주면 답을 완성할 수 있다.

각 노드는 최대 n-1 개의 간선을 가질수 있기 때문에 한번 DFS 할때 최악의 경우
O(n^2) 시간복잡도가 요구되고 이걸 각 노드를 시작점으로 잡는 만큼 반복하기 때문에
알고리즘의 총 시간복잡도는 O(n^3) 이 된다.
"""

import sys

def solution(n, adj_matrix):
    
    def dfs(node):
        for next_node, connected in enumerate(adj_matrix[node]):
            if not connected or visited[start_node][next_node] == 1:
                continue
            visited[start_node][next_node] = 1
            dfs(next_node)

    visited = [[0 for _ in range(n)] for _ in range(n)]    
    for start_node in range(n):
        dfs(start_node)
    return visited

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    adj_matrix = [[int(num) for num in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    visited = solution(n, adj_matrix)
    for r in visited:
        print(" ".join(str(val) for val in r))