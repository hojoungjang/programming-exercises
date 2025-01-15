"""
백준
카드 2
https://www.acmicpc.net/problem/2164

처음에는 수학적으로 접근하는 문제인줄 알고 풀었으나,
또 문제 설명을 임의로 바꿔서 해석하는 실수를 해버렸다.

문제에서는 한 라운드에 두가지 액션을 수행한다고 했다.
1. 맨 위 카드 버리기
2. 그다음 위 카드 맨 뒤로 보내기

어째서인지 나는 임의로 처음시작한 덱에서 모든 홀수번째
카드를 다 버리다고 생각했다. 이렇게 생각하고 진행하면
문제에서 명시한 조건이랑 차이가 생긴다.
"""

import sys
from collections import deque

def solution(n: int) -> int:
    queue = deque((num for num in range(1, n+1)))
    while len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(solution(n))
