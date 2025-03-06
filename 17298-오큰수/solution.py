import sys

IDX = 0
VAL = 1

def solution(nums):
    ans = [-1 for _ in range(len(nums))]
    stack = []
    for i, num in enumerate(nums):
        while stack and stack[-1][VAL] < num:
            idx, _ = stack.pop()
            ans[idx] = num
        stack.append((i, num))
    return ans
        

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    ans = solution(nums)
    print(" ".join(str(num) for num in ans))