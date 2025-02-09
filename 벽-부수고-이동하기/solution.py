"""
백준
벽 부수고 이동하기
https://www.acmicpc.net/problem/2206

의외로 간단한 수준이었다. BFS 를 활용해서 최단거리를 구하는데
이때 주어진 경로안에는 벽이 존재해 막혀있는 부분이 있을 수 있디.
이떄 최대 한번까지는 벽을 무시할 수 있다는 조건을 이용해가면서
BFS 해주면 된다.

한가지 잡아내지 못 했던 부분은 어떠한 위치에 대해 방문체크를 진행
할 때 단순히 위치 정보를 이용하는게 아니라 위치와 벽 부수기를 사용한
여부를 혼합해서 방문체크 값으로 사용해야 한다는 점이다.

예를 들어 벽을 부수고 이동했는데 앞에 벽이 더 있어 더이상 해당 경우에서 
전진 할 수 없을때 지나온 위치들은 방문 체크가 된다. 하지만 만약 벽을 부수지 
않고 똑같은 위치에 도착해서 더 앞으로 나아갈 수 있는 경우라면 계속해서 BFS 가
진행되어야한다. 방문체크를 단순 위치만 사용해서 관리할 경우 이 엣지 케이스들을
고려 할 수 없게 된다.
"""

import sys
from collections import deque

EMPTY = 0
WALL = 1

def solution(board, rows, cols):
    # queue items: (row, column, wall break used)
    queue = deque([(0,0,False), None])
    visited = set([(0,0,False)])
    total_moves = 1

    while queue:
        state = queue.popleft()
        if state is None:
            if queue: queue.append(None)
            total_moves += 1
            continue

        r, c, used = state
        if r == rows - 1 and c == cols - 1:
            return total_moves
        
        for r_move, c_move in ((1,0), (-1,0), (0,1), (0,-1)):
            new_r = r + r_move
            new_c = c + c_move

            if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                continue

            if board[new_r][new_c] == WALL and used:
                continue

            new_state = (new_r, new_c, used or board[new_r][new_c] == WALL)

            if new_state in visited:
                continue
            
            visited.add(new_state)
            queue.append(new_state)
    
    return -1

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    board = [[int(num) for num in sys.stdin.readline().strip()] for _ in range(n)]
    print(solution(board, n, m))
