"""
프로그래머스
롤케이크 자르기
https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""
def solution(topping):
    topping1 = {}
    topping2 = {}
    
    for top in topping:
        if top not in topping2:
            topping2[top] = 0
        topping2[top] += 1
    
    cnt = 0
    
    for top in topping:
        if top not in topping1:
            topping1[top] = 0
        topping1[top] += 1
        topping2[top] -= 1
        if topping2[top] == 0:
            topping2.pop(top)
            
        if len(topping1) == len(topping2):
            cnt += 1
    
    return cnt
