"""
백준
0 만들기
https://www.acmicpc.net/problem/7490

감기에 걸려서 회고는 간략하게.

모든 경우의 수를 찾는 완전탐색으로 해결 가능.
각 숫자들 사이에 +, - 또는 빈공백을 이용해
수식을 만들고 그 수식을 계산해서 0이 되는지 확인.

eval() 함수를 사용하지 않고 풀어보고 싶었지만 일단
간편하게 사용했다. 마지막 결과물은 정렬을 하고 출력한다.
"""
import sys

def format_eq(equation):
    new_eq = equation[:]
    for i in range(len(equation)):
        if new_eq[i] == "":
            new_eq[i] = " "
    return "".join(new_eq)

def solution(n):
    zero_equations = []

    def _solution(equation, num):
        if num > n:
            if eval("".join(equation)) == 0:
                zero_equations.append(format_eq(equation))
            return
    
        for operator in ["+", "-", ""]:
            equation.append(operator)
            equation.append(str(num))
            _solution(equation, num + 1)
            equation.pop()
            equation.pop()

    _solution(["1"], 2)
    zero_equations.sort()
    return zero_equations

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        eqs = solution(n)

        for eq in eqs:
            print(eq)
        print()
