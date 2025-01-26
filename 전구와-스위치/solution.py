"""
백준
전구와 스위치
https://www.acmicpc.net/problem/2138

처음에는 BFS 형태로 시작 상태에서 결과상태까지
최단 방법으로 도달하는 방법을 찾는 것인줄 알았다.

하지만 이럴경우 고려해야되는 경우의 수가 너무 많다.
그리고 문제 특성상 큐에 다음 경우를 넣을때마다 배열을
복사해야되는 비효율적인면도 존재한다. 이부분을 비트 연산으로
해볼까 생각도 해보았지만 결국 큰도움이 되지 않는게 애초에
경우의 수가 너무 많다.

힌트를 참고하고도 도무지 솔루션을 생각해내지 못해서 풀이방법을
보고 풀었다. 이 문제는 그리디 알고리즘을 통해 푸는것이었다.
그리디 알고리즘은 가끔 hit-or-miss 성향이 강해서 안보일때는
절대 풀이방법이 생각이 나지않는다는 특징이 개인적으로 있다고 
생각한다.

어쨋든 왼쪽 끝에서 시작하면서 전구의 값을 하나하나 변경시킬려고하면
해당 전구를 변경시킬수 있는 경우는 그 전구의 오른쪽 전구뿐이라는
점을 이용해서. 왼쪽부터 차례로 전구값을 변경해서 최종 값이 
목표값이랑 동일하게 나오는지 확인한다.
"""
import sys

def solution(start, end, count=0):
    state = [bulb for bulb in start] + ["0"]

    for i in range(1, len(start)):   
        if state[i-1] == end[i-1]:
            continue
        
        state[i-1] = "0" if state[i-1] == "1" else "1"
        state[i] = "0" if state[i] == "1" else "1"
        state[i+1] = "0" if state[i+1] == "1" else "1"
        count += 1

    if "".join(state[:-1]) == end:
        return count
    return -1

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    
    start = sys.stdin.readline().strip()
    end = sys.stdin.readline().strip()
    ans1 = solution(start, end)

    _start = ""
    for i in range(2):
        _start += "0" if start[i] == "1" else "1"

    start = _start + start[2:]
    ans2 = solution(start, end, 1)

    if ans1 != -1:
        print(ans1)
    elif ans2 != -1:
        print(ans2)
    else:
        print(-1)
