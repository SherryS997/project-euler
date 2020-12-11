a = ""
b = open("addons/p054_poker.txt", "r")
player_one_score = 0
moves = []
games = {}
deck = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
y = 0

for line in b:
    a = line.split()
    for x in a:
        moves.append(x)

for x in range(1, 1001):
    games[x] = moves[y: (y + 10)]
    y += 10


def is_consecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))


def is_royal_flush(list):
    royal_flush_hand = ['10', 'J', 'Q', 'K', 'A']
    card = []
    symbol = set()
    for x in list:
        card.append(x[:-1])
        symbol.add(x[-1])
    if card == royal_flush_hand and len(symbol) == 1:
        return True
    else:
        return False


def is_straight_flush(list):
    card = []
    symbol = set()
    for x in list:
        card.append(deck.index(x[:-1]))
        symbol.add(x[-1])
    if is_consecutive(card) and len(symbol) == 1:
        return True
    else:
        return False


def is_four_of_a_kind(list):
    card = []
    for x in list:
        card.append(x[:-1])
    for y in card:
        if card.count(y) == 4:
            return True
    else:
        return False


def is_full_house(list):
    card = set()
    for x in list:
        card.add(x[:-1])
    if len(card) == 2:
        return True
    return False


def is_flush(list):
    symbol = set()
    for x in list:
        symbol.add(x[-1])
    if len(symbol) == 1:
        return True
    else:
        return False


def is_straight(list):
    card = []
    for x in list:
        card.append(deck.index(x[:-1]))
    if is_consecutive(card):
        return True
    else:
        return False


def is_three_of_a_kind(list):
    card = []
    for x in list:
        card.append(x[:-1])
    for y in card:
        if card.count(y) == 3:
            return True
    else:
        return False


def is_two_pairs(list):
    card = set()
    for x in list:
        card.add(x[:-1])
    if len(card) == 3:
        return True
    return False


def is_one_pair(list):
    card = set()
    for x in list:
        card.add(x[:-1])
    if len(card) == 4:
        return True
    return False


def high_card(list):
    card = []
    for x in list:
        card.append(deck.index(x[:-1]))
    score = max(card) / 10
    return score


def poker_points(list):
    if is_royal_flush(list):
        return 10
    elif is_straight_flush(list):
        return 9
    elif is_four_of_a_kind(list):
        return 8
    elif is_full_house(list):
        return 7
    elif is_flush(list):
        return 6
    elif is_straight(list):
        return 5
    elif is_three_of_a_kind(list):
        return 4
    elif is_two_pairs(list):
        return 3
    elif is_one_pair(list):
        return 2
    else:
        score = high_card(list)
        return score


def tie_breaker_score(list):
    if is_full_house(list):
        card = []
        for x in list:
            card.append(x[:-1])
        for y in card:
            if card.count(y) == 3:
                score = deck.index(y) / 10
                return score
    elif is_flush(list):
        card = []
        for x in list:
            card.append(deck.index(x[:-1]))
        score = max(card) / 10
        return score
    elif is_straight(list):
        card = []
        for x in list:
            card.append(deck.index(x[:-1]))
        score = max(card) / 10
        return score
    elif is_three_of_a_kind(list):
        card = []
        for x in list:
            card.append(x[:-1])
        for y in card:
            if card.count(y) == 3:
                score = deck.index(y) / 10
                return score
    elif is_two_pairs(list):
        card = []
        score = 0
        for x in list:
            card.append(x[:-1])
        for y in card:
            if card.count(y) == 2:
                temp_score = deck.index(y) / 10
                if temp_score > score:
                    score = temp_score
        return score
    elif is_one_pair(list):
        card = []
        for x in list:
            card.append(x[:-1])
        for y in card:
            if card.count(y) == 2:
                score = deck.index(y) / 10
                return score
    else:
        card = []
        for x in list:
            card.append(deck.index(x[:-1]))
        card.remove(max(card))
        score = max(card) / 10
        return score


def poker_winner(list):
    player_one = []
    player_two = []
    player_one.extend(list[0:5])
    player_two.extend(list[-5:])
    if poker_points(player_one) > poker_points(player_two):
        return 1
    elif poker_points(player_one) < poker_points(player_two):
        return 0
    else:
        if tie_breaker_score(player_one) > tie_breaker_score(player_two):
            return 1
        elif tie_breaker_score(player_one) < tie_breaker_score(player_two):
            return 0


for x in range(1, 1001):
    if poker_winner(games[x]) == 1:
        player_one_score += 1

print(player_one_score)
