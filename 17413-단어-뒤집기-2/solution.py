"""
백준
단어 뒤집기
https://www.acmicpc.net/problem/17413
"""
import sys

def solution(s):
    new_s = []
    
    i = 0
    while i < len(s):
        if s[i] == "<":
            new_s.append(s[i])
            i += 1
            while i < len(s) and s[i-1] != ">":
                new_s.append(s[i])
                i += 1
        elif s[i] == " ":
            new_s.append(s[i])
            i += 1
        else:
            stack = []
            while i < len(s) and s[i] not in [" ", "<"]:
                stack.append(s[i])
                i += 1
            while stack:
                new_s.append(stack.pop())
    
    return "".join(new_s)


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print(solution(s))