"""
백준
톱니바퀴
https://www.acmicpc.net/problem/14891
"""

import sys
from collections import deque

NUM_OF_WHEELS = 4
N = 0
S = 1
CLOCKWISE = 1
COUNTER_CLOCKWISE = -1

LEFT_IDX = 6
RIGHT_IDX = 2

def get_deque_from_wheels(wheels):
    return [deque(wheel) for wheel in wheels]

def calculate_score(wheels):
    score = 0
    for idx, wheel in enumerate(wheels):
        if wheel[0] == S:
            score += 2 ** idx
    return score

def solution(wheels, rotations):
    # change wheels to deque
    wheels_deque = get_deque_from_wheels(wheels)

    # for each rotation input, calculate chained rotations
    for rotation in rotations:
        wheel_idx = rotation[0] - 1
        direction = rotation[1]

        rotation_ops = [0 for _ in range(NUM_OF_WHEELS)]
        rotation_ops[wheel_idx] = direction

        # Left side rotation
        chain = True
        while chain and wheel_idx > 0:
            if wheels_deque[wheel_idx][LEFT_IDX] != wheels_deque[wheel_idx-1][RIGHT_IDX]:
                direction *= -1
                rotation_ops[wheel_idx-1] = direction
                wheel_idx -= 1
            else:
                chain = False

        # Right side rotation
        wheel_idx = rotation[0] - 1
        direction = rotation[1]
        chain = True
        while chain and wheel_idx < len(wheels_deque) - 1:
            if wheels_deque[wheel_idx][RIGHT_IDX] != wheels_deque[wheel_idx+1][LEFT_IDX]:
                direction *= -1
                rotation_ops[wheel_idx+1] = direction
                wheel_idx += 1
            else:
                chain = False
        
        # rotate the wheels based on calculated chained rotations
        for idx, direction in enumerate(rotation_ops):
            wheels_deque[idx].rotate(direction)

    # calculate the score
    return calculate_score(wheels_deque)

if __name__ == "__main__":
    wheels = []
    for _ in range(NUM_OF_WHEELS):
        wheels.append([int(val) for val in sys.stdin.readline().strip()])
    
    k = int(sys.stdin.readline().strip())
    rotations = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(k)]

    print(solution(wheels, rotations))
