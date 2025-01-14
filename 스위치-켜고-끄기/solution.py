"""
백준
스위치 켜고 끄기
https://www.acmicpc.net/problem/1244

주어진 문제에서는 입력값아랑 설명이 모두 1-index 이다.
즉 첫번째 스위치의 위치를 1 로 표기한다.

하지만 나는 switches 라는 배열 (list) 을 만들었고
0-index 를 통해 각 원소를 접근한다. 

남학생의 스위치 변경 로직에서 for loop 끝 범위 값에서
0-index 를 사용해서 계속 실패가 나왔다. 오히려 이런 사소한것들이
찾기 어렵고 시간을 많이 잡아 먹는다. 되도록이면 이런 실수를 하지
않게 방어적으로 코딩하는것도 하나의 방법이겠다. 예를들어 switches
배열에 더미 값 하나를 넣어 1-index 처럼 다룰수도 있다.

그리고 문제를 제대로 읽지 않은 탓에 출력 형식을 무시하는 바람에
제출시 통과하지 못했다. 물론 이런건 입출력을 직접 다루는 실제 코딩테스트에서는 
큰 문제가 되지 않을것이라고 생각한다.
"""
import sys

def toggle_male(switches, num):
    for i in range(num, len(switches) + 1, num):
        switches[i-1] = 0 if switches[i-1] else 1

def toggle_female(switches, num):
    idx = num - 1
    lo, hi = idx - 1, idx + 1
    while 0 <= lo and hi < len(switches) and switches[lo] == switches[hi]:
        lo -= 1
        hi += 1
    
    for idx in range(lo + 1, hi):
        switches[idx] = 0 if switches[idx] else 1
    
def solution(switches, students):
    for gender, num in students:
        if gender == 1:
            toggle_male(switches, num)
        if gender == 2:
            toggle_female(switches, num)

if __name__ == "__main__":
    _ = int(sys.stdin.readline().strip())
    switches = list(map(int, sys.stdin.readline().strip().split()))
    n = int(sys.stdin.readline().strip())
    students = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

    solution(switches, students)

    for idx in range(0, len(switches), 20):
        print(" ".join([str(num) for num in switches[idx:idx+20]]))
