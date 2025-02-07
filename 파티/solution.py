"""
백준
파티
https://www.acmicpc.net/problem/1238

다익스트라 알고리즘을 활용할 수 있는 형태의 입력 값들이다.
* 정점들과 정점들 사이가 간선으로 이어져 있고 간선마다 양수의 가중치가 주어진다

(문제에서는 가중치가 시간 값이 되기때문에 최단거리 대신 최단시간이라는 표현으로 대체하겠다.)
처음에는 각 정점에서 목적지 까지의 최단시간과 목적지에서 정점까지의 최단시간을
구해서 최대 욍복시간을 구했다. (문제에서 간선은 방향이 정해져있기 때문에 가는길과 돌아오는길이 다를수 있다.)
이렇게 했을 경우, 각 정점마다 다익스트라 알고리즘을 두번씩 사용하게 된다.

최적화를 하기 위해서 살펴보니 반복적으로 계산되는 부분이 보였다. 돌아오는길은 출발지가
항상 파티가 있는 정점이기 때문에 그 정점에서 다른 정점까지의 최단시간을 한번만 구하고 값들을 
재사용하면 된다.

하지만 이렇게해도 전체적인 big O 시간 복잡도는 변하지 않는다. 고민을 해봐도 생각이 나지 않아서
풀이법을 참고해보았더니, 간선의 방향을 뒤집고 원래 목적지 (파티를 하는 정점) 을 출발지로 두고
다른 정점들과의 최단시간을 구하면 각각의 정점에서 시작하여 목적지 정점까지 가는 최단시간이 되는 
마법이 있다. 따라서 최적화를 하면 다익스트라 알고리즘을 총 2번만 사용하여 정답을 찾을 수 있다.

다익스트라 알고리즘은 대략 O((v + e)log(v)) 이다.
* v 정점 개수
* e 간선 개수

따라서 입력의 크기를 보면 
v: (1 ≤ v ≤ 1,000)
e: (1 ≤ e ≤ 10,000)

v * (v+e) * log(v) 는 거의 10^8 정도여서 보통 딱 통과할 수준의 시간복잡도이거나 아니면
시간초과가 되기 쉽다. 반면 최적화한 솔루션은 일반 다익스트라의 시간복잡도를 가진다. O((v+e)log(v))
"""

import sys
from heapq import heappop, heappush

def get_all_min_cost(graph, start):
    pqueue = [(0, start)]
    costs = [float("inf") for _ in range(len(graph))]
    costs[start] = 0

    while pqueue:
        # print(pqueue)
        cost, village = heappop(pqueue)

        for next_village in graph[village]:
            next_cost = cost + graph[village][next_village]
            if next_cost >= costs[next_village]:
                continue

            costs[next_village] = next_cost
            heappush(pqueue, (next_cost, next_village))
    return costs

def solution(graph, reversed_graph, n, target):
    return_costs = get_all_min_cost(graph, target)
    depart_costs = get_all_min_cost(reversed_graph, target)
    return max(return_costs[i] + depart_costs[i] for i in range(1, n+1))


if __name__ == "__main__":
    """
    n 학생/마을 수
    m 간선 수 (단방향)
    x 파티 마을
    """
    n, m, x = map(int, sys.stdin.readline().strip().split(" "))
    graph = [{} for _ in range(n+1)]
    reversed_graph = [{} for _ in range(n+1)]
    for _ in range(m):
        start, end, cost = map(int, sys.stdin.readline().strip().split(" "))
        graph[start][end] = cost
        reversed_graph[end][start] = cost
    
    print(solution(graph, reversed_graph, n, target=x))

