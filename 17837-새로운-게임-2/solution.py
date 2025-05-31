import sys

WHITE = 0
RED = 1
BLUE = 2

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

MOVE = {
    RIGHT: (0, 1),
    LEFT: (0, -1),
    UP: (-1, 0),
    DOWN: (1, 0),
}

class Piece:
    def __init__(self, piece_id, r, c, direction):
        self.piece_id = piece_id
        self.r = r
        self.c = c
        self.direction = direction
        self.active = True

    def reverse(self):
        if self.direction == RIGHT:
            self.direction = LEFT
        elif self.direction == LEFT:
            self.direction = RIGHT
        elif self.direction == UP:
            self.direction = DOWN
        elif self.direction == DOWN:
            self.direction = UP

    def __repr__(self):
        return f"{self.direction} {"active" if self.active else "inactive"}"


def solution(n, grid_colors, piece_info):
    round = 0

    grid = [[[] for _ in range(n)] for _ in range(n)]
    pieces = []
    for piece_id, (r, c, d) in enumerate(piece_info):
        piece = Piece(piece_id, r-1, c-1, d)
        pieces.append(piece)
        grid[r-1][c-1].append(piece)

    complete = False
    while round <= 1000 and not complete:
        round += 1

        for piece in pieces:
            r, c = piece.r, piece.c
            dr, dc = MOVE[piece.direction]
            new_r, new_c = r + dr, c + dc
            piece_idx = [idx for idx, p in enumerate(grid[r][c]) if p is piece][0]
            
            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n or grid_colors[new_r][new_c] == BLUE:
                piece.reverse()
                dr, dc = MOVE[piece.direction]
                new_r, new_c = r + dr, c + dc

                if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n or grid_colors[new_r][new_c] == BLUE:
                    continue
                elif grid_colors[new_r][new_c] == WHITE:
                    grid[new_r][new_c].extend(grid[r][c][piece_idx:])
                    grid[r][c] = grid[r][c][:piece_idx]
                elif grid_colors[new_r][new_c] == RED:
                    grid[new_r][new_c].extend(grid[r][c][piece_idx:][::-1])
                    grid[r][c] = grid[r][c][:piece_idx]
                
            elif grid_colors[new_r][new_c] == WHITE:
                grid[new_r][new_c].extend(grid[r][c][piece_idx:])
                grid[r][c] = grid[r][c][:piece_idx]

            elif grid_colors[new_r][new_c] == RED:
                grid[new_r][new_c].extend(grid[r][c][piece_idx:][::-1])
                grid[r][c] = grid[r][c][:piece_idx]

            for p in grid[r][c]:
                p.r = r
                p.c = c
            
            for p in grid[new_r][new_c]:
                p.r = new_r
                p.c = new_c

            if len(grid[new_r][new_c]) >= 4:
                complete = True
                break

    return round if round <= 1000 else -1


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    grid_colors = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    pieces = [tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(k)]
    print(solution(n, grid_colors, pieces))
