import sys

def solution(eggs):

    def break_eggs(idx, broken_cnt):
        nonlocal max_broken_cnt
        max_broken_cnt = max(max_broken_cnt, broken_cnt)

        if idx >= n:
            return
        
        d1, w1 = eggs[idx]
        
        if d1 <= 0:
            break_eggs(idx + 1, broken_cnt)
            return
        
        orig_broken_cnt = broken_cnt

        for i in range(n):
            d2, w2 = eggs[i]
            
            if i == idx or d2 <= 0:
                continue

            if d1 - w2  <= 0:
                eggs[idx][0] = 0
                broken_cnt += 1
            else:
                eggs[idx][0] = d1 - w2

            if d2 - w1 <= 0:
                eggs[i][0] = 0
                broken_cnt += 1
            else:
                eggs[i][0] = d2 - w1

            break_eggs(idx + 1, broken_cnt)

            broken_cnt = orig_broken_cnt
            eggs[idx][0] = d1
            eggs[i][0] = d2
    
    n = len(eggs)
    max_broken_cnt = 0
    break_eggs(0, 0)
    return max_broken_cnt

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    eggs = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    print(solution(eggs))