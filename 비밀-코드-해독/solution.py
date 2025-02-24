"""
프로그래머스
비밀 코드 해독
https://school.programmers.co.kr/learn/courses/30/lessons/388352

처음에는 어떻게 풀어야 할지 고민이 많이 되었는데 입력의 크기가
그렇게 크지 않아서 brute force 방법을 시도했다.

문제의 조건을 이해하는게 중요한데 예제에서 큰 힌트가 있었다.
시도하였던 모든 조합과 그 조합안에 포함된 정답인 번호의 개수가 있을때
어떤 조합이 비밀번호일 가능성을 갖기 위해서는 시도한 각각의 조합과 겹치는 
숫자가 그 조합을 시도했을때 포함된 정답인 번호의 개수와 동일해야된다는 것이다.

이점을 통해 모든 조합을 가져와서 조건을 확인해준다.
"""

from itertools import combinations

ANS = 0
Q = 1

def solution(n, q, ans):
    valid_combo_cnt = 0
    qna = sorted(zip(ans, q), reverse=True)
    
    if qna[0][ANS] == 5:
        return qna[0][Q]
    
    for combo in combinations(range(1, n+1), 5):
        combo_set = set(combo)
        
        for ans, q in qna:
            cnt = 0
            
            for num in q:
                if num in combo_set:
                    cnt += 1
            
            if cnt != ans:
                break
        else:
            valid_combo_cnt += 1
        
    return valid_combo_cnt