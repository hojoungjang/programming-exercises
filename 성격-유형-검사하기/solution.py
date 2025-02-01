"""
프로그래머스
성격 유형 검사하기
https://school.programmers.co.kr/learn/courses/30/lessons/118666

구현 문제이다. 문제 설명이 길고 중간중간 사소하지만 정답에 차질을 줄 수 있는 디테일이
숨어있기 때문에 이부분을 조심해야 한다.

코드로 풀어내는 난이도는 낮다. 문제를 잘 이해하고 그대로 구현하면 된다. 스코어를 알맞게
합산하고 각 항목끼리 비교하여 문자열을 만든다. MBTI 를 알면 좀 더 문제를 설명이 
친숙하게 다가올 것 같다.

점수 계산 부분을 modular 연산을 써서 좀 간략하게 작성하려고 했는데 더 좋은 방법이
있을지 모르겠다.
"""

def solution(survey, choices):
    scores = {t: 0 for t in ["R", "T", "C", "F", "J", "M", "A", "N"]}
    
    for criteria, choice in zip(survey, choices):
        type_idx, degree = divmod(choice, 4)
        
        if degree == 0:
            continue
        
        t = criteria[type_idx]
        score = 4 - degree if type_idx == 0 else degree
        scores[t] += score
        
    result = []
    if scores["R"] >= scores["T"]:
        result.append("R")
    else:
        result.append("T")
        
    if scores["C"] >= scores["F"]:
        result.append("C")
    else:
        result.append("F")
        
    if scores["J"] >= scores["M"]:
        result.append("J")
    else:
        result.append("M")
        
    if scores["A"] >= scores["N"]:
        result.append("A")
    else:
        result.append("N")

    return "".join(result)