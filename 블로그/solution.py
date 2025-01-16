import sys

def solution(visit_counts, days):
    max_visits = visits = sum(visit_counts[:days])
    max_count = 1
    for i in range(days, len(visit_counts)):
        visits = visits - visit_counts[i - days] + visit_counts[i]
        if max_visits < visits:
            max_visits = visits
            max_count = 1
        elif max_visits == visits:
            max_count += 1
    return max_visits, max_count


if __name__ == "__main__":
    n, x = map(int, sys.stdin.readline().strip().split())
    visit_counts = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    max_visits, max_count = solution(visit_counts, x)
    
    if max_visits:
        print(max_visits)
        print(max_count)
    else:
        print("SAD")