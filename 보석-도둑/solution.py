"""
백준
보석 도둑
https://www.acmicpc.net/problem/1202

각 가방에 대해서 그 가방의 총량보다 작거나 같은 보석중에 가중
값이 비싼 것을 골라 담으면 결국 최댓값을 구할 수 있다.

그러면 이걸 단순하게 풀이하면 각 가방마다 모든 보석을 매칭시켜서
담을수 있는지 확인하고 담을 수 있다면 가장 큰 값을 추적하면 된다.
하지만 이렇게 했을 경우 O(n * k) 가 된다. n은 보석의 수 k는 가방의 수

생각해보면 각 가방은 용량보다 큰 보석은 당연히 담을수 없기 때문에 고려하고
싶지 않다. 그러면 가방의 용량과 보석의 정보를 담은 리스트를 각각 정렬하고
각 리스트에 대해 포인터를 두고 가방또는 보석 정보를 다 소모할때까지 순차적으로
비교하며 순회하면 될거라고 생각했다.

보석 포인터는 로직 사이클이 한번 돌때마다 하나씩 옮겨주고 가방 포인터는 현재 보석의
무게가 현재 가방의 무게보다 크면 다음으로 옮겨준다.

이렇게 할경우 한가지 문제점이 생긴다. 첫번째 가방을 제외하고는 경우의 따라
앞에서 지나온 보석들을 고려하지 못하게 된다. 두번째 예제를 이용하면 쉽게 볼 수 있다.

보석: [(1, 65), (2, 99), (5, 23)]
가방: [2, 10]

가방 10 은 (5,23) 만 고려하게 되지만 실제로는 (1,65) 보석을 담는게 더 최적이다.

따라서 효율적으로 전체 골라지지 않은 보석들중에 현재 가방으로 담을수 있는 가장 큰 값을
찾아내는 방법이 필요한데 변화하는 데이터 컬랙션에서 효율적으로 최적의 값을 찾을수 있는
힙을 떠올렸다. 이렇게 하면 보석을 항상 맥스 힙안에 넣고 만약 새로운 보석의 무게가 현재 가방의
무게보다 클 경우, 힙안에 있는 보석은 가방을 이용해 모두 담을 수 있는 경우일것이고 이때
힙 맨위에 있는 최고 값을 빼서 가방에 담는 식으로 진행할 수 있다.

이렇게 하면 정렬과 힙을 사용하는 로직으로 풀이가 되고 전체 시간 복잡도는 
O(nlogn + klogk + nlogn + klogn)
* nlogn -> 보석 정렬
* klogk -> 가방 정렬
* nlogn -> 총 보석 힙에 추가
* klogn -> 총 가방에 추가하기 위해 보석 힙에서 제거

공간 복잡도는 힙을 사용해서 O(n) 이된다. (경우의 따라 정렬은 logn 정도의 공간 복잡도를 추가하지만
big O 로 표현해서 생략 가능할것같다.)
"""

import sys
from heapq import heappop, heappush

def solution(jewels, cap):
    jewels.sort()
    cap.sort()

    jewels_heap = []
    cap_idx = 0
    total = 0

    for m, v in jewels:
        while cap_idx < len(cap) and cap[cap_idx] < m:
            if jewels_heap:
                total += abs(heappop(jewels_heap))
            cap_idx += 1
        heappush(jewels_heap, -v)
    
    while cap_idx < len(cap) and jewels_heap:
        total += abs(heappop(jewels_heap))
        cap_idx += 1
    return total


if __name__ == "__main__":
    """
    n: 보석 총 개수
    k: 가방 개수 (가방에는 하나의 보석을 담을수 있고 최대 cap[i] 무게)

    각 보석
    m: 무게
    v: 가격
    """
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    jewels = [[int(num) for num in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    cap = [int(sys.stdin.readline().strip()) for _ in range(k)]
    print(solution(jewels, cap))
