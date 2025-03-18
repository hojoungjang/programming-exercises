import sys

def date_to_int_val(date):
    m, d = date
    return m * 100 + d

def clip_durations(durations, season_start, season_end):
    new_durations = []
    for i in range(len(durations)):
        start, end = durations[i]
        if start < season_start and end <= season_start:
            continue
        if start >= season_end and end > season_end:
            continue
        new_duration = (max(start, season_start), min(end, season_end))
        new_durations.append(new_duration)
    return new_durations

def solution(durations):
    season_start = date_to_int_val((3, 1))
    season_end = date_to_int_val((12, 1))
    
    ds = [tuple([date_to_int_val(d[:2]), date_to_int_val(d[2:])]) for d in durations]
    ds = clip_durations(ds, season_start, season_end)
    ds.sort()

    if not ds:
        return 0
    
    start, end = ds[0]
    if start > season_start:
        return 0

    flower_cnt = 1

    for d in ds[1:]:
        d_start, d_end = d

        if d_end <= end:
            continue

        if d_start > end:
            return 0
        elif start < d_start <= end:
            flower_cnt += 1
            start = end
        end = d_end
        
    return flower_cnt if end >= season_end else 0


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    durations = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(durations))
