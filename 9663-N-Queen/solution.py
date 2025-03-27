"""
백준
N-Queen
https://www.acmicpc.net/problem/9663
"""
import sys

def diag_rev_idx(r, c):
    return (n-1) - c + r

def solution(n):
    count = 0
    cols = [0 for _ in range(n)]
    diag = [0 for _ in range(2*n)]
    diag_rev = [0 for _ in range(2*n)]


    def collision(r, c):
        if cols[c] == 1:
            return True
        
        if diag[r+c] == 1:
            return True
        
        if diag_rev[diag_rev_idx(r, c)] == 1:
            return True
        
        return False

    def placement(r, queen_cnt):
        nonlocal count

        if queen_cnt == n:
            count += 1
            return
        
        if r >= n:
            return
        
        for c in range(n):
            if not collision(r, c):
                cols[c] = 1
                diag[r+c] = 1
                diag_rev[diag_rev_idx(r, c)] = 1

                placement(r+1, queen_cnt + 1)
                
                cols[c] = 0
                diag[r+c] = 0
                diag_rev[diag_rev_idx(r, c)] = 0
        
    placement(0, 0)
    return count


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(solution(n))
