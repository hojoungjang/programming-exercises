import sys

LEFT = 0
RIGHT = 1

def solution(heights):
    stack = []
    counts = [0 for _ in range(len(heights))]
    closests = [[-1, -1] for _ in range(len(heights))]

    for i in range(len(heights)):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        if stack:
            closests[i][LEFT] = stack[-1]
        counts[i] += len(stack)
        stack.append(i)

    stack = []
    for i in reversed(range(len(heights))):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        if stack:
            closests[i][RIGHT] = stack[-1]
        counts[i] += len(stack)
        stack.append(i)

    ans = []
    for i in range(len(heights)):
        if closests[i][LEFT] == -1 or closests[i][RIGHT] == -1:
            closest = max(closests[i])
        elif i - closests[i][LEFT] <= closests[i][RIGHT] - i:
            closest = closests[i][LEFT]
        else:
            closest = closests[i][RIGHT]
        ans.append((counts[i], closest+1))
    return ans


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    heights = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    ans = solution(heights)
    for count, closest in ans:
        if count != 0:
            print(count, closest)
        else:
            print(0)
