"""
백준
연료 채우기
https://www.acmicpc.net/problem/1826
"""
import sys
from heapq import heappush, heappop

def solution(target, gas, gas_stations):
    pos = 0
    stations = []
    visited_cnt = 0

    while pos < target:
        if not gas:
            if not stations:
                return -1
            new_gas = heappop(stations) * -1
            gas += new_gas
            visited_cnt += 1

        gas -= 1
        pos += 1

        if pos in gas_stations:
            heappush(stations, -gas_stations[pos])
    
    return visited_cnt
            

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    gas_stations = {}
    for _ in range(n):
        idx, amt = map(int, sys.stdin.readline().strip().split(" "))
        gas_stations[idx] = amt
    target, gas = map(int, sys.stdin.readline().strip().split(" "))
    print(solution(target, gas, gas_stations))
