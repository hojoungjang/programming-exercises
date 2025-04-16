"""
백준
LCS 2
https://www.acmicpc.net/problem/9252
"""

import sys

def solution(s1, s2):
    """
    ACAYKP
    CAPCAK
        "" A C A Y K P
    ""   0 0 0 0 0 0 0
    C    0 0 
    A    0
    P    0
    C    0
    A    0
    K    0
    """

    dp = [[] for _ in range(len(s2))]

    for i in range(len(s1)):
        new_dp = [[] for _ in range(len(s2))]

        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i-1 >= 0 and j-1 >= 0:
                    new_dp[j] += dp[j-1][:]
                new_dp[j].append(s1[i])
            else:
                if j-1 >= 0 and len(new_dp[j-1]) > len(dp[j]):
                    new_dp[j] = new_dp[j-1][:]
                else:
                    new_dp[j] = dp[j][:]
        
        dp = new_dp
    
    lcs = ""
    for s in dp:
        if len(s) > len(lcs):
            lcs = "".join(s)
    return lcs


if __name__ == "__main__":
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    lcs = solution(s1, s2)
    print(len(lcs))
    print(lcs)
