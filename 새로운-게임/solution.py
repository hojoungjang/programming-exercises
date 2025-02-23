import sys
from collections import deque

MAX_ITERATION = 1000

class BoardColor:
    WHITE = 0
    RED = 1
    BLUE = 2

class Piece:
    DIRECTIONS = {
        1: (0, 1),
        2: (0, -1),
        3: (-1, 0),
        4: (1, 0),
    }

    def __init__(self, idx, row, col, direction):
        self._id = idx
        self._row = row - 1
        self._col = col - 1
        self._direction = direction
        self.bottom = True

    def get_id(self):
        return self._id

    def get_position(self):
        return self._row, self._col
    
    def get_next_position(self):
        r_offset, c_offset = self.get_direction()
        return self._row + r_offset, self._col + c_offset
    
    def update_position(self, new_row, new_col):
        self._row = new_row
        self._col = new_col
    
    def get_direction(self):
        return self.DIRECTIONS[self._direction]
    
    def flip_direction(self):
        if self._direction == 1:
            self._direction = 2
        elif self._direction == 2:
            self._direction = 1
        elif self._direction == 3:
            self._direction = 4
        elif self._direction == 4:
            self._direction = 3

    def move(self):
        r_offset, c_offset = self.get_direction()
        self._row += r_offset
        self._col += c_offset

    def __repr__(self):
        return f"(Piece: [{self._row}][{self._col}] {self._direction})"
    

def solution(n, board_color, pieces):
    pieces = [Piece(i, r, c, d) for i, (r, c, d) in enumerate(pieces)]
    board = [[deque() for _ in range(n)] for _ in range(n)]

    for piece in pieces:
        r, c = piece.get_position()
        board[r][c].append(piece)

    for iter_idx in range(MAX_ITERATION):

        for piece in pieces:
            if not piece.bottom:
                continue

            next_r, next_c = piece.get_next_position()

            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= n \
              or board_color[next_r][next_c] == BoardColor.BLUE:
                piece.flip_direction()
                next_r, next_c = piece.get_next_position()
                if next_r < 0 or next_r >= n or next_c < 0 or next_c >= n \
                  or board_color[next_r][next_c] == BoardColor.BLUE:
                    continue
            
            cur_r, cur_c = piece.get_position()
            if board_color[next_r][next_c] == BoardColor.RED:
                while board[cur_r][cur_c]:
                    p = board[cur_r][cur_c].pop()
                    p.update_position(next_r, next_c)
                    board[next_r][next_c].append(p)
            else:
                while board[cur_r][cur_c]:
                    p = board[cur_r][cur_c].popleft()
                    p.update_position(next_r, next_c)
                    board[next_r][next_c].append(p)

            for p in board[next_r][next_c]:
                p.bottom = False
            board[next_r][next_c][0].bottom = True
        
            if len(board[next_r][next_c]) >= 4:
                return iter_idx + 1

    return -1


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    board_color = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    pieces = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(k)]
    print(solution(n, board_color, pieces))
