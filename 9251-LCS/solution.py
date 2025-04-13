import sys

def solution(s1, s2):
    dp = [0 for _ in range(len(s2))]

    for idx1 in range(len(s1)):
        new_dp = [0 for _ in range(len(s2))]

        for idx2 in range(len(s2)):
            if s1[idx1] == s2[idx2]:
                if idx2 - 1 >= 0:
                    new_dp[idx2] += dp[idx2 - 1]
                new_dp[idx2] += 1
            else:
                if idx2 - 1 >= 0:
                    new_dp[idx2] = max(new_dp[idx2], new_dp[idx2-1])
                new_dp[idx2] = max(new_dp[idx2], dp[idx2])
        
        dp = new_dp

    return dp[-1]


if __name__ == "__main__":
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    print(solution(s1, s2))
