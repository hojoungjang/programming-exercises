"""
백준
선 긋기
https://www.acmicpc.net/problem/2170
"""
import sys

def solution(lines):
    lines.sort()

    total_length = 0
    start, end = lines[0]

    for l_start, l_end in lines:
        if max(start, l_start) < min(end, l_end):
            end = max(end, l_end)
        else:
            total_length += end - start
            start = l_start
            end = l_end
    
    total_length += end - start
    return total_length
        

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    lines = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(lines))
