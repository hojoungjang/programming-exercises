"""
백준
팰린드롬 만들기
https://www.acmicpc.net/problem/1213
"""

import sys
from collections import deque

NUM_OF_ALPHABETS = 26

def to_index(char):
    return ord(char) - ord("A")

def solution(name):
    counts = [0 for _ in range(NUM_OF_ALPHABETS)]
    for char in name:
        counts[to_index(char)] += 1
    
    str_builder = deque()
    if len(name) % 2 == 1:
        for i, count in enumerate(counts):
            if count % 2 == 1:
                str_builder.append(chr(i + ord("A")))
                counts[i] -= 1
                break
        else:
            return "I'm Sorry Hansoo"
    
    for i in reversed(range(len(counts))):
        count = counts[i]
        if count % 2 != 0:
            return "I'm Sorry Hansoo"

        for _ in range(0, count, 2):
            str_builder.appendleft(chr(i + ord("A")))
            str_builder.append(chr(i + ord("A")))
    
    return "".join(str_builder)

if __name__ == "__main__":
    name = sys.stdin.readline().strip()
    print(solution(name))