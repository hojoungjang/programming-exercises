"""
백준 
https://www.acmicpc.net/problem/12100

구현 로직이 쉽지도 어렵지도 않지만 상당히 헷갈렸다. 게다가 코드도 
너무 장황하게 작성해 버그를 내기 쉬고 디버깅은 어려운 결과를 초래했다.
"""

import sys
sys.setrecursionlimit(2000)

def solution(n, board):

    def up(board):
        new_board = [[num for num in row] for row in board]

        # move
        for c in range(len(board[0])):
            new_r = 0
            for r in range(len(board)):
                if new_board[r][c] == 0:
                    continue
                new_board[new_r][c] = new_board[r][c]
                new_r += 1
            for r in range(new_r, len(board)):
                new_board[r][c] = 0

        # combine
        for c in range(len(board[0])):
            r = 0
            while r + 1 < len(board):
                if new_board[r][c] == new_board[r+1][c]:
                    new_board[r][c] *= 2
                    new_board[r+1][c] = 0
                    r += 2
                else:
                    r += 1

        # move
        for c in range(len(board[0])):
            new_r = 0
            for r in range(len(board)):
                if new_board[r][c] == 0:
                    continue
                new_board[new_r][c] = new_board[r][c]
                new_r += 1
            for r in range(new_r, len(board)):
                new_board[r][c] = 0

        return new_board

    def down(board):
        new_board = [[num for num in row] for row in board]

        for c in range(len(board[0])):
            new_r = len(board)-1
            for r in range(len(board)-1, -1, -1):
                if new_board[r][c] == 0:
                    continue
                new_board[new_r][c] = new_board[r][c]
                new_r -= 1
            for r in range(new_r, -1, -1):
                new_board[r][c] = 0

        # combine
        for c in range(len(board[0])):
            r = len(board)-1
            while r > 0:
                if new_board[r][c] == new_board[r-1][c]:
                    new_board[r][c] *= 2
                    new_board[r-1][c] = 0
                    r -= 2
                else:
                    r -= 1

        for c in range(len(board[0])):
            new_r = len(board)-1
            for r in range(len(board)-1, -1, -1):
                if new_board[r][c] == 0:
                    continue
                new_board[new_r][c] = new_board[r][c]
                new_r -= 1
            for r in range(new_r, -1, -1):
                new_board[r][c] = 0
        return new_board
    
    def left(board):
        new_board = [[num for num in row] for row in board]

        for r in range(len(board)):
            new_c = 0
            for c in range(len(board[0])):
                if new_board[r][c] == 0:
                    continue
                new_board[r][new_c] = new_board[r][c]
                new_c += 1
            for c in range(new_c, len(board[0])):
                new_board[r][c] = 0

        for r in range(len(board)):
            c = 0
            while c + 1 < len(board[0]):
                if new_board[r][c] == new_board[r][c+1]:
                    new_board[r][c] *= 2
                    new_board[r][c+1] = 0
                    c += 2
                else:
                    c += 1

        for r in range(len(board)):
            new_c = 0
            for c in range(len(board[0])):
                if new_board[r][c] == 0:
                    continue
                new_board[r][new_c] = new_board[r][c]
                new_c += 1
            for c in range(new_c, len(board[0])):
                new_board[r][c] = 0
        return new_board
    
    def right(board):
        new_board = [[num for num in row] for row in board]
        
        for r in range(len(board)):
            new_c = len(board[0])-1
            for c in range(len(board[0])-1, -1, -1):
                if new_board[r][c] == 0:
                    continue
                new_board[r][new_c] = new_board[r][c]
                new_c -= 1
            for c in range(new_c, -1, -1):
                new_board[r][c] = 0

        for r in range(len(board)):
            c = len(board[0]) - 1
            while c > 0:
                if new_board[r][c] == new_board[r][c-1]:
                    new_board[r][c] *= 2
                    new_board[r][c-1] = 0
                    c -= 2
                else:
                    c -= 1
        
        for r in range(len(board)):
            new_c = len(board[0])-1
            for c in range(len(board[0])-1, -1, -1):
                if new_board[r][c] == 0:
                    continue
                new_board[r][new_c] = new_board[r][c]
                new_c -= 1
            for c in range(new_c, -1, -1):
                new_board[r][c] = 0
        return new_board

    def move(board, round=0):
        max_num = max(max(row) for row in board)
        if round == 5:
            return max_num
        for action in [up, left, down, right]:
            max_num = max(max_num, move(action(board), round+1))
        return max_num

    return move(board)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    board = [[i for i in map(int, sys.stdin.readline().strip(" ").split(" "))] for _ in range(n)]
    print(solution(n, board))

