"""
백준
미네랄 2
https://www.acmicpc.net/problem/18500

시작은 일단 미네랄을 부수는 로직을 만들었다. 좌우 번걸아가며
주어진 높이에서 왼쪽/오른쪽에서 부터 첫번째 만나는 미네랄을 찾아 없앤다.

그 다음은 해당 미네랄이 없어지고 생긴 모든 클러스터에 대해 중력에 의한
위치 변경을 해준다. 만약 이미 바닥과 맞닿아 있으면 움직일 필요가 없지만
뜬 상태라면 가장 빨리 바닥 또는 다른 미네랄과 맞닿을 때까지 아래 방향으로
움직여준다.

구현 로직은
1. 입력된 창을 던지는 높이를 순회하며 부딫히는 미네랄을 부순다. (이때 창의 시작 위치와 방향을 번걸아 준다. 처음은 항상 왼쪽-> 오른쪽)
2. 창이 미네랄과 만나 미네랄이 사라질 경우, 여러 클러스터가 생기는 것과 각각의 클러스터가 위치 조정이 필요한지 확인한다.
3. 각각의 클러스터를 순회하며 클러스터 안에 있는 모든 좌표에 있는 미네랄이 최대 움직임을 구해내자
4. 클러스터 안에 있는 모든 좌표에 대한 최대 움직임중 가장 작은 값 만큼만 전체 클러스터를 움직일 수 있다.
3. 클러스터를 위에서 찾은 값만큼 아래로 알맞게 위치를 옮겨준다.

최적화
1. 이때 클러스터를 찾는 로직을 DFS 로 했는데 BFS 로 하면 좀 더 효율적이다. (iterative vs recursion)
2. 클러스터를 찾을때 해당 클러스터의 일부분이 바닥에 닿아 있는 사실여부를 추적해 클러스터를 움직일때 필요한 계산들을
   스킵할 수 있다.

각 높이 마다 클러스터를 찾는 DFS 를 최대 3 번 (최대 3개의 클러스터가 나올수 있기 때문) 그리고 각 클러스터마다 클러스터
안에 있는 모든 좌표를 순회해서 최대 이동거리를 구하고 각 좌표에 담긴 값을 이동시켜 동굴의 상태를 업뎃해준다.

n : 높이의 개수
r : 동굴 행의 개수
c : 동굴 열의 개수
클러스터의 최대 크기는 r*c

n * ((r * c * 3) + (r * c * 3 * 3))
O(n * r * c)
"""
import sys
from collections import deque

EMPTY = "."
MINERAL = "x"

MIN = 0
MAX = 1

def solution(board, heights):
    
    def fall_clusters(r, c):

        def find_clusters(r, c):
            queue = deque([(r,c)])
            visited.add((r,c))
            cluster = set()
            floating = True

            while queue:
                cur_r, cur_c = queue.popleft()
                cluster.add((cur_r, cur_c))

                if cur_r == rows - 1:
                    floating = False
            
                for dr, dc in [(1, 0), (0,-1), (0,1), (-1,0)]:
                    new_r, new_c = cur_r + dr, cur_c + dc

                    if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                        continue
                    
                    if board[new_r][new_c] == EMPTY:
                        continue
                    
                    if (new_r, new_c) in visited:
                        continue

                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))
            
            return cluster, floating

        visited = set()
        clusters = []
        for dr, dc in [(1, 0), (0,-1), (0,1), (-1,0)]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == MINERAL and (new_r, new_c) not in visited:
                cluster, floating = find_clusters(new_r, new_c)
                if cluster and floating:
                    clusters.append(cluster)
        
        for cluster in clusters:
            max_row_offset = rows
            for r, c in cluster:
                dist = 0
                r += 1
                while r < rows:
                    if board[r][c] == MINERAL and (r,c) not in cluster:
                        break
                    dist += 1
                    r += 1
                max_row_offset = min(max_row_offset, dist)

            for r, c in cluster:
                board[r][c] = EMPTY

            for r, c in cluster:
                board[r+max_row_offset][c] = MINERAL

    
    rows = len(board)
    cols = len(board[0])

    for i, height in enumerate(heights):
        r = rows - height
        if i % 2:
            col_idxs = range(cols-1, -1, -1)
        else:
            col_idxs = range(cols)
        
        for c in col_idxs:
            if board[r][c] == MINERAL:
                board[r][c] = EMPTY
                fall_clusters(r, c)
                break

    return board


if __name__ == "__main__":
    rows, cols = map(int, sys.stdin.readline().strip().split(" "))
    board = [[c for c in sys.stdin.readline().strip()] for _ in range(rows)]
    n = int(sys.stdin.readline().strip())
    heights = [int(num) for num in sys.stdin.readline().strip().split(" ")]

    board = solution(board, heights)

    for r in board:
        print("".join(r))
