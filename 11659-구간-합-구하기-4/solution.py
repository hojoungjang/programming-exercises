import sys

def solution(nums, intervals):
    run_sums = [0]
    for num in nums:
        run_sums.append(run_sums[-1] + num)

    ans = []
    for start, end in intervals:
        ans.append(run_sums[end] - run_sums[start-1])
    return ans

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    nums = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    intervals = [tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(m)]
    ans = solution(nums, intervals)
    for val in ans:
        print(val)
