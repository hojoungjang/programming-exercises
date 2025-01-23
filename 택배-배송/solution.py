"""
백준
택배 배송
https://www.acmicpc.net/problem/5972

두개의 그래프 노드의 최단거리를 구하는 문제이다.
다익스트라 알고리즘으로 풀 수 있을거라고 생각했다.
문득 다익스트라를 안쓰고 그냥 평범한 그래프 탐색 알고리즘 (DFS, BFS)
으로 풀 수 있을까도 고민해봤다.

다익스트라는 아무래도 어느정도 시간을 사용해 길들여야지 실제
코딩테스트 환경에서 사용 가능하지 않을까 싶어서 그런 생각을 해보았다.

근데 아무래도 간선에 가중치 (weight/cost) 가 붙는 경우 최단거리
계산은 다익스트라식의 알고리즘을 사용하는게 가장 적합한것같다.
그리고 한가지 주의할 점은 다익스트라는 그리디식 알고리즘이여서 
간선의 가중치가 음수일 경우를 고려하지 못한다. 그럴때는 다익스트라의 대표적인 대안인
벨만포드 알고리즘을 사용한다. 벨만포드는 모든 간선을 순회하며 거리를 업데이트하는데
이때 최대 시작정점을 제외한 정점의 개수 만큼 반복하게 되기 때문에 다익스트라 보다는 좀 더 시간복잡도가
크다.

어쨋든 다익스트라의 핵심은 priority queue 를 이용해서 현재 상황에서 방문할 수 있는
가장 가까운 정점을 선택해 그래프를 탐색해 나갑니다.
풀이를 할때 기억을 더듬으면서 해서 중간중간 많이 버벅거렸다. 그리고 몇가지 디테일은
실제 정석 알고리즘하고 살짝 다르게 작성이되었다.
"""

import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush

def solution(graph, start, end):
    pqueue = [(cost, node) for node, cost in graph[start].items()]
    heapify(pqueue)
    visited = set([start])

    while pqueue:
        cost, node = heappop(pqueue)
        visited.add(node)
        if node == end:
            return cost

        for new_node, new_cost in graph[node].items():
            if new_node in visited:
                continue
            heappush(pqueue, (cost + new_cost, new_node))
    
    return -1


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    graph = defaultdict(dict)

    for _ in range(m):
        node1, node2, cost = map(int, sys.stdin.readline().strip().split(" "))
        if node2 in graph[node1]:
            graph[node1][node2] = min(graph[node1][node2], cost)
            graph[node2][node1] = min(graph[node2][node1], cost)
        else:
            graph[node1][node2] = cost
            graph[node2][node1] = cost

    print(solution(graph, 1, n))
