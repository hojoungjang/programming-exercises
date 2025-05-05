import sys

BLOCKED = "x"
EMPTY = "."

def solution(rows, cols, grid):
    
    def dfs(r, c):
        grid[r][c] = BLOCKED

        if c == cols - 1:
            return 1

        cnt = 0
        for dr in [-1, 0, 1]:
            new_r = r + dr
            if new_r < 0 or new_r >= rows:
                continue

            if grid[new_r][c+1] == BLOCKED:
                continue

            if dfs(new_r, c + 1):
                return 1
        
        return 0

    cnt = 0
    for r in range(rows):
        cnt += dfs(r=r, c=0)
    return cnt

if __name__ == "__main__":
    rows, cols = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[val for val in sys.stdin.readline().strip()] for _ in range(rows)]
    print(solution(rows, cols, grid))
