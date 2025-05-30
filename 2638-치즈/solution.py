import sys
from collections import deque

CLOSED_AIR = 0
OPEN_AIR = -1
CHEESE = 1

def solution(rows, cols, grid):
    
    def is_safe(r, c):
        cnt = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if grid[r + dr][c + dc] == OPEN_AIR:
                cnt += 1
        return True if cnt < 2 else False

    def classify_air():
        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            cur_r, cur_c = queue.popleft()
            grid[cur_r][cur_c] = OPEN_AIR

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r = cur_r + dr
                new_c = cur_c + dc

                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue

                if grid[new_r][new_c] == CHEESE:
                    continue

                if (new_r, new_c) in visited:
                    continue

                visited.add((new_r, new_c))
                queue.append((new_r, new_c))

    iter_cnt = 0
    while sum([row.count(CHEESE) for row in grid]):
        classify_air()
        new_grid = [[grid[r][c] for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == CHEESE and not is_safe(r, c):
                    new_grid[r][c] = OPEN_AIR
        iter_cnt += 1
        grid = new_grid

    return iter_cnt


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(n, m, grid))
