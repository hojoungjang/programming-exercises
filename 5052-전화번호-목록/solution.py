"""
백준
전화번호 목록
https://www.acmicpc.net/problem/5052
"""
import sys

def solution(nums):
    nums.sort()
    seen = set()

    for num in nums:
        for i in range(1, len(num)):
            if num[:i] in seen:
                return False
        seen.add(num)

    return True


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = [sys.stdin.readline().strip() for _ in range(n)]
        if solution(nums):
            print("YES")
        else:
            print("NO")
