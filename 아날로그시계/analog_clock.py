"""
프로그래머스
아날로그 시계
https://school.programmers.co.kr/learn/courses/30/lessons/250135

소수 계산에 주의 할 것
코드 구현에 따라 로직은 맞아도 소수점 문제 때문에 틀릴 수 있음
"""

HOUR_DEG_PER_SEC = 1 / 120
MIN_DEG_PER_SEC = 1 / 10
SEC_DEG_PER_SEC = 6

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def solution(h1, m1, s1, h2, m2, s2):
    sec1 = to_seconds(h1, m1, s1)
    sec2 = to_seconds(h2, m2, s2)
    cnt = 1 if sec1 == 0 or sec1 == (12 * 60 * 60) else 0
    
    for sec in range(sec1, sec2):
        h_deg = (sec * HOUR_DEG_PER_SEC) % 360
        m_deg = (sec * MIN_DEG_PER_SEC) % 360
        s_deg = (sec * SEC_DEG_PER_SEC) % 360 
        
        new_h_deg = ((sec + 1) * HOUR_DEG_PER_SEC) % 360
        new_m_deg = ((sec + 1) * MIN_DEG_PER_SEC) % 360
        new_s_deg = ((sec + 1) * SEC_DEG_PER_SEC) % 360
        
        if new_h_deg == 0: new_h_deg = 360
        if new_m_deg == 0: new_m_deg = 360
        if new_s_deg == 0: new_s_deg = 360
        
        if s_deg < m_deg < new_m_deg <= new_s_deg:
            cnt += 1
        if s_deg < h_deg < new_h_deg <= new_s_deg:
            cnt += 1
        if new_h_deg == new_m_deg == new_s_deg:
            cnt -= 1
    return cnt


if __name__ == "__main__":
    print(solution(0, 0, 0, 23, 59, 59))
