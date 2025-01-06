"""
프로그래머스
광물 캐기
https://school.programmers.co.kr/learn/courses/30/lessons/172927

input constraint 는 모든 경우의 수 완전 탐색을 가능하게 한다.
그래도 뭔가 그리디 알골리즘으로 접근 할 수 있지 않을까라는 생각 때문에 
다섯개씩 짤라서 제일 티어가 높은 광물에 맞춰서 곡괭이를 골랐는데 이 방법은
좋은 곡괭이를 나중에 오는 광물에 사용하는 겅우를 고려하지 못 하기 때문에 알맞지 못하다.
"""

MINERALS = {
    "diamond": 0,
    "iron": 1,
    "stone": 2,
    "": 3,
}

ENERGY_REQUIRED = [
    [1, 1, 1, 0],
    [5, 1, 1, 0],
    [25, 5, 1, 0],
]

def solution(picks, minerals):
    
    def mine(idx):
        if idx >= len(minerals) or all(p == 0 for p in picks):
            return 0
        
        min_energy = float("inf")
        for pick_idx in range(len(picks)):
            available_cnt = picks[pick_idx]
            
            if available_cnt <= 0:
                continue
            
            picks[pick_idx] -= 1
            energy = 0
            for i in range(idx, idx+5):
                mineral_idx = MINERALS[minerals[i]]
                energy += ENERGY_REQUIRED[pick_idx][mineral_idx]
            energy += mine(idx+5)
            min_energy = min(min_energy, energy)
            picks[pick_idx] += 1
            
        return min_energy
    
    
    while len(minerals) % 5 != 0:
        minerals.append("")
    return mine(0)


if __name__ == "__main__":
    print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
