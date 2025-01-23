"""
백준
용액
https://www.acmicpc.net/problem/2467

이 문제는 의외로 간단하다.
배열은 이미 오름차순으로 정렬이 되어있고 배열안에 두수의 합이 최대한 0 에 가까워야하기 때문에
두수의 합이 0 이되는 조합을 찾는다는 목표로 배열의 양쪽 끝에 있는 두수를 골라 점점 안으로
인덱스를 좁혀가는 식으로 풀면된다.

두수의 합이 0 보다 작은 경우, 합이 더 커자야 함으로 왼쪽 인덱스를 오른쪽으로 당기고
두수의 합이 0 보다 큰 경우, 합이 더 작아져야 함으로 오른쪽 인덱스를 왼쪽으로 당긴다.
"""
import sys

def solution(nums):
    lo, hi = 0, len(nums) - 1
    num1, num2 = nums[lo], nums[hi]

    while lo < hi:
        total = nums[lo] + nums[hi]
        if abs(total) < abs(num1 + num2):
            num1 = nums[lo]
            num2 = nums[hi]
        if total < 0:
            lo += 1
        elif total > 0:
            hi -= 1
        else:
            break
    return num1, num2

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    num1, num2 = solution(nums)
    print(f"{num1} {num2}")
