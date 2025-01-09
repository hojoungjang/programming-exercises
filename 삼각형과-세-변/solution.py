"""
백준
삼각형과 세 변
https://www.acmicpc.net/problem/5073
"""

import sys

def solution(triangle_sides: list[list[int]]):
    for sides in triangle_sides:
        if sides[0] + sides[1] <= sides[2]:
            print("Invalid")
        elif sides[0] == sides[1] == sides[2]:
            print("Equilateral")
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            print("Isosceles")
        else:
            print("Scalene")

if __name__ == "__main__":
    triangle_sides = [
        sorted([
            int(side.strip()) 
            for side in line.strip().split(" ")
        ]) for line in sys.stdin.readlines()
    ]
    solution(triangle_sides[:-1])
