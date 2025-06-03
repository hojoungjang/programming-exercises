import sys

def solution(ladder):
    rows = len(ladder)
    cols = len(ladder[0])
    min_used = float("inf")

    def is_success():
        for orig_c in range(cols):
            c = orig_c
            r = 0

            while r < rows:
                if ladder[r][c] != -1:
                    c = ladder[r][c]
                r += 1
            
            if c != orig_c:
                return False
        
        return True

    def _solution(r, c, used):
        nonlocal min_used

        if c == cols:
            c = 0
            r += 1

        if r == rows or used >= 3:
            return
        
        if c < cols-1 and ladder[r][c] == -1:
            ladder[r][c], orig_rc = c+1, ladder[r][c]
            ladder[r][c+1], orig_rc_next = c, ladder[r][c+1]

            if is_success():
                min_used = min(min_used, used + 1)
                ladder[r][c] = orig_rc
                ladder[r][c+1] = orig_rc_next
                return
            
            _solution(r, c+2, used+1)

            ladder[r][c] = orig_rc
            ladder[r][c+1] = orig_rc_next

        _solution(r, c+1, used)

    if is_success():
        return 0
    _solution(0, 0, 0)
    return min_used if min_used != float("inf") else -1


if __name__ == "__main__":
    """
    n: number of vertical lines
    m: number of connections
    h: number of horizontal lines
    """
    n, m, h = map(int, sys.stdin.readline().strip().split(" "))
    ladder = [[-1 for _ in range(n)] for _ in range(h)]
    for _ in range(m):
        row, col = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split(" "))
        ladder[row][col] = col+1
        ladder[row][col+1] = col
    
    print(solution(ladder))