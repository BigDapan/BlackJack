import random

def create_partydeck(nb):
    deck=[]
    colors=['H','S','C','D']
    numbers=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for i in range(nb):
        for color in colors:
            for number in numbers:
                deck.append(number+color)
    random.shuffle(deck)
    return deck


if __name__ == '__main__':
    print(create_partydeck(1))
