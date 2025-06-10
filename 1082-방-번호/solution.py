# import sys

# def solution(costs, budget):
#     min_price = min(costs)

#     def _solution(budget, digits):
#         nonlocal max_num

#         if budget < min_price:
#             num = int("".join(digits))
#             max_num = max(max_num, num)
#             return
        
#         for num, cost in enumerate(costs):
#             if cost <= budget:
#                 digits.append(str(num))
#                 _solution(budget - cost, digits)
#                 digits.pop()
    
#     max_num = -1
#     _solution(budget, [])
#     return max_num
            

# if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     costs = [int(val) for val in sys.stdin.readline().strip().split(" ")]
#     budget = int(sys.stdin.readline().strip())
#     print(solution(costs, budget))

import sys

def solution(costs, budget):
    dp = ["" for _ in range(budget + 1)]
    
    for b in range(1, budget + 1):
        for num, cost in enumerate(costs):
            if b >= cost:
               nums = dp[b - cost] + str(num)
               nums = "".join(sorted(nums, reverse=True))
               
               if not dp[b] or int(nums) > int(dp[b]):
                   dp[b] = nums
    
    return int(dp[budget])

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    costs = [int(val) for val in sys.stdin.readline().strip().split(" ")]
    budget = int(sys.stdin.readline().strip())
    print(solution(costs, budget))

