"""
백준
주유소
https://www.acmicpc.net/problem/13305

간단하다 지나오면서 가장 작은 주유값을 저장하고 그값으로
지나가는 거리 만큼 주유한다고 가장한다.

이미 지나온 거리는 어쩔수 없이 그전에 봐왔던 기름값에서 가장
작은 값으로 주유하는것이 최선이기 때문에 순회하면서
최소값을 갱신해주면 최소경우를 찾을 수 있다.
"""
import sys

def solution(roads, prices):
    min_price = float("inf")
    total = 0
    for road, price in zip(roads, prices):
        min_price = min(min_price, price)
        total += road * min_price
    return total

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    roads = list(map(int, sys.stdin.readline().strip().split(" ")))
    prices = list(map(int, sys.stdin.readline().strip().split(" ")))
    print(solution(roads, prices))
