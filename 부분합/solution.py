"""
백준
부분합
https://www.acmicpc.net/problem/1806

brute force 방법 먼저 살펴보자.
가능한 모든 윈도우의 경우마다 합을 구하고 목표 숫자랑 비교해서 가장 작은
윈도우 경우를 찾을 수 있겠다. 이때 시간 복잡도는 O(n^3) 이다. 
각 윈도우 사이즈마다 모든 시작 인덱스의 대해 그 윈도우 안에 있는 숫자들의
합을 구해야되기 때문이다.

위 방법은 효율적이지 못하다. 살짝 효율성을 높이기 위해 구해둔 시작 인덱스가
바뀔때마다 합을 새로 구하는게 아니라 이전 시작인덱스 원소 값을 빼고 새로 추가
되는 값을 구해둔 합을 더해 줄 수 있다. 하지만 이러게 해도 아직 O(n^2) 
시간 복잡도를 가지고. 조금 더 효율성을 높일 수 있다.

이때 슬라이딩 윈도우를 사용 할 수 있다. 윈도우의 시작과 끝 인덱스를
관리하고 윈도우 안에 있는 숫자들의 합을 시작/끝 인덱스가 바뀔때마다
업데이트 해준다.

끝 인덱스는 하나씩 키워나가고 그때마다 합이 목표 숫자보다 크거나 같으면
시작 인덱스를 윈도우의 합이 작아질때까지 조절하고 그 과정속에서 제일
크기가 작은 윈도우이면서 합이 목표 숫자 이상인 경우를 찾아서 답을 구한다.

이렇게 하면 배열의 크기가 n 일때 O(n) 시간복잡도로 문제를 풀수 있다. 
"""
import sys

def solution(nums, max_sum):
    start = 0
    num_sum = 0
    num_count = len(nums) + 1

    for end in range(len(nums)):
        num_sum += nums[end]

        while start <= end and num_sum >= max_sum:
            num_count = min(num_count, end - start + 1)
            num_sum -= nums[start]
            start += 1
            
    return num_count if num_count != len(nums) + 1 else 0
            

if __name__ == "__main__":
    n,s = map(int, sys.stdin.readline().strip().split(" "))
    nums = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    print(solution(nums, max_sum=s))
