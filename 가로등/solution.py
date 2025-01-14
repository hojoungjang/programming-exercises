"""
백준
크로스 컨트리
https://www.acmicpc.net/problem/9017

한번에 통과하지 못했는데, 그 이유는 round() 함수 때문이었다.
파이썬 round() 함수는 bankers' rounding 이라고 해서
주어진 숫자가 정확히 두 정수의 중간 (즉 xxx.5) 일떄 제일 가까운
짝수 정수로 내림/올림이 된다.

예를 들어 2.5 는 2 3.5 는 4 이런식으로 우리가 생각하는 반올림은
아니다. 그래서 실제 구현에 필요한 올림을 적용하기 위해 math.ceil()
사용했다.
"""

import sys
from math import ceil

def solution(n, lamp_indices):
    # min height to cover inter-lamp distances
    min_height = 0
    for i in range(1, len(lamp_indices)):
        height = ceil((lamp_indices[i] - lamp_indices[i-1]) / 2)
        min_height = max(min_height, height)

    # check if edges are covered
    if not (lamp_indices[0] - min_height <= 0 <= lamp_indices[0]):
        min_height = lamp_indices[0]
    
    if not (lamp_indices[-1] <= n <= lamp_indices[-1] + min_height):
        min_height = n - lamp_indices[-1]

    return min_height

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    # lamp_indices are ordered numbers
    lamp_indices = list(map(int, sys.stdin.readline().strip().split(" ")))
    print(solution(n, lamp_indices))