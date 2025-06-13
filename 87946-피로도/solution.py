"""
https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
def solution(k, dungeons):
    
    def _solution(energy):
        nonlocal max_cnt
        
        max_cnt = max(max_cnt, len(visited))
        
        for i in range(len(dungeons)):
            energy_req, energy_cost = dungeons[i]
            if i in visited:
                continue
            if energy_req > energy:
                continue
            visited.add(i)
            _solution(energy - energy_cost)
            visited.remove(i)
    
    max_cnt = 0
    visited = set()
    _solution(k)
    return max_cnt
