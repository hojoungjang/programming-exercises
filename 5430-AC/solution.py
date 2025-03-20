"""
백준
AC
https://www.acmicpc.net/problem/5430
"""

import sys
from collections import deque

def parse_arr_str(arr_str):
    s = arr_str.lstrip("[").rstrip("]")
    if not s:
        return []
    return [int(val) for val in s.split(",")]

def to_arr_str(arr):
    arr_str = ",".join(str(num) for num in arr)
    return "[" + arr_str + "]"


def solution(fns, arr):
    direction = 1
    queue = deque(arr)

    for fn in fns:
        if fn == "R":
            direction *= -1
        elif fn == "D":
            if not queue:
                return None
            if direction == 1:
                queue.popleft()
            else:
                queue.pop()
    
    return list(queue) if direction == 1 else list(queue)[::-1]

if __name__ == "__main__":
    T  = int(sys.stdin.readline().strip())

    for _ in range(T):
        fns = sys.stdin.readline().strip()
        n = int(sys.stdin.readline().strip())
        arr = parse_arr_str(sys.stdin.readline().strip())
        ans = solution(fns, arr)
        if ans is None:
            print("error")
        else:
            print(to_arr_str(ans))
