import sys
from collections import Counter

def solution(words: list[str], min_len: int) -> list[str]:
    """
    1. only use words with length greater or equal to min_len
    2. higher frequency in the front
    3. longer length in the front
    4. alphabetical
    """
    counts = Counter([word for word in words if len(word) >= min_len])
    return sorted(counts.keys(), key=lambda word: (-counts.get(word, 0), -len(word), word))

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    words = [sys.stdin.readline().strip() for _ in range(n)]
    ordered_words = solution(words, m)
    for word in ordered_words:
        print(word)
