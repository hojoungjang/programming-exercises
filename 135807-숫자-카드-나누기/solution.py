"""
프로그래머스
숫자 카드 나누기
https://school.programmers.co.kr/learn/courses/30/lessons/135807
"""

def gcd(num1, num2):
    num1, num2 = max(num1, num2), min(num1, num2)
    
    if num2 == 0:
        return num1
    
    r = num1 % num2
    return gcd(num2, r)


def all_undivisible(nums, divisor):
    return all([(num % divisor) != 0 for num in nums])


def solution(arrayA, arrayB):
    gcd_a = arrayA[0]
    for num in arrayA[1:]:
        gcd_a = gcd(gcd_a, num)
        
    divisors_a = []
    for i in range(2, int(gcd_a ** 0.5) + 1):
        if gcd_a % i == 0:
            divisors_a.append(i)
    
    gcd_b = arrayB[0]
    for num in arrayB[1:]:
        gcd_b = gcd(gcd_b, num)
    
    divisors_b = []
    for i in range(2, int(gcd_b ** 0.5) + 1):
        if gcd_b % i == 0:
            divisors_b.append(i)
    
    divisors_a.append(1)
    divisors_b.append(1)
    divisors_a = divisors_a[::-1]
    divisors_b = divisors_b[::-1]
    
    while divisors_a or divisors_b:
        if gcd_a > gcd_b or not divisors_b:
            if all_undivisible(arrayB, gcd_a):
                return gcd_a
            if divisors_a:
                gcd_a //= divisors_a[-1]
                divisors_a.pop()
        else:
            if all_undivisible(arrayA, gcd_b):
                return gcd_b
            if divisors_b:
                gcd_b //= divisors_b[-1]
                divisors_b.pop()
    
    return 0
