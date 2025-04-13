import sys
sys.setrecursionlimit(10005)

def solution(amount, coins):

    def _solution(rem, coin_idx):
        nonlocal ans_cnt

        if rem < 0:
            return 0
        
        if rem == 0:
            return 1
        
        if coin_idx >= len(coins):
            return 0
        
        cnt = _solution(rem - coins[coin_idx], coin_idx)
        cnt += _solution(rem, coin_idx + 1)
        return cnt

    ##################################
    ans_cnt = _solution(amount, 0)
    return ans_cnt

def solution_dp(amount, coins):
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for coin in coins:
        for val in range(1, amount + 1):
            if val - coin < 0:
                continue

            dp[val] += dp[val - coin]
    return dp[amount]



if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        coins = [int(val) for val in sys.stdin.readline().strip().split(" ")]
        amount = int(sys.stdin.readline().strip())
        print(solution_dp(amount, coins))