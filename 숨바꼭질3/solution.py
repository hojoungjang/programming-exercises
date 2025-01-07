"""
백준
숨바꼭질 3
https://www.acmicpc.net/problem/13549

처음 접근 방식에서는 현재 숫자에서 뒤에서 보았던 숫자의 결과 값으로 현재 값을 찾는 방식으로 풀었다.
즉 1번 2번의 경우를 찾아서 작은 값을 저장했다.
그리고 마지막에 거꾸로 돌면서 3번의 경우가 더 작으면 저장했다.

이렇게 했을 경우 정 방향으로 순회하면서 1, 2 번 경우를 찾을때 제대로 답이 안 나올 경우도 있다.
그 이유는 3번의 경우가 반영이 되어있지 않기 때문이다.

그래서 초기 설정 값을 넣어줄때 이미 알 수 있는 값들 [0, n] 의 두배가 되는 숫자의 값도 같이 
임시적으로 지정해주고 정방향 순회시 각 숫자에서 1,2,3번의 경우를 모두 비교 후 두배가 되는 숫자에도
찾은 값을 넣어줌으로서 각 단계에서 최소값을 유지해가며 순회하는 상태를 만들수 있다.
"""

import sys

LIMIT = 100_000

def solution(n, k):
    """
    N 에서 시작
    -> N+1, N+2, N+3 ...

    현재 숫자가 number[i] 일때
    1. number[i] - 1
    2. number[i] / 2
    3. number[i] + 1 

    2 번은 number[i] 가 홀수 일때 불가능

    예외
    n > k => 두수의 차 리턴
    """
    if n > k:
        return n - k

    times = [float("inf") for _ in range(LIMIT * 2 + 1)]
    for num in range(n + 1):
        times[num] = n - num
        if n < 2 * num <= LIMIT:
            times[2 * num] = times[num]

    for num in range(n + 1, k+1):
        times[num] = min(times[num], times[num-1] + 1)
        times[num] = min(times[num], times[num+1] + 1)
        if num % 2 == 0:
            times[num] = min(times[num], times[num // 2])
        if 2 * num < len(times):
            times[2 * num] = min(times[2 * num], times[num])

    return times[k]


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split(" "))
    print(solution(n, k))
