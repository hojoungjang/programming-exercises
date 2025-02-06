"""
백준
불!
https://www.acmicpc.net/problem/4179

BFS 를 살짝 비튼 문제라고 생각이든다. BFS 를 사용하지만 단순히
한번에 하나의 정점을 큐에서 빼서 처리하고 넘어가는 것이 아니라
BFS 상 각 레벨에 있는 모든 방문 가능한 정점을 처리후에 나온 미로의
상태에서 탈출 여부를 판단한다. 문제안에서의 시간 개념이  그렇게 동작하기
떄문이다.

예를 들어 불길은 동시다발적으로 번진다. 즉 한번에 하나의 불씨만 다른 정점으로
번지는게 아니라 존재하는 모든 불씨가 번진다. 
마찬가지로 미로안에 사람도 한번에 하나의 방문가능한 정점을 고려하는 것이 아니라
현재 내가 갈 수 있는 모든 정점을 고려해서 탈출가능 여부를 매 시간대 마다 확인해주어야
한다.

처음에 불에 대해서만 레벨 전체를 처리해주고 사람은 하나의 정점만 고려해서 답이 가능한
입력값에 대해서 불가능하다고 처리되는 경우가 생겼다.

시간복잡도는 불씨, 사람 둘다 각각 최대 모든 정점들을 방문할 수 있다. 따라서 O(rows *cols)
가 된다. 공간복잡도는 마찬가지로 둘다 각각 큐를 이용하는데 이때 큐는 최대 모든 정점을
담을 수 있다. O(rows * cols)
"""

import sys
from collections import deque

WALL = "#"
EMPTY = "."
START = "J"
FIRE = "F"

def solution(rows, cols, grid):
    def get_start_pos():
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == START:
                    grid[r][c] = EMPTY
                    return r, c
        return None
    
    def get_all_fire_pos():
        positions = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == FIRE:
                    positions.append((r, c))
        return positions
    
    start_pos = get_start_pos()
    if start_pos is None: return -1
    fire_positions = get_all_fire_pos()

    person_queue = deque([start_pos, None])
    visited = set([start_pos])
    fire_queue = deque([*fire_positions, None])
    time = 1

    while True:
        # first spread the fire!
        while fire_queue:
            fire_pos = fire_queue.popleft()

            if fire_pos is None:
                if fire_queue:
                    fire_queue.append(None)
                break

            for r_move, c_move in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_r_fire = fire_pos[0] + r_move
                new_c_fire = fire_pos[1] + c_move

                if new_r_fire < 0 or new_r_fire >= rows or new_c_fire < 0 or new_c_fire >= cols:
                    continue
                    
                if grid[new_r_fire][new_c_fire] != EMPTY:
                    continue

                grid[new_r_fire][new_c_fire] = FIRE
                fire_queue.append((new_r_fire, new_c_fire))
        
        # move the person
        while person_queue:
            person_pos = person_queue.popleft()

            if person_pos is None:
                if person_queue:
                    person_queue.append(None)
                time += 1
                break

            r_person, c_person = person_pos
            if r_person == 0 or r_person == rows-1 or c_person == 0 or c_person == cols-1:
                return time

            for r_move, c_move in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_r_person = r_person + r_move
                new_c_person = c_person + c_move

                if new_r_person < 0 or new_r_person >= rows or new_c_person < 0 or new_c_person >= cols:
                    continue

                if grid[new_r_person][new_c_person] != EMPTY:
                    continue

                if (new_r_person, new_c_person) in visited:
                    continue

                visited.add((new_r_person, new_c_person))
                person_queue.append((new_r_person, new_c_person))

        if not person_queue:
            break

    return -1


if __name__ == "__main__":
    rows, cols = map(int, sys.stdin.readline().strip().split())
    grid = [[cell for cell in sys.stdin.readline().strip()] for _ in range(rows)]

    ans = solution(rows, cols, grid)
    if ans == -1:
        print("IMPOSSIBLE")
    else:
        print(ans)
