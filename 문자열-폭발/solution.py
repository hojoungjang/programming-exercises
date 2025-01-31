"""
백준
문자열 폭발
https://www.acmicpc.net/problem/9935

스택의 개념을 사용한다. 파이썬에서는 간단하게 리스트로 구현이
가능하다. 원래 문자열에서 문자를 하나씩 가져와서 리스트에 붙이고
새로 문자열이 추가됨에 따라 폭발문자열이 만들어지면 폭발문자열 만큼
리스트에서 없애준다. 

리스트의 append, pop 함수는 amortized O(1) 이기 때문에
매번 새롭게 다시 문자열이나 배열을 복사하는 과정보다 효율적이다.

다른분의 풀이를 통해 한가지 찾아낸 점은 폭발문자열을 비교할때 string
타입으로 비교하는것 보다 list 형태 (즉 list of character string)
으로 비교하는것이 연산이 더 빨랐다는 점이다.
"""

import sys

def solution(string, rm_string):
    new_string = []
    rm_string = [char for char in rm_string]

    for char in string:
        new_string.append(char)

        if new_string[-len(rm_string):] == rm_string:
            for _ in range(len(rm_string)):
                new_string.pop()

    return "".join(new_string) if new_string else "FRULA"

if __name__ == "__main__":
    string = sys.stdin.readline().strip()
    rm_string = sys.stdin.readline().strip()
    print(solution(string, rm_string))