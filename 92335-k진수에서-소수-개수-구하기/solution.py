"""
https://school.programmers.co.kr/learn/courses/30/lessons/92335
"""

def convert(num, base):
    digits = []
    while num:
        q, r = divmod(num, base)
        digits.append(r)
        num = q
    return digits[::-1]

def is_prime(num):
    if num == 1:
        return False
    
    cnt = 0
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            cnt += 1
    return True if cnt == 0 else False
    
def solution(n, k):
    digits = convert(n, k)
    end = 0
    cnt = 0
    print(digits)
    
    while end < len(digits):
        num = 0
        
        while end < len(digits) and digits[end] != 0:
            num = num * 10 + digits[end]
            end += 1
        
        print(num)
        
        if is_prime(num):
            cnt += 1
        
        while end < len(digits) and digits[end] == 0:
            end += 1

    return cnt
