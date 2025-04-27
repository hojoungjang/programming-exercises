"""
백준
개미굴
https://www.acmicpc.net/problem/14725
"""

import sys

LEVEL_STR = "--"

def traverse(root, level=0):
    for val in sorted(root.keys()):
        print(LEVEL_STR * level + val)
        traverse(root[val], level + 1)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    root = {}
    for _ in range(n):
        path = [val for val in sys.stdin.readline().strip().split(" ")[1:]]
        node = root

        for val in path:
            if val not in node:
                node[val] = {}
            node = node[val]

    traverse(root)
