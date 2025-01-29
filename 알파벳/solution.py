"""
백준
알파벳
https://www.acmicpc.net/problem/1987

조금 어려웠던 문제였다. 일단 풀이 방벙은 쉬워지만 한가지
간과했던 부분은 시간복잡도이다. 이문제는 단순한 DFS 가 
아니라 DFS 와 백트래킹을 사용하는 가능한 모든 경우를 찾아내는
풀이이다. 

즉 한점에서 시작해 목표지점으로 가는 DFS 처럼 O(n*m) 이 아니다
(이때 n 은 행의 개수 m 은 열의 개수).

보드의 각 칸에서 움직일수 있는 최대 경우는 4 (상하좌우) 이고 보드안에는
n*m 개의 칸이 존재하기 떄문에 모든 경우를 찾는다고 했을때 최대 O(4 ^ n*m)
이될수있다. 다른 분들의 풀이를 참고해서 놓친부분을 설명하자면 여기서 문제의 
조건을 추가해서 좀 더 정확한 표현이 필요하다. 문제에서는 각 칸은 대문자 알파벳이고
각 알파벳은 한번만 방문이 가능하기 때문에 어떤 경로라고 해도 최대 26 개의 칸까지
갖게 되기때문에 좀 더 정확하게는 O(4 ^ min(n*m, 26)) 이 될 것 같다.

처음에는 set 를 이용해서 방문한 알파벳을 관리했지만 이 방법은 시간초괴가 되었다.
최악의 경우 해시테이블의 종류인 set 또는 dict 는 lookup 이 리니어 서치가 될 수있기
때문에 방문 여부를 배열형태 자료구조로 변경 하였다.

통과는 했지만 이렇게 해도 사실 느리긴 마차가지였다. 나의 제출보다 월등히 빠른 다른 분들의
솔루션을 참고하여 깨달은 사실은 이 문제의 비효울성은 이미 았던 경우를 다시 마주해서 다시 
계산을 할 때 생긴다. 그리고 같은 경우를 판별하는 변수는 보드안에서 행과 열의 위치 그리고
그 위치를 방문했을때의 visited 자료구조의 상태이다.

여기서 주의 할 점은 보통 방문목록을 저장하는 visited 자료구조는 배열, 세트, 테이블, 맵 형태인데
모두 여러 데이터의 집합이여서 그 결과를 읽을때 데이터양에 비례한 리니어 시간 복잡도가 요구되고
다이나믹 프로그래밍의 방식처럼 여러 중간값들을 캐싱하기 위해 키로 사용하기에도 까다롭다.

그래서 보니... 다른분들의 풀이에서는 비트 마스킹을 이용해서 방문 상태를 관리하였고 이렇게 했을때
방문상태는 단순 비트이기 때문에 정수 값으로 표현이된다. 따라서 행, 열, 비트가 나타내는 정수 값의
조합을 이용해 해당 경우를 표현하고 그 경우의 대한 정답 값을 캐싱하여서 중복 연산을 방지할 수 있다.
"""
import sys

def solution(board):
    def _travel(r, c):
        visited[ord(board[r][c]) - ord("A")] = 1
        travel_count = 1

        for r_move, c_move in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_r = r + r_move
            new_c = c + c_move

            if new_r < 0 or new_r >= len(board) or new_c < 0 or new_c >= len(board[0]):
                continue

            if visited[ord(board[new_r][new_c]) - ord("A")] == 1:
                continue

            travel_count = max(travel_count, _travel(new_r, new_c) + 1)

        visited[ord(board[r][c]) - ord("A")] = 0
        return travel_count

    visited = [0 for _ in range(ord("Z") - ord("A") + 1)]
    return _travel(0, 0)

if __name__ == "__main__":
    r, c = map(int, sys.stdin.readline().strip().split(" "))
    board = [sys.stdin.readline().strip() for _ in range(r)]
    print(solution(board))
