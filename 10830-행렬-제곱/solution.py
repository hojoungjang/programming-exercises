"""
백준
행렬 제곱
https://www.acmicpc.net/problem/10830
"""

import sys

def solution(matrix, m):
    if m == 0:
        identity_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            identity_matrix[i][i] = 1
        return identity_matrix

    if m == 1:
        return [[val % 1000 for val in row] for row in matrix]
    
    n = len(matrix)
    mat1 = solution(matrix, m // 2)
    mat2 = solution(matrix, m - (m // 2 * 2))

    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for i in range(n):
                new_matrix[r][c] += mat1[r][i] * mat1[i][c]

    final_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for i in range(n):
                final_matrix[r][c] += new_matrix[r][i] * mat2[i][c]

    for r in range(n):
        for c in range(n):
            final_matrix[r][c] %= 1000

    return final_matrix


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    matrix = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    ans_mat = solution(matrix, m)
    for row in ans_mat:
        print(" ".join(str(val) for val in row))
