"""
백준
거짓말
https://www.acmicpc.net/problem/1043

파티는 진실을 아는 사람이 참여하는 파티부터 일어난다?!
"""

import sys
from collections import deque

def solution(people_cnt, truths, parties):
    graph = [[] for _ in range(people_cnt + 1)]

    for party in parties:
        for i in range(len(party)):
            person1 = party[i]

            for j in range(len(party)):
                if i == j:
                    continue

                person2 = party[j]

                if person2 not in graph[person1]:
                    graph[person1].append(person2)
                if person1 not in graph[person2]:
                    graph[person2].append(person1)

    queue = deque(truths)
    visited_truth = set(truths)

    while queue:
        person = queue.popleft()

        for next_person in graph[person]:
            if next_person not in visited_truth:
                visited_truth.add(next_person)
                queue.append(next_person)

    lie_party_cnt = 0
    for party in parties:
        for person in party:
            if person in visited_truth:
                break
        else:
            lie_party_cnt += 1
    return lie_party_cnt


if __name__ == "__main__":
    people_cnt, party_cnt = map(int, sys.stdin.readline().strip().split(" "))
    truths = [int(val) for val in sys.stdin.readline().strip().split(" ")][1:]
    parties = [[int(val) for val in sys.stdin.readline().strip().split(" ")][1:] for _ in range(party_cnt)]
    print(solution(people_cnt, truths, parties))
