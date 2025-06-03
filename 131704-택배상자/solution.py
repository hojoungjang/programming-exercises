"""
프로그래머스
택배상자
https://school.programmers.co.kr/learn/courses/30/lessons/131704
"""

def solution(order):
    stack = []
    box_idx = 0
    cnt = 0
    
    for box_order in range(len(order)):
        ith_box = order[box_order] - 1
        
        while box_idx < len(order) and (not stack or stack[-1] != ith_box):
            stack.append(box_idx)
            box_idx += 1
            
        if not stack or stack[-1] != ith_box:
            break
        
        stack.pop()
        cnt += 1
        
    return cnt
