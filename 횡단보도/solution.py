"""
백준
횡단보도
https://www.acmicpc.net/problem/24042

각 지점에서 가장 빨리 건널수 있는 상황을 고려하게 되는
시나리오를 생각했을때 다익스트라 알고리즘이 적용 가능하다.
결국 한 지점에서 목표지점까지 최단 시간안에 도착하는게
목표이기 때문에 우선순위 큐를 이용해 항상 가장 빠른 시점에
도달할 수 있는 정점을 순차적으로 방문해서 목표지점까지 도착하면
그게 답이 된다. 

풀이와 구현은 둘째치고 계속해서 시간 초과가 났는데 입력을
받고 그래프를 초기화해주는게 문제였다. 

1차적으로는 n * m 시간복잡도를 이용해서 그래프 자료구조를 
초기화하고 있었던것이었다. 너무나 치명적인데 빨리 알아차리지 못해서
아쉬웠다.

Pypy 를 이용해서 간신히 통과했지만 여전히 솔루션 코드가 왜 느린지 
잘 이해가 가지 않아서 다른 분들의 풀이를 좀 참고했다.
코드를 참고하기도 하고 내것을 변경해본 결과 가급적 리스트로 표현할수
있으면 딕셔너리보다는 리스트를 이용하는게 효율면에 좋다. 일단
딕셔너리는 리스트보다 약간의 오보헤드가 생길 수 밖에 없는것같다. 
아마 내부적으로는 딕셔너리 자체가 리스트로 구현이 되어있을것이다.
내 코드가 엄청 느렸던 이유는 아마 딕셔너리를 심지어 중첩시켜서
그래프를 표현했기 때문이 아닐까 싶다. 따라서 튜플을 담은 리스트로
그래프를 표현했을때랑 확연하게 속도면에서 차이가 났다.
"""

import sys
from heapq import heappush, heappop

def solution(graph, period, n):
    pqueue = [(0, 1)]
    min_time_cost = [float("inf") for _ in range(n + 1)]
    min_time_cost[1] = 0

    while pqueue:
        time_cost, node = heappop(pqueue)

        if node == n:
            break

        if time_cost > min_time_cost[node]:
            continue

        for next_node, next_time_cost in graph[node]:
            cycle_cnt = time_cost // period
            if (time_cost % period) > next_time_cost:
                cycle_cnt += 1
            new_time_cost = period * cycle_cnt + next_time_cost + 1
                
            if new_time_cost >= min_time_cost[next_node]:
                continue
            
            min_time_cost[next_node] = new_time_cost
            heappush(pqueue, (new_time_cost, next_node))
    
    return min_time_cost[n]

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        graph[u].append((v, i))
        graph[v].append((u, i))
    
    print(solution(graph, m, n))
