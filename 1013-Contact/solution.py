"""
백준
Contact
https://www.acmicpc.net/problem/1013

regex 를 이용하지 않은 풀이랑 이용한 풀이랑 둘다 해보았다.
"""

import sys
import re


def solution(code):
    """
    (100+1+ | 01)+
    """
    code = [c for c in code]

    if len(code) < 2:
        return False
    
    idx = 0
    while idx < len(code):
        if code[idx] == "0":
            cnt = 0
            while idx < len(code) and code[idx] == "0":
                cnt += 1
                idx += 1
            
            if cnt == 1:
                if idx >= len(code):
                    return False
                else:
                    code[idx-1] = code[idx] = "-1"
                idx += 1
        else:
            idx += 1

    idx = 0
    while idx < len(code):
        if code[idx] == "0":
            cnt = 0
            temp_idx = idx - 1
            while temp_idx >= 0 and code[temp_idx] == "1":
                cnt += 1
                temp_idx -= 1
            if cnt < 2:
                return False
            idx -= 1

        elif code[idx] == "1":
            if "".join(code[idx:idx+3]) != "100":
                return False
            
            idx += 3
            while idx < len(code) and code[idx] == "0":
                idx += 1

            if idx >= len(code) or code[idx] == "-1":
                return False
            
            while idx < len(code) and code[idx] == "1":
                idx += 1

        else:
            idx += 1
    
    return True


def solution_regex(code):
    pattern = r"((100+1+)|(01))+"
    match = re.fullmatch(pattern, code)
    return False if match is None else True

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        code = sys.stdin.readline().strip()
        print("YES" if solution(code) else "NO")
