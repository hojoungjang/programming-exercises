import sys
from collections import deque

SHARK = 1

def solution(grid):

    def bfs(starts):
        starts.append(None)
        queue = deque(starts)
        dist = 1

        while queue:
            if queue[0] is None:
                queue.popleft()
                if queue:
                    queue.append(None)
                dist += 1
                continue

            r, c = queue.popleft()
            
            for dr, dc in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                next_r = r + dr
                next_c = c + dc

                if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                    continue

                if dist_grid[next_r][next_c] <= dist:
                    continue

                dist_grid[next_r][next_c] = dist
                queue.append((next_r, next_c))

    rows = len(grid)
    cols = len(grid[0])
    dist_grid = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    starts = []

    for start_r in range(rows):
        for start_c in range(cols):
            if grid[start_r][start_c] == SHARK:
                starts.append((start_r, start_c))
                dist_grid[start_r][start_c] = 0
    
    bfs(starts)
    return max([max(row) for row in dist_grid])

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(grid))
