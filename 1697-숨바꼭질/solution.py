import sys
from collections import deque

MAX_NUM = 100_000

def solution(start, target):
    queue = deque([start, None])
    visited = set()
    visited.add(start)
    total_moves = 0

    while queue:
        if queue[0] is None:
            queue.popleft()
            total_moves += 1
            if queue:
                queue.append(None)
            continue

        num = queue.popleft()
        if num == target:
            break

        if (one_less := num - 1) >= 0 and one_less not in visited:
            queue.append(one_less)
            visited.add(one_less)
        if (one_more := num + 1) not in visited:
            queue.append(one_more)
            visited.add(one_more)
        if (doubled := num * 2) not in visited and doubled <= MAX_NUM:
            queue.append(doubled)
            visited.add(doubled)

    return total_moves

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    print(solution(n, k))