import sys
from time import sleep

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

DIRECTIONS = [(-1,0), (0, 1), (1, 0), (0, -1)]

EMPTY = 0
WALL = 1

def solution(room, r, c, direction):
    rows = len(room)
    cols = len(room[0])
    cleaned_cells = set()

    while True:
        cleaned_cells.add((r,c))

        has_empty_cells = False
        for dr, dc in DIRECTIONS:
            new_r = r + dr
            new_c = c + dc

            if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                continue

            if room[new_r][new_c] == EMPTY and (new_r, new_c) not in cleaned_cells:
                has_empty_cells = True
                break

        if not has_empty_cells:
            opposite = (direction + 2) % 4
            dr, dc = DIRECTIONS[opposite]
            r += dr
            c += dc
            if r < 0 or r >= rows or c < 0 or c >= cols:
                break
            if room[r][c] == WALL:
                break
        else:
            while True:
                direction = (direction - 1) % 4
                dr, dc = DIRECTIONS[direction]
                new_r, new_c = r + dr, c + dc
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if room[new_r][new_c] == EMPTY and (new_r, new_c) not in cleaned_cells:
                    r = new_r
                    c = new_c
                    break

    return len(cleaned_cells)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    r, c, d = map(int, sys.stdin.readline().strip().split(" "))
    room = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(room, r, c, d))
