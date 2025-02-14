"""
백준
동전 분배
https://www.acmicpc.net/problem/1943

하다보니 자력으로 다이나믹 프로그래밍 문제를 풀었다.
주어진 문제는 모든 경우의 수를 완전탐색하는 비용이 2 거듭제곱 꼴로
나오기 때문에 자연스럽게 동적 프로그래밍을 떠올리게 된다. 

일단 문제에 대한 해를 다 적은 문제로 표현하고 수식을 찾을려 했고 가장
최근에 풀었던 문제에서 배웠던 느낌을 가지고 접근을 해보았다. 
동전의 총 합을 구해 반으로 나눈 값을 가지고 0 부터 그 값까지 순서대로
현재의 동전 개수로 만들 수 있는지에 대한 여부를 판단하고 가능 할 경우
그 값을 만들고나서의 동전 개수 상태를 저장해가며 최종적으로 총 합의 반 값에
대한 경우를 만들 수 있는지에 대한 결과를 찾아내는 식으로 풀었다.

물론 애초에 반값이 자연수가 아니라면 문제에 대한 답이 없다고 바로 판단한다.

사실 이 회고록을 작성하면서도 순간 이게 왜 되지라고 헷갈려는데 원리는 총합의 반을 만들수
있긴만 하면 동전들을 똑같은 값으로 반으로 나눌수 있다는 뜻이기 때문에 답을 찾을 수 있다.

따라서 동적프로그래밍을 이용해 풀이하면 동전의 총 합의 반 곱하기 
동전의 종류가 시간 및 공간 복잡도가 된다.
O(k / 2 * n)
* k : 동전 값의 총 합
* n : 동전 종류의 개수
"""
import sys

def solution(coins, counts):
    total = sum([coins[i] * counts[i] for i in range(len(coins))])
    
    if total % 2 != 0:
        return 0
    
    target = total // 2
    dp = [None for _ in range(target + 1)]
    dp[0] = counts[:]

    for amount in range(target + 1):
        for idx, coin in enumerate(coins):
            if amount - coin < 0:
                continue

            if dp[amount - coin] and dp[amount - coin][idx] > 0:
                dp[amount] = dp[amount - coin][:]
                dp[amount][idx] -= 1
                break

    return 1 if dp[target] else 0


if __name__ == "__main__":
    for _ in range(3):
        n = int(sys.stdin.readline().strip())
        coins = []
        counts = []
        for _ in range(n):
            coin, count = map(int, sys.stdin.readline().strip().split(" "))
            coins.append(coin)
            counts.append(count)
        print(solution(coins, counts))