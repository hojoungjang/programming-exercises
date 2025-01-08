"""
프로그래머스
디펜스 게임
https://school.programmers.co.kr/learn/courses/30/lessons/142085

* Python heapq 는 default min heap 이다
* heappushpop 은 주어진 원소를 push 한 다음 heap 의 top 을 뺀다.
  공식 문서에 따르면 heappush 와 heappop 을 따로 호출하는 것 보다 효율적이라고 한다.

  그 이유는 heappush 와 heappop 을 따로 할 경우, 각각 log(n) time complexity 를
  가진다. 
  - heappush 는 새 원소를 힙 끝에 붙이고 원소의 알맞은 위치를 찾기 위해 힙을 올라가며
    힙 안에 원소들과 비교한다 O(logn)
  - heappop 은 pop 하는 원소 즉 꼭대기 원소를 끝 원소와 자리를 바꿔서 때어낸다. 그리고
    위치가 꼭대기로 바뀐 끝 원소의 알맞은 위치를 찾기위해 힙을 내려가며 힙 안에 원소들과 비교한다 O(logn)

  반면 heappushpop 은 이 과정은 하나의 과정으로 최적화 할 수 있다. pop 할 꼭대기 원소를 저장하고
  꼭대기에 새로 push 할 원소를 덮어쓴다. 그리고 그 새로운 원소의 알맞은 위치를 찾기위해 힙을 내려가며 
  힙 안에 원소들과 비교한다 O(logn)

아래의 코드는 heappush 와 heappop 을 따로 사용하게 작성이 되었지만 살짝 변형하면 heappushpop 을
이용할 수 있다. 코드를 구현 할 때 떠오르지 않았지만 다른 작성자들의 코드를 보며 배웠다.

그 방법은 처음 힙을 만들때 첫 k 개의 enemy 원소를 넣어주고 나머지 원소를 룹을 통해 순회하는 것이다.
이렇게 하면 룹안에서 heappushpop 을 이용해 힙의 크기가 항상 k 이도록 유지할 수 있다.
"""

from heapq import heappush, heappop

def solution(n, k, enemy):
    game_round = 0
    min_heap = []
    for enemy_count in enemy:
        heappush(min_heap, enemy_count)
        if len(min_heap) > k:
            if (top := heappop(min_heap)) <= n:
                n -= top
            else:
                break
        game_round += 1
    return game_round
