"""
백준
N과 M (2)
https://www.acmicpc.net/problem/15650
"""

import sys

def solution(n, m):
    
    def combine(num):
        if len(seq) == m:
            print(" ".join(str(val) for val in seq))
            return
        
        if num > n:
            return
        
        seq.append(num)
        combine(num + 1)
        seq.pop()
        combine(num + 1)
    
    seq = []
    combine(1)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    solution(n, m)
