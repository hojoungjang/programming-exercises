"""
프로그래머스
할인 행사
https://school.programmers.co.kr/learn/courses/30/lessons/131127
"""

WINDOW = 10

def solution(want, number, discount):
    
    def check_item_counts():
        for item_name, item_count in zip(want, number):
            if discount_items[item_name] < item_count:
                return False
        return True
    
    discount_items = {item: 0 for item in want}
    for i in range(min(WINDOW, len(discount))):
        if (name := discount[i]) not in discount_items:
            discount_items[name] = 0
        discount_items[name] += 1
    
    ans = 0
    if check_item_counts():
        ans += 1
        
    for i in range(WINDOW, len(discount)):
        rm_item_name = discount[i-WINDOW]
        add_item_name = discount[i]
        discount_items[rm_item_name] -= 1
        
        if add_item_name not in discount_items:
            discount_items[add_item_name] = 0
        discount_items[add_item_name] += 1
        
        if check_item_counts():
            ans += 1
    
    return ans
