"""
백준
뒤집기
https://www.acmicpc.net/problem/1439
"""
import sys

def solution(num_str):
    if not num_str:
        return 0
    
    zeros = 0
    ones = 0
    if num_str[0] == "0":
        zeros += 1
    else:
        ones += 1

    for i in range(1, len(num_str)):
        if num_str[i] != num_str[i-1]:
            if num_str[i] == "0":
                zeros += 1
            else:
                ones += 1
    
    return min(zeros, ones)

if __name__ == "__main__":
    num_str = sys.stdin.readline().strip()
    print(solution(num_str))