import sys

def cmp_record(medals1, medals2):
    if medals1[0] != medals2[0]:
        return medals1[0] - medals2[0]
    if medals1[1] != medals2[1]:
        return medals1[1] - medals2[1]
    if medals1[2] != medals2[2]:
        return medals1[2] - medals2[2]
    return 0

def solution(records, country_id):
    medals = (-1, -1, -1)
    sorted_records = sorted(records, key=lambda record: record[1:], reverse=True)
    rank = 0
    for i, record in enumerate(sorted_records):
        if cmp_record(medals, record[1:]) != 0:
            rank = i + 1
            medals = record[1:]
        if record[0] == country_id:
            break
    return rank

if __name__ == "__main__":
    n, country_id = map(int, sys.stdin.readline().strip().split(" "))
    records = [tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]

    print(solution(records, country_id))
