"""
백준
PPAP
https://www.acmicpc.net/problem/16120
"""

import sys

PPAP = "PPAP"
NP = "NP"

def solution(s):
    stack = []

    for char in s:
        stack.append(char)
        if len(stack) >= len(PPAP) and "".join(stack[len(stack) - len(PPAP):len(stack)]) == PPAP:
            for _ in range(len(PPAP)):
                stack.pop()
            stack.append("P")
    
    if len(stack) != 1 or stack[0] != "P":
        return NP

    return PPAP

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print(solution(s))