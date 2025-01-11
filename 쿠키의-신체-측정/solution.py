"""
백준
쿠키의 신체 측정
https://www.acmicpc.net/problem/20125
"""

import sys

def find_head(n, board):
    for r in range(n):
        for c in range(n):
            if board[r][c] == "*":
                return r, c
    return -1, -1

def find_heart(n, board):
    head_r, head_c = find_head(n, board)
    return head_r + 1, head_c

def get_cookie_dimension(n, board):
    def get_body_part_length(r, c, offest_r, offset_c):
        length = 0
        while 0 <= r < n and 0 <= c < n and board[r][c] == "*":
            length += 1
            r += offest_r
            c += offset_c
        return length

    heart_r, heart_c = find_heart(n, board)
    left_arm_len = get_body_part_length(heart_r, heart_c - 1, 0, -1)
    right_arm_len = get_body_part_length(heart_r, heart_c + 1, 0, 1)
    torso_len = get_body_part_length(heart_r+1, heart_c, 1, 0)
    left_leg_len = get_body_part_length(heart_r + torso_len + 1, heart_c - 1, 1, 0)
    right_leg_len = get_body_part_length(heart_r + torso_len + 1, heart_c + 1, 1, 0)
    return heart_r, heart_c, left_arm_len, right_arm_len, torso_len, left_leg_len, right_leg_len

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    board = [[char for char in sys.stdin.readline().strip()] for _ in range(n)]
    heart_r, heart_c, left_arm_len, right_arm_len, torso_len, left_leg_len, right_leg_len = get_cookie_dimension(n, board)

    print(f"{heart_r + 1} {heart_c + 1}")
    print(f"{left_arm_len} {right_arm_len} {torso_len} {left_leg_len} {right_leg_len}")
