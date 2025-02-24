"""
프로그래머스
지게차와 크레인
https://school.programmers.co.kr/learn/courses/30/lessons/388353

문제의 조건이 간단한줄 알았으나 그건 제대로 이해를 못 해서였다.
강제로 화물을 옮길수 있는 타입의 요청이 아니면 외부와 연결된 화물만
빼낼 수 있는데 이때 단순히 한면이 인덱스 범위 밖 또는 이미 그 자리에
있던 화물이 나간 경우로 처음에 고려하였다. 잘 못 됬다는걸 알고 이번에
위, 아래, 오른쪽 왼쪽 직선 방향으로 각각 쭉 움직였을때 밖이랑 연결이
되어있는지 확인했지만 이또한 부정확하다. 가장 알맞게는 DFS 를 해서 
밖으로 확인하는 방법이었는데 사실 문제에서 이부분을 좀더 효율적으로 찾을수
없을까라는 의문이 들만큼 이렇게 하면 시간복잡도가 많이 커진다.

전체적으로 문제의 설명이나 구현은 크게 어렵지 않은 문제였다.
"""

import sys

sys.setrecursionlimit(2500)

EMPTY = "."

def solution(storage, requests):
    
    def dfs(r, c, visited):
        if r < 0 or r >= n or c < 0 or c >= m:
            return True
        
        if storage_status[r][c] != EMPTY:
            return False
        
        visited.add((r,c))
        
        result = False
        for offset in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_r = r+offset[0]
            new_c = c+offset[1]
            if (new_r, new_c) in visited:
                continue
            result |= dfs(new_r, new_c, visited)
        return result
    
    def can_remove(r, c):
        visited = set([(r, c)])
        for offset in [(1,0), (-1,0), (0,1), (0,-1)]:
            r_offset, c_offset = offset
            if dfs(r + r_offset, c + c_offset, visited):
                return True
        return False
    
    n = len(storage)
    m = len(storage[0])
    storage_status = [[c for c in r] for r in storage]
    left = n * m
    
    for request in requests:
        force = len(request) == 2
        target = request[0]
        remove_queue = []
        
        for r in range(n):
            for c in range(m):
                if storage_status[r][c] == target and (force or can_remove(r, c)):
                    remove_queue.append((r, c))
        
        for r, c in remove_queue:
            storage_status[r][c] = EMPTY
            
        left -= len(remove_queue)
    
    return left
    