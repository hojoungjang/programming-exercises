import sys

def solution(budget: int, requests: int) -> int:
    if sum(requests) <= budget:
        return max(requests)
    
    rem = budget
    max_alloc = budget // len(requests)
    for i, req in enumerate(sorted(requests), 1):
        rem -= req
        alloc = rem // (len(requests) - i)
        if alloc < req:
            break
        max_alloc = alloc
    return max_alloc


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    requests = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    budget = int(sys.stdin.readline().strip())
    print(solution(budget, requests))
