HEIGHT = 3
MODULO_VAL = 1_000_000_007

def solution(n):
    counts = [0, 1, 3, 10] + [0 for _ in range(4, n+1)]
    uniques = [12, 2, 4]
    
    for i in range(4, n+1):
        counts[i] = counts[i-1] + counts[i-2] * 2 + counts[i-3] * 5 + uniques[i % HEIGHT]
        uniques[i % HEIGHT] += counts[i-1] * 2 + counts[i-2] * 2 + counts[i-3] * 4
    
    return counts[n] % MODULO_VAL
