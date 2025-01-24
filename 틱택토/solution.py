"""
틱택토
https://www.acmicpc.net/problem/7682

간단한 구현 문제
상황에 맞는 조건을 세우고 확인하면 됨
"""
import sys

BOARD_SIZE = 3

def check_win(board, cand):
    for r in range(BOARD_SIZE):
        if all(board[r][c] == cand for c in range(BOARD_SIZE)):
            return True
    
    for c in range(BOARD_SIZE):
        if all(board[r][c] == cand for r in range(BOARD_SIZE)):
            return True

    if all(board[idx][idx] == cand for idx in range(BOARD_SIZE)):
        return True
    
    if all(board[idx][BOARD_SIZE - idx - 1] == cand for idx in range(BOARD_SIZE)):
            return True
    
    return False

def solution(board):
    o_counts = sum(row.count("O") for row in board)
    x_counts = sum(row.count("X") for row in board)

    # O 가 더 많다
    if o_counts > x_counts:
        return False

    # X 가 O 보다 2 이상 많다
    if x_counts - o_counts > 1:
        return False
    
    # O 가 승리
    if check_win(board, "O"):
        if x_counts != o_counts:
            return False
        return True

    # X 가 승리
    if check_win(board, "X"):
        if x_counts <= o_counts:
            return False
        return True

    # 아무도 승리하지 않음
    empty_counts = sum(row.count(".") for row in board)
    return empty_counts == 0

if __name__ == "__main__":
    while (s := sys.stdin.readline().strip()) != "end":
        board = [s[i:i+3] for i in range(0, len(s), 3)]
        valid = solution(board)
        if valid:
            print("valid")
        else:
            print("invalid")
