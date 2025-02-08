"""
백준
하늘에서 별똥별이 빗발친다
https://www.acmicpc.net/problem/14658

어렵다고 느꼈는데 어렵지 않은 문제인가라고 생각하게 되는..
처음에는 온갖 여러가지 방법을 생각해보다가 그리디 알고리즘스럽게
접근했다. 각 좌표들을 원점과의 거리순으로 오름차순 정렬하고
순서대로 하나씩 트램폴린 면적안에 담아가는식이다. 이때 새로 담을려하는
별똥별 좌표에서 가장 멀리있는 이미 담아져 있는 별똥별의 좌표를 제거하는식으로
풀었다. 그림으로 보면 2d 평면 위에서 슬라이딩 윈도우를 하는 느낌이다.

이런식을로 풀기에는 그리디 알고리즘을 수학적으로 증명/풀어내는 로직이 존재하지 않아서
맞을 때도 있고 틀릴때도 있는것 같다.

결국 이문제는 모든 경우의 수를 고려하는 접근이 필요했다. 풀이법을 참고해서 
두개의 좌표를 골라서 트램폴린 면적이 되는 사각형의 두 변을 맞춰두고 그 안에
담기는 좌표들을 세어주는 방식의 풀이를 하게 되었다.

이때 굳이 두개의 점을 고를 이유가 있을까라는 생각도 자연스럽게 하게 된다. 왜냐하면
하나의 점을 면적이 되는 사각형 한쪽 모서리에 맞춰두는 것도 가능하기 때문이다.

하지만 두개의 좌표를 골라서 풀이를 하게 되면 자연스럽게 하나의 점이 모서리가 되는 경우를
고려할 수 있게 되지만 반대는 그렇지 못하다.

따라서 이문제는 모든 경우의 수를 찾는 브루트포스 풀이법을 이용하지만 어떤식으로 브루트포스 
할것인지에 대한 로직을 찾는 부분이 개인적으로는 어렵다는 느낌이 들었다.

참고로 평면과 트램폴린 면적의 크기 입력값은 크지만 별똥별의 수 (k) 는 그리 크지 않아서 
O(k^3) 시간복잡도로 통과가 가능하다: (두개의 좌표를 조합하고 그 좌표를 기점으로 하는 범위에
떨어지는 좌표의 개수 세기).
"""

import sys

def solution(stars, l):
    max_count = 0

    for x1, y1 in stars:
        for x2, y2 in stars:
            min_x = min(x1, x2)
            min_y = min(y1, y2)
            max_x = min_x + l
            max_y = min_y + l
            count = 0

            for star_x, star_y in stars:
                if min_x <= star_x <= max_x and min_y <= star_y <= max_y:
                    count += 1
            
            max_count = max(max_count, count)

    return len(stars) - max_count
        

if __name__ == "__main__":
    n, m, l, k = map(int, sys.stdin.readline().strip().split(" "))
    stars = [tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(k)]
    print(solution(stars, l))
