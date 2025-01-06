from itertools import combinations, product

DICE_FACES = 6

def dice_combo(n):
    half = n // 2
    for a_combo in combinations(range(n), half):
        b_combo = tuple(i for i in range(n) if i not in a_combo)
        yield (a_combo, b_combo)


def count_wins(dice, a_combo, b_combo):
    wins = 0
    draws = 0
    loses = 0
    half = len(a_combo)
    breakpoint()
    
    face_combos = list(product(*[[i for i in range(DICE_FACES)] for _ in range(half)]))
    
    b_dice_sums = {}
    for b_face_indices in face_combos:
        b_dice_sum = 0
        for b_dice_idx, b_face_idx in zip(b_combo, b_face_indices):
            b_dice_sum += dice[b_dice_idx][b_face_idx]
        b_dice_sums[b_face_indices] = b_dice_sum
    
    for a_face_indices in face_combos:
        
        a_dice_sum = 0

        for a_dice_idx, a_face_idx in zip(a_combo, a_face_indices):
            a_dice_sum += dice[a_dice_idx][a_face_idx]
            
        for b_face_indices in face_combos:
            b_dice_sum = b_dice_sums[b_face_indices]
            
            if a_dice_sum > b_dice_sum:
                wins += 1
            elif a_dice_sum == b_dice_sum:
                draws += 1
            else:
                loses += 1
                
    return wins, draws, loses

    
def solution(dice):
    # sorted_dice = [sorted(d) for d in dice]
    
    combo_wins = {}
    
    for a_combo, b_combo in dice_combo(len(dice)):
        if a_combo in combo_wins:
            continue
        wins, _, loses = count_wins(dice, a_combo, b_combo)
        combo_wins[a_combo] = wins
        combo_wins[b_combo] = loses
    
    max_wins = 0
    max_combo = []
    for combo, wins in combo_wins.items():
        if wins > max_wins:
            max_combo = combo
            max_wins = wins
    
    return [i+1 for i in max_combo]


if __name__ == "__main__":
    dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
    
    ans = solution(dice)
    print(ans)
