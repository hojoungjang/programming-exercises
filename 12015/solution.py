"""
백준
가장 긴 증가하는 부분 수열 2
https://www.acmicpc.net/problem/12015


O(n^2) 까지의 풀이는 해보았는데 거기서 더 최적화하는 방법은
아무리 머리를 굴려도 생각나지 않아 풀이법을 참고하였다.

일단 O(n^2) 풀이는 배열 안에 숫자를 순회하면서 각 숫자에 대해
이 숫자로 끝나는 수열중 가장 길이가 큰 값을 저장해주는 방식이다.
이 가장 큰 길이 값들은 또 다른 배열에 저장해준다고 생각하고
각 숫자에서 먼저 온 숫자들중 현재 숫자보다 작은 숫자들중 가장 
수열의 길이가 긴 값에 1을 더해준 값이 현재 숫자로 끝나는 가장 긴 
수열의 길이가 된다.

시간: O(n^2)
공간: O(n)

그럼 이제 O(n) 이나 O(nlogn) 풀이법이 있을까 고민해본다.
결론부터 보자면 이문제는 이분탐색을 O(nlogn) 풀이가 가능하다.

먼저 증가하는 부분 수열을 담을 빈 리스트를 (inc_subs) 하나 만들어두고
숫자들을 순회하면서 inc_subs 마지막 원소보다 현재 숫자가 더 크다면
뒤에 붙여주고 그렇지 않다면 inc_subs 안에서 들어갈 수 있는 위치를
이분탐색으로 찾아주고 그 자리에 이미 있는 숫자와 교체를 해준다.

여기서 추가가 아니라 교체이다. 자연스럽게 추가하는게 더 직관적이어서 교체한다는
로직이 잘 이해가 되지 않지만 끝까지 한번 해보자. 일단 이 알고리즘대로 하게 되면 
inc_subs 그대로 증가하는 형태를 유지시킬수 있다. 그리고 이전에 보았던 숫자를
결국에는 그자리에 들어갈수 있는 더 작은 숫자로 교체하게 되면 인접한 두 숫자 사이를
최대한으로 컴팩트하게 만들수 있는 효과를 주면서 추후 보게 되는 숫자를 더 이어 붙일수 있는
기회를 마련한다.

이분탐색을 활용한다고 인지를 했을때는 보는 숫자를 점점 추가해야한다고 밖에
생각이 들지 않아서 풀이방법을 도무지 생각해낼 수 없었다. 사실 추가를 하는
효율적인 방법이 있지만 코딩테스트 환경에서 구현하기란 빡세다. 그리고 추가하게
되면 그대로 이분탐색으로 위치를 찾고 현재 숫자보다 작은 숫자들의 개수가 
가장 긴 증가하는 부분 수열의 크기가 될것이다.

마무리하자면 풀이방법을 알아내기 어려운 문제중 하나인것같다.
"""
import sys
from bisect import bisect_left

# def solution(nums):
#     memo = [1 for _ in range(len(nums))]
#     for i in range(len(nums)):
#         for j in range(i):
#             if nums[j] < nums[i]:
#                 memo[i] = max(memo[i], memo[j] + 1)
#     return max(memo)

def solution(nums):
    inc_subs = []

    for num in nums:
        if not inc_subs or num > inc_subs[-1]:
            inc_subs.append(num)
        else:
            rep_idx = bisect_left(inc_subs, num)
            inc_subs[rep_idx] = num
    
    return len(inc_subs)


if __name__ == "__main__":
    _ = sys.stdin.readline()
    nums = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    print(solution(nums))