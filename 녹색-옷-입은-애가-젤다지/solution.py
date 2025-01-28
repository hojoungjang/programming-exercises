"""
백준
녹색 옷 입은 애가 젤다지?
https://www.acmicpc.net/problem/4485

문제 설명은 살짝 안그래 보이지만 그래프에서 최단거리 구하기 형식의 문제이다.
문제 입력에는 음수 간선이 없고 한지점에서 목표지점까지 최소거리 (여기서는 루피) 로
가고싶어하기 때문에 다익스트라 알고리즘을 적용할 수 있다.

이때 처음에는 가지치기 조건문을 안넣어 주었더니 시간초과가 되었다. 정확히 원인이
완벽히 이해는 안되었지만, 경우의 따라 우선순위 큐 크기가 많이 커질수 있어서
거기서 시간초과가 되는것 같다.

따라서 이때 출발지부터 각 지점까지의 거리는 기록하고 이미 발견한 거리보다 작을때만
새로 큐에 넣어주는 식으로 나머지 큰거나 같은 거리 경우들은 고려하지 않는다.
"""
import sys
from heapq import heappush, heappop

def solution(board, n):
    pqueue = [(board[0][0], 0, 0)]
    distances = [[float("inf") for _ in range(n)] for _ in range(n)]
    distances[0][0] = 0

    while pqueue:
        rupees, r, c = heappop(pqueue)
        
        if r == n-1 and c == n-1:
            return rupees
        
        for r_move, c_move in [(0, 1), (1, 0), (0,-1), (-1,0)]:
            new_r = r + r_move
            new_c = c + c_move

            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
                continue

            new_distance = rupees + board[new_r][new_c]
            if new_distance >= distances[new_r][new_c]:
                continue

            distances[new_r][new_c] = new_distance
            heappush(pqueue, (new_distance, new_r, new_c))
    
    return -1


if __name__ == "__main__":
    problem_no = 1
    while (n := int(sys.stdin.readline().strip())) != 0:
        board = [[int(rupee) for rupee in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
        min_black_rupees = solution(board, n)
        print(f"Problem {problem_no}: {min_black_rupees}")
        problem_no += 1