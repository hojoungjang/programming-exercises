"""
백준
회문
https://www.acmicpc.net/problem/17609
"""
import sys

def check_palindrome(s):
    if len(s) % 2 == 0:
        hi = len(s) // 2
        lo = hi - 1
    else:
        mid = len(s) // 2
        lo =  mid - 1
        hi = mid + 1

    while lo >= 0 and hi < len(s):
        if s[lo] != s[hi]:
            return False
        lo -= 1
        hi += 1
    return True

def _check_pseudo_palindrome(s, lo, hi):
    while lo >= 0 and hi < len(s):
        if s[lo] != s[hi]:
            if check_palindrome(s[:lo] + s[lo+1:]) or check_palindrome(s[:hi] + s[hi+1:]):
                return True
            else:
                return False
        lo -= 1
        hi += 1
    return True

def check_pseudo_palindrome(s):
    if len(s) % 2 == 0:
        mid_hi = len(s) // 2
        mid_lo = mid_hi - 1

        for mid in [mid_hi, mid_lo]:
            lo = mid - 1
            hi = mid + 1
            if _check_pseudo_palindrome(s, lo, hi):
                return True
    else:
        mid = len(s) // 2
        for lo, hi in [(mid-1, mid), (mid, mid+1)]:
            if _check_pseudo_palindrome(s, lo, hi):
                return True
        
        if check_palindrome(s[:mid] + s[mid+1:]):
            return True

    return False
    

def solution(s):
    if check_palindrome(s):
        return 0
    elif check_pseudo_palindrome(s):
        return 1
    return 2

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        print(solution(s))