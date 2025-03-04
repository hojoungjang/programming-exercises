"""
백준
회장뽑기
https://www.acmicpc.net/problem/2660

BFS 를 이용하여 각 시작점에서 다른 정점을 모두 방문을 완료했을때
걸린 최대 간선의 개수가 그 시작점 (사람) 의 점수가 된다.
이렇게 해서 각 시작점에 대해 점수를 구하면서 회장 후보를 구한다.

모든 시작점에 대해 BFS 를 새로 돌리기 때문에 최악의 경우 O(n^3) 복잡도이다.
"""

import sys
from collections import deque

def solution(n, adj_list):
    min_score = n
    cands = []

    for person in range(1, n+1):
        queue = deque([person, None])
        visited = set([person])
        score = -1

        while queue:
            cur_person = queue.popleft()
            if cur_person is None:
                if queue:
                    queue.append(None)
                score += 1
                if score > min_score:
                    break
                continue
            
            for friend in adj_list[cur_person]:
                if friend in visited:
                    continue
                queue.append(friend)
                visited.add(friend)
        
        if score < min_score:
            min_score = score
            cands = [person]
        elif score == min_score:
            cands.append(person)
    
    return min_score, cands


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    adj_list = [[] for _ in range(n+1)]
    while True:
        u, v = map(int, sys.stdin.readline().strip().split(" "))
        if u == -1 and v == -1:
            break
        adj_list[u].append(v)
        adj_list[v].append(u)
    score, cands = solution(n, adj_list)
    print(f"{score} {len(cands)}")
    print(" ".join(str(val) for val in sorted(cands)))