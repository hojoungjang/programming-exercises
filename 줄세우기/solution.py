import sys

def solution(heights: list[int]):
    ans = 0
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            if heights[i] > heights[j]:
                ans += 1
    return ans

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        test_case = sys.stdin.readline().strip().split(" ")
        heights = [int(num) for num in test_case[1:]]
        print(f"{test_case[0]} {solution(heights)}")
