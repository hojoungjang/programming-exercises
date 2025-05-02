"""
백준
우체국
https://www.acmicpc.net/problem/2141
"""
import sys

def solution(towns):
    towns.sort()
    lo = towns[0][0]
    hi = towns[-1][0]
    
    closest = float("inf")
    closest_cost = float("inf")

    while lo <= hi:
        mid = (lo + hi) // 2

        left_people = 0
        right_people = 0
        cost = 0

        for pos, people in towns:
            if pos == mid:
                continue

            if pos < mid:
                left_people += people
            elif pos > mid:
                right_people += people
            cost += abs(mid - pos) * people

        if cost < closest_cost:
            closest_cost = cost
            closest = mid
        elif cost == closest_cost:
            closest = min(closest, mid)

        if left_people >= right_people:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return closest

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    towns = [tuple(int(val) for val in sys.stdin.readline().strip().split(" ")) for _ in range(n)]
    print(solution(towns))
