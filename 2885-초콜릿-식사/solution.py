from math import ceil, log2
import sys

def solution(k):
    exp = ceil(log2(k))
    blocks = pow(2, exp)
    cnt = 0

    while k > 0:
        while blocks > k:
            blocks //= 2
            cnt += 1
        k -= blocks
    return pow(2, exp), cnt

if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    blocks, cuts = solution(k)
    print(f"{blocks} {cuts}")
