"""
백준
추월
https://www.acmicpc.net/problem/2002
"""

import sys

def solution(ins, outs):
    speeding_cars = set()
    ins_idx = 0

    for out_car_no in outs:
        if out_car_no == ins[ins_idx]:
            ins_idx += 1
            while ins_idx < len(ins) and ins[ins_idx] in speeding_cars:
                ins_idx += 1
        else:
            speeding_cars.add(out_car_no)
    
    return len(speeding_cars)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    ins = [sys.stdin.readline().strip() for _ in range(n)]
    outs = [sys.stdin.readline().strip() for _ in range(n)]
    print(solution(ins, outs))
