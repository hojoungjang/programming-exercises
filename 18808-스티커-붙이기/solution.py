import sys

def rotate(sticker, deg=0):
    if deg == 0:
        return [[val for val in row] for row in sticker]
        
    rows = len(sticker)
    cols = len(sticker[0])
    
    if deg == 180:
        new_rows = rows
        new_cols = cols
    elif deg == 90 or deg == 270:
        new_rows = cols
        new_cols = rows

    new_sticker = [[0 for _ in range(new_cols)] for _ in range(new_rows)]

    if deg == 90:
        for new_r, c in enumerate(range(cols)):
            for new_c, r in enumerate(reversed(range(rows))):
                new_sticker[new_r][new_c] = sticker[r][c]

    elif deg == 180:
        for new_r, r in enumerate(reversed(range(rows))):
            for new_c, c in enumerate(reversed(range(cols))):
                new_sticker[new_r][new_c] = sticker[r][c]

    elif deg == 270:
        for new_r, c in enumerate(reversed(range(cols))):
            for new_c, r in enumerate(range(rows)):
                new_sticker[new_r][new_c] = sticker[r][c]
    
    return new_sticker

def solution(rows, cols, stickers):
    
    def fit(sticker, r_lo, r_hi, c_lo, c_hi):
        for r_s, r in enumerate(range(r_lo, r_hi)):
            for c_s, c in enumerate(range(c_lo, c_hi)):
                if grid[r][c] and sticker[r_s][c_s]:
                    return False
        return True
    
    def paste(sticker, r_lo, r_hi, c_lo, c_hi):
        for r_s, r in enumerate(range(r_lo, r_hi)):
            for c_s, c in enumerate(range(c_lo, c_hi)):
                grid[r][c] = grid[r][c] or sticker[r_s][c_s]

    def process_sticker(sticker):
        for r_lo in range(rows):
            for c_lo in range(cols):
                
                rows_sticker = len(sticker)
                cols_sticker = len(sticker[0])
                r_hi = r_lo + rows_sticker
                c_hi = c_lo + cols_sticker

                if r_hi > rows or c_hi > cols:
                    continue
                
                if fit(sticker, r_lo, r_hi, c_lo, c_hi):
                    paste(sticker, r_lo, r_hi, c_lo, c_hi)
                    return True
        return False


    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for sticker in stickers:
        for deg in [0, 90, 180, 270]:
            rot_sticker = rotate(sticker, deg=deg)
            if process_sticker(rot_sticker):
                break

    return sum(row.count(1) for row in grid)

if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().strip().split(" "))
    stickers = []
    for _ in range(k):
        r, c = map(int, sys.stdin.readline().strip().split(" "))
        sticker = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(r)]
        stickers.append(sticker)
    print(solution(n, m, stickers))