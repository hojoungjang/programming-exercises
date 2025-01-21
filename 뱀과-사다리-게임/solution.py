"""
백준
뱀과 사다리 게임
https://www.acmicpc.net/problem/16928

처음에는 풀이법이 바로 생각나지 않아서 고민을 좀 하다가 BFS 방식이 떠올랐다.
여기서 중요한건 주사위 횟수가 작은 경우부터 처리를 해주어서 같은 위치를 
더 높은 주사위 횟수로 방문하는 경우를 가지치기하며 100을 도달하는 
최소 주사위 횟수를 구해야한다. 또한, 뱀/사다리 칸은 서있을 수 없고
무조건 연결된 다음 칸으로 이동해야된다.
"""

import sys
from collections import deque

DICE_SIZE = 6
TOTAL_BOARD_CELLS = 100

def solution(graph):
    queue = deque([(1, 0)])
    visited = set([1])

    while queue:
        cur_cell, dice_rolls = queue.popleft()

        if cur_cell == 100:
            return dice_rolls

        for i in range(1, DICE_SIZE+1):
            new_cell = cur_cell + i
            if new_cell > TOTAL_BOARD_CELLS:
                continue
            if new_cell in visited:
                continue
            visited.add(new_cell)

            if graph[new_cell]:
                for jump_cell in graph[new_cell]:
                    if jump_cell in visited:
                        continue
                    visited.add(jump_cell)
                    queue.append((jump_cell, dice_rolls + 1))
            else:
                queue.append((new_cell, dice_rolls + 1))
    
    return -1

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    graph = {i: [] for i in range(1, TOTAL_BOARD_CELLS + 1)}
    for _ in range(n+m):
        s, e = map(int, sys.stdin.readline().strip().split(" "))
        graph[s].append(e)
    print(solution(graph))
