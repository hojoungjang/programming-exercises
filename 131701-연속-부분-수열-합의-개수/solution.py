"""
프로그래머스
연속 부분 수열 합의 개수
https://school.programmers.co.kr/learn/courses/30/lessons/131701
"""

def solution(elements):
    sum_set = set()
    
    for size in range(1, len(elements)+1):
        num_sum = sum(elements[:size])
        start = 0
        while start < len(elements):
            end = (start + size) % len(elements)
            num_sum = num_sum + elements[end] - elements[start]
            sum_set.add(num_sum)
            start += 1
                
    return len(sum_set)
