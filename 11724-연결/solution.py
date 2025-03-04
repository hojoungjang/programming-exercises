"""
연결 요소의 개수
https://www.acmicpc.net/problem/11724

DFS, BFS, Union-find (Disjoint set) 다 가능하다.
DFS, BFS 는 익숙해서 패스해보고 유니온파인드 구현을 좀 살펴보고 싶다.

파인드와 유니언을 잘 구현해야 하는데... 일단 파인드는 보통 간단하게 재귀로
구현한다. 입력 노드부터 시작해서 최상위 노드 즉 노드의 값이랑 부모노드 값이랑
같을 때까지 재귀하며 올라간다. 이렇게 하면 경로 압축을 해줄 수 있다. 

가장 큰 실수를 한게 유니온에서 최상위 부모의 부모값을 바꿔줘야하는데
입력받은 노드의 부모 값을 바꿔서 제대로 그룹핑이 되지 않았다.
"""

import sys

class UnionFind:
    def __init__(self, n):
        self._parents = [num for num in range(n+1)]

    def get_connected_components(self):
        uniques = set()
        for i in range(1, len(self._parents)):
            uniques.add(self.find(i))
        return len(uniques)

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            return
        self._parents[parent2] = parent1

    def find(self, node):
        if node != self._parents[node]:
            self._parents[node] = self.find(self._parents[node])
        return self._parents[node]

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    uf = UnionFind(n)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        uf.union(u, v)
    print(uf.get_connected_components())
