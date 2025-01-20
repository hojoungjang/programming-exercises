"""
백준
컨베이어 벨트 위의 로봇
https://www.acmicpc.net/problem/20055

문제 설명이 헷갈리는 요소가 있는편이다.
예를 들어 로봇은 정확히 언제 올라가고 내려가는지, 문제에서
말하는 단계는 정확히 무엇인지 등.
문제를 몇번 더 읽어보면 명확해진다.

단순 구현문제인데 생각보다 애를 먹었다. 특히 로테이션 부분을
구현할때 인덱스 값을 업데이트 해주는 부분이 계속 머리속에서
혼란을 주었는데 어찌저찌 구현을 해서 통과하는 코드를 작성했다.

다른분들 풀이를 참고해봤는데 queue 를 (정확히 말하면 double-ended queue)
사용해서 풀이하는 방법이었다. double-ended queue 는 앞뒤로 원소들을 붙이거나
땔 수 있어서 배열형식의 데이터를 왼쪽/오른쪽으로 돌릴때 매우 편리한다는걸 배웠다.

심지어 파이썬 deque 구현체는 원소들의 순서를 돌리는 rotate 메서드를 제공하기도 한다.
이렇게 하니 구현이 훨씬 간단하고 깔끔해졌다.
"""
import sys
from collections import deque

def solution(n, k, belt):
    def move_robots():
        robots[n-1] = 0
        for i in reversed(range(n-1)):
            if robots[i] == 0:
                continue
            if belt_q[i+1] > 0 and robots[i+1] == 0:
                belt_q[i+1] -= 1
                robots[i+1] = 1
                robots[i] = 0
        robots[n-1] = 0
    
    """Solution Main Function"""
    stage = 0
    belt_q = deque(belt)
    robots = deque([0 for _ in range(2*n)])

    while belt_q.count(0) < k:
        # move belt
        belt_q.rotate(1)
        robots.rotate(1)

        # move robots
        move_robots()

        # put new robot
        if belt_q[0] > 0:
            robots[0] = 1
            belt_q[0] -= 1

        stage += 1
    return stage


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    belt = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    print(solution(n, k, belt))