"""
백준
임스와 함께하는 미니게임
https://www.acmicpc.net/problem/25757
"""
import sys

PLAYERS_IN_GAME = {
    "Y": 2,
    "F": 3,
    "O": 4,
}

if __name__ == "__main__":
    n, game_type = sys.stdin.readline().strip().split(" ")
    players = set()
    for _ in range(int(n)):
        players.add(sys.stdin.readline().strip())
    player_count = PLAYERS_IN_GAME.get(game_type)
    q, _ = divmod(len(players), player_count - 1)
    print(q)
