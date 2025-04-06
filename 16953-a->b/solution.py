import sys

def solution(a, b):
    cnt = 0
    while b > a:
        first_digit = b % 10
        if first_digit % 2 == 1 and first_digit != 1:
            return -1
        
        if first_digit == 1:
            b //= 10
        else:
            b //= 2
        cnt += 1

    return cnt+1 if a == b else -1

if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    print(solution(a, b))