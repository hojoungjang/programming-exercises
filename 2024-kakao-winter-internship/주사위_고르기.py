from bisect import bisect_left, bisect_right
from itertools import combinations, product


def solution(dice):
    n = len(dice)
    sorted_dice = [sorted(d) for d in dice]     # O(n)
    combo_wins = {}
    
    # Combinations for choosing dice
    dice_selections = list(combinations(range(n), n//2))    # O(n! / (n-k)!k!)
    half_len = len(dice_selections) // 2
    
    # O(n! / (n-k)!k!) * (6^n)log(6^n)
    for a_dice_indices, b_dice_indices in zip(dice_selections[:half_len], dice_selections[-1:half_len-1:-1]):
        a_dice = [sorted_dice[d_idx] for d_idx in a_dice_indices]   # n / 2
        a_dice_sums = [sum(faces) for faces in product(*a_dice)]    # 6 ^ n
        
        b_dice = [sorted_dice[d_idx] for d_idx in b_dice_indices]
        b_dice_sums = sorted([sum(faces) for faces in product(*b_dice)])    # (6^n)log(6^n)

        wins = 0
        loses = 0
        for a_dice_sum in a_dice_sums:
            wins += bisect_left(b_dice_sums, a_dice_sum)
            loses += len(b_dice_sums) - bisect_right(b_dice_sums, a_dice_sum)

        combo_wins[a_dice_indices] = wins
        combo_wins[b_dice_indices] = loses

    max_wins = 0
    max_combo = []
    for combo, wins in combo_wins.items():
        if wins > max_wins:
            max_wins = wins
            max_combo = combo
    return [i + 1 for i in max_combo]


if __name__ == "__main__":
    dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
    
    ans = solution(dice)
    print(ans)
