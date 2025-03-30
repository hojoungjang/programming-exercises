import sys
from heapq import heapify, heappop, heappush

def solution(cards, m):
    heapify(cards)

    for _ in range(m):
        card1 = heappop(cards)
        card2 = heappop(cards)
        new_card = card1 + card2
        heappush(cards, new_card)
        heappush(cards, new_card)

    return sum(cards)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    cards = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    print(solution(cards, m))