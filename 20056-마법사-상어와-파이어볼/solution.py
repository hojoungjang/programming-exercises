"""
백준
마법사 상어와 파이어볼
https://www.acmicpc.net/problem/20056
"""
import sys

DIRECTION_MAP = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0), 
    (1, -1),
    (0, -1),
    (-1, -1),
]

class FireBall:
    def __init__(self, r, c, mass, speed, direction):
        self.r = r
        self.c = c
        self.mass = mass
        self.speed = speed
        self.direction = direction

def solution(grid_size, fire_balls, end_time):
    grid = [[[] for _ in range(grid_size)] for _ in range(grid_size)]
    
    for fb in fire_balls:
        grid[fb.r][fb.c].append(fb)

    time = 0
    while time < end_time:
        new_grid = [[[] for _ in range(grid_size)] for _ in range(grid_size)]

        for r in range(grid_size):
            for c in range(grid_size):
                if len(grid[r][c]) == 0:
                    continue

                for fb in grid[r][c]:
                    speed = fb.speed
                    direction = fb.direction
                    offset_r, offset_c = DIRECTION_MAP[direction]

                    new_r = (fb.r + offset_r * speed) % grid_size
                    new_c = (fb.c + offset_c * speed) % grid_size

                    fb.r = new_r
                    fb.c = new_c
                    new_grid[new_r][new_c].append(fb)

        for r in range(grid_size):
            for c in range(grid_size):
                if len(new_grid[r][c]) < 2:
                    continue

                new_speed = 0
                new_mass = 0
                for fb in new_grid[r][c]:
                    new_speed += fb.speed
                    new_mass += fb.mass
                
                new_speed //= len(new_grid[r][c])
                new_mass //= 5

                if new_mass == 0:
                    new_grid[r][c] = []
                    continue

                if all(fb.direction % 2 == 0 for fb in new_grid[r][c]) or all(fb.direction % 2 == 1 for fb in new_grid[r][c]):
                    new_directions = [0, 2, 4, 6]
                else:
                    new_directions = [1, 3, 5, 7]

                new_fbs = []
                for new_direction in new_directions:
                    new_fbs.append(FireBall(r, c, new_mass, new_speed, new_direction))

                new_grid[r][c] = new_fbs

        grid = new_grid
        time += 1

    total_mass = 0
    for r in range(grid_size):
        for c in range(grid_size):
            for fb in grid[r][c]:
                total_mass += fb.mass
    return total_mass


if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().strip().split(" "))
    fire_balls = []
    for _ in range(m):
        r, c, mass, speed, direction = map(int, sys.stdin.readline().strip().split(" "))
        fire_balls.append(FireBall(r-1, c-1, mass, speed, direction))
    print(solution(n, fire_balls, k))
