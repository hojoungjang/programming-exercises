"""
백준
배열 복원하기
https://www.acmicpc.net/problem/16967
"""
import sys

def solution(h, w, x, y, b):
    a = [[b[i][j] for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if x <= i < (h+x) and y <= j < (w+y):
                a[i][j] -= a[i-x][j-y]
    return a

if __name__ == "__main__":
    h, w, x, y = map(int, sys.stdin.readline().strip().split(" "))
    b = [[int(num) for num in sys.stdin.readline().strip().split(" ")] for _ in range(h+x)]
    a = solution(h, w, x, y, b)
    for r in a:
        print(" ".join(str(num) for num in r))