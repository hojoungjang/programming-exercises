"""
백준
고층 건물
https://www.acmicpc.net/problem/1027

입력의 크기가 별로 크지 않다. 그래서 각 빌딩마다 자신을 제외한
다른 빌딩들과 높이를 비교하며 보이는 빌딩의 수는 세는 방식으로
풀이해 봤다. 일단 문제에서 주어진 조건대로 보이는 빌딩은 두 빌딩
높이를 잇는 선의 의해 결정된다. 더 자세히 보면 그 선의 기울기를
통해 조건에 부합하는지 알아낼 수 있다.

주어진 빌딩의 높이를 선회하며 나는 현재 주어지 빌딩에 대하야
왼쪽과 오른쪽으로 구분을 지어서 풀었다. 현재 빌딩에서 보이는 빌딩들은
제일 가까운 빌딩들부터 시작해서 점점 멀어질때 이미 마주하고 기록해둔
두 빌딩사이의 기울기 보다 작으면 안된다. 기울기가 더 작으면 이미
앞서 있는 빌딩의 의해 가려진다는 의미가 된다. 이때 기울기는 부호를 
포함을 한 상태에서의 더 작음을 뜻한다.

문제를 풀다가 좀 명확하게 로직을 생각하지 못했는지 왼쪽과 오른쪽의
비교가 살짝 다르다.
"""
import sys

def solution(heights):
    max_visible_count = 0

    for i in range(len(heights)):
        slope = float("inf")
        visible_count = 0

        # left
        for j in range(i-1, -1, -1):
            new_slope = (heights[i] - heights[j]) / (i - j)
            if new_slope < slope:
                slope = new_slope
                visible_count += 1
        
        # right
        slope = float("-inf")
        for j in range(i+1, len(heights)):
            new_slope = (heights[j] - heights[i]) / (j - i)
            if new_slope > slope:
                slope = new_slope
                visible_count += 1
        
        max_visible_count = max(max_visible_count, visible_count)

    return max_visible_count


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    heights = [int(h) for h in sys.stdin.readline().strip().split(" ")]
    print(solution(heights))