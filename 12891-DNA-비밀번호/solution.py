"""
백준
비밀번호
https://www.acmicpc.net/problem/12891
"""

import sys

DNA_CHAR_IDX = {"A": 0, "C": 1, "G": 2, "T": 3}

def valid(sub_str_counts, counts):
    for sub_count, count in zip(sub_str_counts, counts):
        if sub_count < count:
            return False
    return True

def solution(dna, length, counts):
    sub_str_counts = [0 for _ in range(len(DNA_CHAR_IDX))]
    for char in dna[:length]:
        sub_str_counts[DNA_CHAR_IDX[char]] += 1

    ans = 1 if valid(sub_str_counts, counts) else 0

    for i in range(length, len(dna)):
        sub_str_counts[DNA_CHAR_IDX[dna[i-length]]] -= 1
        sub_str_counts[DNA_CHAR_IDX[dna[i]]] += 1
        if valid(sub_str_counts, counts):
            ans += 1
    return ans

if __name__ == "__main__":
    s, p = map(int, sys.stdin.readline().strip().split(" "))
    dna = sys.stdin.readline().strip()
    counts = tuple(map(int, sys.stdin.readline().strip().split(" ")))
    print(solution(dna, p, counts))
