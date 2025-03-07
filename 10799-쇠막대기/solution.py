import sys

IDX = 0
VAL = 1

def solution(ps):
    cnt = 0
    stack = []

    for i, p in enumerate(ps):
        if p == "(":
            stack.append((i, p))
        elif p == ")":
            if not stack:
                continue

            idx, _ = stack.pop()
            if idx == i - 1:
                cnt += len(stack)
            else:
                cnt += 1
    return cnt

if __name__ == "__main__":
    ps = sys.stdin.readline().strip()
    print(solution(ps))