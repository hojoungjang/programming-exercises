"""
숫자고르기
https://www.acmicpc.net/problem/2668

문제에서 원하는게 코드상으로 무엇인지 생각해보았다.
분명 싸이클이 생기는 유형을 골라내는것인데 조금 다른부분은
각 인덱스가 동일한 값을 가질수도 있다는 점 그리고 그냥
싸이클이 아니라 시작과 끝이 같은 싸이클이다. 싸이클이
중간 지점하고 이어진다면 해당 시작점은 고려할 수 없음.
"""

import sys

def solution(nums):
    nums_mod = [0] + nums
    ans = []

    for start_num in range(1, len(nums_mod)):
        visited = set()
        next_num = start_num
        while next_num not in visited:
            visited.add(next_num)
            next_num = nums_mod[next_num]
        if next_num == start_num:
            ans.append(start_num)
    
    return ans


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
    ans = solution(nums)
    print(len(ans))
    for num in ans:
        print(num)
