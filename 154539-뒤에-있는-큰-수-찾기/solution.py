"""
프로그래머스
뒤에 있는 큰 수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/154539
"""

INDEX = 0
VALUE = 1

def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    
    for i, num in enumerate(numbers):
        while stack and stack[-1][VALUE] < num:
            idx, _ = stack.pop()
            answer[idx] = num
        stack.append((i, num))
    
    while stack:
        idx, _ = stack.pop()
        answer[idx] = -1
    
    return answer
