"""
백준
성냥개비
https://www.acmicpc.net/problem/3687

모든 방식을 고려하면 아마 대략 10 ^ (n/7) 정도의 시간복잡도가 
나와서 효율적이지 못하다. 풀이법을 고민하면서 성냥의 개수를 점점
키워나가면서 풀이를 하다보니 현재 성냥의 개수로 만들수 있는 가장
큰수는 현재 성냥 개수로 만들수 있는 0 부터 9 까지 숫자 중 하나랑
그 수를 만들고 남은 성냥으로 만들 수 있는 가장 큰수를 이어붙인것중에
가장 큰 수 라는 연관성을 발견했다. 즉 현재의 최적 값은 이전의 최적값으로
표현이 가능해보였고 다이나믹 프로그래밍 유형을 발견했다.

여기까지는 나름 이해도 쉽고 구현도 할만한데 좀 어려웠던 조건이 숫자는 0으로
시작할 수 없다는 것이다. 이 조건은 최소값을 찾을 때 문제가 되는데 성냥 6개로
만들 수 있는 수에서 가장 작은 수는 상황에 따라 달리 해야한다. 이어붙이는 숫자 중
앞에 올 경우 가장 작은 수는 6 이고 뒤에 올경우 0이다.

이부분은 예외를 해결하는 가장 간결하고 쉬운 방법은 두 숫자를 이어붙일때 뒤에 오는
숫자에서의 6은 0이랑 치환해준다. 이걸 작성하면서 든 의문은 "어? 그럼 앞에 있는
숫자 안에서도 첫번째를 제외하고 그 뒤에 붙는 6 도 0으로 치환해주어야 가장 작은 
값을 만들수 있는데 이건 따로 처리를 안해줘도 되나?"

우리는 현재의 최적값을 이전의 상태의 최적값으로 만들기 때문에 이어붙이는 두 숫자의
뒷 숫자만 항상 신경써서 치환하면 자동으로 모든 숫자의 맨 앞자리가 아닌 곳에는 항상 6 대신 0이
오게 할 수 있다.

또 한가지 고민하면서 시간을 많이 허비한 부분은 상태를 저장하는 자료구조의 초기값들과 두수를
이어붙이는 구현 그리고 입력되는 테스트 케이스를 각각 따로 연산 할건지 아니면 상태를 재사용
할거인지 등등. 개인적으로 이것저것 너무 많이 고려하다보면 머리가 복잡해지고 실수를 하기 쉬워진다.
면접이나 코딩테스트 환경에서 시간이 생명이기 때문에 최대한 간단하게 풀어서 통과를 하고 
점진적으로 개선해 나가는법이 훨씬 전략적일것같다.
"""
import sys

MATCH_MAP = {
    2: [1],
    3: [7],
    4: [4],
    5: [2,3,5],
    6: [0,6,9],
    7: [8],
}
MAX_COUNT = 100

def combine(num1: int, num2: int) -> int:
    if num1 == -1 or num1 == float("inf"):
        return num1
    if num2 == -1 or num2 == float("inf"):
        return num2
    return int(str(num1) + str(num2).replace("6", "0"))

def solution(match_counts):
    max_memo = [-1 for _ in range(MAX_COUNT+1)]
    min_memo = [float("inf") for _ in range(MAX_COUNT+1)]

    for key in MATCH_MAP:
        max_memo[key] = MATCH_MAP[key][-1]
        min_memo[key] = MATCH_MAP[key][0] if key != 6 else MATCH_MAP[key][1]

    count = max(match_counts)
    for i in range(2, count+1):
        for key in MATCH_MAP:
            if key > i:
                break
            max_memo[i] = max(max_memo[i], combine(max_memo[key], max_memo[i - key]))
            max_memo[i] = max(max_memo[i], combine(max_memo[i - key], max_memo[key]))
    
    for i in range(2, count+1):
        for key in MATCH_MAP:
            if key > i:
                break
            min_memo[i] = min(min_memo[i], combine(min_memo[key], min_memo[i - key]))
            min_memo[i] = min(min_memo[i], combine(min_memo[i - key], min_memo[key]))

    return [(min_memo[c], max_memo[c]) for c in match_counts]


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    match_counts = [int(sys.stdin.readline().strip()) for _ in range(n)]
    for min_num, max_num in solution(match_counts):
        print(f"{min_num} {max_num}")
