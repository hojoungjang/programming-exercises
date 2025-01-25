"""
백준
빌런 호석
https://www.acmicpc.net/problem/22251

감기에 걸려서 회고는 간략하게.

각 숫자 디스플레이마다 1 부터 min(7, p) 횟수 만큼
변경해보며 바뀐 디스플레이가 숫자를 만드는지 확인한다.
그리고 숫자로 바뀔수 있는 경우를 저장후 최종적으로
자리수 마다 경우의 수를 이용해 조합을 만들고 조건에
부합한 숫자를 최종적으로 만드는지 확인후 세어준다.
"""
import sys

LED_TO_NUM = {
    (1, 1, 1, 1, 0, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (0, 1, 1, 1, 1, 0, 1): 2,
    (0, 1, 1, 0, 1, 1, 1): 3,
    (1, 0, 1, 0, 1, 1, 0): 4,
    (1, 1, 0, 0, 1, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (0, 1, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 0, 1, 1, 1): 9,
}

NUM_TO_LED = {
    0: (1, 1, 1, 1, 0, 1, 1),
    1: (0, 0, 1, 0, 0, 1, 0),
    2: (0, 1, 1, 1, 1, 0, 1),
    3: (0, 1, 1, 0, 1, 1, 1),
    4: (1, 0, 1, 0, 1, 1, 0),
    5: (1, 1, 0, 0, 1, 1, 1),
    6: (1, 1, 0, 1, 1, 1, 1),
    7: (0, 1, 1, 0, 0, 1, 0),
    8: (1, 1, 1, 1, 1, 1, 1),
    9: (1, 1, 1, 0, 1, 1, 1),
}

LED_ELEMENT_COUNT = 7

def solution(n, k, p, x):
    """
    1. for each digit, get possible digits from 1 to p
    2. make combination of the possible digits and check if the number is within the range [1, N]

    n : max number in range
    k : number of LEDs
    p : max number of change
    x : start number
    """
    max_change_count = min(LED_ELEMENT_COUNT, p)

    def get_conversions(digit_led, idx, change_count):
        if change_count > max_change_count:
            return
        
        if change_count != 0 and (t_digit_led := tuple(digit_led)) in LED_TO_NUM:
            num = LED_TO_NUM[t_digit_led]
            conversions[start_digit][change_count].add(num)

        if idx >= LED_ELEMENT_COUNT:
            return
        
        digit_led[idx] = 0 if digit_led[idx] else 1
        get_conversions(digit_led, idx + 1, change_count + 1)
        digit_led[idx] = 0 if digit_led[idx] else 1
        get_conversions(digit_led, idx + 1, change_count)


    def get_digit_combinations(digit_led_chars, idx, change_count):
        num = int("".join(digit_led_chars))
        if 1 <= num <= n and 1 <= change_count <= p:
            ans.add(num)

        if idx >= len(digit_led_chars):
            return
        
        get_digit_combinations(digit_led_chars, idx + 1, change_count)

        digit_led = int(digit_led_chars[idx])
        for i in range(1, LED_ELEMENT_COUNT + 1):
            for new_digit in conversions[digit_led][i]:
                digit_led_chars[idx] = str(new_digit)
                get_digit_combinations(digit_led_chars, idx + 1, change_count + i)
        digit_led_chars[idx] = str(digit_led)


    conversions = [[set() for _ in range(7 + 1)] for _ in range(10)]
    digit_led_chars = [s for s in str(x)]
    if len(digit_led_chars) < k:
        diff = k - len(digit_led_chars)
        digit_led_chars = ["0"] * diff + digit_led_chars
    for digit_led_char in digit_led_chars:
        start_digit = int(digit_led_char)
        get_conversions(list(NUM_TO_LED[start_digit]), 0, 0)

    ans = set()
    get_digit_combinations(digit_led_chars, 0, 0)
    return len(ans)


if __name__ == "__main__":
    n, k, p, x = map(int, sys.stdin.readline().strip().split(" "))
    print(solution(n, k, p, x))
