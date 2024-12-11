from typing import List, Dict


class GiftStat:
    def __init__(self, name: str, friends: List[str]):
        self.name = name
        self.gifts_sent = {f: 0 for f in friends}
        self.gift_exp = 0


def init_gift_stats(friends: List[str], gifts: List[str]):
    gift_stats: Dict[str, GiftStat] = {f: GiftStat(f, friends) for f in friends}
    
    for gift_record in gifts:
        sender, receiver = gift_record.split(" ")
        
        sender_stat = gift_stats.get(sender)
        receiver_stat = gift_stats.get(receiver)
        if not sender_stat or not receiver_stat:
            raise Exception("unable to find sender or receiver in friends list")
        
        sender_stat.gifts_sent[receiver] += 1
        sender_stat.gift_exp += 1
        receiver_stat.gift_exp -= 1
        
    return gift_stats

        
def solution(friends, gifts):
    gift_stats = init_gift_stats(friends, gifts)
    max_exp_gifts = 0
    
    for sender in friends:
        exp_gifts = 0
        sender_stat = gift_stats.get(sender)
        for receiver, sent_cnt in sender_stat.gifts_sent.items():
            receiver_stat = gift_stats.get(receiver)
            received_cnt = receiver_stat.gifts_sent.get(sender, 0)
            
            if sent_cnt > received_cnt:
                exp_gifts += 1
            elif sent_cnt == received_cnt and sender_stat.gift_exp > receiver_stat.gift_exp:
                exp_gifts += 1
        
        max_exp_gifts = max(max_exp_gifts, exp_gifts)
    
    return max_exp_gifts


if __name__ == "__main__":
    friends = ["muzi", "ryan", "frodo", "neo"]
    gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    solution(friends, gifts)
