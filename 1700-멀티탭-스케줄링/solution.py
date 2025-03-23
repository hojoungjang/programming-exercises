"""
백준
멀티탭 스케줄링
https://www.acmicpc.net/problem/1700
"""

import sys

def solution(items, cap):
    used = set()
    unplug_cnt = 0

    for i, item in enumerate(items):
        # free space on the outlet
        if len(used) < cap:
            used.add(item)
            continue

        # item already plugged
        if item in used:
            continue
        
        # evict one item and plug
        evict_item = -1
        evict_item_idx = -1

        for used_item in used:
            next_idx = -1

            for j, next_item in enumerate(items[i:], i):
                if used_item == next_item:
                    next_idx = j
                    break

            if next_idx == -1:
                evict_item = used_item
                break

            if next_idx > evict_item_idx:
                evict_item = used_item
                evict_item_idx = next_idx
        
        used.discard(evict_item)
        used.add(item)
        unplug_cnt += 1
    
    return unplug_cnt


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    items = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    print(solution(items, n))
