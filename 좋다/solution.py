"""
백준
좋다
https://www.acmicpc.net/problem/1253

일단 어떤 수는 주어진 숫자들중 다른 두수를 합쳐서 만들수 있으면 좋은 숫자다.
처음에는 간단해보이지만 몇가지 조건들이 있다.

첫째는 숫자는 중복될수 있다.

둘째는 어떤 수를 다른 두수의 합으로 표현할때 자기 자신은 사용하면 안된다.
예를 들어 0 + 5 = 5 에서 같은 5 가 사용되면 안된다.

일단 입력의 값이 너무 크지 않기 때문에 시간복잡도가 O(n^2) 까지는 괜찮다.
각 숫자마다 자기 자신을 제외한 다른 숫자들과의 차를 구해서 차가 배열에 존재하면
좋은 숫자이다. 이때 차가 자기 자신또는 선택한 숫자랑 겹치는지 확인해준다.

의문인점은 내가 풀이한 방식은 worst case O(n^3) 에 가까운데 통괴가 되긴한다.
더 효율적이면서 이해하기 쉬운 방식은 투포인터 방법이였다.
각 숫자마다 정렬된 배열에서 투포인터를 이용해 합이될때까지 두개의 숫자를 찾아내는 것이다.
물론 이때 고른 숫자들이 서로 겹치지 않게 해야 한다.

다른 방법으로는 정렬후 이분탐색도 가능한것같은데 생각만 해보았을때는 고른 숫자들이 겹치지 않게 하는게 
까다로울것같다.
"""

import sys

def solution(nums):
    index = {num: [] for num in nums}
    for i in range(len(nums)):
        index[nums[i]].append(i)
    
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue

            target = nums[i] - nums[j]
            if target in index and index[target]:
                if len([idx for idx in index[target] if idx not in [i, j]]) > 0:
                    count += 1
                    break

    return count

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    print(solution(nums))
