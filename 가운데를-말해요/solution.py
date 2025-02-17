"""
백준
가운데를 말해요
https://www.acmicpc.net/problem/1655

처음에는 self-balancing BST 를 구현해야되나 고민하다가
뭔가 다른 풀이법이 있을것같다는 생각들면서도 정확히 방법이 떠오르지
않았다. 그러다가 질물 게시판에 힙을 사용했다는 제목을 보고
힙을 이용하면 어떻게 풀 수 있을까 고민하다가 풀이 방법을 떠올려다.

일단 힙 두개를 관리하는데 하나는 min 다른 하나는 max heap 으로
만들어주고 각각 전체 숫자의 반개씩 담도록 한다. 그리고 min heap 에는
가장 큰 숫자들 반개 max heap 에는 가장 작은 숫자들 반개를 유지해준다.
min/max 에 대해 반대되는 식으로 숫자들을 담고 있어서 잘 이해가 되지 
않을 수 있지만 생각해보면 이렇게 보관했을때 각 heap 맨 위에 가운데랑
가장 가까운 수를 보관할 수 있게 되고 heap 의 특성상 맨위에 있는
원소에 대해 작업을 할때 가장 효율적이기 때문에 이런식으로 보관한다.

이렇게 하고 숫자가 들어올때마다 힙의 맨위랑 비교해서 min heap 또는
max heap에 적절히 넣어주고 전체 숫자가 홀수개 일때 항상 max heap 에
숫자가 하나 더 많게 유지해주면 숫자가 홀수개이든 짝수개이든 max heap
맨위가 새로운 숫자를 포함하고 나서의 답이 된다.

이렇게 하면 문제의 streaming 특징을 갖는 입력 데이터에 대해 각 단계에서의
중간값을 효율적으로 찾아낼수 있다. 여기서는 매번 정렬을 해서 답을 찾거나
이분탐색으로 새로운 숫자가 들어갈 위치를 찾아서 풀이 하는 법은 각 단계에서
nlogn 또는 n 만큼의 시간복잡도를 요구하기 때문에 문제의 입력을 통과 할 만큼
효율적이지 못하다.
"""

import sys
from heapq import heappush, heappop

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    min_heap = []   # maintain largest half
    max_heap = []   # maintain smallest half

    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        if min_heap and min_heap[0] < num:
            heappush(min_heap, num)
        else:
            heappush(max_heap, -num)
        
        if len(min_heap) - len(max_heap) > 0:
            heappush(max_heap, -heappop(min_heap))
        if len(max_heap) - len(min_heap) > 1:
            heappush(min_heap, -heappop(max_heap))
        
        print(-max_heap[0])
