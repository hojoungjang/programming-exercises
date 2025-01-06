"""
프로그래머스
과제 진행하기
https://school.programmers.co.kr/learn/courses/30/lessons/176962

문자열 시간을 사칙연산이 용이한 숫자 데이터로 변환하는게 도움이 많이 된다. 
심지어 문자열 시간을 추후에 따로 사용하지 않아서 부담없이 변경해서 사용해도 된다.
"""

def time_in_minutes(time_str):
    hour, minute = map(int, time_str.split(":"))
    return hour * 60 + minute

def solution(plans):
    sorted_plans = sorted(plans, key=lambda plan: plan[1])
    for plan in sorted_plans:
        plan[1] = time_in_minutes(plan[1])
        plan[2] = int(plan[2])
        
    stack = []
    complete = []
    idx = 1
    cur_task = sorted_plans[0][0]
    cur_start_time = sorted_plans[0][1]
    cur_end_time = cur_start_time + sorted_plans[0][2]
    
    while idx < len(sorted_plans):
        name, start, playtime = sorted_plans[idx]
        
        if cur_end_time < start:
            complete.append(cur_task)
            if stack:
                name, playtime = stack.pop()
                start = cur_end_time
            else:
                idx += 1
        elif cur_end_time == start:
            complete.append(cur_task)
            idx += 1
        else:
            stack.append((cur_task, cur_end_time - start))
            idx += 1
            
        cur_task = name
        cur_start_time = start
        cur_end_time = start + playtime
            
    complete.append(cur_task)
    complete.extend(plan[0] for plan in stack[::-1])
    return complete