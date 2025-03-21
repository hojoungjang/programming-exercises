"""
백준
택배
https://www.acmicpc.net/problem/8980
"""
import sys

def solution(ntowns, max_capacity, boxes):
    boxes.sort()
    loaded = [0 for _ in range(ntowns + 1)]
    delivered = 0
    box_idx = 0
    
    for pos in range(1, ntowns + 1):
        delivered += loaded[pos]
        loaded[pos] = 0
        
        while box_idx < len(boxes) and boxes[box_idx][0] == pos:
            s, e, qty = boxes[box_idx]
            loaded[e] += qty
            box_idx += 1
        
        new_loaded = [0 for _ in range(ntowns + 1)]
        capacity = 0
        for idx in range(pos + 1, ntowns + 1):
            qty = min(loaded[idx], max_capacity - capacity)
            new_loaded[idx] = qty
            capacity += qty
            if capacity == max_capacity:
                break

        loaded = new_loaded

    return delivered


if __name__ == "__main__":
    """
    n : number of towns
    c : capacity of the truck
    m : number of boxes
    """
    n, c = map(int, sys.stdin.readline().strip().split(" "))
    m = int(sys.stdin.readline().strip())
    boxes = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(m)]
    print(solution(n, c, boxes))
