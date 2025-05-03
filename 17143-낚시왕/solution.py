"""
백준
낚시왕
https://www.acmicpc.net/problem/17143
"""

import sys

UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4
DIRECTION_OFFSETS = [
    (0, 0),
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
]

class Shark:
    def __init__(self, id, speed, direction, size):
        self.id = id
        self.speed = speed
        self.direction = direction
        self.size = size


def move_sharks(shark_tank):
    rows = len(shark_tank)
    cols = len(shark_tank[0])
    new_shark_tank = [[None for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if shark_tank[r][c] is None:
                continue

            shark = shark_tank[r][c]
            direction = shark.direction
            dr, dc = DIRECTION_OFFSETS[direction]
            new_r, new_c = r + (dr * shark.speed), c + (dc * shark.speed)

            while new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                if new_r < 0:
                    new_r *= -1
                    direction = DOWN
                elif new_r >= rows:
                    new_r = (rows - 1) - (new_r - (rows - 1))
                    direction = UP
                elif new_c < 0:
                    new_c *= -1
                    direction = RIGHT
                elif new_c >= cols:
                    new_c = (cols - 1) - (new_c - (cols - 1))
                    direction = LEFT
            shark.direction = direction

            if new_shark_tank[new_r][new_c] is None or new_shark_tank[new_r][new_c].size < shark.size:
                new_shark_tank[new_r][new_c] = shark
            
    return new_shark_tank


def solution(rows, cols, shark_tank):
    total = 0
    
    for angler_pos in range(cols):
        shark = None
        for r in range(rows):
            if shark_tank[r][angler_pos]:
                shark = shark_tank[r][angler_pos]
                shark_tank[r][angler_pos] = None
                total += shark.size
                break
            
        shark_tank = move_sharks(shark_tank)
    
    return total


if __name__ == "__main__":
    rows, cols, m = map(int, sys.stdin.readline().strip().split(" "))
    shark_tank = [[None for _ in range(cols)] for _ in range(rows)]
    for i in range(m):
        r, c, s, d, z = map(int, sys.stdin.readline().strip().split(" "))
        shark_tank[r-1][c-1] = Shark(id=i, speed=s, direction=d, size=z)

    print(solution(rows, cols, shark_tank))
