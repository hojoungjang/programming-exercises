"""
백준
미세먼지 안녕!
https://www.acmicpc.net/problem/17144
"""
import sys

def print_room(room):
    for row in room:
        print(row)

def spread(room):
    rows = len(room)
    cols = len(room[0])

    new_room = [[room[r][c] for c in range(cols)] for r in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if room[r][c] < 5:
                continue

            amount = room[r][c] // 5

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_r = r + dr
                new_c = c + dc

                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue

                if room[new_r][new_c] == -1:
                    continue

                new_room[new_r][new_c] += amount
                new_room[r][c] -= amount
    
    return new_room


def clean(room):
    def locate():
        for r in range(rows):
            if room[r][0] == -1:
                return r, r+1
        return -1, -1

    rows = len(room)
    cols = len(room[0])
    r1, r2 = locate()
    
    temp = 0
    for c in range(1, cols - 1):
        temp, room[r1][c] = room[r1][c], temp

    for r in range(r1, 0, -1):
        temp, room[r][cols-1] = room[r][cols-1], temp

    for c in range(cols-1, 0, -1):
        temp, room[0][c] = room[0][c], temp

    for r in range(r1):
        temp, room[r][0] = room[r][0], temp

    temp = 0
    for c in range(1, cols - 1):
        temp, room[r2][c] = room[r2][c], temp

    for r in range(r2, rows-1):
        temp, room[r][cols-1] = room[r][cols-1], temp

    for c in range(cols-1, 0, -1):
        temp, room[rows-1][c] = room[rows-1][c], temp

    for r in range(rows-1, r2, -1):
        temp, room[r][0] = room[r][0], temp


def solution(room, t):
    for _ in range(t):
        # 확산
        room = spread(room)

        # 청정
        clean(room)

    total = 0
    for row in room:
        for dust in row:
            if dust > 0:
                total += dust
    return total


if __name__ == "__main__":
    rows, cols, t = map(int, sys.stdin.readline().strip().split(" "))
    room = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(rows)]
    print(solution(room, t))