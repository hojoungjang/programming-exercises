"""
백준
KCPC
https://www.acmicpc.net/problem/3758
"""

import sys

class Team:
    def __init__(self, team_id, problems_cnt):
        self.team_id = team_id
        self.submission_count = 0
        self.last_submission_idx = -1
        self.scores = {problem_id: 0 for problem_id in range(1, problems_cnt+1)}
        self.total_scores = 0

    def update_score(self, problem_id, score):
        old_score = self.scores.get(problem_id) or 0
        if score <= old_score:
            return
        self.scores[problem_id] = score
        self.total_scores = self.total_scores - old_score + score

    def get_total_scores(self):
        return self.total_scores

    def record_submission(self, problem_id, score, submission_idx):
        self.submission_count += 1
        self.last_submission_idx = submission_idx
        self.update_score(problem_id, score)

def solution(problems_cnt: int, teams_cnt: int, my_team_id: int, logs: list) -> int:
    score_board = {
        team_id: Team(team_id, problems_cnt) for team_id in range(1, teams_cnt+1)
    }

    for submission_idx, (team_id, problem_id, score) in enumerate(logs):
        score_board[team_id].record_submission(problem_id, score, submission_idx)

    sorted_teams = sorted(
        score_board.values(),
        key=lambda team: (-team.total_scores, team.submission_count, team.last_submission_idx)
    )
    for rank, team in enumerate(sorted_teams, 1):
        if team.team_id == my_team_id:
            return rank
    return -1


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        teams_cnt, problems_cnt, my_team_id, logs_cnt = map(int, sys.stdin.readline().strip().split(" "))
        logs = [[int(num) for num in sys.stdin.readline().strip().split(" ")] for _ in range(logs_cnt)]
        print(solution(problems_cnt, teams_cnt, my_team_id, logs))
