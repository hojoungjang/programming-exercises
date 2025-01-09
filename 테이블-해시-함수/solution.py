"""
프로그래머스
테이블 해시 함수
https://school.programmers.co.kr/learn/courses/30/lessons/147354
"""

def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda row: (row[col-1], -row[0]))
    ans = 0
    for i, row in enumerate(sorted_data[row_begin - 1:row_end], row_begin):
        s_i = 0
        for num in row:
            s_i += num % i
        ans ^= s_i
    return ans
