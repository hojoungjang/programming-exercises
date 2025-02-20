"""
백준
그래프 트리 분할
https://www.acmicpc.net/problem/22954
"""
import sys

sys.setrecursionlimit(100_000)
NODE = 0
EDGE = 1

def solution(graph):

    def dfs(node):
        visited.add(node)
        tree[NODE].append(node)

        for next_node, edge_idx in graph[node]:
            if next_node in visited:
                continue
            tree[EDGE].append(edge_idx)
            dfs(next_node)

    visited = set()
    trees = []
    for i in range(1, len(graph)):
        if i in visited:
            continue
        tree = [[], []]
        dfs(i)
        trees.append(tree)
    return trees


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    graph = [[] for _ in range(n+1)]
    edges = [None for _ in range(m+1)]
    for i in range(1, m+1):
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        graph[u].append((v, i))
        graph[v].append((u, i))
        edges[i] = (u, v)

    trees = solution(graph)

    if n <= 2 or len(trees) < 0 or len(trees) > 2:
        print(-1)
        sys.exit(0)

    if len(trees) == 1:
        # trees[0][EDGE].pop()
        new_graph = [[] for _ in range(n+1)]
        for edge_idx in trees[0][EDGE]:
            u, v = edges[edge_idx]
            new_graph[u].append((v, edge_idx))
            new_graph[v].append((u, edge_idx))
        for u in range(1, n + 1):
            if len(new_graph[u]) == 1:
                v, edge_idx = new_graph[u].pop()
                new_graph[v].remove((u, edge_idx))
                break
        trees = solution(new_graph)

    if len(trees) != 2:
        print(-1)
        sys.exit(0)

    # print node counts
    tree1_node_cnt = len(trees[0][NODE])
    tree2_node_cnt = len(trees[1][NODE])

    if tree1_node_cnt == tree2_node_cnt:
        print(-1)
        sys.exit(0)

    print(f"{tree1_node_cnt} {tree2_node_cnt}")

    # print tree 1 nodes
    print(" ".join(str(num) for num in trees[0][NODE]))

    # print tree 1 edges
    print(" ".join(str(num) for num in trees[0][EDGE]))

    # print tree 2 nodes
    print(" ".join(str(num) for num in trees[1][NODE]))

    # print tree 2 edges
    print(" ".join(str(num) for num in trees[1][EDGE]))
