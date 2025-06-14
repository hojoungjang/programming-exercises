"""
백준
1로 만들기 2
https://www.acmicpc.net/problem/12852
"""
import sys

def solution(x):
    dp = [0, 0]
    trace = [i for i in range(x+1)]

    for num in range(2, x+1):
        dp.append(float("inf"))
        if num % 3 == 0 and (calcs := dp[num//3] + 1) < dp[num]:
            dp[num] = calcs
            trace[num] = num // 3
        if num % 2 == 0 and (calcs := dp[num//2] + 1) < dp[num]:
            dp[num] = calcs
            trace[num] = num // 2
        if (calcs := dp[num-1] +1) < dp[num]:
            dp[num] = calcs
            trace[num] = num - 1

    path = []
    val = x
    while val != trace[val]:
        path.append(val)
        val = trace[val]
    path.append(1)

    return dp[x], path

if __name__ == "__main__":
    x = int(sys.stdin.readline().strip())
    cnt, path = solution(x)
    print(cnt)
    print(" ".join(str(val) for val in path))
