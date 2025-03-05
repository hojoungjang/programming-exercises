"""
백준
효율적인 해킹
https://www.acmicpc.net/problem/1325

문제의 채점기준이 파이썬 풀이에는 좀 타이트한것 같다.
간단하게 풀면 O(n^2) 이 나오는 풀이가 가능한다. 각
정점에 대해 방문 가능한 다른 정점의 개수를 세우준다.
참고로 입력받은 간선을 뒤집어야 문제에서 원하는대로
그래프를 올바른 방향으로 탐색이 가능하다.

DFS 를 이용하여 풀이하였는데 시간초과가 나서 반복적으로
정점을 방문하는 부분을 효율적으로 바꿀 수 없는지 생각을
좀 해보았지만 마땅히 떠오르지 않았고 질문 게시판을 열심히
보다가 결국 이 문제는 파이썬으로는 어쩔수 없이 BFS 와
Pypy3 제출을 통해 간신히 통과하는 수준이라는 대세의 의견을
따라 풀이를 마무리 지었다.

사실 strongly connect component 라는 방법을 통해 풀이가
가능하다고도 몇몇 의견이 있었지만 이 문제의 수준에 걸맞지 않는
풀이법이라는 의견이 있어서 일단은 나도 스킵했다. 기회가 될때
알아보면 좋겠다.
"""

import sys
from collections import deque

def solution(n, graph):

    def bfs(node):
        queue = deque([node])
        hacked = [0 for _ in range(n+1)]
        hacked[node] = 1
        cnt = 0
        while queue:
            cur_node = queue.popleft()
            cnt += 1
            for next_node in graph[cur_node]:
                if hacked[next_node]:
                    continue
                hacked[next_node] = 1
                queue.append(next_node)
        return cnt
    
    max_hack_cnt = 0
    cmps = []
    for start in range(1, n+1):
        hack_cnt = bfs(start)
        if hack_cnt > max_hack_cnt:
            cmps = [start]
            max_hack_cnt = hack_cnt
        elif hack_cnt == max_hack_cnt:
            cmps.append(start)
    return cmps


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        graph[v].append(u)
    print(" ".join(str(num) for num in solution(n, graph)))