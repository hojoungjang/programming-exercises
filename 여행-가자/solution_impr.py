"""
백준
여행 가자
https://www.acmicpc.net/problem/1976

처음 풀이 방식은 BFS 를 이용해서 풀었다. 단순 BFS 를 (시작 점에서 도착점까지 방문) 
좀 응용해서 풀이했다.

주어진 여행 일정안에 있는 점들을 모두 순서대로 방문 가능한지 확인 해야하기 때문에
연속되는 두개의 정점 쌍을 시작과 도착 지점으로 생각하고 BFS를 진행했다.
이렇게 하면 좀 비효율적이기 하지만 문제의 입력 제한사항을 통과하기에는 충분하다.
O((V+E) * m)
* V 는 노드/정점의 개수
* E 는 간선의 개수
* m 은 여행 정점들의 개수

다른분들의 풀이가 훨씬 속도가 빨라서 참고하였더니 union find 알고리즘으로
풀이를 하였다. 유니언 파인드는 주어진 그래프 데이터에서 연결된수 있는 정점들을
하나의 그룹으로 간주할 수 있게 도와준다.

예를 들어 A, B, C, D, E 가 있는 그래프에서 A, B, C 가 서로 연결되어 있고
D, E 가 서로 연결되어있다면 A, B, C 를 그룹 1 그리고 D, E 를 그룹 2 라고
구분짓는 자료구조를 만들어 낼 수 있다. (당연한 소리이지만 이때 그룹 1 에 있는 
어떤 정점도 그룹 2에 있는 어떤 정점과 연결되어 있지않다.)

이 문제는 결국 여행 계획안에 있는 주어진 정점들이 서로 연결되어있는지를 물어보고 있기
때문에 유니언 파인드로 그래프 안에 정점들의 연결상태를 알아내고 그 상태를 통해
여행 계획안에 있는 정점들이 연결되어있는지 파악하면 된다.

시간 복잡도:
1. 유니언 파인드를 이용해 연결상태 자료구조를 만드는데 O(V+E)
* V 는 노드/정점의 개수
* E 는 간선의 개수

find() 와 union() 은 amortized constant time 이다. 최악의 경우
선형 시간복잡도이고 최선일때는 상수 시간복잡도 이다. 따라서 평균적으로는 상수
시간복잡도이다.

2. 여행 정점들의 연결 상태 확인 O(m)
* m 은 여행 정점들의 개수

여기서도 find() 가 amortized constant time 이기 때문에
전체 시간복잡도는 선형 시간복잡도로 표현 할 수 있다.

따라서 두 부분을 더 한 O(V + E + m)  시간 복잡도를 완성 할 수 있겠다.
"""
import sys

def solution(n, graph, travel_plan):
    def find(node):
        # find root
        root = node
        while root != connectivity[root]:
            root = connectivity[root]

        # update root
        ptr = node
        while root != connectivity[ptr]:
            ptr, connectivity[ptr] = connectivity[ptr], root

        return root

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        connectivity[root2] = root1

    # Start of solution function
    connectivity = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                union(i, j)

    for i in range(len(travel_plan) - 1):
        start = travel_plan[i] - 1
        end = travel_plan[i+1] - 1
        if find(start) != find(end):
            return False
    return True
    

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    graph = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    travel_plan = [int(val) for val in sys.stdin.readline().strip().split(" ")]

    if solution(n, graph, travel_plan):
        print("YES")
    else:
        print("NO")
