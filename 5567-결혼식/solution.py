"""
백준
결혼식
https://www.acmicpc.net/problem/5567
"""

import sys
from collections import deque

def solution(graph):
    sang = 1                        # 상근이 번호 항상 1
    queue = deque([sang, None])     # None 을 이용해 레벨 구분
    level = 0
    visited = set([sang])
    invitee_cnt = 0

    while queue:
        # 다음 레벨
        if queue[0] is None:
            queue.popleft()
            if queue:
                queue.append(None)
            level += 1
            if level > 2:
                break
            continue

        friend = queue.popleft()
        invitee_cnt += 1

        for next_friend in graph[friend]:
            if next_friend not in visited:
                visited.add(next_friend)
                queue.append(next_friend)

    # 상근이 빼기
    return invitee_cnt - 1

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split(" "))
        if b not in graph[a]:
            graph[a].append(b)
        if a not in graph[b]:
            graph[b].append(a)
    print(solution(graph))
