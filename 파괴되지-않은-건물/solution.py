"""
프로그래머스
파괴되지 않은 건물
https://school.programmers.co.kr/learn/courses/30/lessons/92344

간단하게 생각해서 주어진 입력값에 대해 건물의 내구도가 변화하는 것을 시뮬레이션하는
코드를 짜면 답을 찾을 수 있다.

하지만 문제에서 skill 배열은 최대 250,000 크기이다. 이럴경우 단순 시뮬레이션은 
시간초과를 피할 수 없다.
좀 더 시간을 효율적인 코드는 한번에 순회로 내구도 변화를 적용시키는 형태일것 같다는
짐작을 했는데 도저히 떠오르지 않았다.

풀이에 대한 힌트를 보고 풀었지만 아마 왠만해서는 생각해내지 못 했을 방법이라고 느꼈다.

간략하게 설명하면 각 내구도의 변화는 시작 인덱스와 끝 인덱스 구간이 주어지고 그 범위
안에 있는 셀을 주어진 숫자만큼 줄이거나 늘이는데 이때 특정한 방법으로 이 구간의 시작과 
끝부분을 변화량 만큼 마킹을해서 running sum 을 구해주면 해당 범위안에 있는 셀에
변화하는 값만큼 적용이 되는 알고리즘을 사용한 것이다. 이 노트는 설명보단 기록을 위한것이므로
자세한 풀이법은 여기서 확인 할 수 있다. https://tech.kakao.com/posts/488
"""
def solution(board, skill):
    rows = len(board)
    cols = len(board[0])
    mask = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for sign, start_r, start_c, end_r, end_c, degree in skill:
        offset = degree if sign == 2 else -degree
        mask[start_r][start_c] += offset
        if end_c + 1 < cols:
            mask[start_r][end_c + 1] += -offset
        if end_r + 1 < rows:
            mask[end_r + 1][start_c] += -offset
        if end_r + 1 < rows and end_c + 1 < cols:
            mask[end_r + 1][end_c + 1] += offset
            
    for r in range(rows):
        for c in range(1, cols):
            mask[r][c] += mask[r][c-1]
            
    for c in range(cols):
        for r in range(1, rows):
            mask[r][c] += mask[r-1][c]
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            if board[r][c] + mask[r][c] > 0:
                    count += 1
    return count
