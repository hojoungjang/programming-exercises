"""
백준
A와 B 2
https://www.acmicpc.net/problem/12919

모든 경우의 수를 계산할 경우 그 만큼 시간이 오래걸린다.
입력의 크기를 고려해 문자열의 패턴이 있을지 고민하였고
다음 특징을 찾아냈다.

s 가 t 로 만들어질 수 있을 경우
1. t 안에 s 가 정방향 또는 거꾸로 뒤집힌 형태로 sub-string 으로 있다
2. t 안에 있는 s 를 중심으로 t 를 반으로 나눴을 때
   왼쪽과 오른쪽 sub-string 은 특정한 특징이 있다.

둘다 중심을 기점으로 "A" 가 0개 이상 있고 "B" 가 있는 형태인데
이때 s 가 뒤집힌 형태면 "B" 가 홀수개 정방향이면 짝수개 추가가 되었다는
특징도 있다. 이점을 이용하면 왼쪽, 오른쪽 substring 에 대해 유효성 검사를
할 수 있다.

다른분들의 풀이도 참고해 보았는데 대부분 BFS 형식으로 풀었다. 
왜 생각하지 못 했을까 ㅜㅠ. BFS 키워드만 참고해 처음에는 s 에서 t 로 가는 방법으로
풀었는데 이때 경우의 수가 많아져서 시간복잡도가 크다. 좀 더 힌트를 얻어 t 에서 s로 
가는 방법으로 풀었는데 프로그램이 훨씬 빨랐다. 

처음에는 이해가 가지 않았다. s 에서 t 나 t 에서 s 나 경우의 수는 똑같지 않은가?
좀 더 고민해보니 t 에서 s 로 갈때는 문자를 지우면서 가야하기 때문에 조건이 맞아야지만
경우의 수를 고려한다. 예를 들어 B 가 오른쪽 맨끝에 있을때는 지우지 못한다. 왜나하면
B 추가 작업의 역순으로 지우기 작업도 진행이 되어야 하기 때문이다. 그러므로 문자열이 먼저
뒤집히고 거기서 맨 오른쪽에 있는 B를 때어낼 수 있다. 때문에 역으로 가는 경우는
확인할 수 있는 경우가 제한이 되어 시간 복잡도가 문제의 조건 사항을 통과 할 수 있다.
"""
import sys
from collections import deque

def solution(s, t):
    level = len(t)
    queue = deque([t, None])
    visited = set([t])

    while queue:
        t_prime = queue.popleft()

        if t_prime is None:
            level -= 1
            if level < len(s):
                break
            if queue:
                queue.append(None)
            continue
    
        if t_prime == s:
            return 1

        if t_prime[-1] == "A":
            t_prime_a = t_prime[:-1]
            if t_prime_a not in visited:
                visited.add(t_prime_a)
                queue.append(t_prime_a)
        if t_prime[0] == "B":
            t_prime_b = t_prime[len(t_prime)-1:0:-1]
            if t_prime_b not in visited:
                visited.add(t_prime_b)
                queue.append(t_prime_b)
    
    return 0

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    print(solution(s, t))
