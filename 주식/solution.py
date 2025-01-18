"""
백준
주식
https://www.acmicpc.net/problem/11501

최대 수익을 내기 위해서는 각 주식가격에 대해 그 가격 이후에 나오는, 즉
배열의 오른쪽, 더 큰 인덱스, 에 나오는 더 큰 가격 중 제일 큰 가격과의
차를 구해서 합산한다.

가장 간단하게는 각 가격을 다른 가격과 비교하는 O(n^2) 방법도 있지만
가격 배열을 거꾸로 순회하면서 제일 큰 가격을 저장하고 그 가격보다 작은 가격을
마주하면 차를 구해서 더하는 법도 있다. 이럴 경우 O(n) 시간복잡도로 코드를
작성 할 수 있다.
"""

import sys

def solution(prices):
    profit = 0
    max_price = float("-inf")
    for price in prices[::-1]:
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price
    return profit

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        prices = list(map(int, sys.stdin.readline().strip().split(" ")))
        print(solution(prices))
