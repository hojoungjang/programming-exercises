"""
백준
색종이 붙이기
https://www.acmicpc.net/problem/17136
"""

import sys

BOARD_SIZE = 10
TOTAL_PAPER = 25

def solution(board):
    def cover(r, c):
        nonlocal ans

        total = sum(sum(row) for row in board)
        papers_left = sum(papers)
        papers_used = TOTAL_PAPER - papers_left
        if total == 0:
            ans = min(ans, papers_used)
            return

        if papers_left == 0 or papers_used >= ans :
            return
        
        if r >= BOARD_SIZE:
            return
        
        offset_r, new_c = divmod(c + 1, BOARD_SIZE)
        new_r = r + offset_r

        if board[r][c] == 1:
            for paper_size in range(1, len(papers)):
                if papers[paper_size] == 0:
                    continue

                if r + paper_size > BOARD_SIZE or c + paper_size > BOARD_SIZE:
                    continue

                if not all(all(val == 1 for val in row[c:c+paper_size]) for row in board[r:r+paper_size]):
                    break

                for paper_r in range(r, r+paper_size):
                    for paper_c in range(c, c+paper_size):
                        board[paper_r][paper_c] = 0
                papers[paper_size] -= 1

                cover(new_r, new_c)

                for paper_r in range(r, r+paper_size):
                    for paper_c in range(c, c+paper_size):
                        board[paper_r][paper_c] = 1
                papers[paper_size] += 1
        else:
            cover(new_r, new_c)

    ####################################################
    ans = TOTAL_PAPER + 1
    papers = [0, 5, 5, 5, 5, 5]
    cover(0, 0)
    return ans if ans < TOTAL_PAPER + 1 else -1


if __name__ == "__main__":
    board = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(BOARD_SIZE)]
    print(solution(board))
