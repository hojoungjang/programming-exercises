import sys
def solution(nums):
    stack = []
    for num in nums:
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    return sum(stack)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
    print(solution(nums))