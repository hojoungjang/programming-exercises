import sys
from heapq import heappush, heappop

def solution(fields, c):
    visited = set()
    pq = [(0, 0)]
    total = 0

    while pq:
        cost, i = heappop(pq)

        if i in visited:
            continue

        total += cost
        visited.add(i)

        if len(visited) == len(fields):
            break

        for j in range(len(fields)):
            if j in visited:
                continue
            new_cost = (fields[i][0] - fields[j][0]) ** 2 + (fields[i][1] - fields[j][1]) ** 2
            if new_cost < c:
                continue
            heappush(pq, (new_cost, j))
    
    return total if len(visited) == len(fields) else -1


if __name__ == "__main__":
    n, c = map(int, sys.stdin.readline().strip().split(" "))
    fields = [[int(num) for num in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(fields, c))
