"""
백준
크로스 컨트리
https://www.acmicpc.net/problem/9017

이 문제 역시 설명안에서 캐치해야되는 여러 조건들이 있는데
안일하게 읽고 넘어가서 실수를 좀 했다. 예를 들어 각 팀마다
등수를 합산해야되고 각 팀마다 최대 6명의 참가자가 있다고 인지했지만
등수 합산은 탑 4 만 해야된다는 부분을 놓쳤다.

또 무승부일경우 각 팀에서 5번째 참가자를 비교해야되는 경우를 까먹어서
팀별로 합산한 데이터만 보관하는것은 부적절하다는 것을 뒤늦게 알아차렸다던지..

한가지 드는 생각은, 만약 입력의 크기가 별로 크지 않고 조건이 복잡하거나 장화한경우
일단 최대한 심플하게 구현을 마치고 최적화를 하는게 더 효울적일것같다.
"""
import sys
from collections import Counter

RANK_SLICE_IDX = 4  # Top 4
TIE_BREAKER = 5

def solution(records: list[int]) -> int:
    player_counts = Counter(records)
    tally = {}
    rank = 1
    for team in records:
        if player_counts.get(team, 0) < 6:
            continue
        if team not in tally:
            tally[team] = []
        tally[team].append(rank)
        rank += 1
    
    winner = 0
    winner_total = float("inf")
    for team, player_records in tally.items():
        total = sum(player_records[:RANK_SLICE_IDX])
        if total < winner_total or (total == winner_total and player_records[TIE_BREAKER-1] < tally[winner][TIE_BREAKER-1]):
            winner = team
            winner_total = total
    return winner

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        records = list(map(int, sys.stdin.readline().strip().split(" ")))
        print(solution(records))
