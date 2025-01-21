"""
백준
문자열 게임 2
https://www.acmicpc.net/problem/20437

문제의 두번째 조건을 제대로 이해하지 못해서 뻘짓을 좀 했다.
첫번째는 substring 이면서 어떤 문자를 k 개 갖는 문자열중
최소 길이를 찾는것.

문자셋은 소문자 알파벳 a 에서 z 까지이고 각 문자마다
큐를 만들어서 매핑했다. 
나는 입력 문자열의 각 문자를 보면서 해당 문자의 인덱스를 
큐에다가 넣어주고 큐의 길이를 확인해 k 이면 최소길이를 
담고있는 변수를 업데이트 해주고 제일 앞에서 본 문자 인덱스를
제거하는 방법을 떠올렸다.

두번쨰 조건을 처음 봤을때 substring 의 첫번째와 마지막 문자가 같아야 한다로만
이해했다. 근데 알고보니 첫번째와 마지막이 되는 문자가 개수가 k 개인 문자랑
동일하다는 뜻이었다.

이렇게 되면 단순히 위에서 최소길이를 업데이트 할때 최대길이를 담는 변수를 만들어두고
최대길이도 같이 업데이트 해주면 된다.
"""
import sys
from collections import deque

def solution(s, k):
    occurences = {char: deque() for char in "abcdefghijklmnopqrstuvwxyz"}

    min_len = len(s) + 1
    max_len = -1

    for idx, char in enumerate(s):
        occurences[char].append(idx)
        if len(occurences[char]) == k:
            sub_str_len = occurences[char][-1] - occurences[char][0] + 1
            min_len = min(min_len, sub_str_len)
            max_len = max(max_len, sub_str_len)
            occurences[char].popleft()

    return min_len, max_len
    

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        k = int(sys.stdin.readline().strip())
        
        min_len, max_len = solution(s, k)
        
        if max_len == -1:
            print("-1")
        else:
            print(f"{min_len} {max_len}")
