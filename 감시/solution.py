"""
백준
감시
https://www.acmicpc.net/problem/15683

풀이 방식을 생각해내는 것은 금방하였으나, 생각보다 구현과정에서
오래걸렸다. 

주어진 직사각형 안에서 각 cctv 에 대해 DFS 를 하고 각 DFS 안에서 알맞게 돌렸을때의 경우에
대해 또 다른 DFS 를 해서 감시영역의 크기를 구해내는 식으로 풀이를 하였다.

일단 풀이 방식도 처음에는 완벽하지 않았던게 감시영역 크기를 찾는 법을 BFS 식으로 하려다가 실수로
4,5 번 종류의 cctv 에서 범위를 한방향으로 뻗어나가는 식이 아니라 모든 방향으로 점점 펼쳐지는 
방식이 되어버리게 되었다.

그것 외에도 문제에서 찾고자하는 값을 명확히 이해해야 했다. 일단 사각지대가 될수 있는 영역은 무조건
빈 칸이어야 한다. 따라서 cctv 나 벽은 사각지대 크기에 포함되지 않는다. 또한 감시영역을 구할때 
다른 cctv 들 끼리 겹치는 구간을 중복되지 않게 세어주어야한다.

마지막으로 내가 푼 풀이 방법은 백트래킹을 해서 모든 경우의 수를 고려하는데 백트래킹 할때
단순히 boolean 식으로 방문/비방문으로 마킹을 하는게 아니라 정수로 표현하고 하나의 cctv 가
해당 칸을 커버할때 1 씩 증가시켜서 겹칠때의 상황을 고려해서 백트래킹 하였다.

문제의 입력은 그리 크지 않기 때문에 완전탐색으로도 풀이가 가능하다. 
각 cctv 에 대해 DFS 를 하고 각 cctv 종류는 최대 4 가지 돌림 버전이 있고 각 돌림버전마다 최대
가로 + 세로의 길이 만큼 커버를 할 수 있다. 또 문제에서 총 cctv 의 최대 개수는 8 이라고 되어있다.
따라서 대략 O(k ^ n * (r + c)) 가 된다
* k : 회전 가능한 버전의 수
* n : cctv 의 개수
* r : 행의 개수
* c : 열의 개수
"""

import sys

EMPTY = 0
WALL = 6
CCTV = {
    1: [
        [(1,0)],
        [(-1,0)],
        [(0,1)],
        [(0,-1)],
    ],
    2: [
        [(1,0), (-1,0)],
        [(0,1), (0,-1)],
    ],
    3: [
        [(-1,0), (0,1)],
        [(0,1), (1,0)],
        [(1,0), (0,-1)],
        [(0,-1), (-1,0)],
    ],
    4: [
        [(0,-1), (-1,0), (0,1)],
        [(-1,0), (0,1), (1,0)],
        [(0,1), (1,0), (0,-1)],
        [(1,0), (0,-1), (-1,0)],
    ],
    5: [
        [(1,0), (-1,0), (0,1), (0,-1)],
    ],
}

def solution(grid):
    def dfs_rotation(coord, move, history):
        r, c = coord
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 0
        
        if grid[r][c] == WALL:
            return 0
        
        history.append((r, c))
        visited[r][c] += 1

        r_move, c_move = move
        new_r, new_c = r + r_move, c + c_move
        if grid[r][c] != EMPTY or visited[r][c] > 1:
            cnt = 0
        else:
            cnt = 1
        
        return cnt + dfs_rotation((new_r, new_c), move, history)

    def dfs_cctv(cctv_idx, covered_cnt):
        nonlocal max_covered_cnt

        if cctv_idx >= len(cctv_coords):
            max_covered_cnt = max(max_covered_cnt, covered_cnt)
            return
        
        # For the current cctv perform another DFS to find max covered count for each rotation
        cctv_coord = cctv_coords[cctv_idx]
        cctv_type = grid[cctv_coord[0]][cctv_coord[1]]

        for rotation in CCTV[cctv_type]:
            cnt = 0
            visited[cctv_coord[0]][cctv_coord[1]] += 1
            history = [cctv_coord]

            for move in rotation:
                new_r, new_c = cctv_coord[0] + move[0], cctv_coord[1] + move[1]
                cnt += dfs_rotation((new_r, new_c), move, history)

            dfs_cctv(cctv_idx + 1, covered_cnt + cnt)

            # backtrack
            for hist_r, hist_c in history:
                visited[hist_r][hist_c] -= 1

    
    # find all cctvs
    cctv_coords = []
    empty_cnt = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in CCTV:
                cctv_coords.append((r,c))
            if grid[r][c] == EMPTY:
                empty_cnt += 1

    max_covered_cnt = 0
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dfs_cctv(cctv_idx=0, covered_cnt=0)

    return empty_cnt - max_covered_cnt

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    grid = [[int(num) for num in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(grid))