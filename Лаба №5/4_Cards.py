# Laba No5 -- OOP -- Card deck

import random

suits  = ["Піка", "Бубна", "Хрести", "Чирва"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
        random.shuffle(self.cards)
        print(f"У колоді {len(self.cards)} карт")
    def getCardByID(self, id):
        try:
            return self.cards[id]
        except IndexError():
            return False
    def getAllCards(self):
        return self.cards
    def shuffleDeck(self):
        random.shuffle(self.cards)
    def issueCard(self):
        return self.cards.pop(0)
    def issueCards(self, amount=6):
        return [self.cards.pop(0) for i in range(amount)]

class Card:
    def __init__(self, suit, value):
        self.suit  = suit
        self.value = value

# TODO: Showcase of functionality