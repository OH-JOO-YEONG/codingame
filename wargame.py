import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of cards for player 1
deck_1 = []
deck_2 = []
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    deck_1.append(cardp_1)

m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    deck_2.append(cardp_2)


def get_rank(card):
    num = card[:-1]
    if num == "J":
        return 11
    elif num == "Q":
        return 12
    elif num == "K":
        return 13
    elif num == "A":
        return 14
    else:
        return int(num)


def fight(card1, card2):
    rank1 = get_rank(card1)
    rank2 = get_rank(card2)

    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return 2
    else:
        return 0


def war(deck_1, deck_2, card1, card2):
    result = 0

    used_deck1 = [card1]
    used_deck2 = [card2]
    while len(deck_1) > 3 and len(deck_2) > 3:
        for i in range(3):
            used_deck1.append(deck_1.pop(0))
            used_deck2.append(deck_2.pop(0))

        card1 = deck_1.pop(0)
        card2 = deck_2.pop(0)
        used_deck1.append(card1)
        used_deck2.append(card2)

        result = fight(card1, card2)

        if result == 1:
            deck_1.extend(used_deck1)
            deck_1.extend(used_deck2)
            break
        if result == 2:
            deck_2.extend(used_deck1)
            deck_2.extend(used_deck2)
            break
    return (result, deck_1, deck_2)


turn = 0
result = 0

while len(deck_1) > 0 and len(deck_2) > 0:
    turn += 1
    card1 = deck_1.pop(0)
    card2 = deck_2.pop(0)

    result = fight(card1, card2)

    if result == 1:
        deck_1.extend([card1, card2])
    elif result == 2:
        deck_2.extend([card1, card2])
    else:
        result, deck_1, deck_2 = war(deck_1, deck_2, card1, card2)
        if result == 0:
            break

if result == 0:
    print("PAT")
elif len(deck_1) > 0:
    print("1 {}".format(turn))
else:
    print("2 {}".format(turn))

import sys
import math

# card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#
#
# def get_rank(card):
#     return card_ranks.index(card[:-1])
#
#
# def fight(card1, card2):
#     rank1 = get_rank(card1)
#     rank2 = get_rank(card2)
#
#     if rank1 > rank2:
#         return 1
#     elif rank1 < rank2:
#         return 2
#     else:
#         return 0
#
#
# n = int(input())  # the number of cards for player 1
# deck1 = [input() for i in range(n)]
#
# m = int(input())  # the number of cards for player 2
# deck2 = [input() for j in range(m)]
#
# rounds = 0
# result = 0
# while len(deck1) > 0 and len(deck2) > 0:
#     rounds += 1
#     index = 0
#     result = fight(deck1[index], deck2[index])
#     while result == 0:
#         index += 4
#         if index >= len(deck1) or index >= len(deck2):
#             break
#         result = fight(deck1[index], deck2[index])
#
#     if result == 1:
#         deck1, deck2 = deck1[index + 1:] + deck1[:index + 1] + deck2[:index + 1], deck2[index + 1:]
#     elif result == 2:
#         deck1, deck2 = deck1[index + 1:], deck2[index + 1:] + deck1[:index + 1] + deck2[:index + 1]
#     else:
#         break
#
# if result == 0:
#     print("PAT")
# else:
#     print("%d %d" % (result, rounds))