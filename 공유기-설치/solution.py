"""
백준
공유기 설치
https://www.acmicpc.net/problem/2110

처음에는 공유기들을 좌표 오르차순으로 정렬하고 이웃이되는 한쌍끼리 묶어서
각각 (houses[j] - houses[i], i, j) 튜플을 만들어서 힙 자료구조에 저장해서
가장 거리가 가까운 쌍을 뽑아서 쌍을 만드는 두 집 중에 제거 했을때 더 새로 만들어지는
이웃하고의 거리가 더 큰 것을 골러가며 새로 쌍을 만들고 거리를 계산에 다시 힙에 넣었다.
안타깝게도 이 방법은 완벽하게 답을 찾아내지 못한다. 각 단계에서 최적이라고 판단하는
로직이 문제에서 답이 될수 있는경우를 제대로 고려하지 않거나 가지치기 해버린다.

긴 시간 끝에도 풀이를 하지 못해 풀이 방법을 참고하였고 이분탐색으로 해결하는 방식을
보았다. 개인적으로 이분탐색을 적용하는 방식 또는 그 대상이 명확하게 다가오지는 않는 
느낌의 문제다. 

여기서 이분탐색의 범위는 집들 사이의 거리이다. 
이분탐색 구간의 처음 최소 값은 간단하게는 1 더 정확하게는 입력에서 두 집 사이의 거리중
최소거리 정도로 설정해주고 최대값은 두 집 사이의 거리중 최대거리 즉 정렬된 집들의 좌표에서
마지막 집의 위치 빼기 첫번째 집의 위치다.
이렇게 해놓고 일반 이분탐색처럼 중간 값을 ((최소 + 최대) / 2) 구해서 범위를 왼쪽으로 
줄일지 오른쪽으로 줄일지 결정한다. 이때 결정하는 요인은 해당 중간 값을 각 집들 사이의
간격으로 했을때 입력으로 주어진 c 개의 공유기를 모두 설치 할 수 있어야 한다. 적어도 c개를
설치 못하면 각 집들의 거리를 더 좁혀서 더 많은 공유기를 설치해야되므로 왼쪽으로 범위를 좁히고 [lo, mid-1]
반대로 적어도 c 개 설치에 성공하면 거리를 더 넓힐 수 있는지 알아내기 위해 오른쪽으로 범위를 좁히다 [mid + 1, hi]

따라서 각 이분탐색 단계에서 모든 집들을 순회하고 각 이분탐색 단계는 최대 log(n) 번 진행될 수 있다. 이때 n 은
집들의 수. 이게 아니더라도 애초에 모든 집을 처음에 정렬하게 된다. 시간복잡도는 O(nlogn)
공간 복잡도는 정렬 알고리즘에 따라 다르지만 보통은 재귀로 구현되어 있으면 최대 log(n) 깊이 만큼되어 콜스택
프레임을 추가한다고 생각하고 리턴값의 할당하는 자료구조의 크기를 제외하면 log(n) 정도로 생각해 볼 수 있겠다.
"""
import sys

def solution(houses, c):
    if len(houses) < 2:
        return -1
    
    houses.sort()
    lo = 1
    hi = houses[-1] - houses[0]

    while lo <= hi:
        mid = (lo + hi) // 2

        cnt = 1
        last_house_idx = 0
        for i in range(1, len(houses)):
            if houses[i] - houses[last_house_idx] >= mid:
                cnt += 1
                last_house_idx = i
        
        if cnt >= c:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return hi


if __name__ == "__main__":
    n, c = map(int, sys.stdin.readline().strip().split(" "))
    houses = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(houses, c))