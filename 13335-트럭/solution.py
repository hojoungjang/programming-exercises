"""
백준
트럭
https://www.acmicpc.net/problem/13335
"""

import sys
from collections import deque

def solution(trucks, bridge_len, max_weight):
    truck_idx = 0
    weight = 0
    bridge = deque()
    time = 0

    # loop through trucks
    while truck_idx < len(trucks):
        time += 1

        # off load
        if bridge and time - bridge[0][1] >= bridge_len:
            offload_weight, _ = bridge.popleft()
            weight -= offload_weight

        # load
        if weight + trucks[truck_idx] <= max_weight:
            bridge.append((trucks[truck_idx], time))
            weight += trucks[truck_idx]
            truck_idx += 1

    if bridge:
        _, last_truck_load_time = bridge.pop()
        time = last_truck_load_time + bridge_len
    
    return time


if __name__ == "__main__":
    """
    n: 트럭의 개수
    w: 다리의 길이
    l: 최대 하중
    """
    n, w, l = map(int, sys.stdin.readline().strip().split(" "))
    trucks = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    print(solution(trucks, w, l))
