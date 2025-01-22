"""
백준
빗물
https://www.acmicpc.net/problem/14719

조금 헷갈렸다. 그래도 이전에 풀어본적이 있던 문제이다.

문제의 답을 구하기 위해서는 블록의 높이를 보며 물이 담기는 구간을 찾아 물의 양을 구해야 한다
이렇게 했을때 그 구간은 두개의 블록으로 감싸지고 그 사이 모든 블록의 높이는 감싸는 블록의 높이보다
작다.

블록 높이를 순회하며 만약 현재 높이가 이때까지 봐온 높이보다 크거나 같으면 우리가 찾고자 하는
물이 갇히는 구간을 발견했다는 뜻이다.

이렇게 정방향 순회를 하고나면 경우의 따라 마지막 구간의 계산은 처리되지 않는다. 이런 경우는
마지막까지 현재 최고 높이의 블록보다 크거나 같은 높이의 블록을 만나지 못했다는 경우다.
이 경우를 처리하기 위해 뒤에서부터 마지막으로 본 최고 높이 블록까지 반대방향으로 순회하며
같은 계산을 해주면 된다.
"""
import sys

def solution(heights):
    if not heights:
        return 0
    
    max_height = heights[0]
    max_height_idx = 0
    block_amount = 0
    water_amount = 0

    for i in range(1, len(heights)):
        if heights[i] >= max_height:
            water_amount += max_height * (i - max_height_idx - 1) - block_amount
            max_height = heights[i]
            max_height_idx = i
            block_amount = 0
        else:
            block_amount += heights[i]

    # 끝 부분
    start_idx = max_height_idx
    max_height = heights[-1]
    max_height_idx = len(heights) - 1
    block_amount = 0

    for i in reversed(range(start_idx, len(heights) - 1)):
        if heights[i] >= max_height:
            water_amount += max_height * (max_height_idx - i - 1) - block_amount
            max_height = heights[i]
            max_height_idx = i
            block_amount = 0
        else:
            block_amount += heights[i]

    return water_amount


if __name__ == "__main__":
    _, _ = map(int, sys.stdin.readline().strip().split(" "))
    heights = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    print(solution(heights))
