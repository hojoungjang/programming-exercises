"""
백준
비슷한 단어
https://www.acmicpc.net/problem/2607
"""

import sys
from collections import Counter

def solution(word: str, cmp_words: list[str]) -> int:
    similar_count = 0
    word_char_counts = Counter(word)

    for cmp_word in cmp_words:
        cmp_word_char_counts = Counter(cmp_word)
        cmp_word_char_counts.subtract(word_char_counts)

        diff_pos_sum = 0
        diff_neg_sum = 0
        for diff in cmp_word_char_counts.values():
            if diff < 0:
                diff_neg_sum += abs(diff)
            else:
                diff_pos_sum += diff
        if max(diff_pos_sum, diff_neg_sum) < 2:
            similar_count += 1

    return similar_count

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    words = [sys.stdin.readline().strip() for _ in range(n)]
    print(solution(words[0], words[1:]))