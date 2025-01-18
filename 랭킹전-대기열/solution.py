"""
백준
랭킹전 대기열
https://www.acmicpc.net/problem/20006

플레이어의 수       p
플레이어의 닉네임    n
플레이어의 레벨     l
방 한개의 정원     m

플레이어를 알맞게 배정하기 위해 각 방에 대해 그 방의
방장 레벨, 플레이어 인원수, 만들어진 순서가 필요하다.

레벨은 따로 저장
플레이어 인원은 플레이어 정보를 담는 배열로 저장.
(플레이어 정보는 출력시 필요하기 때문)
만들어진 순서에 따라 배정을 하기 위해 만들어지는 방은
배열에 순서대로 보관하고 배정할때도 배열을 순회해서 순차적으로
확인해서 순서대로 배정해야하는 조건을 만족시킨다.

이때 최악의 경우 모든 방을 확인하지만 문제의 주어진 입력 조건상
괜찮다.
"""
import sys

class Room:
    def __init__(self, level):
        self.level = level
        self.players = []

def solution(players, room_size):
    """
    players -> [(level, name), ...]
    
    returns -> [Room 1, Room 2, ...]
    """
    rooms = []
    for level, name in players:
        for room in rooms:
            if room.level - 10 <= level <= room.level + 10 and len(room.players) < room_size:
                room.players.append((level, name))
                break
        else:
            new_room = Room(level)
            new_room.players.append((level, name))
            rooms.append(new_room)
    return rooms

if __name__ == "__main__":
    p, m = map(int, sys.stdin.readline().strip().split(" "))
    players = []
    for _ in range(p):
        player = sys.stdin.readline().strip().split(" ")
        players.append((int(player[0]), player[1]))

    rooms = solution(players, m)
    for room in rooms:
        players = sorted(room.players, key=lambda x: x[1])
        print("Started!" if len(room.players) == m else "Waiting!")
        for player in players:
            print(f"{player[0]} {player[1]}")
