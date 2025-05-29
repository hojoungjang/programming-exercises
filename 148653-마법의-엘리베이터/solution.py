"""
프로그래머스
마법의 엘리베이터
https://school.programmers.co.kr/learn/courses/30/lessons/148653
"""

def solution(storey):
    count = 0
    carry = 0
    while storey > 0:
        storey, digit = divmod(storey, 10)
        digit += carry
        if digit < 5:
            count += digit
            carry = 0
        elif digit == 5:
            if (storey % 10) + 1 > 5:
                carry = 1
            else:
                carry = 0
            count += digit
        else:
            count += 10 - digit
            carry = 1
    return count + carry
