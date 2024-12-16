from itertools import product
from math import ceil

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    combo = product(discounts, repeat=len(emoticons))
    
    max_membership = 0
    max_memb_revenue = 0
    
    for disc_combo in combo:
        rate_map = {disc: [] for disc in discounts}
        
        for i, disc_rate in enumerate(disc_combo):
            rate_map[disc_rate].append(emoticons[i] * (1 - disc_rate / 100))
        
        membership = 0
        revenue = 0
        
        for disc_req, memb_threshold in users:
            disc_req = ceil(disc_req / 10) * 10
            spend = 0
            
            for disc in discounts:
                if disc >= disc_req:
                    spend += sum(rate_map[disc])
            
            if spend >= memb_threshold:
                membership += 1
            else:
                revenue += spend
                
        if membership > max_membership:
            max_membership = membership
            max_memb_revenue = revenue
        elif membership == max_membership and revenue > max_memb_revenue:
            max_memb_revenue = revenue

    return [max_membership, int(max_memb_revenue)]


if __name__ == "__main__":
    print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
