"""
백준
평범한 배낭
https://www.acmicpc.net/problem/12865


너무 어려웠다. 다이내믹 프로그래밍은 매번 좌절하게 된다. 언젠가는 극복할 수 있을까.
풀다가 몇번 뇌정지가 와서 맨붕이였다.

일단 입력의 크기를 보면 모든 경우의 수를 찾는 방식은 적합하지 않다. 따라서 자연스럽게
DP 방식일거라는 생각이 들었다. 고민을 한끝에 나름의 점화식을 세워서 값들을 저장해 나가며
풀이를 해보았지만 완벽한 정답은 아니었다.

방식은 이러했다. 중간 값들을 저장 할 2D 배열을 만드는데 row 와 column 둘다 물건의 개수 (n)
으로 하였다. row 는 물건을 고려했을때 column 은 그때의 물건의 개수를 뜻하게 했다.
나름 열심히 경우의 수를 분석해서 이런식의 유추가 가능할거라고 판단이 되었지만 수학에는 재능이
없는 모양이다.

결국 문제에서 원하는 DP 식을 세우는 방법을 참고해서 풀었다. 이때 row 는 1 부터 k 까지의
가방크기고 column 은 물건의 개수 만큼 만든다. 이 2D 배열이 의미하는 바는 이렇다:
해당 가방 크기일때 물건을 고려했을때의 최적화된 값이다. 이런식으로 생각했을때 만들어지는 
DP 식은 이렇게 된다.

dp[bag_size][i] = max(dp[bag_size][i-1], dp[bag_size - weight_i] + value_i) 

물론 가방크기가 될 경우만 i 번째 물건을 담는 max() 의 두번째 인자를 고려할 수 있다.
"""

import sys

WEIGHT = 0
VALUE = 1

def solution(items, k):
    dp = [[0 for _ in range(len(items) + 1)] for _ in range(k+1)]
    max_val = 0

    for bag_size in range(1, k+1):
        for i in range(len(items)):
            weight, value = items[i]

            dp_idx = i + 1
            dp[bag_size][dp_idx] = dp[bag_size][dp_idx-1]

            if weight > bag_size:
                continue

            dp[bag_size][dp_idx] = max(dp[bag_size][dp_idx], dp[bag_size - weight][dp_idx-1] + value)
            max_val = max(max_val, dp[bag_size][dp_idx])

    return max_val

if __name__ == "__main__":
    """
    n 물품의 개수
    k 준서가 버틸 수 있는 무게
    (weight, value)
    """
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    items = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]
    print(solution(items, k))
