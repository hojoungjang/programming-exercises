"""
백준
자두나무
https://www.acmicpc.net/problem/2240
"""

import sys

TREE_1 = 1
TREE_2 = 2

def solution(t, w, plums):
    tree1 = [0 for _ in range(w+1)]
    tree2 = [0 for _ in range(w+1)]
    first_tree2 = True
    plums = [1] + plums

    for i in range(1, t + 1):
        if plums[i] == 1:
            for j in range(w+1):
                tree1[j] = tree1[j] + 1
                if j > 0:
                    tree1[j] = max(tree1[j], tree2[j-1] + 1)
        else:
            for j in range(w+1):
                if not first_tree2:
                    tree2[j] = tree2[j] + 1
                if j > 0:
                    tree2[j] = max(tree2[j], tree1[j-1] + 1)
            first_tree2 = False

    return max(max(tree1), max(tree2))

if __name__ == "__main__":
    t, w = map(int, sys.stdin.readline().strip().split(" "))
    plums = [int(sys.stdin.readline().strip()) for _ in range(t)]
    print(solution(t, w, plums))
