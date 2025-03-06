import sys

def solution(seq):
    idx = 0
    stack = []
    ops = []
    for num in range(1, len(seq) + 1):
        stack.append(num)
        ops.append("+")
        while stack and stack[-1] == seq[idx]:
            stack.pop()
            idx += 1
            ops.append("-")

    while idx < len(seq):
        if not stack or stack.pop() != seq[idx]:
            return []
        idx += 1
        ops.append("-")

    return ops


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    seq = [int(sys.stdin.readline().strip()) for _ in range(n)]
    ops = solution(seq)
    if not ops:
        print("NO")
    else:
        for op in ops:
            print(op)