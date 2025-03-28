"""
백준
N과 M (3)
https://www.acmicpc.net/problem/15651
"""

import sys

def solution(n, m):
    
    def combine():
        if len(seq) == m:
            print(" ".join(str(val) for val in seq))
            return
        
        for num in range(1, n+1):
            seq.append(num)
            combine()
            seq.pop()
    
    seq = []
    combine()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    solution(n, m)
