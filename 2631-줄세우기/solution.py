"""
백준
2631 줄세우기
https://www.acmicpc.net/problem/2631

어떻게 풀어야할지 명확이 보이지 않아 고생을 좀 했다.
처음에 그리디로 풀 수 있을까도 고민해보고 역시 경우의 수를
다 고려해서 그중 최솟값을 찾아야되어보여서 가능성에서 제외했다.

그래서 문든 문제를 보다가 결국 주어진 배열속에서 이미 정렬되어 있는
가장 큰 부분을 놔두고 나머지 숫자들만 알맞는 자리로 옮겨주면 최솟값을
만들 수 있다는 사실을 깨달았다.

그래서 처음에는 시작점을 고정해두고 그 시작 숫자로 만들수 있는 최대 길이의
오름차순으로 연속되는 숫자들의 길이를 구해서 주어진 배열 길이에서 뺏다.
엣지 케이스가 있었는지 통과되지 않았고 결국 질문게시판을 참고해서
이 문제가 longest increasing subsequence (LIS) 구하는 문제라는것을 
명확히 인지하고 LIS 어떻게 구하는건지 고민을 했다. 처음에는 내가 풀이한게 
LIS 를 구하는 방법 아닌가 했다. 하지만 엣지 케이스가 존재했고 DP 방식으로 
접근해야 한다는 힌트를 참고했다. 따라서 O(n^2) 형태의 LIS 길이를 구하는
로직을 완성했다.

결론은 각 숫자를 LIS 마지막 숫자라고 생각하고 이전에 보았던 길이들 중에
마지막 숫자가 현재 내 숫자보다 작은것들중에 제일 긴것을 골라서 내 자신을 LIS 추가한
+1 길이 값을 구하는 것이다.

접근 방향은 좋았지만 오름차순의 가장 긴 subsequence 찾는 코드를 제대로 작성하지
못 했다.
"""

import sys

def solution(nums):
    lengths = [1 for _ in range(len(nums)+1)]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                lengths[nums[i]] = max(lengths[nums[i]], lengths[nums[j]] + 1)

    return len(nums) - max(lengths)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(nums))
