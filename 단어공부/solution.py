"""
백준
단어공부
https://www.acmicpc.net/problem/1157
"""

import sys
from collections import Counter

def solution(word: str)-> str:
    char_counts = Counter(word.lower())
    max_char = "?"
    max_count = 0
    for char, count in char_counts.items():
        if count > max_count:
            max_count = count
            max_char = char
        elif count == max_count:
            max_char = "?"
    return max_char.upper()

if __name__ == "__main__":
    word = sys.stdin.readline().strip()
    print(solution(word))
