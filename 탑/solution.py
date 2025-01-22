"""
백준
탑
https://www.acmicpc.net/problem/2493

빨주노초 암 레젠드 따노스.. 가 아니라 이문제는 쉽다.

거꾸로 순회하며 나보다 높이가 높거나 같은 타워를 만나면 그 타워의 인덱스를
나의 인덱스의 저장하는 것이다. 

간다하게는 nested loop 을 사용해서 n^2 시간복잡도 형시으로 푸는것이지만 더
효율적인 방법이 있다. 그걸 이루기 위해 look back 개념의 구현이 필요한데 
바로 스택을 이용하는거다.

만약 현재 보고있는 타워의 높이가 스택위에 있는 타워의 높이보다 크거나 같으면
스택 위의 타워보다 작을 때까지 스택을 pop 한다.
스택안에는 해당 높이의 인덱스 정보를 필수적으로 담아주고 있어야 하고 그 인덱스를
사용해 해당 인덱스의 값으로 현재 타워의 높이를 담아준다.
그리고 더 낮은 높이의 타워를 만나면 바로 스택에 넣고 다음 타워로 넘어간다.
"""
import sys

def solution(heights):
    receivers = [0 for _ in range(len(heights))]
    stack = []
    for cur_idx in reversed(range(len(heights))):
        while stack and heights[stack[-1]] <= heights[cur_idx]:
            stack_top_idx = stack.pop()
            receivers[stack_top_idx] = cur_idx + 1
        stack.append(cur_idx)
    return receivers

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    heights = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    ans = solution(heights)
    print(" ".join(str(h) for h in ans))