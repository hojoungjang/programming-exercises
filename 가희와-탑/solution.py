"""
백준
가희와 탑
https://www.acmicpc.net/problem/24337

일단 a 와 b 의 합이 n+1 보다 큰 경우는 없다. 이 말은 
문제의 조건과 모순이 생긴다. 

그리고 나서 생각을 해보면 일단 조건을 만족하려면 왼쪽에서 오른쪽으로 이동하면서
오름차순으로 붙이는 숫자들의 길이가 a 이고 반대로 오른쪽에서 왼쪽으로
이동하면서 오름차순으로 붙이는 숫자들의 길이가 b 다

이때 사전순으로 가장 앞서는 조건을 만족하려면 큰 숫자들이 최대한 오른쪽으로 있어야
된다. 그리고 가장 높은 높이는 a 와 b 둘중 더 큰 값에 맞춘다. 이렇게 하면 자연스럽게
b 의 조건을 딱 맞출수 있는 경우를 떠올려 n - b 인덱스 값에 가장 높은 높이를 저장하고
그 중심으로 높이를 점점 내려가며 배열을 완성한다.

이렇게 하면 거의 다 맞춰는데 한가지 예외가 존재했다. 그건 a 가 1 이고 b 가 2 이상일때이다.
위의 조건대로 배열을 완성하면 a 조건이 (가희가 보는 빌딩의 수) 제대로 만족이 안되는 경우가 생긴다.
그래서 살펴본 결과 이런경우 가장 높은 높이를 제일 첫번째 인덱스로 가져오고 원래자리에 1 을 넣어주는
방식으로 풀었다.
"""

import sys

def solution(n, a, b):
    if a + b > n + 1:
        return [-1]
    
    heights = [1 for _ in range(n)]
    pivot = n - b
    heights[pivot] = max(a, b)

    for offset, i in enumerate(range(pivot+1, n), 1):
        if b - offset == 0:
            break
        heights[i] = b - offset
    
    for offset, i in enumerate(reversed(range(pivot)), 1):
        if a - offset == 0:
            break
        heights[i] = a - offset
    
    if a == 1:
        heights[pivot], heights[0] = 1, heights[pivot]

    return heights

if __name__ == "__main__":
    """
    n : number  of towers
    a : visible to gahui
    b : visible to danbi
    """
    n, a, b = map(int, sys.stdin.readline().strip().split(" "))
    heights = solution(n, a, b)
    print(" ".join(str(h) for h in heights))