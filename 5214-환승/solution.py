"""
백준
환승
https://www.acmicpc.net/problem/5214
"""

import sys
from collections import deque

def solution(station_tube_map, tubes, end):
    start = 1
    queue = deque([start, None])
    visited = set([start])
    tube_visited = set()
    station_count = 1

    while queue:
        if queue[0] is None:
            queue.popleft()
            if queue:
                queue.append(None)
            station_count += 1
            continue

        station = queue.popleft()
        if station == end:
            return station_count
        
        for tube_idx in station_tube_map[station]:
            if tube_idx in tube_visited:
                continue
            tube_visited.add(tube_idx)
            for next_station in tubes[tube_idx]:
                if next_station in visited:
                    continue
                visited.add(next_station)
                queue.append(next_station)
        
    return -1


if __name__ == "__main__":
    """
    n: 역의 개수
    k: 하이퍼튜브가 연결하는 역의 개수
    m: 하이퍼튜브의 개수

    [0] 1,2,3
    [1] 1 4 5

    1: [0, 1]
    2: [0]
    3: [0]
    4: [1]
    5: [1, 3]
    6: [2,3,4]
    7: [2,3]
    """
    n, k, m = map(int, sys.stdin.readline().strip().split(" "))
    station_tube_map = [[] for _ in range(n+1)]
    tubes = []
    for tube_idx in range(m):
        tube = [int(val) for val in sys.stdin.readline().strip().split(" ")]
        tubes.append(tube)
        for station in tube:
            station_tube_map[station].append(tube_idx)

    print(solution(station_tube_map, tubes, n))
