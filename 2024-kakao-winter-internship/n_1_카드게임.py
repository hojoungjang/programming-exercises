def get_round_distance(cards, target):
    dist = {}
    for idx, card in enumerate(cards):
        pair = target - card
        pair_idx = cards.index(pair)
        dist[card] = abs((idx // 2) - (pair_idx // 2))
    return dist

def solution(coin, cards):
    target = len(cards) + 1
    dist = get_round_distance(cards, target)
    
    start_idx = len(cards) // 3
    my_cards = set(cards[:start_idx])
    pair_stash = set()
    for card in my_cards:
        if target - card in my_cards:
            pair = tuple(sorted([card, target - card]))
            pair_stash.add(pair)
    
    reserved_cards = set()
    for card in my_cards:
        for round_offset in range(len(pair_stash)+1):
            i = start_idx + 2 * round_offset
            if cards[i] + card == target:
                reserved_cards.add(cards[i])
                coin -= 1
            elif cards[i+1] + card == target:
                reserved_cards.add(cards[i+1])
                coin -= 1

    round = 1

    for i in range(start_idx, len(cards), 2):
        if not pair_stash and not coin:
            break

        if cards[i] in reserved_cards:
            pair_stash.add((cards[i], target - cards[i]))
            reserved_cards.remove(cards[i])
            my_cards.add(cards[i])

        if cards[i+1] in reserved_cards:
            pair_stash.add((cards[i+1], target - cards[i+1]))
            reserved_cards.remove(cards[i+1])
            my_cards.add(cards[i+1])

        # if cards[i] not in my_cards and target - cards[i] in my_cards and coin:
        #     pair_stash.add((cards[i], target - cards[i]))
        #     coin -= 1
        #     my_cards.add(cards[i])
        
        # if cards[i+1] not in my_cards and target - cards[i+1] in my_cards and coin:
        #     pair_stash.add((cards[i+1], target - cards[i+1]))
        #     coin -= 1
        #     my_cards.add(cards[i+1])

        if cards[i] not in my_cards and cards[i+1] not in my_cards and cards[i] + cards[i+1] == target and coin >= 2:
            pair_stash.add((cards[i], cards[i+1]))
            coin -= 2
            my_cards.add(cards[i])
            my_cards.add(cards[i+1])

        if cards[i] not in my_cards:
            card_dist = dist[cards[i]]
            if card_dist <= len(pair_stash):
                my_cards.add(cards[i])
                reserved_cards.add(target - cards[i])
                coin -= 2

        if cards[i+1] not in my_cards:
            card_dist = dist[cards[i+1]]
            if card_dist <= len(pair_stash):
                my_cards.add(cards[i+1])
                reserved_cards.add(target - cards[i+1])
                coin -= 2
        
        if not pair_stash:
            break

        num1, num2 = pair_stash.pop()
        my_cards.remove(num1)
        my_cards.remove(num2)
        round += 1
    
    return round


# class Solution:
#     def __init__(self, coin, cards):
#         self.coin = coin
#         self.cards = cards
#         self.round = 1
#         self.target = len(self.cards) + 1
#         self.start_idx = len(self.cards) // 3
#         self.my_cards = set()
#         self.discarded = set()
#         self.pair_stash = set()
        
#     def setup_game(self):
#         for card in self.cards[:self.start_idx]:
#             if self.target - card in self.my_cards:
#                 pair = tuple(sorted([card, self.target - card]))
#                 self.pair_stash.add(pair)
#                 self.my_cards.remove(self.target - card)
#             else:
#                 self.my_cards.add(card)

#     def match_my_and_new_cards(self, new_cards):
#         used = set()
#         for card in new_cards:
#             if self.target - card in self.my_cards and self.coin:
#                 self.pair_stash.add((card, self.target - card))
#                 self.my_cards.remove(self.target - card)
#                 used.add(card)
#                 coin -= 1
#         return used

#     def match_discard_and_new_cards(self, new_cards):
#         used = set()
#         for card in new_cards:
#             if self.target - card in self.discarded and coin >= 2:
#                 self.pair_stash.add((card, self.target - card))
#                 self.discarded.remove(self.target - card)
#                 used.add(card)
#                 coin -= 2
#                 break
        
#         return used
#             # else:
#             #     self.discarded.add(card)
        

#     def match_discard_and_discard_cards(self, new_cards):
#         pass

#     def start_game(self):
#         start_idx = len(self.cards) // 3
#         actions = [
#             self.match_my_and_new_cards,
#             self.match_discard_and_new_cards,
#             self.match_discard_and_discard_cards,
#         ]
        
#         for i in range(start_idx, len(self.cards), 2):
#             new_cards = self.cards[i:i + 2]
#             used = set()

#             for action in actions:
#                 action()
#                 if self.pair_stash:
#                     break
            
#             self.pair_stash.pop()




def solution2(coin, cards):
    target = len(cards) + 1
    start_idx = len(cards) // 3
    my_cards = set()
    discarded = set()
    pair_stash = set()
    for card in cards[:start_idx]:
        if target - card in my_cards:
            pair = tuple(sorted([card, target - card]))
            pair_stash.add(pair)
            my_cards.remove(target - card)
        else:
            my_cards.add(card)

    round = 1

    for i in range(start_idx, len(cards), 2):
        if target - cards[i] in my_cards and coin:
            pair_stash.add((cards[i], target - cards[i]))
            my_cards.remove(target - cards[i])
            coin -= 1

        if target - cards[i+1] in my_cards and coin:
            pair_stash.add((cards[i+1], target - cards[i+1]))
            my_cards.remove(target - cards[i+1])
            coin -= 1

        if pair_stash:
            pair_stash.pop()
            if (cards[i], target - cards[i],) not in pair_stash:
                discarded.add(cards[i])
            if (cards[i+1], target - cards[i+1],) not in pair_stash:
                discarded.add(cards[i+1])
            round += 1
            continue

        if target - cards[i] in discarded and coin >= 2:
            pair_stash.add((cards[i], target - cards[i]))
            discarded.remove(target - cards[i])
            coin -= 2
        else:
            discarded.add(cards[i])
        
        if target - cards[i+1] in discarded and coin >= 2:
            pair_stash.add((cards[i+1], target - cards[i+1]))
            discarded.remove(target - cards[i+1])
            coin -= 2
        else:
            discarded.add(cards[i+1])

        if not pair_stash and coin >= 2:
            for card in discarded:
                if target - card in discarded:
                    pair_stash.add((card, target - card))
                    discarded.remove(card)
                    discarded.remove(target - card)
                    coin -= 2
                    break

        if not pair_stash:
            break
            
        pair_stash.pop()
        round += 1
    
    return round


if __name__ == "__main__":
    ans = solution2(coin=4, cards=[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])
    print(ans)

    ans = solution2(coin=3, cards=[1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12])
    print(ans)
    
    ans = solution2(coin=2, cards=[5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7])
    print(ans)

    ans = solution2(coin=10, cards=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    print(ans)

    ans = solution2(coin=3, cards=[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    print(ans)    
