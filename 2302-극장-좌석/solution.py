import sys

def solution(n, vips):
    two_away = 0
    one_away = 1
    vips = set(vips)

    for num in range(1, n + 1):
        if num in vips or num - 1 in vips:
            one_away, two_away = one_away, one_away
        else:
            one_away, two_away = one_away + two_away, one_away

    return one_away


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    vips = [int(sys.stdin.readline().strip()) for _ in range(m)]
    print(solution(n, vips))