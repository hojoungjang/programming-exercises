import sys

LEFT = 1
UP = 2
RIGHT = 4
DOWN = 8

def solution(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    def dfs_rooms(r, c):
        room_grid[r][c] = room_id

        size = 1
        for dr, dc, dw in [(-1, 0, UP), (1, 0, DOWN), (0, -1, LEFT), (0, 1, RIGHT)]:
            next_r = r + dr
            next_c = c + dc

            if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                continue

            if room_grid[next_r][next_c] != -1:
                continue

            if grid[r][c] & dw == dw:
                continue

            size += dfs_rooms(next_r, next_c)
        return size

    room_id = 0
    room_grid = [[-1 for _ in range(cols)] for _ in range(rows)]
    room_size = {}

    for r in range(rows):
        for c in range(cols):
            if room_grid[r][c] == -1:
                size = dfs_rooms(r, c)
                room_size[room_id] = size
                room_id += 1

    max_two_room_size = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc, dw in [(-1, 0, UP), (1, 0, DOWN), (0, -1, LEFT), (0, 1, RIGHT)]:
                next_r = r + dr
                next_c = c + dc

                if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                    continue

                if room_grid[r][c] == room_grid[next_r][next_c]:
                    continue

                max_two_room_size = max(max_two_room_size, room_size[room_grid[r][c]] + room_size[room_grid[next_r][next_c]])

    return room_id, max(room_size.values()), max_two_room_size


if __name__ == "__main__":
    cols, rows = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(rows)]
    for val in solution(grid):
        print(val)
