"""
백준
IOIOI
https://www.acmicpc.net/problem/5525
"""
import sys

def get_ioi_len(s, i):
    if s[i] == "O":
        return 0
    
    l = 0
    while i + 2 < len(s):
        if s[i+1] == "O" and s[i+2] == "I":
            l += 1
        else:
            return l
        i += 2
    return l

def solution(s, n):
    cnt = 0
    i = 0
    while i < len(s):
        length = get_ioi_len(s, i)
        if length >= n:
            cnt += length - n + 1
        
        if length:
            i += 2 * (length - 1) + 3
        else:
            i += 1
    return cnt


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    print(solution(s, n))