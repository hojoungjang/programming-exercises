import sys

WEIGHT = 0
HEIGHT = 1

def solution(bodies):
    ranks = [-1 for _ in range(len(bodies))]
    for i in range(len(bodies)):
        rank = 1
        for j in range(len(bodies)):
            if bodies[i][WEIGHT] < bodies[j][WEIGHT] and bodies[i][HEIGHT] < bodies[j][HEIGHT]:
                rank += 1
        ranks[i] = rank
    return ranks

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    bodies = [tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]
    ranks = solution(bodies)
    print(" ".join([str(rank) for rank in ranks]))
