import sys

def solution(n):
    if n < 3:
        return n

    uniques = [0, 1, 1]
    total = [0 for _ in range(n+1)]
    total[1] = 1
    total[2] = 2

    for num in range(3, n+1):
        total[num] = uniques[1] * total[num-1] + uniques[2] * total[num-2]
    return total[num] % 10_007

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(solution(n))