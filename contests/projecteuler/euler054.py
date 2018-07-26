# ProjectEuler+ > Project Euler #54: Poker hands
# Poker Hands
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler054
# challenge id: 2680
#

# original problem:
# https://projecteuler.net/problem=54


card_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def hand_value(hand):
    hand.sort(key=lambda x: card_order[x[0]])

    cards = list(card_order[x[0]] for x in hand)

    if cards == [2, 3, 4, 5, 14]:
        cards = [1, 2, 3, 4, 5]

    is_flush = all(x[1] == hand[0][1] for x in hand)
    counts = {}
    for x in cards:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    counts = sorted(list((v, k) for k, v in counts.items()), reverse=True)
    is_straight = len(counts) == 5 and cards[4] - cards[0] == 4

    # royal flush
    if is_straight and is_flush and cards[0] == 10:  # starting at T
        return 10, 0

    # straight flush
    if is_straight and is_flush:
        return 9, cards[4]       # second key: highest card

    # four of a kind
    if counts[0][0] == 4:
        return 8, counts[0][1], counts[1][1]    # keys: the four kind, then the last card

    # full house
    if counts[0][0] == 3 and counts[1][0] == 2:
        return 7, counts[0][1], counts[1][1]

    # flush
    if is_flush:
        return 6, cards[4], cards[3], cards[2], cards[1], cards[0]

    # straight
    if is_straight:
        return 5, cards[4]

    # three of a kind
    if counts[0][0] == 3:
        a, b = counts[1][1], counts[2][1]
        if a < b: a, b = b, a
        return 4, counts[0][1], a, b

    # two pairs
    if counts[0][0] == 2 and counts[1][0] == 2:
        a, b = counts[0][1], counts[1][1]
        if a < b: a, b = b, a
        return 3, a, b, counts[2][1]

    # one pair
    if counts[0][0] == 2:
        a, b, c = sorted([counts[1][1], counts[2][1], counts[3][1] ], reverse=True)
        return 2, counts[0][1], a, b, c

    return 1, cards[4], cards[3], cards[2], cards[1], cards[0]


for _ in range(int(input())):

    cards = input().split()

    player1 = hand_value(cards[0:5])
    player2 = hand_value(cards[5:10])

    if player1 > player2:
        print("Player 1")
    elif player1 < player2:
        print("Player 2")
    else:
        print("Deuce")  # not in the testcases
