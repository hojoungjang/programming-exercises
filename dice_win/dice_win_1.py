import heapq
from itertools import combinations, product

DICE_FACES = 6

def dice_combo(n):
    half = n // 2
    for a_combo in combinations(range(n), half):
        b_combo = tuple(i for i in range(n) if i not in a_combo)
        yield (a_combo, b_combo)


def count_wins(dice, a_combo, b_combo):
    wins = 0
    half = len(a_combo)
    for a_face_indices in product(*[[i for i in range(DICE_FACES)] for _ in range(half)]):
        
        a_dice_sum = 0

        for a_dice_idx, a_face_idx in zip(a_combo, a_face_indices):
            a_dice_sum += dice[a_dice_idx][a_face_idx]
            
        b_dice_sum = sum(dice[b_dice_idx][0] for b_dice_idx in b_combo)
        
        if b_dice_sum >= a_dice_sum: continue
            
        b_face_indices = {b_dice_idx: 1 for b_dice_idx in b_combo}
        min_heap = [(dice[b_dice_idx][1], b_dice_idx) for b_dice_idx in b_combo]
        heapq.heapify(min_heap)
        
        while a_dice_sum > b_dice_sum: 
            
            while min_heap:
                min_val, b_dice_idx = heapq.heappop(min_heap)
                if b_dice_idx < DICE_FACES:
                    break
            else:
                break
            
            b_face_idx = b_face_indices[b_dice_idx]
            b_dice_sum -= dice[b_dice_idx][b_face_idx-1]
            b_dice_sum += dice[b_dice_idx][b_face_idx]
            b_face_indices[b_dice_idx] = b_face_idx + 1

            if b_face_idx + 1 < DICE_FACES:
                heapq.heappush(min_heap, (dice[b_dice_idx][b_face_idx+1], b_dice_idx))
            
        current_wins = 1
        for _, b_face_idx in b_face_indices.items():
            current_wins *= b_face_idx
            
        wins += current_wins
                
    return wins

    
def solution(dice):
    # sort each dice
    sorted_dice = [sorted(d) for d in dice]
    print(sorted_dice)
    
    max_wins = 0
    max_combo = []
    
    # Pick (n / 2) out of n combination
    for a_combo, b_combo in dice_combo(len(dice)):
        wins = count_wins(sorted_dice, a_combo, b_combo)
        print(wins)
        if wins > max_wins:
            max_wins = wins
            max_combo = list(a_combo)
    
    return [idx+1 for idx in max_combo]


if __name__ == "__main__":
    dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
    
    ans = solution(dice)
    print(ans)
