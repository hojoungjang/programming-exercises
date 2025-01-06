"""
프로그래머스
퍼즐 게임 첼린지
https://school.programmers.co.kr/learn/courses/30/lessons/340212
"""

def calculate_level_time(level, diffs, times):
    level_time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            level_time += times[i]
        else:
            level_time += (diffs[i] - level) * (times[i] + times[i-1]) + times[i]
    return level_time

def solution(diffs, times, limit) -> int:
    # diffs[0] 은 항상 1
    lo = 1
    hi = max(diffs)
    while lo <= hi:
        mid = (lo + hi) // 2
        level_time = calculate_level_time(mid, diffs, times)
        if level_time <= limit:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    print(solution(
        diffs=[1, 5, 3],
        times=[2, 4, 7],
        limit=30,
    ))

    print(solution(
        diffs=[1, 4, 4, 2],
        times=[6, 3, 8, 2],
        limit=59,
    ))

    print(solution(
        diffs=[1, 328, 467, 209, 54],
        times=[2, 7, 1, 4, 3],
        limit=1723,
    ))

    print(solution(
        diffs=[1, 99999, 100000, 99995],
        times=[9999, 9001, 9999, 9001],
        limit=3456789012,
    ))
    