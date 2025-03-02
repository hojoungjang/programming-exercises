"""
백준
수 찾기
https://www.acmicpc.net/problem/1920

사실 배열에서 수를 찾는 방법은 가장 간단하게는 
리니어 서치를 하면 된다. 배열을 순회하면서 찾고싶은 
값과 비교한다.

하지만 문제를 보면 찾고 싶은 값이 여러개이다. 이러면 
찾고 싶은 값만큼 배열을 선형 순회해야한다. 때문에
이분탐색을 이용하여 효율을 높일수 있다. 

탐색을 할 배열을 정렬시키고 찾고 싶은 값들을 각각
이분탐색으로 찾아낸다. 배열을 1차적으로 정렬하는데
nlogn 시간복잡도 비용이 들지만 나머지 값들을 logn 비용으로
탐색할 수 있기 때문에 전체적인 효율을 올라간다. 
O(nlogn + mlogn)
* n : 탐색 배열의 크기
* m : 팀섹 깂들의 개수
"""
import sys
from bisect import bisect_left

def solution(nums, targets):
    sorted_nums = sorted(nums)
    ans = [0 for _ in targets]
    
    for i, target in enumerate(targets):
        insert_idx = bisect_left(sorted_nums, target)
        if insert_idx < len(sorted_nums) and sorted_nums[insert_idx] == target:
            ans[i] = 1
    
    return ans


if __name__ == "__main__":
    _ = sys.stdin.readline()
    nums = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    _ = sys.stdin.readline()
    targets = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    ans = solution(nums, targets)
    for num in ans:
        print(num)
