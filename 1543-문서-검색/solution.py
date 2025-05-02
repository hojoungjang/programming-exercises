"""
백준
문서 검색
https://www.acmicpc.net/problem/1543
"""

import sys

def solution(doc, search):
    idx = 0
    cnt = 0
    while idx < len(doc):
        if doc[idx:idx + len(search)] == search:
            cnt += 1
            idx += len(search)
        else:
            idx += 1
    return cnt

if __name__ == "__main__":
    doc = sys.stdin.readline().strip()
    search = sys.stdin.readline().strip()
    print(solution(doc, search))
