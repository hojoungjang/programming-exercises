"""
백준
나무 재테크
https://www.acmicpc.net/problem/16235
"""

import sys


def solution(renew_amounts, trees, k):
    n = len(renew_amounts)
    
    nutrition_grid = [[5 for _ in range(n)] for _ in range(n)]
    
    land = [[[] for _ in range(n)] for _ in range(n)]
    for r, c, age in trees:
        land[r][c].append(age)

    for _ in range(k):

        for r in range(n):
            for c in range(n):

                # Spring
                if not land[r][c]:
                    continue

                new_cell = []
                while nutrition_grid[r][c] and land[r][c]:
                    # 가장 어린 나무의 나이
                    age = land[r][c][-1]

                    if age > nutrition_grid[r][c]:
                        break

                    age = land[r][c].pop()
                    new_cell.append(age + 1)
                    nutrition_grid[r][c] -= age

                land[r][c], dead_trees = new_cell[::-1], land[r][c]

                # Summer
                for age in dead_trees:
                    nutrition_grid[r][c] += (age // 2)

        new_land = [[t[:] for t in row] for row in land]
        for r in range(n):
            for c in range(n):
                
                # Fall
                for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1,0), (1,1)]:
                    new_r = dr + r
                    new_c = dc + c

                    if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
                        continue

                    for age in land[r][c]:
                        if (age % 5):
                            continue
                        new_land[new_r][new_c].append(1)

                # Winter
                nutrition_grid[r][c] += renew_amounts[r][c]
        land = new_land

    return sum(sum(len(cell) for cell in row) for row in land)


if __name__ == "__main__":
    """
    n: 땅의 크 n x n
    m: 나무의 수
    k: 년 회수
    """
    n, m, k = map(int, sys.stdin.readline().strip().split(" "))

    renew_amounts = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    
    # (r, c, age)
    trees = []
    for _ in range(m):
        r, c, age = map(int, sys.stdin.readline().strip().split(" "))
        trees.append((r-1, c-1, age))

    print(solution(renew_amounts, trees, k))
