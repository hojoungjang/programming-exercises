def solution(scores):
    wanho_score = tuple(scores[0])

    eligible_scores = []
    max_score2 = 0
    for score1, score2 in sorted(scores, key=lambda s: (-s[0], s[1])):
        if score2 < max_score2:
            continue
        max_score2 = score2
        eligible_scores.append((score1, score2))
        
    eligible_scores.sort(key=lambda s: sum(s), reverse=True)
    rank = 0
    rank_size = 1
    score_sum = float("inf")
    
    for i in range(len(eligible_scores)):
        new_score_sum = sum(eligible_scores[i])
        
        if new_score_sum < score_sum:
            score_sum = new_score_sum
            rank += rank_size
            rank_size = 1
        elif new_score_sum == score_sum:
            rank_size += 1
            
        if eligible_scores[i] == wanho_score:
            return rank
        
    return -1
