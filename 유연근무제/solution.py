"""
프로그래머스
유연근무제
https://school.programmers.co.kr/learn/courses/30/lessons/388351
"""

def solution(schedules, timelogs, startday):
    """
    schedules 목표 출근 시간
    timelogs  실제 출근 시간들 일주일 단위
    startday 시작일
    
    토요일(6) 일요일(7)은 영향 무 
    """
    n = len(schedules)
    cnt = 0

    for i in range(n):
        start = schedules[i]
        h, m = divmod(start, 100)
        extra_h, m = divmod(m + 10, 60)
        end = (h + extra_h) * 100 + m
        
        for day_idx, time in enumerate(timelogs[i]):
            if (startday + day_idx) % 7 in (6, 0):
                continue
            if time > end:
                break
        else:
             cnt += 1   
        
    return cnt
