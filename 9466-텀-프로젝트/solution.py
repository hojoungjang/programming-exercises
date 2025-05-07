"""
백준
텀 프로젝트
https://www.acmicpc.net/problem/9466
"""
import sys

def solution(nums):
    visited = set()
    team_visited = set()

    for num, next_num in enumerate(nums[1:], 1): 
        if num in visited:
            continue

        _visited = set()
        while num not in _visited:
            if num in visited:
                cycle = False
                break

            _visited.add(num)
            visited.add(num)
            num = next_num
            next_num = nums[num]
        else:
            cycle = True

        if cycle:
            while num not in team_visited:
                team_visited.add(num)
                num = next_num
                next_num = nums[num]

    return len(nums) - 1 - len(team_visited)
        

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = [int(val) for val in sys.stdin.readline().strip().split(" ")]
        nums = [0] + nums
        print(solution(nums))
