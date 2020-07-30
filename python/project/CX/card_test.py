#-*- coding:utf-8 -*- 
import random
from cards import Card

deck = []
# 建立一副牌
for suit_id in range(1, 5):
    for rand_id in range(1, 14):
        deck.append(Card(suit_id, rand_id))

# 从一副牌中选 5 张牌作为一手牌
hand = []
for cards in range(0, 5):
    a = random.choice(deck)
    hand.append(a)
    deck.remove(a)

print
for card in hand:
    print card.short_name, "  值:", card.value