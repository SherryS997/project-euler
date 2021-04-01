def blackjack_hand_greater_than(hand_1, hand_2):
    scores= {'A': 11,'K': 10,'Q': 10,'J': 10,'10': 10,'9': 9, '8': 8,'7': 7, '6': 6, '5': 5, '4': 4, '3': 3,'2': 2}
    total1 = 0
    total2 = 0
    ace = 0
    for x in hand_1:
        if x == 'A':
            ace += 1
        total1 += scores[x]
    if total1 > 21:
        for x in range(ace):
            total1 -= 10
    print(total1)
    if total1 > 21:
        return False
    else:
        ace = 0
        for x in hand_2:
            ace = 0
            if x == 'A':
                ace += 1
            total2 += scores[x]
        if total2 > 21:
            for x in range(ace):
                total2 -= 10
        print(total2)
        if total2 > 21:
            return True
        else:
            return total1 > total2


print(blackjack_hand_greater_than(['J', 'A', 'A', '2'], ['9', 'Q', '8', 'A']))
