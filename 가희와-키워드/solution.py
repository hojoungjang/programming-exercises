"""
백준
가희와 키워드
https://www.acmicpc.net/problem/22233

파이썬 set discard 함수는 키가 존재하지 않아도
exception 이 나지 않아서 이 문제에 사용하기 적합하다.

반면 remove 함수는 키가 없을 때 exception 을 raise
하고 프로그램이 종료된다.
"""
import sys

def solution(words, blog_posts):
    words_set = set(words)
    remaining_counts = []
    for used_words in blog_posts:
        for word in used_words:
            words_set.discard(word)
        remaining_counts.append(len(words_set))
    return remaining_counts

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    words = [sys.stdin.readline().strip() for _ in range(n)]
    blog_posts = [sys.stdin.readline().strip().split(",") for _ in range(m)]
    remain_counts = solution(words, blog_posts)
    for c in remain_counts:
        print(c)