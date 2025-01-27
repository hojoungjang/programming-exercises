"""
백준
스카이라인 쉬운거
https://www.acmicpc.net/problem/1863

높이가 변할때마다 빌딩의 최소개수가 늘어나는 규칙이 보인다.
단 예외가 이미 보았던 높이는 이어지는 경우로 만들수 있기 때문에
최소빌딩 조건을 고려했을때 카운트 하지 않는게 맞다.

처음에는 set 을 이용해서 유니크한 높이들의 개수로 생각하고 풀어지만
예외 케이스가 존재 했다. 이 경우는 높이가 낮아졌다가 다시 높아지는 경우다.
아래의 경우 높이 3은 고유하게 처리하면 하나의 빌딩으로 되지만 실제로는
빌딩 두개이다.

 x x
 x x
xxxx

따라서 고유 높이를 카운트하는것이 아니라 높아지고 낮아지는 경우의 따라
로직을 처리를 해줘야한다. 이때 생각난게 스택이다. 높이가 높아질때는 
스택에 계속 높이값을 넣어주고 낮아졌을때는 스택 맨위 있는 높이가 현재
높이보다 작거나 같은때까지 스택을 팝하고 빌딩개수를 늘려준다.
주의할점은 스택에 높이 0 이나 스택 맨위가 현재 높이가 같을경우
현재 높이값을 추가 하지 않는것이다. 높이가 0이면 빌딩이 없다는 뜻이고
높이가 같을 경우 이전에 봤던 빌딩을 늘려 이어줄 수 있기 때문에 이 두경우
모두 값을 추가해버려 잘 못된 최소빌딩수를 계산한다. 
"""
import sys

def solution(coords):
    stack = []
    building_count = 0

    for _, y in coords:
        while stack and stack[-1] > y:
            stack.pop()
            building_count += 1
        if y != 0 and (not stack or stack[-1] != y):
            stack.append(y)

    building_count += len(stack)
    return building_count

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    coords = [tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]
    print(solution(coords))
