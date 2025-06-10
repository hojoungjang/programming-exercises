import sys
sys.setrecursionlimit(3000 + 1)

def solution(folds):

    def _solution(lo, hi):
        if lo > hi:
            return True
        
        mid = (lo + hi) // 2
        
        if not _solution(lo, mid - 1) or not _solution(mid + 1, hi):
            return False
        
        i = mid - 1
        j = mid + 1
        while i >= lo and j <= hi:
            if folds[i] == folds[j]:
                return False
            i -= 1
            j += 1
        return True

    return _solution(0, len(folds)-1)


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        folds = [val for val in sys.stdin.readline().strip()]
        if solution(folds):
            print("YES")
        else:
            print("NO")
