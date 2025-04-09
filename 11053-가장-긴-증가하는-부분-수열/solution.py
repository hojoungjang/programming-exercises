import sys
from bisect import bisect_left

def solution(nums):
    max_lengths = [1 for _ in range(len(nums))]

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                max_lengths[i] = max(max_lengths[i], max_lengths[j] + 1)

    return max(max_lengths)

def solution_bst(nums):
    lis = []
    for num in nums:    
        idx = bisect_left(lis, num)
        if idx == len(lis):
            lis.append(num)
        else:
            lis[idx] = num
    return len(lis)
        

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    print(solution_bst(nums))