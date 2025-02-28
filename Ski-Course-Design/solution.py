"""
백준
ski course design
https://www.acmicpc.net/problem/9881

대략 난감하다. 난이도는 높지 않다고 되어있는데, 풀이법이 보이지 않았다.
정렬하고 최소값하고 최대값 차이를 구해서 threshold 값하고 비교하고 
그 차의 반을 각각 최소값하고 최댓값에서 빼주는 건가? 하고 생각도 해보고
그러면 만약 그 다음 최소값이나 최댓값의 차이가 threshold 보다 크면 어쩌지?

막 뭔가 딱 떨어지지 않는 풀이법 밖에 생각나지 않아서 멘붕...
좀 힌트를 얻어서 그냥 브루트포스로 푸는 문제라고 되어있고 높이의 입력 범위가
0 에서 100이라는 점을 이용해서 모든 최소값과 최댓값 쌍으로 입력받은 언덕
높이에 대해 차이를 구해서 축적한 값중 가장 최소값이 답이 된다 ㅠㅠ.

갈길이 멀다...

이렇게 풀이하면 모든 쌍에 대해 각각의 언덕 높이를 순회하니 시간복잡도를 분석해보면
O(k * n) 정도이다.
* k 는 언덕 높이의 범위안에 가능한 값들의 개수
* n 는 입력되는 높이의 개수
"""

import sys

THRESHOLD = 17
MAX_HEIGHT = 100

def solution(hills):
    min_cost = float("inf")
    for min_height in range(MAX_HEIGHT - THRESHOLD + 1):
        max_height = min_height + THRESHOLD
        cost = 0

        for height in hills:
            if height < min_height or height > max_height:
                cost += min((height - min_height) ** 2, (height - max_height) ** 2)
        
        min_cost = min(min_cost, cost)
    return min_cost

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    hills = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(hills))