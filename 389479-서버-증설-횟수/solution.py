"""
프로그래머스
서버 증설 횟수
https://school.programmers.co.kr/learn/courses/30/lessons/389479
"""

from collections import deque

def solution(players, m, k):
    queue = deque()
    cnt = 0
    
    for time, player in enumerate(players):
        while queue and queue[0] <= time:
            queue.popleft()
        
        req_servers = player // m
        
        while req_servers > (servers := len(queue)):
            queue.append(time + k)
            cnt += 1
        
    return cnt
