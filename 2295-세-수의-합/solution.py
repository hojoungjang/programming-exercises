"""
백준
세 수의 합
https://www.acmicpc.net/problem/2295

이분탐색을 응용한 문제여서 처음에 어떻게 풀지 고민하였지만 
처음 풀이법은 어쩌다보니 이분탐색을 전혀 사용하지 않았다.

문제는 다양하게 풀이가 가능한데 그 중심에는 네개의 숫자를
사용해서 n1 + n2 + n3 = n4 가 되는 숫자 네개를 
주어진 숫자 집합에서 고르는것이다. 그리고 그중 n4 가
가장 큰 값을 찾는다.

가장 쉽게는 O(n^4) - 숫자 네개를 각각 골라 조합한다.
그 다음으로는 O(n^3) - 숫자 세개를 골라 그들의 합이 
집합에 존재하는지 확인한다. 이때 메모리를 추가로 사용해서 set 를 만들어서
룩업을 O(1) 으로 만들어줘야한다.

그 다음으로는 O(n^2 * logn) 이다. 숫자 두개의 조합의 합들을
배열에 따로 저장하고 정렬한다. 이 배열을 arr 이라고 하자. 
그리고 다시 숫자 두개를 조합해가면서 둘의 차를 이분탐색으로 arr 에서
탐색해서 존재 여부를 확인하면서 세 숫자의 합을 최대값으로 갱신하면서
진행한다.

마지막으로는 그전 풀이와 거의 동일하지만 arr 을 배열이 아닌 set 로
저장하고 이분탐색 없이 O(1) 룩업으로 진행해볼 수 있다.
그러면 O(n^2) 까지 시간복잡도를 개선 할 수 있을것같다.
"""

import sys
from bisect import bisect_left

def solution(nums):
    two_sums = []
    for num1 in nums:
        for num2 in nums:
            two_sums.append(num1 + num2)

    two_sums.sort()

    largest = float("-inf")
    for total_sum in nums:
        for num3 in nums:
            target = total_sum - num3
            idx = bisect_left(two_sums, target)
            if two_sums[idx] == target:
                largest = max(largest, total_sum)
    
    return largest

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(nums))