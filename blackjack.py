import random


def create_deck(nb):
    deck = []
    colors = ['H', 'S', 'C', 'D']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for i in range(nb):
        for color in colors:
            for number in numbers:
                deck.append(number + color)
    random.shuffle(deck)
    return deck


def shuffledeck(deck):
    random.shuffle(deck)
    return deck


def valuehand(hand):
    aceinhand = 0
    value = 0
    refval = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
              'K': 10}
    for card in hand:
        valuecard = card[:-1]
        if valuecard == "A":
            aceinhand += 1
        else:
            value += refval[valuecard]
    next

    #Ace value magement
    if aceinhand > 3:
        value += 10 + aceinhand - 1
    elif aceinhand > 0:
        for i in range(aceinhand):
            if value + 10 > 21:
                value += 1
            else:
                value += 10
    return value


if __name__ == '__main__':
    print(valuehand(['AD', 'AC', '8D', 'AD', 'AD']))
