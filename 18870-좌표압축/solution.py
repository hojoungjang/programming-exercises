"""
백준
좌표 압축
https://www.acmicpc.net/problem/18870

이분탐색을 직접 구현해 보았다. 문제 유형에 따라 다르겠지만
가끔씩 직접구현했을때 살짝 헷갈릴수 있는 요소들이 있다. 
그런 유형은 보통 찾고자 하는 값의 존재 여부를 찾는다기 보다는
찾고자하는 값이 들어갈 수 있는 위치를 물어본다. 즉 찾고자하는
값보다 작은 값과 큰값으로 배열을 두개로 나눈다고 생각해볼수 있다.
탐색 배열안에 (search space) 안에 이미 같은 값이 있을경우 
같은 값을 왼쪽에 넣을지 오른쪽에 넣을지도 문제 상황에 따라
고려해준다. 

이 문제에서는 찾고자하는 값보다 작은 값들의 개수를 원하기 때문에 같은
값들은 오른쪽으로 보냄으로 문제에서 원하는 값을 구할 수 있다. 따라서
이분탐색시 서치 스페이스를 줄여나갈때 중간값이 찾고자하는 값보다 크거나 같으면
탐색 범위를 왼쪽으로 줄인다.

문제를 풀이를 할때 안일하게 생각한부분은 중복으로 없애는 부분인데. 이때 단순하게
set 자료구조를 이용해서 없앴지만 이런식으로 언어의 편리성을 이용하기 보단
로직적으로 어떤식으로 구현해볼 수 있을지 고민하는것도 좋다. 이떄 사용할 수 있는
법은 배열을 정렬하고 정렬된 상태로 앞에서부터 순회하면서 새로운 값을 볼때마다 
새 배열 또는 기존배열 위에 복사해주면 된다. 이 방법은 생각해보면 간단하기 때문에
구체적인 설명은 생략 🙏

이렇게 하면 풀이의 시간 복잡도는 nlogn (정렬) + nlogn (탐색) 이된다.
O(nlogn)
"""

import sys

def solution(nums):

    def binary_search_left(target):
        lo = 0
        hi = len(sorted_nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target > sorted_nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    ans = [0 for _ in range(len(nums))]
    sorted_nums = sorted(set(nums))
    for i, num in enumerate(nums):
        ans[i] = binary_search_left(num)
    return ans


if __name__ == "__main__":
    _ = sys.stdin.readline()
    nums = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    print(" ".join(str(num) for num in solution(nums)))