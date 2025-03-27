"""
백준
N과 M
https://www.acmicpc.net/problem/15649
"""

import sys

def solution(n, m):

    def combination():
        if len(seq) == m:
            print(" ".join(str(val) for val in seq))
            return
        
        for num in range(1, n+1):
            if num in used:
                continue

            used.add(num)

            seq.append(num)
            combination()
            seq.pop()

            used.remove(num)

    seq = []
    used = set()
    combination()
    

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    solution(n, m)
